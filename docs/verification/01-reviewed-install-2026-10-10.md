# 工单 01：审核收录到原生首次安装

对应 [工单 #2](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/issues/2)，2026-10-10 验证。市场仓库维护注册记录、只读构建器、PR 审核工作流与 GitHub Pages 输出；[Nanobug 宿主](https://github.com/T-miracle/Nanobug)维护原生 GPUI 浏览和既有 `Package` / `Manager` 安装链路。

宿主提交：[`a07eafc`](https://github.com/T-miracle/Nanobug/commit/a07eafc848044092bbbfd55c108b0f81b69c13ef)。仓库内其他未提交变更、已有图片暂存删除没有进入该提交。市场 CI 校验器固定在此提交。
市场实现提交：[`27127ef`](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/commit/27127ef72451f45b144e880c2abc7151593188ee)。[首次部署工作流](https://github.com/T-miracle/Nanobug-Plugin-Marketplace/actions/runs/38013946070) 的 `validate` 和 `deploy` 作业均成功，Pages 来源为 GitHub Actions；线上 [`catalog.json`](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/catalog.json) 读回 `schema=1`、`plugins=[]`。

## 已验证的边界

- 构建器用公开 GitHub 仓库、维护者、源码 commit、稳定 Release、开源 SPDX 许可证、固定 ZIP 和 SHA-256 生成目录。既有 ID/版本/摘要不可静默替换，归属转移需独立记录；包只做静态读取及宿主 `Package` 解析，不执行访客代码。
- Python 构建器输出的**同一**受控目录和 ZIP 由本地 HTTP 服务交给客户端。宿主完成清单、兼容性、来源与摘要核对，原生确认之后才下载，最终由既有 `Manager` 安装。声明式包及由宿主 `--plugin-package` 直接构建的实际 WASM 包均通过。
- 测试覆盖五字段搜索、分类/标签、四种排序与兼容版回退、目录刷新失败和恢复、缓存只读及最后获取时间、取消、摘要与清单不符、受限工作区、初始安装记录未就绪、已安装 ID 拒绝在线重装。既有安装记录保持原摘要。受控 SVG/Markdown 含外部图片引用时，原生浏览未发起外部请求。
- 中英文、深浅主题、搜索输入、原生指针确认、详情滚动、150% 缩放及源码/反馈链接点击由 GPUI 集成测试实际驱动。代码审查的 Standards 与 Spec 两条轴均已复查，无剩余阻断项。

## 命令与结果

| 位置 | 命令 | 结果 |
| --- | --- | --- |
| 市场仓库 | `python -m unittest discover -s tests -v` | 4/4 通过 |
| 市场仓库 | `python marketplace.py --output dist` | 生成 `schema: 1` 的空目录 |
| Pages 线上 | `GET https://t-miracle.github.io/Nanobug-Plugin-Marketplace/catalog.json` | 200；`schema=1`，零条插件 |
| Nanobug | `cargo fmt --check` | 通过 |
| Nanobug | `cargo test --workspace --exclude editor-app` | 通过；不含 `editor-app` 和 ignored 测试 |
| Nanobug | `cargo check --workspace` | 通过 |
| Nanobug | `cargo test -p editor-app marketplace` | 5 项；4 项默认通过，WASM 项显式运行后通过 |
| 独立提交候选 | `cargo fmt --check`、`cargo check --workspace`、`cargo test -p plugin-runtime --test marketplace`、`cargo test -p editor-app marketplace` | 全部通过；运行时 3/3，原生市场 4/4，实际 WASM 默认 ignored，在宿主工作树显式运行通过 |
| 固定宿主校验器 | `cargo build --locked -p plugin-runtime --example inspect_package`，并读取受控 ZIP | 构建通过，输出 `test.notes@1.0.0` |

受控声明式 ZIP SHA-256：`1ebba0f7d272fb1d05b29ddd291c6ecaf2c7df9e20005b7c22df29d7c08777f7`。受控 WASM ZIP SHA-256：`975551d65fefd84d6054dbe075a9e0c250f9ab84a6d040a0ceb8e7bea5fc8d2b`；使用 `target/debug/editor-app.exe --plugin-package plugins/capability-example --output target/marketplace-controlled`，再由 `python -m tests.export_wasm_fixture ...` 导出到本地临时目录。两个夹具仅供验收，没有提交到线上注册表。

## 线上边界

初次交付时用户确认暂时没有第三方 Release 候选，先发布空目录。2026-10-11 已由首批七个官方独立插件完成真实公开仓库候选的 PR 校验、本批收录授权、正式非空 Pages、统计及客户端线上首次安装；结果见[工单 03 验收](03-official-distribution-2026-10-11.md)。独立第三方作者没有参与本批实测，不将自有官方包称为第三方作者实测；面向第三方的相同准入限制继续由生产校验及共享负面矩阵验证。下载统计、历史版本安装、更新红点已在工单 02 独立验证，最终无随附发行由 04 负责。
