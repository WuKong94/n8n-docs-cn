---
title: Autopilot 凭据
description: Autopilot 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Autopilot 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Autopilot 凭据
originalFilePath: integrations/builtin/credentials/autopilot.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/autopilot
url: https://docs.n8n.io/integrations/builtin/credentials/autopilot
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Autopilot 凭据 <a href="#autopilot-credentials" id="autopilot-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Autopilot](../app-nodes/n8n-nodes-base.autopilot.md)
- [Autopilot Trigger（触发器）](../trigger-nodes/n8n-nodes-base.autopilottrigger.md)

{% hint style="warning" %}
**Autopilot 品牌名称变更**

Autopilot 已更名为 Ortto。Autopilot 凭据和节点仅兼容原有 Autopilot，不兼容新的 Ortto API。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Autopilot](https://app.autopilothq.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Autopilot API 文档](https://autopilot.docs.apiary.io/#)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：在 **Settings > Autopilot API（设置 > Autopilot API）** 中生成密钥。更多信息请参阅 [Autopilot API 身份验证](https://autopilot.docs.apiary.io/#reference/authentication)。

