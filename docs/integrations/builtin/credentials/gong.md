---
title: Gong 凭据
description: Gong 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Gong 的身份验证。
contentType:
- integration
- reference
nodeTitle: Gong 凭据
originalFilePath: integrations/builtin/credentials/gong.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/gong
url: https://docs.n8n.io/integrations/builtin/credentials/gong
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gong 凭据 <a href="#gong-credentials" id="gong-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Gong](../app-nodes/n8n-nodes-base.gong.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Gong API 文档](https://gong.app.gong.io/settings/api/documentation)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [Gong](https://app.gong.io/welcome/sign-in) 账号，以及：

- **Access Key**（访问密钥）
- **Access Key Secret**（访问密钥对应的密钥值）

这两个值均可在 [Gong API 页面](https://app.gong.io/company/api)创建；必须是 Gong 技术管理员才能访问该页面。

有关该服务身份验证的更多信息，请参阅 [Gong API 文档](https://gong.app.gong.io/settings/api/documentation)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Gong](https://app.gong.io/welcome/sign-in) 账户、一个 [Gong 开发者](https://gong.partnerfleet.app/application_forms/become-a-gong-technology-partner/partner_applications/new)账户，以及：

* **Client ID**（客户端 ID）：为 Gong 创建 OAuth 应用时生成。
* **Client Secret**（客户端密钥）：为 Gong 创建 OAuth 应用时生成。

如果[自行托管](../../../deploy/host-n8n/README.md) n8n，需要先[创建应用](https://help.gong.io/docs/create-an-app-for-gong)才能配置 OAuth2。设置 OAuth2 的更多信息，请参阅 [Gong OAuth 文档](https://gong.app.gong.io/settings/api/documentation)。
