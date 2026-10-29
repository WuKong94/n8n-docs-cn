---
title: Text Classifier（文本分类器） 节点文档
description: 了解如何在 n8n 中使用 Text Classifier（文本分类器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Text Classifier（文本分类器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Text Classifier（文本分类器） 节点 <a href="#text-classifier-node" id="text-classifier-node"></a>

使用 Text Classifier 节点，对传入数据进行分类。节点将每个数据项传给模型，由模型根据参数中提供的类别（见下文）判断其所属类别。

本页列出了 Text Classifier 节点的参数，并提供更多资源的链接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Input Prompt**（输入提示词）：定义要分类的输入，通常是引用输入项字段的表达式。例如，输入来自聊天触发器时，可使用 `{{ $json.chatInput }}`。默认引用 `text` 字段。
* **Categories**（类别）：添加要将输入划分到的类别。每个类别包含名称和描述。使用描述向模型解释类别的含义，尤其是在含义不明确时。可按需添加任意数量的类别。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Allow Multiple Classes To Be True**（允许匹配多个类别）：关闭时，分类器始终为每个数据项输出一个类别；开启时，允许模型选择多个类别。
* **When No Clear Match**（没有明确匹配时）：定义模型无法为某个数据项找到合适类别时的处理方式，可选：
    - **Discard Item**（丢弃数据项，默认）：节点未检测到任何类别时，丢弃该数据项。
    - **Output on Extra, 'Other' Branch**（输出到额外的 Other 分支）：创建名为 **Other** 的独立输出分支。节点未检测到任何类别时，将数据项输出到此分支。
* **System Prompt Template**（系统提示词模板）：修改分类使用的系统提示词，其中使用 `{categories}` 占位符表示类别。

* **Enable Auto-Fixing**（启用自动修复）：开启后，节点会将架构解析错误发送给 LLM，要求其修复模型输出，以符合预期格式。


## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

