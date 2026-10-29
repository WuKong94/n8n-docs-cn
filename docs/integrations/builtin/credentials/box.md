---
title: Box 凭据
description: Box 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Box 的身份验证。
contentType:
- integration
- reference
nodeTitle: Box 凭据
originalFilePath: integrations/builtin/credentials/box.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/box
url: https://docs.n8n.io/integrations/builtin/credentials/box
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Box 凭据 <a href="#box-credentials" id="box-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Box](../app-nodes/n8n-nodes-base.box.md)
- [Box Trigger（触发器）](../trigger-nodes/n8n-nodes-base.boxtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Box](https://www.box.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Box API 文档](https://developer.box.com/reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或希望进一步了解 OAuth 网页授权流程，需要创建自定义应用。更多信息请参阅 [Box OAuth2 配置文档](https://developer.box.com/guides/authentication/oauth2/oauth2-setup/)。

