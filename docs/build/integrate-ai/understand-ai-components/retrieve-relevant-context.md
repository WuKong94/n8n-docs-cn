---
title: n8n 中的 RAG
description: 通过检索增强生成（RAG），让模型访问与上下文相关的资源，以生成切题的回答。了解其原理，以及如何在 n8n 中使用 RAG。
contentType: overview
nodeTitle: 检索相关上下文
originalFilePath: advanced-ai/rag-in-n8n.md
originalUrl: https://docs.n8n.io/advanced-ai/rag-in-n8n
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->





# n8n 中的 RAG <a href="#rag-in-n8n" id="rag-in-n8n"></a>

## 什么是 RAG <a href="#what-is-rag" id="what-is-rag"></a>

[检索增强生成（RAG）](#user-content-fn-1)[^1]将语言模型与外部数据源结合，以改善 AI 的回答。RAG 系统不只依赖模型内部的训练数据，还会检索相关文档，使回答以最新、特定领域或专有知识为依据[^2]。RAG 工作流通常依赖向量存储来高效管理和搜索这些外部数据。

## 什么是向量存储？ <a href="#what-is-a-vector-store" id="what-is-a-vector-store"></a>

[向量存储](#user-content-fn-3)[^3]是一种专门用于存储和搜索高维向量的数据库，向量可以表示文本、图片或其他数据。上传文档后，向量存储会将其拆分为片段，并通过[嵌入模型](#user-content-fn-4)[^4]将各片段转换为向量。

你可以通过相似度搜索查询这些向量，搜索结果依据的是*语义*，而非关键词匹配。因此，向量存储是 RAG 及其他需要检索大量知识并据此推理的 AI 系统的重要基础。

## 如何在 n8n 中使用 RAG <a href="#how-to-use-rag-in-n8n" id="how-to-use-rag-in-n8n"></a>

{% hint style="info" %}
**从 RAG 模板开始**

👉 使用 [RAG 入门模板](https://n8n.io/workflows/5010-rag-starter-template-using-simple-vector-stores-form-trigger-and-openai)，体验 n8n 中的 RAG。模板包含两个现成工作流：一个用于上传文件，另一个用于查询文件。
{% endhint %}

### 向向量存储中插入数据 <a href="#inserting-data-into-your-vector-store" id="inserting-data-into-your-vector-store"></a>

智能体访问自定义知识前，需要先将数据上传到向量存储：

1. 添加获取源数据所需的节点。
2. 插入一个 **Vector Store（向量存储）**节点，例如 [Simple Vector Store](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md)，选择 **Insert Documents（插入文档）**操作。
3. 选择**嵌入模型**，将文本转换为向量嵌入。有关[选择合适的嵌入模型](#how-do-i-choose-the-right-embedding-model)，请参阅常见问题。
4. 添加 [Default Data Loader](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md) 节点，将内容拆分为片段。可以使用默认设置，或自行定义分块策略：
	* **Character Text Splitter（字符文本分割器）**：按字符长度拆分。
	* **Recursive Character Text Splitter（递归字符文本分割器）**：根据 Markdown、HTML、代码块或普通字符递归拆分，推荐用于大多数场景。
	* **Token Text Splitter（Token 文本分割器）**：按 token 数量拆分。
5. （可选）为每个片段添加**元数据**，丰富上下文，便于后续筛选。

### 查询数据 <a href="#querying-your-data" id="querying-your-data"></a>

主要有两种查询方式：使用智能体，或直接通过节点查询。

### 使用智能体 <a href="#using-agents" id="using-agents"></a>

1. 在工作流中添加一个[智能体](../../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)。
2. 将向量存储作为**工具**添加，并填写**说明**，帮助智能体判断何时使用：
	* 设置 **limit（数量限制）**，指定返回的片段数量。
	* 启用 **Include Metadata（包含元数据）**，为每个片段提供更多上下文。
3. 添加与插入数据时相同的**嵌入模型**。

{% hint style="info" %}
**实用技巧**

为减少高价模型消耗的 token，可以先通过 [Vector Store Question Answer 工具](../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md)检索相关数据，再将结果传递给 Agent。具体做法请参阅[此模板](https://n8n.io/workflows/5011-save-costs-in-rag-workflows-using-the-qanda-tool-with-multiple-models)。
{% endhint %}

### 直接使用节点 <a href="#using-the-node-directly" id="using-the-node-directly"></a>

1. 将向量存储节点添加到画布，选择 **Get Many（获取多条）**操作。
2. 输入查询或提示词：
	* 设置 **limit（数量限制）**，指定返回的片段数量。
	* 按需启用 **Include Metadata（包含元数据）**。

## 常见问题 <a href="#faqs" id="faqs"></a>


### 如何选择合适的嵌入模型？ <a href="#how-do-i-choose-the-right-embedding-model" id="how-do-i-choose-the-right-embedding-model"></a>


合适的嵌入模型因场景而异。

一般来说，较小的模型，例如 `text-embedding-ada-002`，速度更快、成本更低，适用于简短的通用文档或轻量 RAG 工作流。较大的模型，例如 `text-embedding-3-large`，语义理解能力更强，适用于长文档、复杂主题或对准确性要求高的场景。


### 我的场景适合哪种文本分块方式？ <a href="#what-is-the-best-text-splitting-for-my-use-case" id="what-is-the-best-text-splitting-for-my-use-case"></a>


这同样很大程度上取决于数据：

* 较小的片段，例如 200 到 500 个 token，适合精细检索。
* 较大的片段可以保留更多上下文，但信息可能被稀释或混入噪声。

合适的片段重叠大小有助于 AI 理解片段上下文。这也是为什么使用 Markdown 或代码块拆分，往往能改善分块效果。

另一种好方法是为片段补充更多上下文，例如其来源文档的信息。想进一步了解，可以参阅 [Anthropic 的这篇文章](https://www.anthropic.com/news/contextual-retrieval)。

<a id="user-content-fn-1"></a>
[^1]: 检索增强生成（RAG）是一种让 LLM 访问外部来源的新信息，从而改善 AI 回答的技术。RAG 系统检索相关文档，使回答以最新、特定领域或专有知识为依据，补充原有训练数据。RAG 系统通常依赖向量存储，高效管理和搜索这些外部数据。
[^2]: 在 AI，尤其是检索增强生成（RAG）场景中，有据性（groundedness）衡量模型回答准确反映来源信息的程度。有据回答基于源文档生成；缺乏依据的回答则包含源文档无法支持的猜测或幻觉。
<a id="user-content-fn-3"></a>
[^3]: 向量存储，也称向量数据库，用数学形式表示并存储信息。将其与嵌入模型和检索器配合使用，可以创建供 AI 回答问题时访问的数据库。
<a id="user-content-fn-4"></a>
[^4]: 嵌入（embedding）是使用向量对数据进行的数值表示。AI 通过将数值映射到多个维度来理解复杂数据及其关系。向量数据库，也称向量存储，是专门用于存储和访问嵌入的数据库。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [链的作用](what-chains-do.md)
* [智能体的作用](what-agents-do.md)
* [记忆的工作原理](how-memory-works.md)
* [工具的工作原理](how-tools-work.md)
* [使用向量存储和搜索数据](store-and-search-data-with-vectors.md)
* [智能体与链的对比](agents-vs-chains.md)
