---
title: 创建并设置错误工作流
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

1. 创建新工作流，以 Error Trigger 作为第一个节点。
2. 为工作流命名，例如 `Error Handler`。
3. 选择 **Save（保存）**。
4. 在要使用此错误工作流的工作流中：
	1. 选择 **Options（选项）** <img src="../../assets/three-dot-options-menu.png" alt="Options menu icon" data-size="line"> > **Settings（设置）**。
	2. 在 **Error workflow（错误工作流）** 中，选择刚创建的工作流。例如，如果命名为 Error Handler，则选择 **Error handler**。
	3. 选择 **Save（保存）**。
	现在，该工作流发生错误时，关联的错误工作流就会运行。
