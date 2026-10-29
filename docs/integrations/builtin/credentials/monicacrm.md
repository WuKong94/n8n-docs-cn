---
title: Monica CRM 凭据
description: Monica CRM 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Monica CRM 的身份验证。
contentType:
- integration
- reference
nodeTitle: Monica CRM 凭据
originalFilePath: integrations/builtin/credentials/monicacrm.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/monicacrm
url: https://docs.n8n.io/integrations/builtin/credentials/monicacrm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Monica CRM 凭据 <a href="#monica-crm-credentials" id="monica-crm-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Monica CRM](../app-nodes/n8n-nodes-base.monicacrm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

注册 [Monica CRM](https://www.monicahq.com/) 账户，或自行托管实例。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Monica 文档](https://docs.monicahq.com/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- **Environment**（环境）：
    - 如果通过 Monica 访问实例，选择 **Cloud-Hosted**（云托管）。
    - 如果在自己的服务器上托管 Monica，选择 **Self-Hosted**（自托管），并提供 **Self-Hosted Domain**（自托管域名）。
- **API Token**（API 令牌）：在 **Settings > API**（设置 > API）中生成。

