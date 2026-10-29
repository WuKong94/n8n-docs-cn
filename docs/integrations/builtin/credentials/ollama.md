---
title: Ollama 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Ollama 凭据
originalFilePath: integrations/builtin/credentials/ollama.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ollama
url: https://docs.n8n.io/integrations/builtin/credentials/ollama
description: Ollama 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Ollama 的身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Ollama 凭据 <a id="ollama-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Ollama](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/README.md)
* [Chat Ollama（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/README.md)
* [Embeddings Ollama（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建并运行一个只有一个用户的 [Ollama](https://ollama.com/) 实例。更多信息请参阅 Ollama [快速入门](https://github.com/ollama/ollama/blob/main/README.md#quickstart)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Instance URL（实例 URL）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Ollama API 文档](https://github.com/ollama/ollama/blob/main/docs/api.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用实例 URL <a href="#using-instance-url" id="using-instance-url"></a>

配置此凭据需要：

* 你的 Ollama 实例或经过身份验证的远程 Ollama 实例的 **Base URL**（基础 URL）。
* （可选）连接需要身份验证的远程代理时，用于 Bearer 令牌身份验证的 **API Key**（API 密钥）。

默认 **Base URL**（基础 URL）为 `http://localhost:11434`，但如果设置了 `OLLAMA_HOST` 环境变量，请输入该变量的值。如果连接本地 n8n 服务器时遇到问题，可尝试使用 `127.0.0.1` 替代 `localhost`。

如果通过需要身份验证的代理服务（例如 [Open WebUI](https://docs.openwebui.com/getting-started/api-endpoints/#-ollama-api-proxy-support)）连接 Ollama，必须提供 API 密钥。如果无需身份验证，请将此字段留空。提供 API 密钥后，请求 Ollama API 时会将其作为 Bearer 令牌发送到请求的 `Authorization` 头中。

更多信息请参阅[如何配置 Ollama 服务器？](https://github.com/ollama/ollama/blob/main/docs/faq.mdx#how-do-i-configure-ollama-server)

### Ollama 与自行托管的 n8n <a href="#ollama-and-self-hosted-n8n" id="ollama-and-self-hosted-n8n"></a>

如果 Ollama 和 n8n 分别运行在不同的 Docker 容器中，请将两个容器连接到同一个用户自定义桥接网络。将 **Base URL**（基础 URL）设为 `http://<ollama-container>:11434`，将 `<ollama-container>` 替换为 Ollama 容器的名称。例如，容器名称为 `ollama` 时，使用 `http://ollama:11434`。

配置步骤请参阅 [Ollama Chat Model 节点常见问题](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md#if-ollama-and-n8n-are-running-in-separate-docker-containers)。
