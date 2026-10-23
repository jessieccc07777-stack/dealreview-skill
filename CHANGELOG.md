# Changelog

本文件记录 DealReview 的版本变更。

## [1.0.0] - 2026-08-10

首个公开发布（开源）版本，对应参赛提交的 `DealReview_20260810` 包。

### 内容
- **SKILL.md**：五步工作流（接件确认 → 协议识别与路由 → 逐条五段式审查 → 专项扫描 → 双交付物）
- **references/clause-cards.md**：五段式条款卡库（回购、优先清算、反稀释、拖售/随售、优先购买/认购、MFN、一票否决、信息权、董事、不竞争、股权质押/担保等）
- **references/**：intake-routing / risk-grading / special-scans / deliverables / redline-word
- **scripts/redline_word.py**：Word 修订模式（track changes）redline 生成器（python-docx + 原始 OOXML，本地运行、无联网）

### 核心理念
- 促成交易（Deal Facilitation）：每风险必附可接受底线；🟢 建议放行清单；三栏谈判框架
- 被投资方（公司 + 创始团队）视角

### 许可
- 代码（SKILL.md、scripts、examples、docs）：MIT
- 知识库（references/clause-cards.md 等）：CC BY-NC-SA 4.0

---

*内部迭代版本（2025–2026）未在此列明，首个公开版本以 1.0.0 起算。*
