---
title: PostHog 凭据
description: PostHog 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 PostHog 的身份验证。
contentType:
- integration
- reference
nodeTitle: PostHog 凭据
originalFilePath: integrations/builtin/credentials/posthog.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/posthog
url: https://docs.n8n.io/integrations/builtin/credentials/posthog
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# PostHog 凭据 <a href="#posthog-credentials" id="posthog-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [PostHog](../app-nodes/n8n-nodes-base.posthog.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [PostHog](https://posthog.com/) 账户，或在自己的服务器上托管 PostHog。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [PostHog API 文档](https://posthog.com/docs/api)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- API **URL**：输入适用于 API 请求的域名：
    - 在 US Cloud（美国云）中，公开且仅支持 POST 的端点使用 `https://us.i.posthog.com`，私有端点使用 `https://us.posthog.com`。
    - 在 EU Cloud（欧洲云）中，公开且仅支持 POST 的端点使用 `https://eu.i.posthog.com`，私有端点使用 `https://eu.posthog.com`。
    - 自托管实例使用自己的域名。
    - 检查 PostHog 实例 URL，确认实际所用域名。
- **API Key**（API 密钥）：根据访问公开端点还是私有端点，选择对应的 API 密钥：
    - 公开且仅支持 POST 的端点，使用项目 **General**（常规）设置中的 [Project API key](https://app.posthog.com/project/settings)（项目 API 密钥）。
    - 私有端点，使用用户账户 **Personal API Keys**（个人 API 密钥）设置中的 [Personal API key](https://app.posthog.com/settings/user-api-keys)。更多信息请参阅[如何获取个人 API 密钥](https://posthog.com/docs/api#private-endpoint-authentication)。
