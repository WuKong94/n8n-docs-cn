---
title: Help Scout 凭据
description: Help Scout 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Help Scout 的身份验证。
contentType:
- integration
- reference
nodeTitle: Help Scout 凭据
originalFilePath: integrations/builtin/credentials/helpscout.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/helpscout
url: https://docs.n8n.io/integrations/builtin/credentials/helpscout
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Help Scout 凭据 <a href="#help-scout-credentials" id="help-scout-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Help Scout](../app-nodes/n8n-nodes-base.helpscout.md)
- [Help Scout Trigger（触发器）](../trigger-nodes/n8n-nodes-base.helpscouttrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Help Scout](https://www.helpscout.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Help Scout API 文档](https://developer.helpscout.com/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或希望进一步了解 OAuth 网页授权流程，需要创建 Help Scout 应用。更多信息请参阅 [Help Scout OAuth 文档](https://developer.helpscout.com/mailbox-api/overview/authentication/#oauth2-application)中的说明。
