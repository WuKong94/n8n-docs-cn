---
title: n8n 代码使用文档与指南
description: 查阅在 n8n 中使用代码和表达式的文档、指南及其他开发者资源。
contentType: overview
hide:
- feedback
- kapaButton
nodeTitle: 在 n8n 中编写代码
originalFilePath: code/index.md
originalUrl: https://docs.n8n.io/code
url: https://docs.n8n.io/build/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 n8n 中编写代码 <a href="#code-in-n8n" id="code-in-n8n"></a>

n8n 是低代码工具。这意味着无需代码就能完成许多任务，并可在需要时加入代码。

## 本节内容 <a id="in-this-section"></a>

* [使用 Code 节点](using-the-code-node.md)：向工作流添加 JavaScript 或 Python 代码。
* [获取 AI 编程帮助](get-coding-help-from-ai.md)：使用 GPT 在 Code 节点中生成代码。
* [使用内置快捷方法](use-built-in-shortcuts.md)：查阅可用于表达式和代码的 n8n 内置方法与变量。
* [定义自定义变量](define-custom-variables.md)：在工作流之间存储和复用值。
* [实用示例](cookbook/README.md)：常见编程任务的示例与解决方法。

## 工作流中的代码 <a href="#code-in-your-workflows" id="code-in-your-workflows"></a>

工作流中有两处可以使用代码：

<div class="grid-cards-vertical cards" markdown>

- __表达式__

	使用表达式[^1]转换节点中的[数据](../work-with-data/README.md)。表达式中可以使用 JavaScript，以及 n8n 的[内置方法和变量](use-built-in-shortcuts.md)。

	[→ 表达式](../work-with-data/expressions-versus-data-nodes.md)

- __Code 节点__

	使用 Code 节点，向工作流添加 JavaScript 或 Python。

	[→ Code 节点](using-the-code-node.md)

</div>


## 其他技术资源 <a href="#other-technical-resources" id="other-technical-resources"></a>

以下功能面向技术用户。

### 技术节点 <a href="#technical-nodes" id="technical-nodes"></a>

n8n 提供核心节点，方便添加 API 请求、Webhook、定时任务和文件处理等关键功能。

<div class="grid-cards-vertical cards" markdown>

- __编写后端__

	[HTTP Request](../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)、[Webhook](../../integrations/builtin/core-nodes/n8n-nodes-base.webhook/README.md) 和 [Code](using-the-code-node.md) 节点可以帮助你调用 API、响应 Webhook，并在工作流中编写任意 JavaScript。

	可以用它们[创建 API 端点](https://n8n.io/workflows/1750-creating-an-api-endpoint/)等。

	[→ 核心节点](../../integrations/builtin/core-nodes/README.md)

- __实现复杂逻辑__

	可以使用 [If](../../integrations/builtin/core-nodes/n8n-nodes-base.if.md)、[Switch](../../integrations/builtin/core-nodes/n8n-nodes-base.switch.md) 和 [Merge](../../integrations/builtin/core-nodes/n8n-nodes-base.merge.md) 等节点构建复杂流程。

	[→ 流程逻辑](../flow-logic/README.md)

</div>

### 其他开发者资源 <a href="#other-developer-resources" id="other-developer-resources"></a>

<div class="grid-cards-vertical cards" markdown>

- __n8n API__

	n8n 提供 API，可以通过编程执行许多与图形界面相同的任务。工作流内可通过 [n8n API 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)访问此 API。

	[→ API](../../connect/n8n-api/README.md)

- __自托管__

	可以自行托管 n8n，将数据保留在自己的基础设施上。

	[→ 托管](../../deploy/host-n8n/README.md)

- __构建自己的节点__

	可以构建自定义节点，在自己的 n8n 实例中安装，并发布到 [npm](https://www.npmjs.com/)。

	[→ 创建节点](../../connect/create-nodes/overview.md)

</div>

[^1]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义值，而不是提供静态值。

## 相关资源 <a id="related-resources"></a>

* [构建](../)
* [理解工作流](../understand-workflows/README.md)
* [构建和管理智能体](../build-and-manage-agents/README.md)
* [构建工作流的方式](../ways-of-building-workflows/README.md)
* [管理工作流](../manage-workflows/README.md)
* [流程逻辑](../flow-logic/README.md)
* [处理数据](../work-with-data/README.md)
* [集成 AI](../integrate-ai/README.md)
* [键盘快捷键](../keyboard-shortcuts.md)
