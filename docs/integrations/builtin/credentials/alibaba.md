---
title: Qwen Cloud 凭据
description: Qwen Cloud 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Qwen Cloud 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Qwen Cloud 凭据
originalFilePath: integrations/builtin/credentials/alibaba.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/alibaba
url: https://docs.n8n.io/integrations/builtin/credentials/alibaba
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Qwen Cloud 凭据 <a href="#alibaba-cloud-credentials" id="alibaba-cloud-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 Qwen Cloud 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

- [Qwen Cloud](../app-nodes/n8n-nodes-langchain.alibabacloud.md)
- [Qwen Cloud Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Qwen Cloud](https://qwencloud.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Qwen Cloud API 密钥文档](https://docs.qwencloud.com/developer-guides/administration/api-keys)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

1. 登录 [Qwen Cloud](https://qwencloud.com/)。
2. 进入 **API Keys**（API 密钥）。
3. 使用侧边栏底部的工作区切换器，选择要在其中创建密钥的工作区。
4. 选择 **Create API key**（创建 API 密钥）。
5. 输入描述，再选择 **Generate Key**（生成密钥）。
6. 复制 API 密钥，密钥只会显示一次。
7. 将 API 密钥填入 n8n 凭据。
8. 对于 Qwen Cloud 账户，将 **Region**（地区）设为 **Singapore**（新加坡）。只有使用 Alibaba Cloud Model Studio 时，才选择其他地区。

更多信息请参阅 [Qwen Cloud API 密钥文档](https://docs.qwencloud.com/developer-guides/administration/api-keys)。
