# DealReview 安装指南（Installation SOP）

> 一句话：把 `dealreview-skill/` 整个文件夹，放进你所用 AI 助手的 **skills 目录**，然后对 AI 说"帮我审核这份协议"即可。

## 支持哪些 AI 助手？

DealReview 遵循开放的 **SKILL.md** 标准，凡是支持 SKILL.md 的 AI 助手都能安装，包括：

| AI 助手 | skills 目录 | 安装方式 |
|---|---|---|
| Claude Code | `~/.claude/skills/` | 复制文件夹 |
| Cursor | `~/.cursor/skills/`（或项目 `.cursor/skills/`） | 复制文件夹 |
| Codex CLI | `~/.codex/skills/` | 复制文件夹 |
| WorkBuddy | `~/.workbuddy/skills/` | 复制文件夹 |
| 其他支持 SKILL.md 的助手 | 各自 skills 目录 | 复制文件夹 |

## 分步安装（以 Claude Code 为例）

### 方式一：下载 ZIP

1. 在 GitHub 仓库页点 **Code → Download ZIP**，解压
2. 打开终端，创建 skills 目录（若没有）：
   ```bash
   mkdir -p ~/.claude/skills
   ```
3. 把解压出的 `dealreview-skill/` 整个文件夹复制进去：
   ```bash
   cp -r dealreview-skill ~/.claude/skills/dealreview
   ```
4. 重启 AI 助手（或新开一个会话），安装完成

### 方式二：git clone

```bash
git clone https://github.com/jessieccc07777-stack/dealreview-skill.git ~/.claude/skills/dealreview
```

### 方式三：通过技能市场安装

若本 skill 已收录到 agentskill.sh / skills.sh 等目录，可直接用对应安装命令：
```bash
# agentskill.sh
/learn @jessieccc07777-stack/dealreview-skill
# skills.sh
npx skills add jessieccc07777-stack/dealreview-skill
```

## 验证安装成功

新开一个会话，输入：

> 帮我审核这份协议：[上传你的 docx]

如果 AI 按"接件确认 → 五段式审查 → 双交付物"的流程走，就说明安装成功。

## 常见问题（FAQ）

**Q：为什么 AI 没触发 DealReview 流程？**
A：确认 skills 目录路径正确、文件夹名不带多余层级（`SKILL.md` 应位于 skills 目录下的一个子文件夹内）；换新会话再试。

**Q：redline 脚本需要什么依赖？**
A：`scripts/redline_word.py` 需要 Python 3 + `python-docx`：
```bash
pip install python-docx
```
该脚本**完全本地运行**，不联网、不访问任何私有路径。

**Q：协议文件会传到云端吗？**
A：不会。skill 设计为本地优先处理，协议无需离开你的设备；如需对外演示可用脱敏模式（匿名化主体名称）。

**Q：这是法律意见吗？**
A：不是。输出仅供理解与谈判参考，签署前请咨询执业律师。
