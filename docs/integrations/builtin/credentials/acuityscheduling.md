---
title: Acuity Scheduling 凭据
description: Acuity Scheduling 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Acuity Scheduling 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Acuity Scheduling 凭据
originalFilePath: integrations/builtin/credentials/acuityscheduling.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/acuityscheduling
url: https://docs.n8n.io/integrations/builtin/credentials/acuityscheduling
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Acuity Scheduling 凭据 <a href="#acuity-scheduling-credentials" id="acuity-scheduling-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Acuity Scheduling Trigger（触发器）](../trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Acuity Scheduling](https://acuityscheduling.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何使用该服务的更多信息，请参阅 [Acuity API 文档](https://developers.acuityscheduling.com/reference/quick-start)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个数字形式的 **User ID（用户 ID）**
- 一个 **API Key（API 密钥）**

生成 API 密钥和查看用户 ID 的方法，请参阅 [Acuity API 快速入门中的身份验证说明](https://developers.acuityscheduling.com/reference/quick-start#authentication)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果需要从头设置，请填写 [Acuity OAuth2 账号注册页面](https://acuityscheduling.com/oauth2/register)，并使用注册后提供的 **Client ID（客户端 ID）** 和 **Client Secret（客户端密钥）**。
