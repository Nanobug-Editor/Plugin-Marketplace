# 官方插件市场登记审核（2026-11-03）

本批对应已发布的十二个固定稳定版本。维护者在本聊天明确要求完成登记、审核、合并与部署；以下为 Codex 实际执行的源码、权限和产物检查，不伪造另一位维护者的 GitHub 审核身份。最终发布以 PR 检查、合并提交、Pages 部署和线上目录读回为准。

## 固定版本

| 插件 | Release | 源码提交 | ZIP SHA-256 |
| --- | --- | --- | --- |
| git | [0.1.55](https://github.com/Nanobug-Editor/Git/releases/tag/v0.1.55) | `ef8b3739e00ad2536f5277fffb0dbb4030585d37` | `e364292193541f28a38a5c9bd871157ded2306bc3af2838e7196e9efe7b3be6d` |
| html | [0.3.3](https://github.com/Nanobug-Editor/HTML/releases/tag/v0.3.3) | `fc2292a2040678ea420afae813bc8f12f2e53b0a` | `81c6d3f63ec661c8f4e27dda078885226950aac9753c9829e046affe3ebf5a3f` |
| svg | [0.6.4](https://github.com/Nanobug-Editor/Image/releases/tag/v0.6.4) | `8e7859feb3c1edca16c1c6b64ac96d61b874732d` | `d34ef97165afb81333ed56581c19f3c3fb810676b2ca0be38c0da4b2468faf62` |
| java | [0.1.36](https://github.com/Nanobug-Editor/Java/releases/tag/v0.1.36) | `503dfa46895300f6e7d7aa28b74f5e1666515b83` | `3fa63626f3f6d6cbe29d7c8e12e6611f44cb6104a8007d084e5f56af0881e55c` |
| javascript | [0.4.0](https://github.com/Nanobug-Editor/JavaScript/releases/tag/v0.4.0) | `430a0600159a97f356068d9f4da2297536dfc78e` | `1aaaac101b326ff4d77e77bb7e5a817d6ca018c6a364116a54ec006167b44d46` |
| markdown | [0.18.8](https://github.com/Nanobug-Editor/Markdown/releases/tag/v0.18.8) | `f0fbb1415e26989d2235d68cb1df07e80fd2c8c2` | `9325a0f9c400e77f9cec3044c8e36fb1669744e6ca64b6fe61f023fd50d9b384` |
| maven | [0.1.20](https://github.com/Nanobug-Editor/Maven/releases/tag/v0.1.20) | `c4e08e4eca2a45fcbf4dfa2d86013c4121cc0b5c` | `8a9e31e9f6f0c8ff51aee00d46e0f5b5b6f17b7517d59f08e850415c371e314d` |
| rust | [0.6.5](https://github.com/Nanobug-Editor/Rust/releases/tag/v0.6.5) | `33b7ec569e53e6573a68f8fcf4e5b172ed3be813` | `b5e4f2fead33af0a11a1e9f8cbe6cb1b5c6a963ebbfed7a0e2af1f1747ce8fe7` |
| toml | [0.2.5](https://github.com/Nanobug-Editor/TOML/releases/tag/v0.2.5) | `55034f72267dd5605a3a2db8b7bd7cb71663edee` | `5d041fd9e431ba402685e69f869d18ef4578a312b9f89a57f3b0fdbd5b7c86d0` |
| typescript | [0.1.19](https://github.com/Nanobug-Editor/TypeScript/releases/tag/v0.1.19) | `a32df805030a8ed3efb332feb3e4af7dcc976e9b` | `9ea80e0850137b6ac0c7287ec47917b69da6dfb5d8f38a4e3eabca3994f0892d` |
| vue | [0.2.0](https://github.com/Nanobug-Editor/Vue/releases/tag/v0.2.0) | `0061aeb3e77b7bc0f31e0562d74a7dd288fda272` | `6f6a59b0e7b1d8ca2ab647b4e8bf32ef3e0c3b48415384c8bebdbc8c21c53b47` |
| xml | [0.2.4](https://github.com/Nanobug-Editor/XML/releases/tag/v0.2.4) | `6d16fac67b0de969925d90c2c41c159e89def68d` | `a383f8b9e1b47d14f4afbcb3a88d9f9df6dcd1987b316bdb920d903880f7b2cf` |

## 审核依据

- 十二个仓库均属于 `Nanobug-Editor`，当前维护者认证逐仓确认具有 push 权限；registry 的 repository、maintainers 与安装 ID 保持不变。所有固定源码均包含 MIT 许可证。
- Release 均为公开稳定版，标签、源码提交、附件名和完整 ZIP 摘要与本轮发行账本一致。时间与更新日志从正式 Release 读取后固定登记。
- Git、HTML、Image、Java、Markdown、Maven、Rust、TOML、XML 的源码变化仅为发行版本。TypeScript 收窄主分析角色至 TS/TSX；JavaScript、Vue 使用自身原生分析角色，不要求安装 TypeScript 插件。源码及真实包行为证据见[宿主统一发行验收](https://github.com/Nanobug-Editor/Editor/blob/main/docs/distribution/verification/release-all-2026-11-03.md)。
- JS/Vue 的原生分析归档摘要为 `5532b77fcb6fe31612525caa140a1e499a0d10efa67326cd4ce3201fde0faf07`，各自 16 个 native 源文件逐字节匹配 TypeScript 固定提交 `770af0cf3818ce3960992e6909dccb1349aad9b1`；Vue 协作 helper 也匹配该来源。依赖来源、许可与私有进程边界保留。
- 本轮保留原有 20 条版本记录且逐字段一致，仅追加 12 条新记录；不更改校验器 pin、可信构建器、工作流或审核机制。

## 新增权限及必要性

| 插件 | 新增权限 | 代码与用途 |
| --- | --- | --- |
| JavaScript 0.4.0 | `editor.read`、`workspace.read`、`process.service.analysis` | 清单中的公开 document control 契约读取相关文档与工作区上下文；固定的 analysis 服务提供 import 定义和悬浮，不要求任意 Shell 执行权限 |
| Vue 0.2.0 | `dependencies.prepare`、`process.service.engine` | 准备固定摘要的包内工具依赖，启动自身 engine；`src/owned.rs` 经公开语言 control 调用，并保留取消和资源关闭路径 |
| 其余十个版本 | 无 | 完整权限与线上上一版相同 |

用户安装或升级仍需按宿主规则确认新增权限；市场收录本身不授予权限。两个原生分析服务的发行平台为 Windows x64，不声明本轮已验证其他平台。

## 验证与交付

- `python -m unittest discover -s tests -v`：16 项通过。
- 使用 `.github/validator.json` 固定的宿主 `845e2f95389457f7635a913fe670e4a9c3293027`；复用校验器 SHA-256 `26ed5e45f3eaadfbaef6cc8a1f7086482942599d31dd6138608efb7b064557d5`，只做 Package 内容检查，不运行插件代码。
- 联网完整目录构建、PR CI 与部署状态由对应流水线和本机证据记录。首次本机构建遇到 TLS EOF，保留失败日志并重试，不将其计为通过。
- 本轮复用相同 ZIP 的宿主发行测试与公开下载 SHA-256 证据，不重打包、不覆盖已发布附件。

本机证据目录：`C:/Users/Tmiracle/.codex/task-artifacts/nanobug-marketplace-20261103/`，包括 `review-inputs.json`、`ownership-review.json`、原始线上目录、追加前 registry、完整目录构建日志和发布读回。

返回[文档入口](../README.md)。
