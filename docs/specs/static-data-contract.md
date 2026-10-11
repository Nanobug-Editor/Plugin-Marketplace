# 静态目录与下载统计契约

本文件记录工单 01–02 的实际静态数据格式，产品要求仍以[执行规格](plugin-marketplace.md)为准。Pages 只发布 `catalog.json`、`stats.json` 与 `.nojekyll`；Release ZIP 由登记作者托管。

## 目录和撤回

`catalog.json` 的 `schema` 为 1，`plugins` 为空时是有效空市场。条目字段及版本快照以 `marketplace.py` 的输出和 Nanobug `plugin_runtime::marketplace::Catalog` 的解析器为契约两端；不兼容的新字段不能静默忽略。

每版固定 `version`、`manifest`、`host_version`、`platforms`、`sha256`、`commit`、`license`、`url`、`asset_id`、`published_at`、`readme`、`icon`、`changelog`。`withdrawn` 默认假；旧目录可省略 `withdrawal_reason`，新输出包含该字段。撤回为真时必须提供非空理由。一次人工审核可将未撤回改为撤回，不能解除或改写撤回记录；其他字段仍不可变。

注册表基线来自 PR 的可信 base，发布基线来自最后成功 Pages 部署。撤回快照来自该市场已发布目录，并核对 ID、仓库、版本、源码 commit 与 ZIP 摘要；作者删除附件后不重写历史。没有可核对的快照时发布失败，旧 Pages 保持可用。

客户端每次安装或升级核对完整 ZIP 字节的 SHA-256，再核对实际清单。相同源码重新打包的 ZIP 可以有不同摘要；不同字节必须提升版本重新审核。摘要不是源码可复现构建证明。

## 独立统计

```json
{
  "schema": 1,
  "measured_at": "2026-10-11T01:00:00Z",
  "plugins": [{
    "id": "example-id",
    "total": 18,
    "versions": [
      {"version": "1.0.0", "downloads": 7},
      {"version": "1.1.0", "downloads": 11}
    ]
  }]
}
```

示例仅说明格式，不代表上架插件。次数是非负 u64，累计等于本次各收录版本的和。统计程序仅访问目录中登记的附件 ID，并核对上传状态、ZIP 名称与完整下载 URL，不计算源码归档或校验文件。次数包含重复和市场外下载，不代表安装人数。

一轮统计是原子快照：任一附件/API 失败保留整份历史值及 `measured_at`。首次失败使用 `measured_at: null`、`total: null` 和 `downloads: null`，不显示虚假零。新增版本在旧快照中不存在时，其次数暂不可用。工作流目标每六小时执行；时间以实际测量为准，不承诺严格准时。

只有旧快照明确返回 404 才按首次部署处理。若旧快照临时无法读取且本轮 API 也失败，停止本轮 Pages 发布以保留远端原有目录和统计；客户端仍可刷新原已发布目录并安装。获取到旧快照后的统计故障可继续发布原统计，不影响新目录。

客户端独立获取、缓存和展示统计。统计错误不改变目录新鲜度、权限或安装资格；排序和详情使用同一份已发布数据，不逐插件请求 GitHub API。目录刷新失败仍禁止市场新装与升级，旧统计和旧目录只供浏览。
