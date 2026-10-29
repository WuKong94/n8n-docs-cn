---
title: Wolfram|Alpha 凭据
description: Wolfram|Alpha 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Wolfram|Alpha 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Wolfram|Alpha 凭据
originalFilePath: integrations/builtin/credentials/wolframalpha.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/wolframalpha
url: https://docs.n8n.io/integrations/builtin/credentials/wolframalpha
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wolfram|Alpha 凭据 <a href="#wolframoralpha-credentials" id="wolframoralpha-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Wolfram|Alpha](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Wolfram|Alpha Simple API 文档](https://products.wolframalpha.com/simple-api/documentation)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要已注册的 [Wolfram ID](https://account.wolfram.com)，以及：

- **App ID**（应用 ID）

获取 App ID 的步骤如下：

1. 打开 Wolfram|Alpha Developer Portal（开发者门户），进入 [**API Access**（API 访问）](https://developer.wolframalpha.com/access)。
2. 选择 **Get an App ID**（获取应用 ID）。
3. 输入应用的 **Name**（名称），例如 `n8n integration`。
4. 输入应用的 **Description**（描述）。
5. 将 **API** 设为 **Simple API**。
6. 选择 **Submit**（提交）。
6. 复制生成的 **App ID**（应用 ID），填入 n8n 凭据。

更多信息，请参阅 [Wolfram|Alpha Simple API 文档](https://products.wolframalpha.com/simple-api/documentation)中的 **Getting Started**（入门）。

## 解决 Forbidden（禁止访问）连接错误 <a href="#resolve-forbidden-connection-error" id="resolve-forbidden-connection-error"></a>

输入 App ID 后，如果收到凭据为 **Forbidden**（禁止访问）的错误，请确保已验证 Wolfram ID 的电子邮箱地址：

1. 打开 [Wolfram ID 详情](https://account.wolfram.com/wolframid)。
2. 如果 **Email address**（电子邮箱地址）下未显示 **Verified**（已验证）标签，请选择 **Send a verification email**（发送验证邮件）链接。
3. 必须打开邮件中的链接，验证电子邮箱地址。

验证状态可能需要几分钟才会同步到 API；同步后，重试 n8n 凭据应可成功。
