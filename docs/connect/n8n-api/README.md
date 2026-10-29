---
title: n8n 公共 REST API 文档与指南
description: 使用 n8n 公共 REST API，以编程方式完成任务。
contentType: overview
search:
  boost: 5
hide:
- feedback
- kapaButton
nodeTitle: n8n API
originalFilePath: api/index.md
originalUrl: https://docs.n8n.io/api
url: https://docs.n8n.io/connect/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 公共 REST API <a href="#n8n-public-rest-api" id="n8n-public-rest-api"></a>

{% hint style="info" %}
**功能可用范围**

n8n API 可用于：

- **n8n Cloud：**Starter、Pro、Enterprise。
- **自托管：**所有版本。

免费试用期间无法使用。
{% endhint %}

通过 n8n 公共 API[^1]，可以用编程方式完成图形界面中的许多同类任务。对于支持的 POST 请求，[幂等键](idempotency.md)可使重试返回第一次成功的响应，避免重复执行请求。

n8n 提供 [n8n API 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)，供工作流访问 API。

## 本节内容 <a id="in-this-section"></a>

* [身份验证](authentication.md)：如何验证 n8n API 请求。
* [分页](pagination.md)：对大型结果集分页。
* [幂等性](idempotency.md)：使用 `Idempotency-Key` 请求头重试 POST。
* [使用 API 测试台](use-an-api-playground.md)：在内置测试台中尝试 API（仅自托管 n8n）。
* [端点参考](api-reference.md)：由 OpenAPI 规范生成的完整端点参考。

## 选择交互方式 <a href="#choose-your-interaction-method" id="choose-your-interaction-method"></a>

### REST API（本节） <a href="#rest-api-this-section" id="rest-api-this-section"></a>
使用 HTTP 请求直接与 n8n 交互，适合：
* 自定义集成和应用。
* 不依赖特定编程语言的 HTTP 调用。
* 在工作流中直接使用 REST API。

### n8n CLI（推荐开发者使用） <a href="#n8n-cli-recommended-for-developers" id="n8n-cli-recommended-for-developers"></a>
使用 [n8n CLI](../n8n-cli.md) 获得命令行操作体验。它封装了公共 API，适合：
* 命令行自动化与脚本。
* CI/CD 流水线集成。
* AI 智能体集成（Claude Code、Cursor 等）。
* 偏好 CLI 工具的开发者。

## 了解 REST API <a href="#learn-about-rest-apis" id="learn-about-rest-apis"></a>

API 文档假定你已熟悉 REST API。如果尚不了解，以下资源可能有帮助：

* [KnowledgeOwl 的 API 使用指南](https://support.knowledgeowl.com/help/working-with-apis)：基础介绍，包含 REST API 调用示例。
* [IBM Cloud Learn Hub：什么是应用程序编程接口（API）](https://www.ibm.com/cloud/learn/api)：从技术角度介绍 API 的一般概念。
* [IBM Cloud Learn Hub：什么是 REST API？](https://www.ibm.com/cloud/learn/rest-apis)：更详细地介绍 REST API。
* [MDN Web 文档：HTTP 概览](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)：REST API 通过 HTTP 工作，并使用 HTTP 动词（方法）指定要执行的操作。

{% hint style="info" %}
**使用 API 测试台**

在[测试台](use-an-api-playground.md)中尝试 API，有助于理解 API 的工作方式。如果担心更改正式数据，可以建立测试工作流或测试 n8n 实例。
{% endhint %}

[^1]: API（应用程序编程接口）提供以编程方式访问服务数据和功能的方法，让软件更容易与外部系统交互。它常作为通过浏览器或图形界面操作的传统用户界面的替代方式。

## 相关资源 <a id="related-resources"></a>

* [连接](../)
* [n8n CLI](../n8n-cli.md)
* [连接 n8n MCP 服务器](../connect-to-n8n-mcp-server.md)
* [连接 n8n 文档 MCP 服务器](../connect-to-n8n-docs-mcp-server.md)
* [创建节点](../create-nodes/README.md)
