---
title: PostBin 节点文档
description: 了解如何在 n8n 中使用 PostBin 节点，并按照技术文档将 PostBin 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: PostBin 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postbin.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# PostBin 节点 <a href="#postbin-node" id="postbin-node"></a>

PostBin 是用于测试 API 客户端和 Webhook 的服务。使用 PostBin 节点自动处理 PostBin 中的工作，并将其与其他应用集成。n8n 内置支持多种 PostBin 功能，包括创建和删除 Bin（请求收集箱），以及获取和发送请求。

本页列出了 PostBin 节点支持的操作，并提供更多资源的链接。

## 操作 <a href="#operations" id="operations"></a>

* Bin（请求收集箱）
	* Create（创建）
	* Get（获取）
	* Delete（删除）
* Request（请求）
	* Get（获取）
	* Remove First（移除首条请求）
	* Send（发送）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 PostBin 集成模板](https://n8n.io/integrations/postbin)，或[搜索所有模板](https://n8n.io/workflows/)

## 发送请求 <a href="#send-requests" id="send-requests"></a>

向 PostBin 的 Bin 发送请求：

1. 进入 [PostBin](https://www.toptal.com/developers/postbin/)，按步骤生成新 Bin。PostBin 会提供包含 Bin ID 的专属 URL。
2. 在 PostBin 节点中选择 **Request**（请求）资源。
3. 选择要执行的 **Operation**（操作）类型。
4. 在 **Bin ID** 中输入 Bin ID。

## 创建和管理 Bin <a href="#create-and-manage-bins" id="create-and-manage-bins"></a>

可以通过 PostBin 节点创建和管理 PostBin 的 Bin。

1. 在 **Resource**（资源）中选择 **Bin**。
2. 选择 **Operation**（操作），可以创建、删除或获取 Bin。
