---
title: ClickUp 凭据
description: ClickUp 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 ClickUp 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: ClickUp 凭据
originalFilePath: integrations/builtin/credentials/clickup.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/clickup
url: https://docs.n8n.io/integrations/builtin/credentials/clickup
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ClickUp 凭据 <a href="#clickup-credentials" id="clickup-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [ClickUp](../app-nodes/n8n-nodes-base.clickup.md)
- [ClickUp Trigger（触发器）](../trigger-nodes/n8n-nodes-base.clickuptrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ClickUp 文档](https://clickup.com/api/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [ClickUp](https://www.clickup.com/) 账号，以及：

- 个人 API **Access Token**（访问令牌）

获取个人 API 令牌的步骤如下：

1. 使用 ClickUp 2.0 时，选择左下角的头像，再选择 **Apps**（应用）。使用 ClickUp 3.0 时，选择右上角的头像，选择 **Settings**（设置），向下滚动后在侧边栏选择 **Apps**（应用）。
2. 在 **API Token**（API 令牌）下选择 **Generate**（生成）。
3. 复制 **Personal API token**（个人 API 令牌），填入 n8n 凭据的 **Access Token**（访问令牌）。

更多信息，请参阅 [ClickUp 个人令牌文档](https://clickup.com/api/developer-portal/authentication#personal-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，则需要创建 OAuth 应用：

1. 在 ClickUp 中选择头像，再选择 **Integrations**（集成）。
2. 选择 **ClickUp API**。
3. 选择 **Create an App**（创建应用）。
4. 输入应用的 **Name**（名称）。
5. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 ClickUp 应用的 **Redirect URL**（重定向 URL）。
6. 创建应用后，复制 **client_id** 和 **secret**，填入 n8n 凭据。
7. 选择 **Connect my account**（连接我的账户），按照屏幕提示完成凭据连接。

 更多信息，请参阅 [ClickUp OAuth 流程文档](https://clickup.com/api/developer-portal/authentication#oauth-flow)。
