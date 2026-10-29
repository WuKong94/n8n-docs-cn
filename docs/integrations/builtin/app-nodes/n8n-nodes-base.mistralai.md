---
title: Mistral AI 节点
description: 了解如何在 n8n 中使用 Mistral AI 节点，并将其集成到工作流。
contentType:
- integration
- reference
nodeTitle: Mistral AI 节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mistral AI 节点 <a href="#mistral-ai-node" id="mistral-ai-node"></a>

使用 Mistral AI 节点自动处理 Mistral AI 中的工作，并将其与其他应用集成。n8n 内置支持多种模型、文件类型和输入方式的文本提取。

本页列出了 Mistral AI 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关此节点的身份验证信息，请参阅 [Mistral Cloud 凭据文档](../credentials/mistral.md)。
{% endhint %}


## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Resource**（资源）：Mistral AI 要操作的资源。本文对应的实现支持“Document”（文档）资源。
* **Operation**（操作）：要执行的操作：
    * **Extract Text**（提取文本）：使用光学字符识别（OCR）从文档或图片中提取文本。
* **Model**（模型）：用于此操作的模型。本文对应的版本要求使用 `mistral-ocr-latest` 模型。
* **Document Type**（文档类型）：要处理的文档格式，可选“Document”（文档）或“Image”（图片）。
* **Input Type**（输入类型）：文档的输入方式：
    * **Binary Data**（二进制数据）：通过二进制字段将文档传入此节点。
    * **URL**：从指定 URL 获取文档。
* **Input Binary Field**（输入二进制字段）：使用“Binary Data”（二进制数据）输入类型时，指定包含文件的输入二进制字段名称。
* **URL**：使用“URL”输入类型时，指定要处理的文档或图片的 URL。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Enable Batch Processing**（启用批量处理）：是否在同一次 API 调用中处理多个文档。合并请求可能降低成本。
* **Batch Size**（批次大小）：启用“Enable Batch Processing”（启用批量处理）时，设置每批最多处理的文档数量。
* **Delete Files After Processing**（处理后删除文件）：启用“Enable Batch Processing”（启用批量处理）时，选择是否在处理完成后从 Mistral Cloud 删除文件。


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Mistral AI 集成模板](https://n8n.io/integrations/mistral-ai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Mistral AI 文档](https://docs.mistral.ai/api/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
