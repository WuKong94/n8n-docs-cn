---
title: 等待
description: 如何让工作流执行进入等待状态。
contentType: howto
nodeTitle: 等待
originalFilePath: flow-logic/waiting.md
originalUrl: https://docs.n8n.io/flow-logic/waiting
url: https://docs.n8n.io/build/flow-logic/wait
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 等待 <a href="#waiting" id="waiting"></a>

等待功能可以在工作流执行过程中暂停，之后携带相同数据，从暂停处继续执行。如果需要限制服务调用频率，或等待外部事件完成，这会很有用。可以等待指定时长，也可以等待 Webhook 被触发。等待是 n8n [流程逻辑](./)的一部分：需要降低批处理速度时，可与[循环](loop.md)配合使用；也可以用于多次节点执行之间的数据[合并](merge-data.md)。

使用 [Wait](../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md) 节点让工作流等待。使用详情请参阅该节点文档。

n8n 提供了一个工作流模板，演示[限制调用频率和等待外部事件](https://n8n.io/workflows/1749-rate-limiting-and-waiting-for-external-events/)的基本用法。

## 相关资源 <a id="related-resources"></a>

* [流程逻辑](./)
* [按条件分支](split-with-conditionals.md)
* [合并数据](merge-data.md)
* [循环](loop.md)
* [理解执行顺序](understand-execution-order.md)
* [将工作流拆分为更小的部分](break-workflows-into-smaller-parts.md)
* [转换为子工作流](convert-to-sub-workflows.md)
* [妥善处理错误](handle-errors-gracefully.md)
