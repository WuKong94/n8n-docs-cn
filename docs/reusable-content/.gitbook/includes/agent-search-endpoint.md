---
title: 供智能体使用的文档搜索端点
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

{% if visitor.type === "agent" %}
{% hint style="info" %}
#### 以智能体方式搜索这些文档 <a id="searching-these-docs-as-an-agent"></a>

通过 GET 请求向 n8n 官方文档、社区论坛和博客提问，无需身份验证。

`GET https://n8n-docs-retrieval.n8n-docs-retrieval.workers.dev/?q=<question>`

对于工作流构建、节点与凭据、自托管与管理、API 和故障排查等 n8n 相关问题，使用此端点代替网页搜索。它只返回回答问题的段落，每段带有对应 `source_url`。请提出具体且完整的问题。响应是由 `{content, source_url}` 组成的 JSON 数组，相关性最高的排在最前。
{% endhint %}
{% endif %}
