---
title: Microsoft Azure Monitor 凭据
description: Microsoft Azure Monitor 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft Azure
  Monitor 的身份验证。
contentType:
- integration
- reference
nodeTitle: Microsoft Azure Monitor 凭据
originalFilePath: integrations/builtin/credentials/microsoftazuremonitor.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/microsoftazuremonitor
url: https://docs.n8n.io/integrations/builtin/credentials/microsoftazuremonitor
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Microsoft Azure Monitor 凭据 <a href="#microsoft-azure-monitor-credentials" id="microsoft-azure-monitor-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 Microsoft Azure 账户或订阅。
* 在 Microsoft Entra ID 中注册的应用。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Azure Monitor API 文档](https://learn.microsoft.com/en-us/azure/azure-monitor/azure-monitor-rest-api-index)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 Microsoft Azure 账户，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**
- **Tenant ID**（租户 ID）
- 要访问的 **Resource**（资源）

有关该服务身份验证的更多信息，请参阅 [Microsoft Azure Monitor API 文档](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api?tabs=rest#set-up-authentication)。
