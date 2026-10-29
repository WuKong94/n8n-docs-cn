---
title: GraphQL 节点
description: 了解 n8n 中 GraphQL 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: medium
nodeTitle: GraphQL 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.graphql.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.graphql
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.graphql
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GraphQL 节点 <a href="#graphql" id="graphql"></a>

[GraphQL](https://graphql.org/) 是用于 API 的开源数据查询与操作语言，也提供利用现有数据执行查询的运行时。使用 GraphQL 节点查询 GraphQL 端点。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

### Authentication（身份验证） <a href="#authentication" id="authentication"></a>

选择身份验证类型。如果目标服务支持，n8n 建议使用 **Predefined Credential Type**（预定义凭据类型）。与手动配置通用凭据相比，它更便于设置和管理凭据。

选择 **Predefined Credential Type**（预定义凭据类型）后，会出现 **Credential Type**（凭据类型）参数。选择要使用的应用或服务，再选择已有凭据或创建新凭据。更多信息，请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)。

如果选择除 **None**（无）之外的其他身份验证方式，会显示 **Credential for <selected-auth-type>**（所选认证类型的凭据）参数，可选择已有凭据或为该认证类型创建新凭据。

### HTTP Request Method（HTTP 请求方法） <a href="#http-request-method" id="http-request-method"></a>

选择节点底层 HTTP 请求使用的方法，可选：

* **GET**
* **POST**：选择此方法后，还需选择查询载荷使用的 **Request Format**（请求格式），可选：
    * **GraphQL (Raw)**（原始 GraphQL）
    * **JSON**

### Endpoint（端点） <a href="#endpoint" id="endpoint"></a>

输入要访问的 GraphQL 端点。

### Ignore SSL Issues（忽略 SSL 问题） <a href="#ignore-ssl-issues" id="ignore-ssl-issues"></a>

开启此选项时，n8n 会忽略 SSL 证书验证失败。

### Query（查询） <a href="#query" id="query"></a>

输入要执行的 GraphQL 查询。

关于如何编写查询，请参阅[相关资源](#related-resources)。

### Response Format（响应格式） <a href="#response-format" id="response-format"></a>

选择接收查询结果的格式，可选：

* **JSON**
* **String**（字符串）：选择此格式后，输入 **Response Data Property Name**（响应数据属性名称），指定用于存放该字符串的属性。

## Headers（请求头） <a href="#headers" id="headers"></a>

以 **Headers**（请求头）的 **Name**（名称）/**Value**（值）对形式，输入查询中要传递的请求头。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 GraphQL 集成模板](https://n8n.io/integrations/graphql)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

使用 GraphQL 节点需要了解 GraphQL 查询语言，可参考 GraphQL 官方的 [GraphQL 入门](https://graphql.org/learn/)教程。

