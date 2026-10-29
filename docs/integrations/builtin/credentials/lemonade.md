---
title: Lemonade 凭据
description: Lemonade 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Lemonade 的身份验证。
contentType:
- integration
- reference
nodeTitle: Lemonade 凭据
originalFilePath: integrations/builtin/credentials/lemonade.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/lemonade
url: https://docs.n8n.io/integrations/builtin/credentials/lemonade
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Lemonade 凭据 <a href="#lemonade-credentials" id="lemonade-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Lemonade Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md)
* [Lemonade Model（模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md)
* [Embeddings Lemonade（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

Lemonade 在本地运行 AI 推理。这些节点直接连接到运行于本机或网络中的 Lemonade 服务器进程。在 n8n 中创建凭据前，请先[安装并运行 Lemonade 服务器](https://lemonade-server.ai/install_options.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Lemonade server connection（服务器连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Lemonade 文档](https://lemonade-server.ai/docs/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 配置 Lemonade 服务器连接 <a href="#configuring-lemonade-server-connection" id="configuring-lemonade-server-connection"></a>

配置此凭据需要：

- **Base URL**（基础 URL）：Lemonade 服务器的 URL，包含 API 路径。本地安装的默认值为 `http://localhost:8000/api/v1`。如果在 Docker 中运行 n8n，改用 `http://host.docker.internal:8000/api/v1`。如果 Lemonade 服务器位于远程机器，将 `localhost` 替换为服务器地址。
- **API key**（可选）：用于 Lemonade 服务器身份验证的可选 API 密钥。默认安装的 Lemonade 不需要此值。


