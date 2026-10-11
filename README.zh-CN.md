# Nanobug 插件市场

[English](README.md)

Nanobug 官方插件注册表与分发项目，英文名为 Nanobug-Plugin-Marketplace。

工单 01–04 已实现并通过验收：审核后的原生安装、历史版本与安全升级、七个官方插件独立发布，以及无随附 Windows 交付。[工单目录](docs/tickets/README.md)链接交付记录与真实 GitHub 状态；[最终 Windows 记录](docs/verification/04-unbundled-delivery-2026-10-11.md)说明实测范围与其他平台限制。

## 范围

- 编辑器内插件发现、下载、下载次数、历史版本及兼容版本安装。
- 第三方公开开源插件通过 PR 审核收录。
- GitHub Pages 托管静态目录，各作者 GitHub Releases 托管 ZIP。
- 七个官方插件独立维护，最终编辑器发行不随附插件。
- 首版不做独立市场网页、评分、付费、私有插件来源或额外后端。

## 文档

- [文档入口](docs/README.md)
- [执行规格](docs/specs/plugin-marketplace.md)
- [四张工单与测试安排](docs/tickets/README.md)
- [议题发布记录](docs/tickets/publication.json)
- [AI 协作规范](AGENTS.md)

Nanobug 宿主负责原生界面与安装运行时；各插件仓库维护自己的源码与包；本仓库维护注册表、审核发布、统计和本主题的方案与工单。

## 构建与投稿

目录构建器和测试仅需 Python 3.11+：

```powershell
# 使用固定 ZIP 与 GitHub 夹具验证注册表约束。
python -m unittest discover -s tests -v
# 构建空目录；已有插件记录时追加 --validator <inspect_package.exe>。
python marketplace.py --output dist
# 仅统计收录的 Release ZIP 附件；API 失败时保留历史统计。
python market_statistics.py --catalog dist/catalog.json --previous-url https://t-miracle.github.io/Nanobug-Plugin-Marketplace/stats.json --output dist/stats.json
```

通过 PR 提交[注册记录](registry/README.md)，每个版本均需人工审核。[归属转移](transfers/README.md)单独审核。PR 校验使用基线构建器及固定 Nanobug `Package` 校验器，不运行访客代码。在 Nanobug 仓库检出 `.github/validator.json` 固定的提交，以 `cargo build --locked -p plugin-runtime --example inspect_package` 构建校验器。

Actions 向可信构建器提供只读 `GH_TOKEN`，仅用于 `https://api.github.com` 的公开元数据。API 重定向必须保持同一来源，Release ZIP 请求不携带该凭据。本地验证也可不提供凭据，但会受到 GitHub 未认证 API 限流约束。

`Reviewed catalog` 工作流仅将 main 数据发布至 [catalog.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/catalog.json)。Pages 来源须设为 **GitHub Actions**，仅上传 `dist/`，不建设独立网站。首个真实插件通过审核前，注册表保持为空；受控测试插件不发布。

原生客户端缓存目录及最后成功获取时间。刷新失败时禁止市场新装和升级，成功后恢复。详情不加载 Markdown 内嵌图片、不解析 SVG 外部文件或网络引用；源码和反馈按钮打开已校验的 GitHub 仓库。首装须经过用户确认、SHA-256 与清单一致性、兼容性及信任检查；已安装插件只允许升至更高兼容稳定版，新增权限再次确认。启动后及运行约六小时异步检查，不自动下载更新；标题栏红点在没有可用升级时才清除。

工作流目标每六小时测量下载量，独立发布 [stats.json](https://t-miracle.github.io/Nanobug-Plugin-Marketplace/stats.json)。次数包含重复及市场外下载，不等于安装人数。API 失败保留旧值和时间，未测量次数显示暂不可用；统计失败不阻止安装。格式见[静态数据契约](docs/specs/static-data-contract.md)。
