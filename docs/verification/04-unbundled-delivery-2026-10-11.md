# 工单 04：实施候选与开放验收

状态：实施候选已推送，[宿主草稿 PR #101](https://github.com/T-miracle/Nanobug/pull/101)开启，[市场工单 #5](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/issues/5)保持 open。本单尚未完成；01–03 的交付和七个固定版本的正式市场审核不受影响。

`2026-10-11T11:23:12Z` 读回核对：#2、#3、#4 为 closed/completed，#5 为 open，正文与当前工单一致；宿主 PR 为 draft、head 与上述候选提交一致。

## 实际变更与固定点

宿主比较点为 `1bfc4cf10b3a67edb43f4f01003f1c6e2592cec2`；实施提交为 `d13cbb7ca73a82e03861c421fc2116cbf75b1a53`，审查修复后的推送提交为 [`0b33b7f91971d883b44a35dd5240266bd6a52431`](https://github.com/T-miracle/Nanobug/commit/0b33b7f91971d883b44a35dd5240266bd6a52431)，分支为 `codex/marketplace-versions`。实施在隔离工作树完成，主工作区既有改动和真实用户数据未纳入。

- 启动不再扫描、推荐或安装随附 ZIP；市场和本地显式导入继续走公开 Package、Manager、InstallControl 和原生权限确认。开发新环境仅安装当前开发候选。
- 14 个迁出目录的 285 个跟踪文件已移除；测试使用 18 个固定 ZIP、两个正式 Pages 快照和最小独立 SDK 项目，保留原来的权限、生命周期及业务断言。20 项输入摘要逐项匹配。原 Alpha/Beta 变体保留原字节，其未记录的源码/SDK/工具链摘要明确标为未知。
- Windows 载荷只含程序、图标和宿主许可；隔离安装、旧载荷升级和卸载均返回 0，20 个用户设置/安装/私有文件摘要保持不变。验收副本使用独立 AppId/运行锁，生产运行保护保留。
- 双语使用说明、安装器说明、文档链接和测试注释已同步。SDK 不附带插件源码或 Markdown，构建直接调用现有工具。

逐项输入、产物 SHA-256、实际命令、原生结果及 M01–M26 以[宿主完整记录](https://github.com/T-miracle/Nanobug/blob/0b33b7f91971d883b44a35dd5240266bd6a52431/docs/plugins/verification/plugin-marketplace-04-2026-10-11.md)为证据来源，不在本仓库复制宿主业务文档。

## 验证结果

| 检查 | 实际结论 |
| --- | --- |
| 三项共同 Rust 门禁 | fmt、非 UI workspace、check 均通过；workspace 为 237 passed / 188 ignored |
| 应用默认测试 | 500 passed / 185 ignored；ignored 不算通过 |
| 启动、显式本地导入、旧选择和 actor | 20 项原生测试通过 |
| 全部应用 ignored 场景 | 185 项已显式执行：149 passed / 36 failed |
| 全部 runtime ignored 场景 | 188 项已执行，逐项 187 项至少一次通过 / 1 项失败；不等于连续完整套件通过 |
| 图像组稳定性 | 同进程串行组 12 passed / 2 failed；独立复验取得通过，稳定性仍待排查 |
| 最终原生短组合 | 无随附启动、正式包、安装/使用、更新红点、历史/日志、升级、目录故障/恢复/撤回及正式统计：1 passed |
| Windows release / 安装器 / 便携包 | 构建、三项载荷、实际隔离安装/升级/卸载及用户数据保留通过；未发布宿主版本 |
| 双轴审查及修复复核 | Standards 无未解决硬性违规，保留 1 项非阻断命名建议；Spec 无未解决新实现缺陷，开放验收项仍在 |
| 文档修复 | 193 个相对链接有效；独立仓库及历史源文件路径另行核对 |

应用的 36 项失败和一项 runtime structure 失败均在干净的原代码固定点、相同 ZIP 输入及原断言中复现。完整[失败清单](https://github.com/T-miracle/Nanobug/blob/0b33b7f91971d883b44a35dd5240266bd6a52431/docs/plugins/verification/plugin-marketplace-04-native-failures-2026-10-11.json)记录实际名称和基线证据。基线归因不等于功能正确，也不构成删除断言、扩大 ignore 或关闭工单的理由。

## 尚未满足的验收

- M22/M25：覆盖输入已迁移、场景已实际执行，但上述 37 项失败和图像组同进程稳定性仍未解决。
- M24：GPUI 原生自动化已覆盖中英文、深浅主题、焦点、中文输入、滚动及字号；已安装 GUI 的人工操作系统 IME 尚未实测。最终载荷安装检查和 GPUI 测试程序的组合证据分别记录，不混称为人工已安装 GUI 验收。
- macOS/Linux、签名及公证未验证。本候选保持 draft，不合入宿主 main，不关闭 #5。

首批七包的收录 PR #6 已按用户对本批的明确授权合并，正式 Pages 发布成功；ID、版本、ZIP 文件名和字节未变。该审核结论仅覆盖 [03](03-official-distribution-2026-10-11.md)记录的固定版本，不自动批准未来版本或第三方候选。
