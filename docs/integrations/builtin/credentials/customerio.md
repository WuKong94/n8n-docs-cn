---
title: Customer.io 凭据
description: Customer.io 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Customer.io 的身份验证。
contentType:
- integration
- reference
nodeTitle: Customer.io 凭据
originalFilePath: integrations/builtin/credentials/customerio.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/customerio
url: https://docs.n8n.io/integrations/builtin/credentials/customerio
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Customer.io 凭据 <a href="#customerio-credentials" id="customerio-credentials"></a>

这些凭据可用于以下节点与 Customer.io 之间的身份验证。

- [Customer.io](../app-nodes/n8n-nodes-base.customerio.md)
- [Customer.io Trigger（触发器）](../trigger-nodes/n8n-nodes-base.customeriotrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Customer.io](https://customer.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API Key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Customer.io API 概览文档](https://customer.io/docs/api/?api=journeys)。

各 API 的详细参考文档，请参阅 [Track API 文档](https://customer.io/docs/api/track/)和 [App API 文档](https://customer.io/docs/api/app/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Tracking API Key**（跟踪 API 密钥）：用于位于 `https://track.customer.io/api/v1/` 的 [Track API](https://customer.io/docs/api/track/)。详情请参阅下方常见问答。
- **Region**（区域）：Customer.io 根据所选区域使用不同的 API 子域名，可选：
    - **Global region**（全球区域）：两个 API 都保留默认 URL，适用于所有非欧盟国家或地区。
    - **EU region**（欧盟区域）：将 Track API 子域名改为 `track-eu`，将 App API 子域名改为 `api-eu`；仅在位于欧盟时使用此项。
- **Tracking Site ID**（跟踪站点 ID）：使用 **Tracking API Key**（跟踪 API 密钥）时必填。
- **App API Key**（应用 API 密钥）：用于位于 `https://api.customer.io/v1/api/` 的 [App API](https://customer.io/docs/api/app/)。详情请参阅下方常见问答。

如何创建 Tracking API 和 App API 密钥，请参阅 [Customer.io 查找和管理 API 凭据文档](https://customer.io/docs/accounts-and-workspaces/managing-credentials/)。

## 为什么需要 Tracking API Key 和 App API Key <a href="#why-you-need-a-tracking-api-key-and-an-app-api-key" id="why-you-need-a-tracking-api-key-and-an-app-api-key"></a>

Customer.io 有两个不同的 API 端点，各自生成及存储密钥的方式略有不同：

- 位于 `https://track.customer.io/api/v1/` 的 [Track API](https://customer.io/docs/api/track/)
- 位于 `https://api.customer.io/v1/api/` 的 [App API](https://customer.io/docs/api/app/)

Track API 需要 Tracking Site ID，App API 不需要。

n8n 会根据要执行的操作，使用正确的 API 密钥及其对应端点。

