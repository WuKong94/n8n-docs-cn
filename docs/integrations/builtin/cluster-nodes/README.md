---
contentType: overview
title: 集群节点
description: 了解 n8n 中的集群节点，并浏览集群节点库。
nodeTitle: 集群节点
originalFilePath: integrations/builtin/cluster-nodes/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes
url: https://docs.n8n.io/integrations/builtin/cluster-nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 集群节点 <a href="#cluster-nodes" id="cluster-nodes"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/cluster-nodes-summary.md" %}


## 根节点 <a href="#root-nodes" id="root-nodes"></a>

每个集群都以一个[根节点](#user-content-fn-1)[^1]开始。

## 子节点 <a href="#sub-nodes" id="sub-nodes"></a>

每个根节点可以连接一个或多个子节点[^2]。

<a id="user-content-fn-1"></a>
[^1]: 每个 n8n 集群节点都包含一个根节点，用于定义集群的主要功能。一个或多个子节点连接到根节点，以扩展其功能。
[^2]: n8n 集群节点由连接到根节点的一个或多个子节点组成。子节点通过访问特定服务或资源，或提供特定类型的专用处理（例如计算器功能），扩展根节点的功能。
