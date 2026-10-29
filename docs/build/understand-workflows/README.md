---
description: 了解 n8n 工作流的关键组件。
contentType: overview
nodeTitle: 理解工作流
originalFilePath: workflows/index.md
originalUrl: https://docs.n8n.io/workflows
url: https://docs.n8n.io/build/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流 <a href="#workflows" id="workflows"></a>

工作流[^1]由一组相互连接的节点组成，用于自动化处理流程。可以[创建](create-and-run-workflows.md)工作流，也可以使用[工作流模板](../ways-of-building-workflows/use-templates.md)帮助入门。工作流运行后，可以将其[共享](../manage-workflows/share-with-others.md)给他人。

如果是第一次构建工作流，可以使用[快速入门指南](../../get-started/build-your-first-workflow.md)，迅速体验 n8n 的功能。

## 本节内容 <a id="in-this-section"></a>

* [创建和运行工作流](create-and-run-workflows.md)：创建、运行和发布工作流。
* [保存和发布工作流](save-and-publish-workflows.md)：保存、发布、取消发布以及为工作流版本命名。
* [创建和编辑凭据](create-and-edit-credentials.md)：安全地存储工作流所需的身份验证信息。
* [使用 Gateway 额度](use-gateway-credits.md)：无需设置自己的凭据，即可运行支持的 AI 模型和服务。
* [工作流组件](workflow-components/README.md)：节点和连接等工作流的构建模块。
* [理解执行](understand-executions/README.md)：了解什么是执行，以及如何查看、筛选和调试执行。

## 相关资源 <a id="related-resources"></a>

* [构建](../)
* [构建和管理智能体](../build-and-manage-agents/README.md)
* [构建工作流的方式](../ways-of-building-workflows/README.md)
* [管理工作流](../manage-workflows/README.md)
* [流程逻辑](../flow-logic/README.md)
* [处理数据](../work-with-data/README.md)
* [在 n8n 中编写代码](../code-in-n8n/README.md)
* [集成 AI](../integrate-ai/README.md)
* [键盘快捷键](../keyboard-shortcuts.md)

[^1]: n8n 工作流由一组节点组成，用于自动化处理流程。触发条件满足时，工作流开始执行，并按顺序运行节点以完成复杂任务。
