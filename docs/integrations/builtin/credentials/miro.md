---
title: Miro 凭据
description: Miro 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Miro 的身份验证。
contentType:
- integration
- reference
nodeTitle: Miro 凭据
originalFilePath: integrations/builtin/credentials/miro.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/miro
url: https://docs.n8n.io/integrations/builtin/credentials/miro
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Miro 凭据 <a href="#miro-credentials" id="miro-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Miro](https://miro.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Miro API 文档](https://developers.miro.com/reference/overview)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/miro/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Miro](https://miro.com/login/) 账户和应用，以及：

- **Client ID**（客户端 ID）：创建新的 OAuth2 应用时生成。
- **Client Secret**（客户端密钥）：创建新的 OAuth2 应用时生成。

有关该服务身份验证的更多信息，请参阅 [Miro API 文档](https://developers.miro.com/reference/overview)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自行托管](../../../deploy/host-n8n/README.md) n8n，需要先[创建应用](https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app)才能配置 OAuth2。设置 OAuth2 的更多信息，请参阅 [Miro OAuth 文档](https://developers.miro.com/docs/getting-started-with-oauth)。
