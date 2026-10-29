---
description: 根据 OpenAPI 规范生成的 n8n 公共 REST API 端点参考。
contentType: reference
nodeTitle: 端点参考
originalFilePath: api/api-reference.md
originalUrl: 'https://docs.n8n.io/api/api-reference'
url: 'https://docs.n8n.io/connect/n8n-api/api-reference'
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 端点参考 <a id="endpoint-reference"></a>

本节是根据 OpenAPI 规范生成的 n8n 公共 REST API 完整端点参考。你可以查阅所有可用操作，以及参数、请求体和响应结构。

{% hint style="info" %}
**功能可用范围**

以下套餐和版本可以使用 n8n API：

- **n8n Cloud：** Starter、Pro、Enterprise
- **自托管：** 所有版本

免费试用期间无法使用。
{% endhint %}

## 开始之前 <a id="before-you-start"></a>

* **身份验证**：每个请求都需要 API 密钥。请参阅[身份验证](authentication.md)。
* **设置基础 URL**：
    * n8n Cloud：`https://<your-instance>.app.n8n.cloud/api/v1`
    * 自托管：`https://<your-domain>/api/v1`
* 对大型结果集使用**分页**。请参阅[分页](pagination.md)。
* 使用 `Idempotency-Key` 请求头**重试 POST 请求**。请参阅[幂等性](idempotency.md)。

## 浏览端点 <a id="browse-the-endpoints"></a>

左侧边栏的 **n8n API** 下按资源对端点分组，包括 Workflow（工作流）、Execution（执行）、Credential（凭据）、User（用户）、Audit（审计）、Tags（标签）、Source Control（源代码管理）、Variables（变量）、Data Table（数据表）、Projects（项目）等。每个页面都说明该资源的操作和数据结构。

{% hint style="info" %}
**安全地试用 API**

如需尝试实际 API 调用，请使用[内置 API 调试界面](use-an-api-playground.md)（仅限自托管 n8n），或将请求发送到测试工作流或测试实例。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [n8n API](./)
* [身份验证](authentication.md)
* [分页](pagination.md)
* [幂等性](idempotency.md)
* [使用 API 调试界面](use-an-api-playground.md)
