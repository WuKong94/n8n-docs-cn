---
title: AI Transform（AI 转换）
contentType:
- integration
- reference
nodeTitle: AI Transform（AI 转换）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform
description: 工作流自动化平台 n8n 中的 AI Transform（AI 转换） 节点文档，包括使用说明和示例链接。
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


# AI Transform（AI 转换） <a id="ai-transform"></a>

使用 AI Transform 节点，根据提示词生成代码片段。AI 能感知上下文，理解工作流中的节点及其数据类型。

{% hint style="info" %}
**功能可用性**

AI Transform 节点可用于：

- **n8n Cloud：**所有套餐。

自行托管的 n8n 不提供此节点。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Instructions（指令） <a href="#instructions" id="instructions"></a>

输入给 AI 的提示词，点击 **Generate code**（生成代码）按钮，即可自动填充 **Transformation Code**（转换代码）。例如，可指定希望如何处理数据或对数据分类。更多信息请参阅[编写优质提示词](../../../build/code-in-n8n/get-coding-help-from-ai.md#writing-good-prompts)。

提示词应使用普通英文，且少于 500 个字符。

### Transformation Code（转换代码） <a href="#transformation-code" id="transformation-code"></a>

节点生成的代码片段为只读。要编辑代码，请调整 **Instructions**（指令）中的提示词，或将代码复制并粘贴到 [Code](n8n-nodes-base.code/README.md) 节点。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AI Transform（AI 转换） 集成模板](https://n8n.io/integrations/ai-transform)，或[搜索所有模板](https://n8n.io/workflows/)
