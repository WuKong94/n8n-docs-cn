---
title: Flow 凭据
description: Flow 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Flow 的身份验证。
contentType:
- integration
- reference
nodeTitle: Flow 凭据
originalFilePath: integrations/builtin/credentials/flow.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/flow
url: https://docs.n8n.io/integrations/builtin/credentials/flow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Flow 凭据 <a href="#flow-credentials" id="flow-credentials"></a>


{% hint style="warning" %}
**功能可用范围**

Flow 服务已关闭，其 API 不再响应，因此 Flow 和 Flow Trigger（触发器）节点无法连接到该服务。使用这些节点的工作流将会失败。请移除这些节点，或改用其他服务。
{% endhint %}

这些凭据可用于以下节点的身份验证：

- [Flow](../app-nodes/n8n-nodes-base.flow.md)
- [Flow Trigger（触发器）](../trigger-nodes/n8n-nodes-base.flowtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 Flow 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 你的数字形式的 **Organization ID（组织 ID）**
- 一个 **Access Token（访问令牌）**
