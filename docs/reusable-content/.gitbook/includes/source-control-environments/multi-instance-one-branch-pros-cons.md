---
title: 多实例、单分支的优缺点
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

此模式的优点是：从一个实例推送后，其他环境可以立即获取这些工作。

缺点如下：

* 如果误推送，工作可能进入生产实例。如果[使用 GitHub Action 自动拉取](../../../../administer/use-source-control-and-environments/tutorial-create-environments-with-source-control.md#optional-use-a-github-action-to-automate-pulls)到生产环境，必须改用多实例、多分支模式，或严格避免推送不希望进入生产环境的工作。
* 对同一实例既推送又拉取，可能因操作覆盖更改而造成数据丢失。应建立流程，确保内容单向流动。
