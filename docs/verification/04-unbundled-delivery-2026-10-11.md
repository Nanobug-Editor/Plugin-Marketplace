# 工单 04：无随附 Windows 交付验收

状态：Windows 行为验收完成，[宿主 PR #101](https://github.com/T-miracle/Nanobug/pull/101)已于 `2026-10-11T16:25:49Z` 合并。[市场工单 #5](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/issues/5)已于 `2026-10-11T16:34:37Z` 关闭。最终复核日期为北京时间 2026-10-12。

`2026-10-11T16:35:12Z` 读回 #2、#3、#4、#5 均为 closed/completed，#5 正文与本地工单完全一致；父规格 #1 和历史 Nanobug #100 保持 open，状态与实际 ID 保存于[发布记录](../tickets/publication.json)。

## 实际变更与固定点

删除阶段比较点为 `1bfc4cf10b3a67edb43f4f01003f1c6e2592cec2`；首轮候选为 `0b33b7f91971d883b44a35dd5240266bd6a52431`；最终测试代码为 `556658e065fa63abcf53404b1205e5e624009086`。最终证据提交 `576606294cdcf678ade52673c86c1f7a23fc89b1` 只修改文档与夹具说明。宿主合并提交为 [`4d172b97cbbf7aff2bbcd986116321e3566023b9`](https://github.com/T-miracle/Nanobug/commit/4d172b97cbbf7aff2bbcd986116321e3566023b9)，分支为 `codex/marketplace-versions`。实施在隔离工作树完成，主工作区既有改动和真实用户数据未纳入。

- 启动不再扫描、推荐或安装随附 ZIP；市场和本地显式导入继续走公开 Package、Manager、InstallControl 和原生权限确认。
- 14 个迁出目录的 285 个跟踪文件已移除。消费者使用 21 个固定 ZIP、两个正式 Pages 快照及最小独立公开 SDK 项目；23 项实际摘要全部匹配，保留权限、生命周期、UI 与业务断言。原 Alpha/Beta 变体保留原字节，未知源码/SDK/工具链摘要继续明确标记。
- Windows 载荷只含程序、图标和宿主许可。最终六阶段便携、干净安装、旧载荷安装、升级及两次卸载均 exit 0；40 个隔离用户文件的身份与 SHA-256 保持不变。验收副本使用独立 AppId/运行锁，生产运行保护保留。
- 双语说明、安装器说明、文档链接和测试注释已同步。SDK 不附带插件源码或 Markdown；构建直接调用现有工具，不调用退役脚本。

逐项输入、产物 SHA-256、命令、原生结果及 M01–M26 以[宿主完整记录](https://github.com/T-miracle/Nanobug/blob/4d172b97cbbf7aff2bbcd986116321e3566023b9/docs/plugins/verification/plugin-marketplace-04-2026-10-11.md)为证据来源，不在本仓库复制宿主业务文档。

## 最终验证结果

| 检查 | 实际结论 |
| --- | --- |
| 三项共同 Rust 门禁 | fmt、非 UI workspace、check 均通过；workspace 为 238 passed / 0 failed / 188 ignored |
| 全部应用测试，含全部 ignored | **686 passed / 0 failed / 0 ignored**，855.91 秒 |
| 全部 runtime ignored | **188 passed / 0 failed / 0 ignored**，50 个二进制连续执行 |
| 图像组 / structure | 同进程串行 14 / 3 项全部通过，已包含在 runtime 188 项中 |
| Markdown 独立包 | 单元 76 项、真实包原生 88 项通过；原生 88 项已包含在应用 686 项中 |
| 原生市场与最终短组合 | 全部 14 项通过，包含无随附启动、正式包安装/使用、更新红点、历史/日志、升级、目录故障/恢复/撤回和正式统计；已包含在应用 686 项中 |
| Windows release / 安装器 / 便携包 | 构建和载荷检查通过，实际隔离安装/升级/卸载及 40 文件数据保留通过 |
| 市场代码与正式发布 | Python 13 项通过；[main CI / Pages deploy](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/actions/runs/38154042902)成功 |
| 双轴审查及最终证据复核 | Standards 未解决硬性违规 0；Spec 缺漏、错误实现、范围蔓延均 0 |

workspace 中 188 项 ignored 不计通过，其实际执行由独立列出的 runtime 结果证明。输入未变化的六个插件及初批版本未重复构建；变动的 Markdown 在独立仓库重新构建、验包并测试。

首轮 36 项应用失败、一项 runtime structure 失败及图像组同进程稳定性已经解决。[失败账本](https://github.com/T-miracle/Nanobug/blob/4d172b97cbbf7aff2bbcd986116321e3566023b9/docs/plugins/verification/plugin-marketplace-04-native-failures-2026-10-11.json)保留原结果与基线日志，并逐项追加最终通过证据。未删除测试、扩大 ignore、提高资源配额或添加插件专属宿主 API。

## 正式市场与版本不可变性

首批七包的收录 [PR #6](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/pull/6)已按用户对本批的明确授权合并，正式 Pages 发布成功。新增 [Markdown 0.17.2](https://github.com/T-miracle/Markdown-for-Nanobug/releases/tag/v0.17.2)经[插件 PR #1](https://github.com/T-miracle/Markdown-for-Nanobug/pull/1)、独立验证及[市场 PR #7](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/pull/7)审核发布；市场合并提交为 `5ba32ff21d16ffde5340d78f1236f651a9201be0`。

新包源码为 `8480eb38e059d575cb5dafd740ed14f035d20936`，616350 字节，SHA-256 为 `cac840637b5348c553da810e0d101f318088714caec18e30710bbc97c8327e13`，asset ID 为 `631092655`。正式 Pages 读回七个插件，Markdown 同时保留 0.17.2 和原 0.17.1；旧版 ID、源码、ZIP 文件名与摘要均未改写。

统计读回测量时间为 `2026-10-11T16:10:50Z`，Markdown 当时 total 9，版本分别为 1 和 8；下载次数不等于安装人数。正式客户端在线消费及受控正式快照短组合均有实际通过证据。第一次 PR CI 因未认证 GitHub API 限流失败的历史保留；后续只读认证严格限制到 HTTPS API 来源，Release ZIP 不携带凭据，PR 仍使用可信基线校验器且不执行访客代码。

## 验收范围与边界

M22 的覆盖迁移、M23 的无随附发行和旧数据保留、M25 的交付门禁均已满足。M24 使用原生 GPUI 自动化，覆盖中英文、深浅主题、键盘/焦点、中文输入与 composition、滚动、14/18/24 字号和实际布局；未实测物理 OS IME 候选窗口，不宣称其他 run-config 规格的专项人工验收完成。

macOS/Linux、签名及公证未验证；没有发布新的宿主版本标签。非阻断建议是后续合并几个 Markdown 测试中重复的 LocateViewport 辅助逻辑。父市场规格 #1 和历史 Nanobug #100 不随实施工单关闭。
