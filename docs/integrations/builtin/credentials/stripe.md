---
title: Stripe 凭据
description: Stripe 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Stripe 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Stripe 凭据
originalFilePath: integrations/builtin/credentials/stripe.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/stripe
url: https://docs.n8n.io/integrations/builtin/credentials/stripe
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Stripe 凭据 <a href="#stripe-credentials" id="stripe-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Stripe Trigger（触发器）](../trigger-nodes/n8n-nodes-base.stripetrigger.md)
- [Stripe](../app-nodes/n8n-nodes-base.stripe.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Secret key（秘密密钥）

n8n 还强烈建议设置 **Signature Secret**（签名密钥，有时也称端点密钥）。每个 webhook 端点具有唯一密钥，使 [Stripe Trigger（触发器）](../trigger-nodes/n8n-nodes-base.stripetrigger.md)节点能够验证传入请求确实来自 Stripe。设置步骤，请参阅[验证传入请求](#verify-incoming-requests)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

配置此凭据需要一个 Stripe 管理员或开发者账户。有关该服务的更多信息，请参阅 [Stripe API 文档](https://docs.stripe.com/api)。

生成 API 密钥之前，先决定使用正式模式还是测试模式。两种模式的更多信息，请参阅[测试模式与正式模式](#test-mode-and-live-mode)。

### 正式模式 Secret key（秘密密钥） <a href="#live-mode-secret-key" id="live-mode-secret-key"></a>

在正式模式生成 Secret key 的步骤如下：

1. 打开 [Stripe 开发者控制台](https://dashboard.stripe.com/developers)，选择 [**API Keys**（API 密钥）](https://dashboard.stripe.com/apikeys)。
2. 在 **Standard Keys**（标准密钥）部分，选择 **Create secret key**（创建秘密密钥）。
3. 输入 **Key name**（密钥名称），例如 `n8n integration`。
4. 选择 **Create**（创建），随后显示新的 API 密钥。
4. 复制密钥，填入 n8n 凭据的 **Secret Key**（秘密密钥）。

更多信息，请参阅 Stripe 的[创建秘密 API 密钥](https://docs.stripe.com/keys#create-api-secret-key)。

### 测试模式 Secret key（秘密密钥） <a href="#test-mode-secret-key" id="test-mode-secret-key"></a>

如需在测试模式使用 Secret key，必须复制已有密钥：

1. 打开 [Stripe 测试模式开发者控制台](https://dashboard.stripe.com/test/developers)，选择 [**API Keys**（API 密钥）](https://dashboard.stripe.com/test/apikeys)。
2. 在 **Standard Keys**（标准密钥）部分，为 **Secret key**（秘密密钥）选择 **Reveal test key**（显示测试密钥）。
3. 复制密钥，填入 n8n 凭据的 **Secret Key**（秘密密钥）。

更多信息，请参阅 Stripe 的[创建秘密 API 密钥](https://docs.stripe.com/keys#create-api-secret-key)。

## 验证传入请求 <a href="#verify-incoming-requests" id="verify-incoming-requests"></a>

{% hint style="info" %}
**功能可用范围**

传入请求验证从 n8n 2.25.7 和 n8n 2.26.2 起可用。
{% endhint %}

Stripe Trigger 节点可验证传入的 webhook 请求确实来自 Stripe。

n8n 强烈建议设置 **Signature Secret**（签名密钥），这样即使其他人知道 webhook URL，也无法向工作流发送伪造事件。

发布工作流时，n8n 会为你创建并管理 Stripe webhook 端点，因此应在端点存在后设置 **Signature Secret**（签名密钥）：

1. 使用 **Stripe Trigger** 节点构建工作流并发布。n8n 会在 Stripe 账户中创建 webhook 端点。
2. 在 Stripe 控制台中，进入 **Workbench**（工作台）> **Webhooks**。较旧控制台中，进入 **Developers**（开发者）> **Webhooks**。
3. 选择 n8n 创建的端点。可通过描述 `Created by n8n for workflow ID: <workflow-id>` 和 webhook URL 识别，它的 URL 与 n8n 生产 webhook URL 一致。
4. 在 **Signing secret**（签名密钥）下，选择 **Click to reveal**（点击显示），复制该值。它以 `whsec_` 开头。
5. 在 n8n 中打开 Stripe 凭据，将该值粘贴到 **Signature Secret**（签名密钥）字段并保存。

Stripe 为每个端点生成唯一签名密钥，测试模式和正式模式也各不相同。请从与你使用的凭据匹配的端点复制密钥。更多信息，请参阅 Stripe 的 [Webhook 文档](https://docs.stripe.com/webhooks)。

## 测试模式与正式模式 <a href="#test-mode-and-live-mode" id="test-mode-and-live-mode"></a>

所有 Stripe API 请求都发生在[测试模式](https://docs.stripe.com/test-mode)或正式模式下，每种模式有自己的 API 密钥。

测试模式用于访问模拟测试数据，正式模式用于访问真实账户数据。一种模式中的对象无法从另一种模式访问。

各模式的可用功能及使用建议，请参阅 [API 密钥 | 测试模式与正式模式](https://docs.stripe.com/keys#test-live-modes)。

{% hint style="info" %}
**为两种模式分别保存 n8n 凭据**

如需同时使用正式模式和测试模式的密钥，请为每种模式分别创建 n8n 凭据，保存各自的密钥。
{% endhint %}

## 密钥前缀 <a href="#key-prefixes" id="key-prefixes"></a>

Stripe 的 Secret key 始终以 `sk_` 开头：

- 正式密钥以 `sk_live_` 开头。
- 测试密钥以 `sk_test_` 开头。

n8n 尚未使用 Restricted（受限）密钥（前缀 `rk_`）测试这些凭据。

{% hint style="warning" %}
**Publishable key（可发布密钥）**

请勿将 Publishable key（前缀 `pk_`）用于 n8n 凭据。
{% endhint %}
