---
title: Default Data Loader（默认数据加载器） 节点文档
description: 了解如何在 n8n 中使用 Default Data Loader（默认数据加载器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Default Data Loader（默认数据加载器） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Default Data Loader（默认数据加载器） 节点 <a href="#default-data-loader-node" id="default-data-loader-node"></a>

使用 Default Data Loader 节点，为[向量存储](#user-content-fn-1)[^1]或摘要处理加载二进制数据文件或 JSON 数据。

本页列出了 Default Data Loader 节点支持的参数，并提供更多资源的链接。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text Splitting**（文本拆分）：可选择：
    * **Simple**（简单）：使用 [Recursive Character Text Splitter（递归字符文本拆分器）](n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)，块大小为 1000，重叠量为 200。
    * **Custom**（自定义）：可连接你选择的文本拆分器。
* **Type of Data**（数据类型）：选择 **Binary**（二进制）或 **JSON**。
* **Mode**（模式）：可选择：
    * **Load All Input Data**（加载全部输入数据）：使用节点的所有输入数据。
    * **Load Specific Data**（加载指定数据）：使用[表达式](../../../../build/work-with-data/expressions-versus-data-nodes.md)定义要加载的数据。除表达式外，也可添加文本，从而混合文本和表达式创建自定义文档。
* **Data Format**（数据格式）：**Type of Data**（数据类型）设为 **Binary**（二进制）时显示。选择二进制数据的文件 MIME 类型。如果希望 n8n 自动设置数据格式，选择 **Automatically Detect by MIME Type**（按 MIME 类型自动检测）。指定数据格式后，如果传入文件的 MIME 类型与其不符，节点会报错；使用自动检测时，如果文件 MIME 类型无法匹配受支持的数据格式，节点会回退到文本格式。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Metadata**（元数据）：设置文档在向量存储中应附带的元数据。使用向量存储节点检索数据时，**Metadata Filter**（元数据筛选）选项会与这些元数据匹配。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Default Data Loader（默认数据加载器） 集成模板](https://n8n.io/integrations/default-data-loader)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-doc-loaders-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

<a id="user-content-fn-1"></a>
[^1]: 向量存储或向量数据库用于存储信息的数学表示。将其与嵌入模型和检索器配合使用，可创建供 AI 在回答问题时访问的数据库。
