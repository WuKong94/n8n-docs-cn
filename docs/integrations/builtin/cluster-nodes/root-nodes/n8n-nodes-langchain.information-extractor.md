---
title: Information Extractor（信息提取器） 节点文档
description: 了解如何在 n8n 中使用 Information Extractor（信息提取器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Information Extractor（信息提取器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Information Extractor（信息提取器） 节点 <a href="#information-extractor-node" id="information-extractor-node"></a>

使用 Information Extractor 节点，从传入数据中提取结构化信息。

本页列出了 Information Extractor 节点的参数，
并提供更多资源的链接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text**（文本）：定义要从中提取信息的输入文本，通常是引用输入项字段的表达式。例如，输入来自聊天触发器时，可使用 `{{ $json.chatInput }}`；前一个节点为 Extract from PDF 时，可使用 `{{ $json.text }}`。
* 使用 **Schema Type**（架构类型）选择如何描述所需的输出数据格式。可选：
    * **From Attribute Descriptions**（根据属性描述）：指定属性及其描述列表来定义架构。
    * **Generate From JSON Example**（根据 JSON 示例生成）：输入 JSON 对象示例，自动生成架构。节点使用对象属性的类型和名称，忽略实际值。根据 JSON 示例生成架构时，n8n 将每个字段都视为必填字段。
    * **Define using JSON Schema**（使用 JSON Schema 定义）：手动输入 JSON Schema。创建有效 JSON Schema 的帮助信息，请参阅 JSON Schema [指南与示例](https://json-schema.org/learn/miscellaneous-examples)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **System Prompt Template**（系统提示词模板）：修改信息提取使用的系统提示词。n8n 会自动在提示词后附加格式规范指令。


## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

