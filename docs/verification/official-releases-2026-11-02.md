# 官方插件市场候选验收（2026-11-02）

本记录覆盖本批十二个固定稳定版本；正式发布状态以对应注册表 PR 和线上目录读回为准。
尚未以本记录替代维护者对每个版本的人工审核。

## 候选与来源

源码归属均为 Nanobug-Editor，当前维护者 T-miracle 的仓库管理权限已用现有 Git 认证读回核对。
每个固定提交的 GitHub 许可证识别为 MIT，Release 均为公开、非 draft、非 prerelease。

| 插件 | 版本 / Release | 固定源码 | 完整 ZIP SHA-256 |
| --- | --- | --- | --- |
| Git | [0.1.54](https://github.com/Nanobug-Editor/Git/releases/tag/v0.1.54) | [7c638cfd](https://github.com/Nanobug-Editor/Git/commit/7c638cfdd3601d4b8e976379278900fe767e674a) | `90703755fd398e5f7a10017dbe248ca593e847b7c88277880a49638e681e609c` |
| Java | [0.1.35](https://github.com/Nanobug-Editor/Java/releases/tag/v0.1.35) | [fe9fc149](https://github.com/Nanobug-Editor/Java/commit/fe9fc149486435369392aabe6641ae032a7495c3) | `87d8de87986f6d674cbb9ebcd7a0ce8c6d35387cc1cb4a8b56b58d20d9f54d7d` |
| Maven | [0.1.19](https://github.com/Nanobug-Editor/Maven/releases/tag/v0.1.19) | [52cf81bb](https://github.com/Nanobug-Editor/Maven/commit/52cf81bb8da5cbe49dfaf53f14c65734df624ed9) | `37aabd02a5377e9172cc056ca90a7e0892b7e54f814f291e74afd09ac3565726` |
| Rust | [0.6.4](https://github.com/Nanobug-Editor/Rust/releases/tag/v0.6.4) | [f945e2fb](https://github.com/Nanobug-Editor/Rust/commit/f945e2fb647bf7a1aba089b69238d389808154f2) | `828fd92968e092210f24d9c5bb020ffec25f86e31b9a1c49031417fbde449bf1` |
| HTML | [0.3.2](https://github.com/Nanobug-Editor/HTML/releases/tag/v0.3.2) | [fbf8dade](https://github.com/Nanobug-Editor/HTML/commit/fbf8dade18b962ed662e97b04b21491f97743cf5) | `e119b6e2d0c24a83f575a3c1e9b1f3cbb62c9f9e0cd76c239db6f7d533f9f834` |
| JavaScript | [0.3.2](https://github.com/Nanobug-Editor/JavaScript/releases/tag/v0.3.2) | [ed583ee1](https://github.com/Nanobug-Editor/JavaScript/commit/ed583ee1dda00b80245a8fb7d7fdf674417c8da1) | `8616f43e305a67b995de93df4b2f6ced23b78e73d7253537e48bf30a386fca79` |
| TOML | [0.2.4](https://github.com/Nanobug-Editor/TOML/releases/tag/v0.2.4) | [9c6dd679](https://github.com/Nanobug-Editor/TOML/commit/9c6dd67905ad28b83b9df987827e6191650ee5df) | `3f3a13ef0541d9960cac91c96f7bcac5368ab68f00945e2ea844ff1e98090c08` |
| XML | [0.2.3](https://github.com/Nanobug-Editor/XML/releases/tag/v0.2.3) | [a9cc1059](https://github.com/Nanobug-Editor/XML/commit/a9cc1059cbb89cab8da95078ec86d3b359486615) | `a60bf19271c97fb9e245eaff86913e14171a47025f77d3aa4f92c07ae3d71920` |
| Image | [0.6.3](https://github.com/Nanobug-Editor/Image/releases/tag/v0.6.3) | [7659ce57](https://github.com/Nanobug-Editor/Image/commit/7659ce57763c3945df7f35ba44e0cf7c88c989b0) | `34bc13ecf2c848b612aeefd8c26afc6ca89cb7103e06825d701aef63130ec8a7` |
| Markdown | [0.18.7](https://github.com/Nanobug-Editor/Markdown/releases/tag/v0.18.7) | [afb21d2d](https://github.com/Nanobug-Editor/Markdown/commit/afb21d2d716972ea29c7fd7eb4feeff396fc67d9) | `df534bf48812b7abdd49c926e9a70d56241e9c9e378c09168da7c6516e276329` |
| TypeScript | [0.1.18](https://github.com/Nanobug-Editor/TypeScript/releases/tag/v0.1.18) | [770af0cf](https://github.com/Nanobug-Editor/TypeScript/commit/770af0cf3818ce3960992e6909dccb1349aad9b1) | `20944532fc6f1d86bfbce528a1bb0b40687dcfec55314ff170b8da14320e87cc` |
| Vue | [0.1.13](https://github.com/Nanobug-Editor/Vue/releases/tag/v0.1.13) | [ef274326](https://github.com/Nanobug-Editor/Vue/commit/ef27432604737b7d4e309c27a0045781068689a9) | `b31b19a638eccedd644adc67269d06d6ae79ab3741aa7b091251103291e179fc` |

## 权限

既有七个插件的新版本相对线上最高旧版均无新增权限。首次登记的五个插件需要逐项审核以下完整声明；
收录不会给用户安装实例授予权限，首次安装及新增权限仍走宿主确认流程。

- **Git 0.1.54**：`process.exec`, `process.service.rebase`, `dependencies.prepare`, `ui.panels`, `ui.interaction`, `assets.read`, `editor.read`, `editor.write`, `workspace.read`, `workspace.write`, `storage`。
- **Java 0.1.35**：`editor.read`, `editor.write`, `workspace.read`, `workspace.write`, `ui.panels`, `process.exec`, `process.service.analysis`, `dependencies.prepare`, `storage`, `process.service.local-runtime`, `process.service.local8`, `process.service.managed8`, `process.service.compiler8`, `process.service.local11`, `process.service.managed11`, `process.service.compiler11`, `process.service.local17`, `process.service.managed17`, `process.service.compiler17`, `process.service.local21`, `process.service.managed21`, `process.service.compiler21`, `process.service.local25`, `process.service.managed25`, `process.service.compiler25`, `native.modules`。
- **Maven 0.1.19**：`services.call`, `workspace.read`, `process.exec`, `process.service.maven`, `dependencies.prepare`, `storage`, `editor.read`, `native.modules`, `editor.write`, `workspace.write`, `ui.panels`。
- **TypeScript 0.1.18**：`editor.read`, `editor.write`, `workspace.read`, `process.service.engine`, `dependencies.prepare`, `native.modules`, `services.call`, `ui.interaction`, `storage`。
- **Vue 0.1.13**：`editor.read`, `workspace.read`, `native.modules`, `services.call`, `editor.write`。

## 实际验证

- `python -m unittest discover -s tests -v`：16 项通过；包含历史快照保留、新版不得借用快照跳过校验、错误身份或摘要不得绕过当前校验的回归。
- 将固定校验器升级为宿主 `845e2f95389457f7635a913fe670e4a9c3293027`。本地校验器
  SHA-256 为 `26ed5e45f3eaadfbaef6cc8a1f7086482942599d31dd6138608efb7b064557d5`，只读 Package，不启动访客。
- 升级前已实际复现旧包 `editor.layout ^1` 被当前校验器拒绝；修复后，原 7 个插件的 8 个
  历史版本与正式目录逐字段相同，不删除、不撤回、不改写其源码或摘要。
- 生产构建器以真实 HTTPS 和固定当前校验器生成候选：12 个插件、20 个版本。
  所有新增 ZIP 均实际下载并验证摘要、tag/source、清单和声明。产物 367,076 字节。
- 下载统计程序生成 12 项候选统计，测量时间为 `2026-11-02T04:34:15Z`；统计不代表安装人数。
- Git 原 0.1.53 缺少独立许可证，虽 Cargo 已声明 MIT，许可证接口仍返回 404。已发布 0.1.54，
  补齐 LICENSE 和包内双语说明，258 项单元及实际包安装/卸载/重新打开场景通过；原权限和
  原生辅助程序字节不变，0.1.53 标签及附件保留。

详细命令和日志保存在项目外 `C:/Users/Tmiracle/.codex/tmp/nanobug-marketplace-publish-2026-11-02/`。
本次数据发布不重跑全部插件业务矩阵，复用同输入的此前构建与代表场景证据；实际变化的 Git 包已单独复验。

返回[文档入口](../README.md)。
