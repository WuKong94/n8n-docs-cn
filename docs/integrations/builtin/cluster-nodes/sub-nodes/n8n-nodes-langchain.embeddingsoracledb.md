---
title: Embeddings Oracle Database（Oracle Database 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings Oracle Database（Oracle Database 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings Oracle Database（Oracle Database 嵌入模型） 节点 <a id="embeddings-oracle-database-node"></a>

使用 Embeddings Oracle Database 节点，通过存储在 Oracle Database 中的 ONNX 模型生成嵌入向量[^1]。此节点适用于语义搜索、相似度匹配、检索增强生成，以及其他需要文本向量表示的工作流。

本页列出了 Embeddings Oracle Database 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Oracle Database 凭据文档](../../credentials/oracledb.md)。
{% endhint %}

{% hint style="info" %}
**ONNX 模型**

Oracle Database 实例必须支持 Oracle AI Vector Search 和 ONNX 模型执行功能。

使用此节点前，请向 Oracle Database 导入一个或多个 ONNX 嵌入模型。仅已导入的模型可供选择。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a id="node-parameters"></a>

* **Model**（模型）：选择用于生成嵌入向量的 ONNX 模型。可从 Oracle Database 实例的可用模型列表中选择，也可手动指定模型 ID。所选模型决定嵌入维度和支持的输入类型。

节点通过已配置的 Oracle Database 连接，从 `USER_MINING_MODELS` 视图加载可用模型，仅显示当前数据库用户可访问的模型。

## 模板与示例 <a id="templates-and-examples"></a>

[浏览 Embeddings Oracle Database（Oracle Database 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-oracle-database)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a id="related-resources"></a>

向 Oracle Database 导入 ONNX 模型的更多信息，请参阅 [Oracle 的 ONNX 模型导入文档](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/import-onnx-models-oracle-ai-database-end-end-example.html)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
