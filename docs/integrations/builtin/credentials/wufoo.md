---
title: Wufoo 凭据
description: Wufoo 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Wufoo 的身份验证。
contentType:
- integration
- reference
nodeTitle: Wufoo 凭据
originalFilePath: integrations/builtin/credentials/wufoo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/wufoo
url: https://docs.n8n.io/integrations/builtin/credentials/wufoo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wufoo 凭据 <a href="#wufoo-credentials" id="wufoo-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Wufoo Trigger（触发器）](../trigger-nodes/n8n-nodes-base.wufootrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Wufoo](https://wufoo.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Wufoo API 文档](https://wufoo.github.io/docs/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：从 [Wufoo Form Manager（表单管理器）](https://app.wufoo.com/#/form-manager)获取密钥。在表单右侧选择 **More > API Information（更多 > API 信息）**。更多信息请参阅[使用 API 信息和 Webhook](https://help.surveymonkey.com/en/wufoo/integrations/wufoo-api/)。
- 一个 **Subdomain（子域名）**：即 Wufoo URL 中位于 `https://` 之后、`wufoo.com` 之前的部分。例如，完整域名为 `https://n8n.wufoo.com` 时，子域名为 `n8n`。管理员可以在 [**Account Manager（账号管理器）**](https://help.surveymonkey.com/en/wufoo/account/account-manager/)中查看子域名。更多信息请参阅[你的子域名](https://help.surveymonkey.com/en/wufoo/account/your-subdomain/)。

