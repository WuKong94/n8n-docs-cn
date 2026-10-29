---
title: MiniMax 凭据
description: MiniMax 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MiniMax 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: MiniMax 凭据
originalFilePath: integrations/builtin/credentials/minimax.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/minimax
url: https://docs.n8n.io/integrations/builtin/credentials/minimax
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MiniMax 凭据 <a href="#minimax-credentials" id="minimax-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 MiniMax 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

* [MiniMax](../app-nodes/n8n-nodes-langchain.minimax.md)
* [MiniMax Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MiniMax](https://platform.minimax.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MiniMax API 文档](https://platform.minimax.io/docs/guides/models-intro)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Region**（地区）：根据 MiniMax 账户选择 **International**（国际）或 **China**（中国）。
- 一个 **API Key（API 密钥）**

获取 API 密钥的步骤如下：

1. 登录 [MiniMax 账户](https://platform.minimax.io/)。
2. 进入 **Account**（账户）> **API Keys**（API 密钥）。
3. 选择 **Create API Key**（创建 API 密钥）。
4. 复制密钥，填入 n8n 凭据。
