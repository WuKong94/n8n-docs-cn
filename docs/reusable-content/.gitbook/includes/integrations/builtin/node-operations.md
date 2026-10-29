---
title: 节点操作：触发器与操作
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## 节点操作：触发器与操作 <a href="#node-operations-triggers-and-actions" id="node-operations-triggers-and-actions"></a>

向工作流添加节点时，n8n 会显示可用操作列表。操作是节点执行的任务，例如获取或发送数据。

操作分为两类：

* 触发器（Triggers）会在服务中发生特定事件或满足条件时启动工作流。选择触发器后，n8n 会向工作流添加触发器节点，并预先选中所选触发操作。在 n8n 中搜索节点时，触发操作带有闪电图标 <img src="../../../assets/trigger.png" alt="Trigger icon" data-size="line">。
* 操作（Actions）代表工作流中的特定任务，可以用于操作数据、在外部系统中执行任务，以及在其他系统中触发事件。选择操作后，n8n 会向工作流添加节点，并预先选中所选操作。
