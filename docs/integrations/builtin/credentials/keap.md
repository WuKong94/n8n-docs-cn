---
title: Keap 凭据
description: Keap 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Keap 的身份验证。
contentType:
- integration
- reference
nodeTitle: Keap 凭据
originalFilePath: integrations/builtin/credentials/keap.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/keap
url: https://docs.n8n.io/integrations/builtin/credentials/keap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Keap 凭据 <a href="#keap-credentials" id="keap-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Keap](../app-nodes/n8n-nodes-base.keap.md)
- [Keap Trigger（触发器）](../trigger-nodes/n8n-nodes-base.keaptrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Keap](https://developer.keap.com/) 开发者账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 Keap 的 [REST API 文档](https://developer.keap.com/docs/restv2/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或希望进一步了解 OAuth 网页授权流程，请参阅 [OAuth2 入门文档](https://developer.keap.com/getting-started-oauth-keys/)中的说明。

