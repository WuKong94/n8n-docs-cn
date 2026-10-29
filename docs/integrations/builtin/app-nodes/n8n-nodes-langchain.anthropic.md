---
title: Anthropic 节点文档
description: 了解如何在 n8n 中使用 Anthropic 节点，并按照技术文档将 Anthropic 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Anthropic 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Anthropic 节点 <a href="#anthropic-node" id="anthropic-node"></a>

{% hint style="info" %}
在 n8n Cloud 上，可以使用 [Gateway 额度](../../../deploy/use-n8n-cloud/gateway-credits/README.md)运行 Anthropic 节点，无需自己的 Anthropic API 密钥。在节点的凭据字段选择 **Use Gateway credits**（使用 Gateway 额度），即可在没有 Anthropic 账户的情况下运行节点。
{% endhint %}

使用 Anthropic 节点自动处理 Anthropic 中的工作，并将其与其他应用集成。n8n 内置支持多种 Anthropic 功能，包括分析、上传、获取和删除文档、文件及图像，以及生成、改进提示词或将提示词模板化。

本页列出了 Anthropic 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

该节点的身份验证信息，请参阅 [Anthropic 凭据文档](../credentials/anthropic.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Document（文档）：
    * Analyze Document（分析文档）：接收文档并回答相关问题。
* File（文件）：
    * Upload File（上传文件）：将文件上传到 Anthropic API，供后续使用。
    * Get File Metadata（获取文件元数据）：从 Anthropic API 获取文件元数据。
    * List Files（列出文件）：列出 Anthropic API 中的文件。
    * Delete File（删除文件）：从 Anthropic API 删除文件。
* Image（图像）：
    * Analyze Image（分析图像）：接收图像并回答相关问题。
* Prompt（提示词）：
    * Generate Prompt（生成提示词）：为模型生成提示词。
    * Improve Prompt（改进提示词）：改进模型的提示词。
    * Templatize Prompt（将提示词模板化）：将模型的提示词转换为模板。
* Text（文本）：
    * Message a Model（向模型发送消息）：使用 Anthropic 模型生成补全结果。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Anthropic 集成模板](https://n8n.io/integrations/anthropic)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Anthropic 文档](https://docs.anthropic.com/en/api/overview)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
