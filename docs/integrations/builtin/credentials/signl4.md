---
title: SIGNL4 凭据
description: SIGNL4 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SIGNL4 的身份验证。
contentType:
- integration
- reference
nodeTitle: SIGNL4 凭据
originalFilePath: integrations/builtin/credentials/signl4.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/signl4
url: https://docs.n8n.io/integrations/builtin/credentials/signl4
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SIGNL4 凭据 <a href="#signl4-credentials" id="signl4-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SIGNL4](../app-nodes/n8n-nodes-base.signl4.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SIGNL4](https://www.signl4.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Webhook secret（Webhook 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [SIGNL4 Inbound Webhook 文档](https://connect.signl4.com/webhook/docs/index.html)。

## 使用 Webhook 密钥 <a href="#using-webhook-secret" id="using-webhook-secret"></a>

配置此凭据需要：

- **Team Secret**（团队密钥）：SIGNL4 会在“✅ Sign up complete”邮件中提供此密钥，它是 Webhook URL 的最后一段。例如，Webhook URL 为 `https://connect.signl4.com/webhook/helloworld` 时，团队密钥为 `helloworld`。

