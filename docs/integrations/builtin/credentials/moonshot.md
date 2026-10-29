---
title: Moonshot 凭据
description: Moonshot 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Moonshot 的身份验证。
contentType:
- integration
- reference
nodeTitle: Moonshot 凭据
originalFilePath: integrations/builtin/credentials/moonshot.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/moonshot
url: https://docs.n8n.io/integrations/builtin/credentials/moonshot
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->



# Moonshot 凭据 <a href="#moonshot-credentials" id="moonshot-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 Moonshot 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

* [Moonshot Kimi](../app-nodes/n8n-nodes-langchain.moonshot.md)
* [Moonshot Kimi Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Kimi API Platform 账户](https://platform.kimi.ai/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Moonshot 文档](https://platform.kimi.ai/docs/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Kimi API Platform](https://platform.kimi.ai/) 账户和 API 密钥：

1. 在 [Kimi API Platform 控制台](https://platform.kimi.ai/console/api-keys)中选择 **API Keys**（API 密钥）。
2. 选择 **Create API Key**（创建 API 密钥）。
3. 为 API 密钥输入 **name**（名称）和 **project**（项目）。
4. 复制 API 密钥，填入 n8n 凭据。
