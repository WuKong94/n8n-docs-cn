---
title: 节点
contentType: overview
hide:
- feedback
- kapaButton
nodeTitle: 集成
originalFilePath: integrations/index.md
originalUrl: https://docs.n8n.io/integrations
url: https://docs.n8n.io/integrations/
description: 了解 n8n 的内置节点、社区节点、MCP 服务器和通用集成。
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点 <a id="nodes"></a>

n8n 将集成称为节点。

节点是 n8n 工作流的构建单元，可以作为获取数据的入口、处理数据的功能模块，或发送数据的出口。数据处理包括筛选、重组和修改数据。一个 API、服务或应用可以对应一个或多个节点。连接多个节点，即可构建复杂工作流。

## 内置节点 <a href="#built-in-nodes" id="built-in-nodes"></a>

n8n 提供多种内置集成。所有内置节点的文档，请参阅[内置节点](builtin/node-types.md)。

## 社区节点 <a href="#community-nodes" id="community-nodes"></a>

除了内置节点，还可以安装社区开发的节点。更多信息，请参阅[社区节点](community-nodes/installation-and-management/README.md)。

## MCP 服务器 <a href="#mcp-servers" id="mcp-servers"></a>

n8n 还提供 MCP 服务器注册表，可直接在节点面板中一键将服务器连接到智能体。更多信息，请参阅 [MCP 服务器](../build/integrate-ai/mcp-servers.md)。

## 仅凭据节点与自定义操作 <a href="#credential-only-nodes-and-custom-operations" id="credential-only-nodes-and-custom-operations"></a>

{% include "../reusable-content/.gitbook/includes/integrations/credential-only-intro.md" %}

更多信息，请参阅[自定义操作](builtin/custom-api-actions-for-existing-nodes.md)。

## 通用集成 <a href="#generic-integrations" id="generic-integrations"></a>

如果 n8n 未为所需服务提供节点或仅凭据节点，仍可使用 [HTTP Request](builtin/core-nodes/n8n-nodes-base.httprequest/README.md) 节点。设置身份验证和创建 API 调用的方法，请参阅该节点文档。

## 后续学习 <a href="#where-to-go-next" id="where-to-go-next"></a>

* 要创建自己的节点，请参阅[创建节点](../connect/create-nodes/overview.md)章节。
* 要了解如何安装和管理社区开发的节点，请参阅[社区节点](community-nodes/using-community-nodes.md)。
* 要了解 n8n 中的各类节点、功能和用法示例，请查看节点库：[核心节点](builtin/core-nodes/README.md)、[动作节点](builtin/app-nodes/README.md)和[触发器节点](builtin/trigger-nodes/README.md)。
* 要了解如何为各类节点添加凭据，请参阅[凭据](builtin/credentials/README.md)章节。
