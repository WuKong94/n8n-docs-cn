---
title: 向量存储结果重排序
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

启用重排序。开启此选项后，必须将 [Reranker Cohere（Cohere 重排序器）](../../../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md)等重排序节点连接到向量存储，由其重新排列查询结果。此选项可用于 `Get Many`、`Retrieve Documents (As Vector Store for Chain/Tool)` 和 `Retrieve Documents (As Tool for AI Agent)` 模式。
