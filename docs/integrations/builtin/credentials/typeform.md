---
title: Typeform 凭据
description: Typeform 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Typeform 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Typeform 凭据
originalFilePath: integrations/builtin/credentials/typeform.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/typeform
url: https://docs.n8n.io/integrations/builtin/credentials/typeform
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Typeform 凭据 <a href="#typeform-credentials" id="typeform-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Typeform Trigger（触发器）](../trigger-nodes/n8n-nodes-base.typeformtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Typeform API 文档](https://www.typeform.com/developers/get-started/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要一个 [Typeform](https://typeform.com/) 账号，以及：

- 个人 **Access Token**（访问令牌）

获取个人访问令牌的步骤如下：

1. 登录 Typeform 账户。
2. 选择右上角的个人头像，进入 **Account > Your settings >** [**Personal Tokens**](https://admin.typeform.com/user/tokens)（账户 > 你的设置 > 个人令牌）。
3. 选择 **Generate a new token**（生成新令牌）。
4. 为令牌设置 **Name**（名称），例如 `n8n integration`。
5. 在 **Scopes**（作用域）中选择 **Custom scopes**（自定义作用域），并选择以下作用域：
    - Forms: Read（表单：读取）
    - Webhooks: Read, Write（Webhook：读取、写入）
6. 选择 **Generate token**（生成令牌）。
7. 复制令牌，填入 n8n 凭据。

更多信息，请参阅 Typeform 的[个人访问令牌文档](https://www.typeform.com/developers/get-started/personal-access-token/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Typeform](https://typeform.com/) 账号，以及：

- **Client ID**（客户端 ID）：注册应用时生成。
- **Client Secret**（客户端密钥）：注册应用时生成。

如需获取 Client ID 和 Client Secret，请注册新的 Typeform 应用：

1. 登录 Typeform 账户。
2. 在左上角选择组织的下拉列表，再选择 **Developer apps**（开发者应用）。
3. 选择 **Register a new app**（注册新应用）。
4. 输入适当的 **App Name**（应用名称），例如 `n8n OAuth2 integration`。
5. 将 n8n 基础 URL 填入 **App website**（应用网站），例如 `https://n8n-sample.app.n8n.cloud/`。
6. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Typeform 的 **Redirect URI(s)**（重定向 URI）。
7. 选择 **Register app**（注册应用）。
8. 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
9. 在 Typeform 中选择 **Got it**（知道了），关闭客户端密钥弹窗。
10. **Developer apps**（开发者应用）面板会显示新应用。复制 **Client ID**（客户端 ID），填入 n8n 凭据。
11. 在 n8n 中输入 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）后，选择 **Connect my account**（连接我的账户），按照屏幕提示完成应用授权。

更多信息，请参阅[创建与 Typeform API 集成的应用](https://www.typeform.com/developers/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel)。

## 设置自定义权限范围 <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Typeform OAuth2 凭据默认使用以下作用域：

- `forms:read`
- `webhooks:read`
- `webhooks:write`

如需为凭据选择其他作用域，请启用 **Custom Scopes**（自定义作用域）开关，编辑 **Enabled Scopes**（已启用的作用域）字段。移除默认作用域时请谨慎，这可能使 [Typeform Trigger（触发器）](../trigger-nodes/n8n-nodes-base.typeformtrigger.md)节点停止工作。

全部可用作用域，请参阅 Typeform 的[作用域文档](https://www.typeform.com/developers/get-started/scopes/)。
