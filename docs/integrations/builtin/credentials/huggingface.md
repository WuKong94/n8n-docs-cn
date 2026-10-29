---
title: Hugging Face 凭据
description: Hugging Face 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Hugging Face 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Hugging Face 凭据
originalFilePath: integrations/builtin/credentials/huggingface.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/huggingface
url: https://docs.n8n.io/integrations/builtin/credentials/huggingface
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Hugging Face 凭据 <a href="#hugging-face-credentials" id="hugging-face-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Hugging Face Inference（推理）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md)
* [Embeddings Hugging Face Inference（嵌入推理）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Hugging Face 文档](https://huggingface.co/docs/api-inference/quicktour)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Hugging Face](https://huggingface.co/) 账号，以及：

- **API Key**（API 密钥）：Hugging Face 将其称为 API token（API 令牌）。

获取 API 令牌：

1. 打开 Hugging Face 个人资料，进入 [**Tokens**](https://huggingface.co/settings/tokens)（令牌）部分。
2. 复制其中列出的令牌，它应以 `hf_` 开头。
3. 将此 API 令牌填入 n8n 凭据的 **API Key** 字段。

更多信息请参阅[获取 API 令牌](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token)。
