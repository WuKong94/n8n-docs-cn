---
title: Brave Search 凭据
description: Brave Search 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Brave Search 的身份验证。
contentType:
- integration
- reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Brave Search 凭据 <a id="brave-search-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 Brave Search 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

创建一个 [Brave Search API](https://api.search.brave.com/) 账户。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 [Brave Search API 文档](https://api-dashboard.search.brave.com/documentation)。

## 使用 API 密钥 <a id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：即 Brave Search 订阅令牌。

获取 API 密钥的步骤如下：

1. 进入 [api.search.brave.com](https://api.search.brave.com/) 并注册或登录。
2. 选择订阅方案。Brave 提供每月查询次数有限的免费层级。
3. 进入控制台中的 [API Keys](https://api-dashboard.search.brave.com/app/keys) 页面。
4. 复制 API 密钥，填入 n8n 凭据的 **API Key** 字段。