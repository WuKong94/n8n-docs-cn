---
title: Harvest 凭据
description: Harvest 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Harvest 的身份验证。
contentType:
- integration
- reference
nodeTitle: Harvest 凭据
originalFilePath: integrations/builtin/credentials/harvest.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/harvest
url: https://docs.n8n.io/integrations/builtin/credentials/harvest
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Harvest 凭据 <a href="#harvest-credentials" id="harvest-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Harvest](../app-nodes/n8n-nodes-base.harvest.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Harvest](https://www.getharvest.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Harvest API 文档](https://help.getharvest.com/api-v2/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个个人 **Access Token（访问令牌）**：创建方法请参阅 [Harvest 个人访问令牌身份验证文档](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#personal-access-tokens)。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或希望进一步了解 OAuth 网页授权流程，请按照 [Harvest OAuth2 文档](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#oauth2-application)中的说明设置 OAuth。

