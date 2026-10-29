---
title: Anthropic 凭据
description: Anthropic 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Anthropic 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Anthropic 凭据
originalFilePath: integrations/builtin/credentials/anthropic.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/anthropic
url: https://docs.n8n.io/integrations/builtin/credentials/anthropic
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Anthropic 凭据 <a href="#anthropic-credentials" id="anthropic-credentials"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以在支持此功能的节点凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**，无需另行设置 Anthropic 凭据。详情请参阅 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

- [Anthropic](../app-nodes/n8n-nodes-langchain.anthropic.md)
- [Anthropic Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Anthropic 文档](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个可访问 Claude 的 [Anthropic Console 账户](https://console.anthropic.com)。

然后：

1. 在 Anthropic Console 中打开 **Settings >** [**API Keys**](https://console.anthropic.com/settings/keys)（设置 > API 密钥）。
2. 选择 **+ Create Key**（创建密钥）。
3. 为密钥设置 **Name**（名称），例如 `n8n-integration`。
4. 选择 **Copy Key**（复制密钥），复制该密钥。
5. 将其填入 n8n 凭据的 **API Key**（API 密钥）字段。
6. （可选）为 API 请求添加自定义请求头：
    1. 启用 **Add Custom Header**（添加自定义请求头）开关。
    2. 输入自定义请求头的 **Header Name**（请求头名称）。
    3. 输入自定义请求头的 **Header Value**（请求头值）。

更多信息请参阅 Anthropic 的 [Claude 简介](https://docs.anthropic.com/en/docs/intro-to-claude)和[快速入门](https://docs.anthropic.com/en/docs/quickstart)。
