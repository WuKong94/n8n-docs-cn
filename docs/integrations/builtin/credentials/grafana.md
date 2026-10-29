---
title: Grafana 凭据
description: Grafana 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Grafana 的身份验证。
contentType:
- integration
- reference
nodeTitle: Grafana 凭据
originalFilePath: integrations/builtin/credentials/grafana.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/grafana
url: https://docs.n8n.io/integrations/builtin/credentials/grafana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Grafana 凭据 <a href="#grafana-credentials" id="grafana-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Grafana](../app-nodes/n8n-nodes-base.grafana.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Grafana](https://grafana.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [Grafana API 文档](https://grafana.com/docs/grafana/latest/developers/http_api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：创建密钥的详细步骤，请参阅[创建 API 密钥文档](https://grafana.com/docs/grafana/latest/administration/api-keys/#create-an-api-key)。
- Grafana 实例的 **Base URL（基础 URL）**，例如 `https://n8n.grafana.net`。

