---
title: 向量存储元数据筛选
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

适用于 **Get Many**（获取多条）模式。搜索数据时，使用此项匹配与文档关联的元数据。

这是一个 `AND` 查询。如果指定多个元数据筛选字段，必须全部匹配。

插入数据时，元数据通过文档加载器设置。加载文档的更多信息，请参阅 [Default Data Loader（默认数据加载器）](../../../../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。
