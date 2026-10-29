---
title: Plivo 凭据
description: Plivo 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Plivo 的身份验证。
contentType:
- integration
- reference
nodeTitle: Plivo 凭据
originalFilePath: integrations/builtin/credentials/plivo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/plivo
url: https://docs.n8n.io/integrations/builtin/credentials/plivo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Plivo 凭据 <a href="#plivo-credentials" id="plivo-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Plivo](../app-nodes/n8n-nodes-base.plivo.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Plivo](https://www.plivo.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Plivo API 文档](https://www.plivo.com/docs/voice/api/overview/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 一个 **Auth ID（身份验证 ID）**：相当于用户名。从 Plivo [控制台](https://console.plivo.com/dashboard/)的 **Overview（概览）** 页面复制。
- 一个 **Auth Token（身份验证令牌）**：相当于密码。从 Plivo [控制台](https://console.plivo.com/dashboard/)的 **Overview（概览）** 页面复制。

详细说明请参阅[如何更改 Auth ID 或 Auth Token？](https://support.plivo.com/hc/en-us/articles/360041731231-How-can-I-change-my-Auth-ID-or-Auth-Token)。

