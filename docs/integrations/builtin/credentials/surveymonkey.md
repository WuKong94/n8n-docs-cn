---
title: SurveyMonkey 凭据
description: SurveyMonkey 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SurveyMonkey 的身份验证。
contentType:
- integration
- reference
nodeTitle: SurveyMonkey 凭据
originalFilePath: integrations/builtin/credentials/surveymonkey.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/surveymonkey
url: https://docs.n8n.io/integrations/builtin/credentials/surveymonkey
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SurveyMonkey 凭据 <a href="#surveymonkey-credentials" id="surveymonkey-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SurveyMonkey Trigger（触发器）](../trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [SurveyMonkey](https://www.surveymonkey.com) 账号。
- 在 [**Developer dashboard > My apps**（开发者控制台 > 我的应用）](https://developer.surveymonkey.com/apps/)中[注册应用](https://api.surveymonkey.com/v3/docs?api_key=3yr7n6m8sjwvm48x8nhxej52#registering-an-app)。
    - 必需作用域的相关信息，请参阅[应用所需作用域](#required-app-scopes)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SurveyMonkey API 文档](https://developer.surveymonkey.com/api/v3/#SurveyMonkey-Api)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- **Access Token**（访问令牌）：创建应用后生成。
- **Client ID**（客户端 ID）：创建应用后生成。
- **Client Secret**（客户端密钥）：创建应用后生成。

创建应用并分配适当作用域后，进入 **Settings > Credentials**（设置 > 凭据）。复制 **Access Token**（访问令牌）、**Client ID**（客户端 ID）和 **Secret**（秘密值），填入 n8n。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：创建应用后生成。
- **Client Secret**（客户端密钥）：创建应用后生成。

创建应用并分配适当作用域后：

1. 进入应用的 **Settings > Settings**（设置 > 设置）。
2. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
3. 用此 URL 覆盖应用现有的 **OAuth Redirect URL**（OAuth 重定向 URL）。
4. 选择 **Submit Changes**（提交更改）。
5. 确保 **Scopes**（作用域）部分包含[应用所需作用域](#required-app-scopes)。

从应用的 **Settings > Credentials**（设置 > 凭据）中，复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据。现在可在 n8n 中选择 **Connect my account**（连接我的账户）。

{% hint style="info" %}
**SurveyMonkey Test OAuth Flow（测试 OAuth 流程）**

此选项仅在保留默认 SurveyMonkey **OAuth Redirect URL**（OAuth 重定向 URL），并将 n8n OAuth 重定向 URL 添加为 **Additional Redirect URL**（其他重定向 URL）时有效。
{% endhint %}

## 应用所需作用域 <a href="#required-app-scopes" id="required-app-scopes"></a>

创建应用后，进入 **Settings > Scopes**（设置 > 作用域）。选择以下作用域，确保 n8n 凭据正常工作：

- **View Surveys**（查看问卷）
- **View Collectors**（查看收集器）
- **View Responses**（查看回答）
- **View Response Details**（查看回答详情）
- **Create/Modify Webhooks**（创建或修改 Webhook）
- **View Webhooks**（查看 Webhook）

选择 **Update Scopes**（更新作用域），保存设置。
