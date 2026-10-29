---
title: Manual Trigger（手动触发器） 节点文档
contentType:
- integration
- reference
priority: critical
nodeTitle: Manual Trigger（手动触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger
description: 了解如何在 n8n 中使用 Manual Trigger（手动触发器） 节点，并按照技术文档将其集成到工作流中。
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


# Manual Trigger（手动触发器） <a id="manual-trigger"></a>

如果希望通过选择 **Execute Workflow**（执行工作流）启动工作流，且不需要任何自动运行方式，请使用此节点。

工作流始终需要触发器或起点。大多数工作流由响应外部事件的触发器节点启动，或由按计划触发的 [Schedule Trigger](n8n-nodes-base.scheduletrigger/README.md) 启动。

对于没有自动触发器的工作流，Manual Trigger 节点充当其触发器。

在以下情况下使用此触发器：

* 在添加某种自动触发器之前测试工作流。
* 不希望工作流自动运行。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Manual Trigger 节点的常见错误和问题，以及解决或排查步骤。

### Only one 'Manual Trigger' node is allowed in a workflow（一个工作流只允许一个 Manual Trigger 节点） <a href="#only-one-manual-trigger-node-is-allowed-in-a-workflow" id="only-one-manual-trigger-node-is-allowed-in-a-workflow"></a>

尝试向已经包含 Manual Trigger 节点的工作流再次添加该节点时，会显示此错误。

移除现有的 Manual Trigger，或编辑工作流，将该触发器连接到其他节点。
