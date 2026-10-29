---
title: Cortex 凭据
description: Cortex 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cortex 的身份验证。
contentType:
- integration
- reference
nodeTitle: Cortex 凭据
originalFilePath: integrations/builtin/credentials/cortex.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cortex
url: https://docs.n8n.io/integrations/builtin/credentials/cortex
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cortex 凭据 <a href="#cortex-credentials" id="cortex-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Cortex](../app-nodes/n8n-nodes-base.cortex.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在服务器上安装 [Cortex](https://docs.strangebee.com/cortex/installation-and-configuration/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cortex API 文档](https://docs.strangebee.com/cortex/api/api-guide/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：生成密钥的详细步骤，请参阅 [Cortex API 身份验证文档](https://docs.strangebee.com/cortex/api/api-guide/#authentication)。
- **Cortex Instance（实例）** 的 URL／服务器地址，默认值为 `http://<your_server_address>:9001/`。

