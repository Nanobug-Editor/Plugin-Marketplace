# 工单 03：独立 Release 与市场收录候选

2026-10-11；对应 [#4](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/issues/4)。七个新命名仓库、稳定 Release、固定 ZIP、原生首次安装与各自代表行为已验证；维护者已授权本批通过收录，待更新后的可信 PR 校验及正式非空 Pages 验收，议题仍 open。

## 固定来源

公开宿主 / SDK 为 [`b77e6317bf7e3d3d3d0fe9490cabd362d266e0a5`](https://github.com/T-miracle/Nanobug/commit/b77e6317bf7e3d3d3d0fe9490cabd362d266e0a5)，市场可信校验器基线为 `4d7ee9a96bc86ccc1a62ac51f8d8944ef1b0acac`。七仓 owner/maintainer 均为 T-miracle；生产构建器通过真实新地址读回每个源码 commit 的 MIT 许可证、固定 tag、非 draft/非 prerelease 状态与完整 ZIP SHA-256。下表源码 CI 是原仓同一提交的已通过证据，新仓构建结果另行记录，不将进行中任务记为通过。

| 仓库 | 安装 ID / Release | 源码 commit | 完整 ZIP SHA-256 | 源码 CI |
| --- | --- | --- | --- | --- |
| [HTML](https://github.com/T-miracle/HTML-for-Nanobug) | `html` / [0.3.1](https://github.com/T-miracle/HTML-for-Nanobug/releases/tag/v0.3.1) | `68b8c7baabd0790cba884aa19e4f2523b2b2e7ce` | `6f1ad3e33ade378f9fdbdedef5d1d8e6f91b4059f620f7a490f0dd97af4a4f5e` | [通过](https://github.com/T-miracle/Nanobug-Plugin-HTML/actions/runs/38118544496) |
| [JavaScript](https://github.com/T-miracle/JavaScript-for-Nanobug) | `javascript` / [0.3.1](https://github.com/T-miracle/JavaScript-for-Nanobug/releases/tag/v0.3.1) | `18dc8818787857b75cb1ae1b4ffd88edfa35a631` | `a09afb41de50211e5e0a866d2698dde2a6d524b54dc74149eda573f42eabe144` | [通过](https://github.com/T-miracle/Nanobug-Plugin-JavaScript/actions/runs/38118553877) |
| [Markdown](https://github.com/T-miracle/Markdown-for-Nanobug) | `markdown` / [0.17.1](https://github.com/T-miracle/Markdown-for-Nanobug/releases/tag/v0.17.1) | `31516790679c2ab591105d11e6fd15e974b72505` | `2438a081165de70acf0c30c560905167d46b44a5c30d7abf856fa420a14a17a3` | [通过](https://github.com/T-miracle/Nanobug-Plugin-Markdown/actions/runs/38118561389) |
| [Rust](https://github.com/T-miracle/Rust-for-Nanobug) | `rust` / [0.6.1](https://github.com/T-miracle/Rust-for-Nanobug/releases/tag/v0.6.1) | `942a905e4d4dfe02a9b9b162c35e3c2788691d5f` | `9da637f2852318c51fb7b008c1abaefe4848a1d0896d6205210558a561de6867` | [通过](https://github.com/T-miracle/Nanobug-Plugin-Rust/actions/runs/38118570843) |
| [Image](https://github.com/T-miracle/Image-for-Nanobug) | `svg` / [0.6.1](https://github.com/T-miracle/Image-for-Nanobug/releases/tag/v0.6.1) | `cac09895b6bc9cd227a6e318edb8c868da41084e` | `911932c643bc9b7a538b3f4b5baa34e04a939256b61ee49bf6d2f9e84656a654` | [通过](https://github.com/T-miracle/Nanobug-Plugin-Image/actions/runs/38118577996) |
| [TOML](https://github.com/T-miracle/TOML-for-Nanobug) | `toml` / [0.2.3](https://github.com/T-miracle/TOML-for-Nanobug/releases/tag/v0.2.3) | `a1a4677118403ac01e6a0fd2f667cfa788aa9bd2` | `2b3dabe0b2f67b2ed2440fe5eb8e7ac2b3e408105accc2f7bbdc9a2ccf6ebeed` | [通过](https://github.com/T-miracle/Nanobug-Plugin-TOML/actions/runs/38118585073) |
| [XML](https://github.com/T-miracle/XML-for-Nanobug) | `xml` / [0.2.2](https://github.com/T-miracle/XML-for-Nanobug/releases/tag/v0.2.2) | `69749e0d37ca28571e39101678f77a051a939ca8` | `c6bde8af6e724d2c9570502293f4e9d024137761759205baffb6f10a8bd3dd8a` | [通过](https://github.com/T-miracle/Nanobug-Plugin-XML/actions/runs/38118592031) |

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

宿主最终验收提交 [`443ba91682b33a7b6e83eeb6dd9bee14d6ae1b58`](https://github.com/T-miracle/Nanobug/commit/443ba91682b33a7b6e83eeb6dd9bee14d6ae1b58) 已普通推送并核对远程 main 与工作分支；[完整原生证据](https://github.com/T-miracle/Nanobug/blob/443ba91682b33a7b6e83eeb6dd9bee14d6ae1b58/docs/plugins/verification/plugin-marketplace-03-2026-10-11.md)。主工作区已有改动及真实用户数据未改写。追加变化只有测试与文档，正式 SDK/ZIP 输入仍固定 b77e631。

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

此前维护者要求重新创建项目并命名为 `X for Nanobug`。已创建上表七个 `X-for-Nanobug` 新仓库，保留原源码 commit、tag、ID、版本、ZIP 文件名和字节。Release 正文与发布日期按新仓库读回，候选记录尚未正式发布，来源更新不覆盖已发布市场记录。包内历史说明保持其冻结版本。

原仓源码 CI 的通过证据可复用：输入源码、SDK、工具链和包资源未变。新仓库独立构建已启动，最终结果另行读回记录；源码 CI 只证明可独立构建，不宣称不同机器重建 ZIP 必然相同。新地址必须重新经过真实 HTTPS 下载、完整摘要及惰性 Package 校验。

尚需更新后的可信 PR CI、正式非空 Pages/统计及客户端消费验收；01/03 不提前关闭。04 仅做删除前盘点，尚未删除源码/示例或改变发行。完整 ZIP 哈希锁定审核字节，不能单凭它证明所列源码的可复现构建。GPUI 验收使用原生事件与布局自动测试；人工操作系统 IME 和非 Windows 执行未验证。
