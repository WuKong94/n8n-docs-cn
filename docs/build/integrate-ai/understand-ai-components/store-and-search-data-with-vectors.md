---
title: 什么是向量数据库？
description: 了解向量数据库，以及 n8n 如何提供向量数据库和配套组件，包括嵌入模型、检索器和文档加载器。
contentType: explanation
nodeTitle: 使用向量存储和搜索数据
originalFilePath: advanced-ai/examples/understand-vector-databases.md
originalUrl: https://docs.n8n.io/advanced-ai/examples/understand-vector-databases
url: https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 什么是向量数据库？ <a href="#what-are-vector-databases" id="what-are-vector-databases"></a>

向量数据库以数字形式存储信息：

> 向量数据库是一种以高维向量形式存储数据的数据库。向量是特征或属性的数学表示。（[来源](https://learn.microsoft.com/en-us/semantic-kernel/memories/vector-db)）

这让快速、准确的相似度搜索成为可能。使用向量数据库时，你可以根据语义和上下文含义搜索相关数据，而不必采用传统数据库查询。

## 一个简化示例 <a href="#a-simplified-example" id="a-simplified-example"></a>

向量数据库可以存储“n8n 是一款源代码可用、支持自托管的自动化工具”这句话。不过，它存储的不是文本，而是表示句子特征的维度数组，在此简化示例中使用 0 到 1 之间的数字。这并不是把句子中的每个字母转换为数字，而是用向量来描述句子。

假设在某个向量存储中，`0.1` 表示 `automation tool`，`0.2` 表示 `source available`，`0.3` 表示 `can be self-hosted`，则可能得到以下向量：

| 句子 | 向量（维度数组） |
| -------- | ------ |
| n8n 是一款源代码可用、支持自托管的自动化工具 | [0.1, 0.2, 0.3] |
| Zapier 是一款自动化工具 | [0.1] |
| Make 是一款自动化工具 | [0.1] |
| Confluence 是一款支持自托管的 wiki 工具 | [0.3] |

{% hint style="info" %}
**此示例经过大幅简化**

实际向量远比这复杂，维度可能从数十到数千不等。维度与单一特征并非一一对应，因此无法将单个维度直接解释为单个概念。此示例仅用于帮助建立大致理解，不能代替准确的技术认识。
{% endhint %}


## 展示相似度搜索的能力 <a href="#demonstrating-the-power-of-similarity-search" id="demonstrating-the-power-of-similarity-search"></a>

Qdrant 提供了[向量搜索演示](https://qdrant.tech/demo/)，帮助用户了解向量数据库的能力。其中的[美食发现演示](https://food-discovery.qdrant.tech/)展示了如何利用向量存储，根据视觉相似性匹配图片。

> 此演示使用外卖服务的数据。用户可以对菜品照片表示喜欢或不喜欢，应用会根据外观推荐更多相似餐食。也可以选择只查看配送范围内餐厅的结果。（[来源](https://qdrant.tech/demo/)）

完整技术细节请参阅 [Qdrant demo-food-discovery GitHub 仓库](https://github.com/qdrant/demo-food-discovery)。

## 嵌入模型、检索器、文本分割器和文档加载器 <a href="#embeddings-retrievers-text-splitters-and-document-loaders" id="embeddings-retrievers-text-splitters-and-document-loaders"></a>

向量数据库需要配合其他工具使用：

- 文档加载器和文本分割器：文档加载器获取文档和数据，为生成嵌入[^1]做好准备。文档加载器可以使用文本分割器，将文档拆分为片段。
- 嵌入模型：将文本、图片等数据转换为向量，用于相似度检索；这不是将向量还原为原始数据的过程。请注意，n8n 仅支持文本嵌入。
- 检索器：从向量数据库中获取相关文档。配合嵌入模型将查询转换为向量，再通过相似度搜索找到对应文档，而不是从向量逆向还原原始数据。

[^1]: 嵌入（embedding）是使用向量对数据进行的数值表示。AI 通过将数值映射到多个维度来理解复杂数据及其关系。向量数据库，也称向量存储，是专门用于存储和访问嵌入的数据库。

## 相关资源 <a id="related-resources"></a>

* [理解 AI 组件](./)
* [链的作用](what-chains-do.md)
* [智能体的作用](what-agents-do.md)
* [记忆的工作原理](how-memory-works.md)
* [工具的工作原理](how-tools-work.md)
* [检索相关上下文](retrieve-relevant-context.md)
* [智能体与链的对比](agents-vs-chains.md)
