---
title: Groq 凭据
description: Groq 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Groq 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Groq 凭据
originalFilePath: integrations/builtin/credentials/groq.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/groq
url: https://docs.n8n.io/integrations/builtin/credentials/groq
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Groq 凭据 <a href="#groq-credentials" id="groq-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Groq Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Groq](https://groq.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Groq 文档](https://console.groq.com/docs/quickstart)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

获取 API 密钥的步骤如下：

1. 进入 Groq 控制台的 [API Keys](https://console.groq.com/keys)（API 密钥）页面。
2. 选择 **Create API Key**（创建 API 密钥）。
3. 为密钥输入 **display name**（显示名称），例如 `n8n integration`，再选择 **Submit**（提交）。
4. 复制密钥，粘贴到 n8n 凭据中。

更多信息请参阅 [Groq API Keys 文档](https://console.groq.com/docs/quickstart)。

{% hint style="info" %}
**Groq API 密钥**

Groq 将 API 密钥绑定到组织，而非用户。
{% endhint %}
