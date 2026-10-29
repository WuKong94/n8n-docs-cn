---
title: 共享工作流时保护凭据信息
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

{% hint style="warning" %}
**共享凭据**

导出的工作流 JSON 文件包含[凭据](../../../../get-started/key-concept-glossary.md#credential-n8n)名称和 ID。ID 本身不敏感，但名称是否敏感取决于命名方式。从 cURL 导入的 HTTP Request 节点还可能包含身份验证请求头。共享前，请从 JSON 文件中移除这些信息或将其匿名化，以保护凭据。
{% endhint %}
