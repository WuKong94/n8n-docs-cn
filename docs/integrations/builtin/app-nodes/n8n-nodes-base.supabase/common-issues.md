---
title: Supabase 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Supabase 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues
description: 了解 n8n 工作流自动化平台中 Supabase 节点的常见错误和问题，包括问题详情及建议的解决方法。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 常见问题 <a id="common-issues"></a>

以下介绍 [Supabase 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 按元数据筛选行 <a href="#filtering-rows-by-metadata" id="filtering-rows-by-metadata"></a>

要按 [Supabase 元数据](https://supabase.com/docs/guides/ai/python/metadata)筛选行，请将 **Select Type**（选择类型）设为 **String**（字符串）。

之后可在 **Filters (String)**（筛选条件，字符串）参数中构建查询，使用 [Supabase 元数据查询语言](https://supabase.com/docs/guides/ai/python/metadata#metadata-query-language)筛选元数据。该语言借鉴了 [MongoDB 选择器](https://www.mongodb.com/docs/manual/reference/operator/query/)格式。使用 [Postgres 的 `->>` JSON 箭头运算符](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING)访问元数据属性，如下所示，大括号中的内容需要自行填写：

```
metadata->>{your-property}={comparison-operator}.{comparison-value}
```

例如，要访问元数据中的 `age` 属性，并返回大于或等于 21 的结果，可在 **Filters (String)**（筛选条件，字符串）字段中输入：

```
metadata->>age=gte.21
```

可组合这些运算符，构建更复杂的查询。

## 使用 Docker 时无法连接本地 Supabase 数据库 <a href="#cant-connect-to-a-local-supabase-database-when-using-docker" id="cant-connect-to-a-local-supabase-database-when-using-docker"></a>

在 Docker 中运行 Supabase 时，需要配置网络，使 n8n 能够连接到 Supabase。

解决方法取决于两个组件的托管方式。

### 仅 Supabase 在 Docker 中运行 <a href="#if-only-supabase-is-in-docker" id="if-only-supabase-is-in-docker"></a>

如果仅 Supabase 在 Docker 中运行，[自托管指南](https://supabase.com/docs/guides/self-hosting/docker)使用的 Docker Compose 文件已将 Supabase 绑定到正确的网络接口。

配置 [Supabase 凭据](../../credentials/supabase.md)时，`localhost` 地址应能正常工作，将 **Host**（主机）设为 `localhost` 即可。

### Supabase 与 n8n 在不同的 Docker 容器中运行 <a href="#if-supabase-and-n8n-are-running-in-separate-docker-containers" id="if-supabase-and-n8n-are-running-in-separate-docker-containers"></a>

如果 n8n 和 Supabase 均在 Docker 中运行，且位于不同容器，可使用 Docker 网络连接它们。

在容器内将 Supabase 绑定到 `0.0.0.0`，使其监听所有网络接口，官方 [Docker Compose 配置](https://supabase.com/docs/guides/self-hosting/docker)已这样设置。如果尚未在同一个 Docker Compose 文件中统一管理两者，请将 Supabase 和 n8n 组件加入同一个[用户自定义桥接网络](https://docs.docker.com/engine/network/drivers/bridge/)。

配置 [Supabase 凭据](../../credentials/supabase.md)时，请使用 Supabase API 网关容器的名称（默认为 `supabase-kong`）作为主机地址，而非 `localhost`。例如，使用默认配置时，将 **Host**（主机）设为 `http://supabase-kong:8000`。

## 可通过 Postgres 访问记录，但无法通过 Supabase 访问 <a href="#records-are-accessible-through-postgres-but-not-supabase" id="records-are-accessible-through-postgres-but-not-supabase"></a>

如果通过 Supabase 节点查询记录返回空结果，但通过 [Postgres](../n8n-nodes-base.postgres/README.md) 节点或 Postgres 客户端可以访问这些记录，可能与 Supabase 的[行级安全（RLS）](https://supabase.com/docs/guides/database/postgres/row-level-security)策略存在冲突。

使用 Table Editor（表编辑器）在 public 模式中创建表时，Supabase 始终启用 RLS。启用 RLS 后，在创建策略之前，API 不会向使用公开 `anon` 密钥的请求返回任何数据。这项安全措施确保仅公开你希望公开的数据。

要以 `anon` 角色访问启用了 RLS 的表，请[创建策略](https://supabase.com/docs/guides/database/postgres/row-level-security#creating-policies)，允许你希望使用的访问方式。
