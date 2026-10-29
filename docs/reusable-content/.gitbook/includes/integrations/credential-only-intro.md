---
title: 仅凭据节点简介
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

设置 API 调用时，管理身份验证是最复杂的部分之一。对于内置节点尚未支持的操作和服务，n8n 也提供[凭据](../../../../get-started/key-concept-glossary.md#credential-n8n)支持。

* 现有节点的自定义操作：n8n 提供数百个节点，可构建连接多个产品的工作流。但部分节点没有涵盖产品 API 支持的全部操作。此时可以通过 [HTTP Request](../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md) 节点发起自定义 API 调用。
* 仅凭据节点：n8n 提供某些集成的凭据配置，供 HTTP Request 节点使用，但不提供独立节点。这些集成称为仅凭据节点。与其他集成一样，可以在节点面板中找到它们。
