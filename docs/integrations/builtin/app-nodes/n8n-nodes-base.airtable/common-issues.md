---
title: Airtable 节点常见问题
description: 了解 n8n 工作流自动化平台中 Airtable 节点的常见错误和问题，包括问题详情及建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: Airtable 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Airtable 节点常见问题 <a href="#airtable-node-common-issues" id="airtable-node-common-issues"></a>

以下介绍 [Airtable 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## Forbidden - perhaps check your credentials（禁止访问，请检查凭据） <a href="#forbidden-perhaps-check-your-credentials" id="forbidden-perhaps-check-your-credentials"></a>

尝试执行当前访问权限不允许的操作时，会出现此错误。完整错误文本类似于：

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

最常见的原因是，所用凭据缺少管理目标资源所需的作用域。

更多信息，请参阅 [Airtable 凭据](../../credentials/airtable.md)及 [Airtable 作用域文档](https://airtable.com/developers/web/api/scopes)。

## Service is receiving too many requests from you（服务收到的请求过多） <a href="#service-is-receiving-too-many-requests-from-you" id="service-is-receiving-too-many-requests-from-you"></a>

Airtable 对使用个人访问令牌发出的 API 请求数量有硬性限制。

每个数据库每秒发送超过五个请求时，会收到 429 错误，表示请求过多。必须等待 30 秒后才能继续请求。每个访问令牌跨所有数据库发送超过 50 个请求时，也适用相同限制。

更多信息，请参阅 [Airtable 速率限制文档](https://airtable.com/developers/web/api/rate-limits)。如果使用 Airtable 节点时遇到速率限制，可考虑采用[处理速率限制](../../handle-rate-limits.md)页面中的建议。
