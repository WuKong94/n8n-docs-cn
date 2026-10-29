---
title: Drift 凭据
description: Drift 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Drift 的身份验证。
contentType:
- integration
- reference
nodeTitle: Drift 凭据
originalFilePath: integrations/builtin/credentials/drift.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/drift
url: https://docs.n8n.io/integrations/builtin/credentials/drift
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Drift 凭据 <a href="#drift-credentials" id="drift-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Drift](../app-nodes/n8n-nodes-base.drift.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Drift](https://www.drift.com/) 账号。
- [创建 Drift 应用](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API personal access token（API 个人访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Drift API 文档](https://devdocs.drift.com/docs/using-drift-apis)。

## 使用 API 个人访问令牌 <a href="#using-api-personal-access-token" id="using-api-personal-access-token"></a>

配置此凭据需要：

- **Personal Access Token**（个人访问令牌）：先[创建 Drift 应用](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-)，再[安装应用](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-)以生成 OAuth 访问令牌。将其填入 n8n 凭据的 **Personal Access Token** 字段。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头配置 OAuth2，或了解 OAuth 网页流程的更多细节，请按照 [Drift 的 Authentication and Scopes 文档](https://devdocs.drift.com/docs/authentication-and-scopes)为应用设置 OAuth。
