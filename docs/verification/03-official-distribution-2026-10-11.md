# 工单 03：独立 Release 与市场收录候选

2026-10-11；对应 [#4](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/issues/4)。七个新命名仓库、稳定 Release、固定 ZIP、原生首次安装与各自代表行为已验证；维护者已授权本批通过收录；PR #6 已合并，可信 CI、正式非空 Pages/统计及客户端消费验收通过。

## 固定来源

公开宿主 / SDK 为 [`b77e6317bf7e3d3d3d0fe9490cabd362d266e0a5`](https://github.com/T-miracle/Nanobug/commit/b77e6317bf7e3d3d3d0fe9490cabd362d266e0a5)，市场可信校验器基线为 `4d7ee9a96bc86ccc1a62ac51f8d8944ef1b0acac`。七仓 owner/maintainer 均为 T-miracle；生产构建器通过真实新地址读回每个源码 commit 的 MIT 许可证、固定 tag、非 draft/非 prerelease 状态与完整 ZIP SHA-256。下表是七个新仓固定源码提交的独立构建 CI，现已全部 success；main 的双语 README 命名更新不改变发布 tag。

| 仓库 | 安装 ID / Release | 源码 commit | 完整 ZIP SHA-256 | 源码 CI |
| --- | --- | --- | --- | --- |
| [HTML](https://github.com/T-miracle/HTML-for-Nanobug) | `html` / [0.3.1](https://github.com/T-miracle/HTML-for-Nanobug/releases/tag/v0.3.1) | `68b8c7baabd0790cba884aa19e4f2523b2b2e7ce` | `6f1ad3e33ade378f9fdbdedef5d1d8e6f91b4059f620f7a490f0dd97af4a4f5e` | [通过](https://github.com/T-miracle/HTML-for-Nanobug/actions/runs/38121945903) |
| [JavaScript](https://github.com/T-miracle/JavaScript-for-Nanobug) | `javascript` / [0.3.1](https://github.com/T-miracle/JavaScript-for-Nanobug/releases/tag/v0.3.1) | `18dc8818787857b75cb1ae1b4ffd88edfa35a631` | `a09afb41de50211e5e0a866d2698dde2a6d524b54dc74149eda573f42eabe144` | [通过](https://github.com/T-miracle/JavaScript-for-Nanobug/actions/runs/38121955827) |
| [Markdown](https://github.com/T-miracle/Markdown-for-Nanobug) | `markdown` / [0.17.1](https://github.com/T-miracle/Markdown-for-Nanobug/releases/tag/v0.17.1) | `31516790679c2ab591105d11e6fd15e974b72505` | `2438a081165de70acf0c30c560905167d46b44a5c30d7abf856fa420a14a17a3` | [通过](https://github.com/T-miracle/Markdown-for-Nanobug/actions/runs/38121964796) |
| [Rust](https://github.com/T-miracle/Rust-for-Nanobug) | `rust` / [0.6.1](https://github.com/T-miracle/Rust-for-Nanobug/releases/tag/v0.6.1) | `942a905e4d4dfe02a9b9b162c35e3c2788691d5f` | `9da637f2852318c51fb7b008c1abaefe4848a1d0896d6205210558a561de6867` | [通过](https://github.com/T-miracle/Rust-for-Nanobug/actions/runs/38121974536) |
| [Image](https://github.com/T-miracle/Image-for-Nanobug) | `svg` / [0.6.1](https://github.com/T-miracle/Image-for-Nanobug/releases/tag/v0.6.1) | `cac09895b6bc9cd227a6e318edb8c868da41084e` | `911932c643bc9b7a538b3f4b5baa34e04a939256b61ee49bf6d2f9e84656a654` | [通过](https://github.com/T-miracle/Image-for-Nanobug/actions/runs/38121983340) |
| [TOML](https://github.com/T-miracle/TOML-for-Nanobug) | `toml` / [0.2.3](https://github.com/T-miracle/TOML-for-Nanobug/releases/tag/v0.2.3) | `a1a4677118403ac01e6a0fd2f667cfa788aa9bd2` | `2b3dabe0b2f67b2ed2440fe5eb8e7ac2b3e408105accc2f7bbdc9a2ccf6ebeed` | [通过](https://github.com/T-miracle/TOML-for-Nanobug/actions/runs/38121992075) |
| [XML](https://github.com/T-miracle/XML-for-Nanobug) | `xml` / [0.2.2](https://github.com/T-miracle/XML-for-Nanobug/releases/tag/v0.2.2) | `69749e0d37ca28571e39101678f77a051a939ca8` | `c6bde8af6e724d2c9570502293f4e9d024137761759205baffb6f10a8bd3dd8a` | [通过](https://github.com/T-miracle/XML-for-Nanobug/actions/runs/38122000455) |

独立仓库使用公开 SDK 缓存，不引用主项目 crates 路径、不附带 SDK 源码副本。Image 保留 `svg` 身份，Rust 只发布已合并包，不发布独立 Rust Debugger 或示例。原宿主源码暂作冻结输入，业务维护以独立仓库为准，04 验证替代输入后再删除。

## 审核权限与依赖

| 包 | 实际权限 | 必要性及受控原生来源 |
| --- | --- | --- |
| HTML | `process.service.analysis`、`dependencies.prepare` | 补全、格式化及配对标签；Windows 私有 Node 24.19.0 与包内 server.cjs |
| JavaScript | `process.service.format`、`dependencies.prepare` | 私有 Node 24.19.0 格式化服务；不宣称补全 |
| Markdown | `editor.read`、`editor.write`、`workspace.read`、`workspace.write`、`clipboard`、`network.images`、`navigation.external`、`storage` | 预览、编辑、图片、链接、剪贴板及私有偏好，无原生服务 |
| Rust | `workspace.read`、`process.exec`、`ui.panels`、`process.service.analysis`、`process.service.adapter`、`dependencies.prepare` | Cargo/运行/调试与 Rust Analyzer；延迟私有 CodeLLDB 1.12.3 和包内桥，不安装整个 Rust 工具链 |
| Image | `editor.read`、`workspace.read`、`storage` | SVG 预览、位图显示和私有视图偏好，无原生服务 |
| TOML | 无 | 声明式识别及 Tree-sitter 高亮，不附空 WASM |
| XML | `process.service.analysis`、`dependencies.prepare`、`editor.read` | LemMinX 与纯 WASM 补全/结构；Windows 私有 LemMinX，其他平台仍可配置本机服务 |

外部依赖固定摘要：Node（nodejs.org）`3602f2bb1a10f2cbab4c36886218a33c1ab3db87290e73b033c46c77147d0237`；CodeLLDB（vadimcn/codelldb v1.12.3）`a916e509308dac817732f63ca604a8b93ed29cd16f38a2fa9f0b64ed58e8f51a`；LemMinX（redhat-developer/vscode-xml 0.29.3）`7eaefaac68253b0ec8e0ad1f1c0f2d0755423d4e99e52497428b52f80df28eb7`。清单同时固定包内原生资源摘要。此表是人工审阅输入，自动检查不代替权限必要性或源码/构建来源判断。

## 实际验证

宿主七包原生验收提交 [`443ba91682b33a7b6e83eeb6dd9bee14d6ae1b58`](https://github.com/T-miracle/Nanobug/commit/443ba91682b33a7b6e83eeb6dd9bee14d6ae1b58) 已普通推送并核对远程 main 与工作分支；正式 Pages/Release 线上安装及最新[完整证据](https://github.com/T-miracle/Nanobug/blob/1bfc4cf10b3a67edb43f4f01003f1c6e2592cec2/docs/plugins/verification/plugin-marketplace-03-2026-10-11.md)对应宿主提交 `1bfc4cf10b3a67edb43f4f01003f1c6e2592cec2`。主工作区已有改动及真实用户数据未改写。追加变化只有测试与文档，正式 SDK/ZIP 输入仍固定 b77e631。

- 现有 Rust/Cargo 1.98.1、Windows x86_64 MSVC 与 wasip2；Markdown 73、Rust 6、Image 8 个 guest 单元测试通过，XML guest 编译通过。未安装新本机工具。
- 公开 `--plugin-package` 构建七包，惰性 Package 检查通过。生产构建器使用真实公开 GitHub HTTP、许可、tag、Release 与 ZIP 导出候选；重新下载的七个附件全部匹配完整 SHA-256，候选目录尚未发布。PR CI 不执行访客代码。
- `python -m unittest discover -s tests -v`：9 passed，覆盖不可变版本、上游替换/非法包拒绝、来源/许可、撤回及统计失败保留；共用一次负面矩阵。
- `marketplace_official_releases_install_with_native_consent --ignored`：1 passed / 0 ignored，147.81 秒。参数化七包，经原生确认、真实 HTTP、完整摘要和公开 Worker/Manager 安装/激活；各自隔离目录，确认前 0 次下载，成功后各 1 次；ID、清单、授权及六种语言真实识别/高亮正确，交替中英文和深浅主题。
- XML 实际包/LemMinX/schema/补全/导航/设置验收：1 passed / 0 ignored，668.67 秒。
- 使用同次已编译的原生测试可执行文件逐项 `--ignored --test-threads=1 --nocapture`：HTML/XML 配对标签/重命名/中文输入/Undo 78.50 秒；JavaScript 格式化和提供者保留 7.56 秒；Markdown 未保存编辑、预览及分屏回收 20.59 秒；Image 四种位图原生绘制 17.99 秒；合并 Rust 的真实 Cargo 双目标 CodeLLDB 调试及市场确认取消 55.09 秒。五项均 1 passed / 0 ignored，输入为上表最终附件。
- 最终宿主门禁全部通过：`cargo fmt --check`；非 UI workspace 237 passed / 188 ignored；`cargo check --workspace` 0.96 秒。普通市场 7 passed / 5 ignored，6.46 秒；已显式执行的七包场景独立计入，不把其他 skipped 算作通过。

七包首次验收的第一次执行在 XML 安装记录提交后超过共享 60 秒而失败。实际 XML 对照用例持续推进；新增七包场景单独使用 180 秒预算，XML 最后 69.21 秒完成，普通回归仍为 60 秒。生产代码未因此修改，没有删除断言或扩大 ignore。

## 本批收录授权与发布状态

2026-10-11，维护者在当前 Codex 会话明确要求“这几个本地插件帮我自动通过审核”。该指令授权本次七个既有本地官方插件的固定版本通过收录并合并 [PR #6](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/pull/6)。审核继续校验来源、权限、原生依赖、稳定 tag、完整 ZIP 哈希和可信 PR CI；不将这次授权扩展为第三方或以后版本的自动准入。

此前维护者要求重新创建项目并命名为 `X for Nanobug`。已创建上表七个 `X-for-Nanobug` 新仓库，保留原源码 commit、tag、ID、版本、ZIP 文件名和字节。Release 正文与发布日期按新仓库读回，候选在未发布时更新来源，最终新仓记录已正式部署，未覆盖先前已发布版本。包内历史说明保持其冻结版本。

原仓源码 CI 的通过证据可复用：输入源码、SDK、工具链和包资源未变。新仓库独立构建已全部 success，并读回核对；源码 CI 只证明可独立构建，不宣称不同机器重建 ZIP 必然相同。新地址已重新经过真实 HTTPS 下载、完整摘要及惰性 Package 校验。

新地址复验：生产构建器从七个新仓库重新读取来源、许可、tag、Release 正文与 ZIP，七个完整 SHA-256 及惰性 Package 校验均通过；市场单元/契约测试 9 passed。使用该新目录的七包原生安装场景 `marketplace_official_releases_install_with_native_consent --ignored` 再次通过，1 passed / 0 ignored，131.83 秒，其中 XML 66.90 秒；确认、安装、授权、语言注册与真实高亮断言全部保留。包业务源码与字节未变，复用上文代表行为验收，不重复执行完整业务矩阵。

七个仓库的 main 双语 README 已改为项目名 `X for Nanobug`，并说明 Release 标签及字节仍冻结。改动只涉及文档，没有移动 tag、改变清单 ID/版本或重新打包；文档提交跳过重复源码 CI，标签指向的原源码构建继续独立运行。

本批可信 PR CI、正式非空 Pages/统计及客户端消费验收已通过。04 仅做删除前盘点，尚未删除源码/示例或改变发行。完整 ZIP 哈希锁定审核字节，不能单凭它证明所列源码的可复现构建。GPUI 验收使用原生事件与布局自动测试；人工操作系统 IME 和非 Windows 执行未验证。


## 正式收录与线上验收

维护者于 2026-10-11 明确要求“这几个本地插件帮我自动通过审核”，授权本批七个既有本地官方插件的固定版本收录并合并。授权只覆盖本批；以后版本和第三方仍按市场规格经 PR 审核。已核对各包来源、许可证、权限、原生依赖、固定 tag 和完整 ZIP 摘要。

[PR #6](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/pull/6) 对 `6cec7a06e1727d4d1d28406f4d9d973bc7c0098f` 的[可信 CI](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/actions/runs/38122382439)通过，独立 Standards 与 Spec 复审分别 0 阻断。PR 已于 2026-10-11T07:48:46Z 合并，市场提交为 `8d1a8ca28d5c7a6a88dd2c93c2f9ce4598c38b99`；[main 校验、统计及 Pages 部署](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/actions/runs/38122634435)均 success。

维护者要求七个新项目使用 `X for Nanobug` 名称，因此重新创建 `X-for-Nanobug` 仓库。七个新仓均保留原源码 commit、tag、安装 ID、版本、ZIP 名和字节；main 只有双语 README 的命名与链接更新，未移动发布标签或重新打包。新仓七个独立构建 CI 已全部通过，前表提供实际 run 链接。新地址经生产构建器真实 HTTPS 重新导出，许可/tag/Release/完整 ZIP 摘要及惰性 Package 校验均通过。

- 新地址七包原生安装复验：`marketplace_official_releases_install_with_native_consent --ignored`，1 passed / 0 ignored，131.83 秒；XML 66.90 秒。隔离数据目录、确认前零下载、确认后恰一次、真实安装/激活及语言高亮断言均保留。
- 正式 [catalog.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/catalog.json) 返回七个新仓条目，与生产构建器快照逐版本相符；[stats.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/stats.json)包含七包及实际测量时间 `2026-10-11T07:53:39Z`。
- `marketplace_published_pages_installs_reviewed_release --ignored`：1 passed / 0 ignored，1.34 秒。通过公开 Worker 的正式 Pages URL 刷新，再从新仓 GitHub Release 下载 TOML 0.2.3，以公开 Manager 安装到隔离目录；身份、权限、版本、完整摘要、启用及持久化缓存正确，正式统计可读取。这项只验证真实网络/安装链路；原生确认与七包代表能力由前述共享 GPUI 用例验证，不重复完整矩阵。
- 首次线上用例在部署前空目录状态下失败，未将其记为通过；部署成功后使用相同正式网络入口完成上述验收。新增测试释放 actor 状态锁后再断言，避免测试失败破坏清理；未因此改变生产协议、SDK 或正式包。
- 本阶段三项共同门禁通过：格式检查、非 UI workspace 237 passed / 188 ignored、workspace 编译检查；新增源码仅为 cfg(test)。市场契约/统计 9 passed。七包 SDK 与 ZIP 输入未变，复用前文代表能力证据。
