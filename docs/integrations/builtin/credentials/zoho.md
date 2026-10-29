---
title: Zoho 凭据
description: Zoho 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zoho 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zoho 凭据
originalFilePath: integrations/builtin/credentials/zoho.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zoho
url: https://docs.n8n.io/integrations/builtin/credentials/zoho
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zoho 凭据 <a href="#zoho-credentials" id="zoho-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Zoho CRM](../app-nodes/n8n-nodes-base.zohocrm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zoho](https://www.zoho.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zoho CRM API 文档](https://www.zoho.com/crm/developer/docs/api/v3/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- 一个 **Access Token URL**（访问令牌 URL）：Zoho 为不同区域提供不同的访问令牌 URL。请选择与你的 Zoho 数据中心最匹配的区域：
    - **AU**：澳大利亚数据中心选择此项。
    - **CN**：中国数据中心选择此项。
    - **EU**：欧盟数据中心选择此项。
    - **IN**：印度数据中心选择此项。
    - **US**：美国数据中心选择此项。

译注：原文将 CN 说明为加拿大。Zoho 官方 Multi DC 文档列出 CN 对应 accounts.zoho.com.cn，加拿大则为 CA，对应 accounts.zohocloud.ca。此处仅修正区域说明，保留原有选项列表，不据此推断其他 n8n 版本是否提供 CA 选项。

选择数据中心的更多信息，请参阅 [Multi DC（多数据中心）](https://www.zoho.com/crm/developer/docs/api/v3/multi-dc.html)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，请向 Zoho [注册应用](https://www.zoho.com/accounts/protocol/oauth-setup.html)。

为应用采用以下设置：

- 将 **Client Type**（客户端类型）设为 **Server-based Applications**（基于服务器的应用）。
- 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），填入 Zoho 的 **Authorized Redirect URIs**（授权重定向 URI）字段。
- 从应用中复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据。

