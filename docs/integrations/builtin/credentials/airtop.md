---
title: Airtop 凭据
description: Airtop 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Airtop 的身份验证。
contentType:
- integration
- reference
nodeTitle: Airtop 凭据
originalFilePath: integrations/builtin/credentials/airtop.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/airtop
url: https://docs.n8n.io/integrations/builtin/credentials/airtop
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Airtop 凭据 <a href="#airtop-credentials" id="airtop-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Airtop](../app-nodes/n8n-nodes-base.airtop.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Airtop](https://portal.airtop.ai/sign-up) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Airtop API 文档](https://docs.airtop.ai/api-reference/airtop-api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Airtop](https://portal.airtop.ai/sign-up) 账户和 **API key**（API 密钥）。生成新密钥：

1. 登录 [Airtop Portal](https://portal.airtop.ai)。
2. 进入 [API Keys](https://portal.airtop.ai/api-keys)（API 密钥）。
3. 选择 **+ Create new key**（创建新密钥）按钮。
4. 输入 API 密钥名称。
5. 选择生成的密钥以复制。
6. 将其填入 n8n 凭据的 **API Key** 字段。

创建 API 密钥时如遇到问题，请联系 [Airtop 支持](https://docs.airtop.ai/guides/misc/support)寻求帮助。
