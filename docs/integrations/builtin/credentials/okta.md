---
title: Okta 凭据
description: Okta 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Okta 的身份验证。
contentType:
- integration
- reference
nodeTitle: Okta 凭据
originalFilePath: integrations/builtin/credentials/okta.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/okta
url: https://docs.n8n.io/integrations/builtin/credentials/okta
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Okta 凭据 <a href="#okta-credentials" id="okta-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Okta](../app-nodes/n8n-nodes-base.okta.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Okta 免费试用](https://www.okta.com/free-trial/)账户，或在现有 Okta 组织中创建管理员账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- SSWS API Access token（SSWS API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Okta 文档](https://developer.okta.com/docs/reference/)。

## 使用 SSWS API 访问令牌 <a href="#using-ssws-api-access-token" id="using-ssws-api-access-token"></a>

配置此凭据需要：

- **URL**：Okta 组织的基础 URL，也称专属子域名。有两种快速获取方式：
    1. 在 Admin Console（管理控制台）中选择 **Profile**（个人资料），将鼠标悬停在用户名下方的域名上，再选择 **Copy**（复制）图标。粘贴到 n8n，并确保在前面加上 `https://`。
    2. 复制 Admin Console 地址中的基础 URL，例如 `https://dev-123456-admin.okta.com`。粘贴到 n8n，并移除 `-admin`，例如 `https://dev-123456.okta.com`。
- **SSWS Access Token**（SSWS 访问令牌）：进入 **Security > API > Tokens > Create token**（安全 > API > 令牌 > 创建令牌）创建。更多信息请参阅[创建 Okta API 令牌](https://help.okta.com/en-us/content/topics/security/api.htm?cshid=ext-create-api-token#create-okta-api-token)。
