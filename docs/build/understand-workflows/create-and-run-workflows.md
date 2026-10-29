---
contentType: howto
nodeTitle: 创建和运行工作流
originalFilePath: workflows/create.md
originalUrl: https://docs.n8n.io/workflows/create
url: https://docs.n8n.io/build/understand-workflows/create-and-run-workflows
description: 创建、运行和发布工作流。
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
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 创建和运行工作流 <a id="create-and-run-workflows"></a>

工作流[^1]由一组相互连接的节点组成，用于自动化处理流程。你可以在[工作流画布](#user-content-fn-2)[^2]上构建工作流。

## 创建工作流 <a href="#create-a-workflow" id="create-a-workflow"></a>

1. 选择侧边菜单左上角的 <img src="../.gitbook/assets/universal-resource-button (1).png" alt="通用资源创建图标" data-size="line"> **按钮**，再选择工作流。
2. 如果 n8n 实例支持项目，还需要选择是在**个人空间**中创建工作流，还是在你有权访问的某个**项目**中创建。使用社区版时，工作流始终在个人空间中创建。
3. 首先添加触发器节点：选择 **Add first step...（添加第一步……）**。

或者：

1. 在 **Overview（概览）** 页面或某个**项目**中，选择右上角的 <img src="../.gitbook/assets/universal-resource-button (1).png" alt="通用资源创建图标" data-size="line"> **create（创建）** 按钮，再选择工作流。
2. 如果从 **Overview（概览）** 页面操作，工作流会创建在个人空间中；如果从项目中操作，则会创建在该项目中。
3. 首先添加触发器节点：选择 **Add first step...（添加第一步……）**。

如果是第一次构建工作流，可以使用[快速入门指南](../../get-started/build-your-first-workflow.md)，迅速体验 n8n 的功能。

## 手动运行工作流 <a href="#run-workflows-manually" id="run-workflows-manually"></a>

在构建和测试过程中，或工作流没有触发器节点时，可能需要手动运行工作流。

要手动运行，选择 **Execute Workflow（执行工作流）**。

## 自动运行工作流 <a href="#run-workflows-automatically" id="run-workflows-automatically"></a>

所有新工作流默认都处于未发布状态。请参阅[发布和保存工作流](save-and-publish-workflows.md)。

以触发器节点或 Webhook 节点开始的工作流，需要发布后才能自动运行。工作流未发布时，必须手动运行。

要发布工作流，打开工作流并点击 **Publish（发布）**。取消发布的选项位于工作流设置菜单中。

已发布的工作流会在满足触发条件时运行。

[^1]: n8n 工作流由一组节点组成，用于自动化处理流程。触发条件满足时，工作流开始执行，并按顺序运行节点以完成复杂任务。
<a id="user-content-fn-2"></a>
[^2]: 画布是 n8n 编辑器中构建工作流的主要界面。你可以在画布上添加并连接节点，组成工作流。

## 相关资源 <a id="related-resources"></a>

* [理解工作流](./)
* [保存和发布工作流](save-and-publish-workflows.md)
* [创建和编辑凭据](create-and-edit-credentials.md)
* [使用 Gateway 额度](use-gateway-credits.md)
* [工作流组件](workflow-components/README.md)
* [理解执行](understand-executions/README.md)
