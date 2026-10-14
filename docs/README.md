# 文档入口

本仓库是插件市场主题资料的唯一维护位置。状态与实际远程议题、验收证据一起核对。

| 内容 | 入口 |
| --- | --- |
| 产品范围与执行决策 | [执行规格](specs/plugin-marketplace.md) |
| 四张工单、依赖与测试主责 | [工单目录](tickets/README.md) |
| 实际议题 ID 与关系 | [发布记录](tickets/publication.json) |
| GitHub 操作与授权 | [议题跟踪器](agents/issue-tracker.md) |
| 分诊词汇 | [标签约定](agents/triage-labels.md) |
| 项目初始化与议题发布证据 | [初始化记录](verification/project-bootstrap-2026-10-09.md) |
| 工单 01 实现与验收 | [审核收录到原生首次安装](verification/01-reviewed-install-2026-10-10.md) |
| 工单 02 实现与验收 | [历史版本、统计与升级](verification/02-versions-updates-2026-10-11.md) |
| 工单 03 当前证据 | [七仓稳定 Release 与收录候选](verification/03-official-distribution-2026-10-11.md) |
| 工单 04 最终证据 | [无随附 Windows 交付验收](verification/04-unbundled-delivery-2026-10-11.md) |
| 组织迁移：旧仓删除前覆盖核对 | [历史提交、Release 资产与议题元数据](verification/organization-migration-legacy-audit.json) |
| 发布数据契约 | [目录、撤回与统计](specs/static-data-contract.md) |
| 仓库规范 | [AGENTS.md](../AGENTS.md) |

后续验收进入 docs/verification 并从对应工单链接。方案、工单和证据分别维护，不复制 Nanobug 宿主与独立插件的业务文档。文档在 GitHub 可阅读，但不作为独立市场网页发布。

组织迁移保留已审核版本及 ZIP 字节。删除旧的 `Nanobug-Plugin-*` 仓库后，冻结包 README 中指向它们的历史链接会失效；当前说明和同版本 tag 下的原始资料从 [Nanobug 组织](https://github.com/Nanobug-Editor)中对应插件仓库读取。该链接限制不改变安装 ID、包摘要或用户私有数据。
