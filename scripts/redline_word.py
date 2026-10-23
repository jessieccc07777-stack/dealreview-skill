# -*- coding: utf-8 -*-
"""
DealReview · Word 修订模式 redline 生成器
==========================================

在【客户上传的原协议 docx 副本】上，将《风险审查报告》中"修订条款"以
Word 修订模式（track changes：w:ins / w:del）直接落地，产出一份带真实
修订标记的 .docx，用户在 Word 中开启"审阅→显示标记"即可看到每一处增删，
最后由用户把关。

设计原则（与开源安全一致）：
- 纯 python-docx + 原始 OOXML，无任何外部私有路径 / 联网 / 代码执行。
- 修订内容全部由运行时《风险审查报告》提供，脚本本身不含任何条款立场。
- 仅做"定位原文 → 包成删除 + 插入"，不破坏原文档其他内容。

用法（运行时由 AI 调用）：
    from redline_word import apply_redline
    apply_redline("客户协议.docx",
                  [("原条款文本…", "修订后条款文本…"), ...],
                  out_path="客户协议_修订模式.docx")

说明：
- 若 new_text 为空字符串 ""，表示【整段删除】该条款（只留 w:del）。
- 默认仅替换文档中【第一次】出现的 old_text（条款通常唯一）；
  如需全部替换，传 replace_all=True。
- 若条款跨多段落，请逐段分别给定 (old, new)；本工具按段落定位。
"""

import copy
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

_WORD_ID = [0]


def _rid():
    _WORD_ID[0] += 1
    return str(_WORD_ID[0])


def _make_ins(text, rpr=None):
    """生成一个 w:ins 修订节点（插入），内含一个 w:r/w:t。"""
    ins = OxmlElement('w:ins')
    ins.set(qn('w:author'), 'DealReview')
    ins.set(qn('w:date'), '2026-01-01T00:00:00Z')
    ins.set(qn('w:id'), _rid())
    r = OxmlElement('w:r')
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    ins.append(r)
    return ins


def _make_del(text, rpr=None):
    """生成一个 w:del 修订节点（删除），内含一个 w:r/w:delText。"""
    delel = OxmlElement('w:del')
    delel.set(qn('w:author'), 'DealReview')
    delel.set(qn('w:date'), '2026-01-01T00:00:00Z')
    delel.set(qn('w:id'), _rid())
    r = OxmlElement('w:r')
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    dt = OxmlElement('w:delText')
    dt.set(qn('xml:space'), 'preserve')
    dt.text = text
    r.append(dt)
    delel.append(r)
    return delel


def _runs_of(paragraph):
    """返回段落中文本 run 列表 [(w:r, 文本)]，忽略非 run 节点。"""
    out = []
    for child in paragraph._p:
        if child.tag == qn('w:r'):
            txt = ''.join(t.text or '' for t in child.iter(qn('w:t')))
            out.append((child, txt))
    return out


def _clone_run(src_r, text):
    """深拷贝一个 w:r 并将其首个 w:t 文本设为 text（其余 w:t 清空）。"""
    new = copy.deepcopy(src_r)
    ts = list(new.iter(qn('w:t')))
    if ts:
        ts[0].text = text
        for t in ts[1:]:
            t.text = ''
    return new


def replace_in_paragraph(paragraph, old, new):
    """在单个段落中将 old 文本替换成【删除 old + 插入 new】的修订标记。
    成功返回 True；段落中找不到 old 返回 False。
    """
    runs = _runs_of(paragraph)
    full = ''.join(t for _, t in runs)
    idx = full.find(old)
    if idx < 0:
        return False

    match_start = idx
    match_end = idx + len(old)

    before_runs = []
    matched = []          # [(w:r, mid_text)]
    after_runs = []
    cursor = 0
    for r, txt in runs:
        r_start = cursor
        r_end = cursor + len(txt)
        if r_end <= match_start:
            before_runs.append((r, txt))
        elif r_start >= match_end:
            after_runs.append((r, txt))
        else:
            ov_start = max(r_start, match_start)
            ov_end = min(r_end, match_end)
            pre = txt[: ov_start - r_start]
            mid = txt[ov_start - r_start: ov_end - r_start]
            post = txt[ov_end - r_start:]
            if pre:
                before_runs.append((_clone_run(r, pre), pre))
            if mid:
                matched.append((r, mid))
            if post:
                after_runs.append((_clone_run(r, post)))
        cursor = r_end

    p = paragraph._p
    # 移除原有 w:r
    for r, _ in runs:
        p.remove(r)
    # 重新装配：before + del(matched) + ins(new) + after
    for r, _ in before_runs:
        p.append(r)
    if matched:
        first_rpr = matched[0][0].find(qn('w:rPr'))
        del_text = ''.join(t for _, t in matched)
        p.append(_make_del(del_text, first_rpr))
    if new:  # 非空才插入（空字符串 = 整段删除）
        p.append(_make_ins(new))
    for r, _ in after_runs:
        p.append(r)
    return True


def iter_paragraphs(doc):
    """遍历文档所有段落，含表格内段落。"""
    for p in doc.paragraphs:
        yield p
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p


def apply_redline(input_docx, replacements, out_path=None, replace_all=False):
    """对 input_docx 应用一组 (old, new) 修订，保存到 out_path。
    返回统计：{"applied": [(old, new)], "not_found": [old, ...]}。
    """
    doc = Document(input_docx)
    applied = []
    not_found = []
    for old, new in replacements:
        if not old:
            not_found.append(old)
            continue
        hit = False
        for p in iter_paragraphs(doc):
            if replace_in_paragraph(p, old, new):
                hit = True
                if not replace_all:
                    break
        if hit:
            applied.append((old, new))
        else:
            not_found.append(old)
    if out_path is None:
        out_path = input_docx
    doc.save(out_path)
    return {"applied": applied, "not_found": not_found}


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        inp = sys.argv[1]
        outp = sys.argv[2]
        # 演示：可在命令行用 JSON 传入 replacements；此处仅做冒烟测试占位
        print("use apply_redline() programmatically; see module docstring.")
    else:
        print("usage: redline_word.py input.docx output.docx")
