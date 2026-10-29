---
title: 多分支工作流的执行顺序
description: n8n 如何决定多分支工作流中的节点执行顺序。
contentType: explanation
nodeTitle: 理解执行顺序
originalFilePath: flow-logic/execution-order.md
originalUrl: https://docs.n8n.io/flow-logic/execution-order
url: https://docs.n8n.io/build/flow-logic/understand-execution-order
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 多分支工作流的执行顺序 <a href="#execution-order-in-multi-branch-workflows" id="execution-order-in-multi-branch-workflows"></a>

执行顺序属于工作流的[流程逻辑](./)，在[拆分为多个分支](split-with-conditionals.md)的工作流中尤为重要。

n8n 的节点执行顺序取决于所用的 n8n 版本：

* 对于在 n8n 1.0 之前创建的工作流：n8n 先执行每个分支的第一个节点，再执行每个分支的第二个节点，依此类推。
* 对于从 n8n 1.0 起创建的工作流：依次执行各个分支，完成一个分支后再开始下一个。n8n 根据分支在画布[^1]上的位置，从上到下排序。如果两个分支高度相同，则先执行最左侧的分支。

可以在[工作流设置](../manage-workflows/configure-workflow-settings.md)中更改执行顺序。

[^1]: 画布是 n8n 编辑器中构建工作流的主要界面。你可以在画布上添加并连接节点，组成工作流。

## 相关资源 <a id="related-resources"></a>

* [流程逻辑](./)
* [按条件分支](split-with-conditionals.md)
* [合并数据](merge-data.md)
* [循环](loop.md)
* [等待](wait.md)
* [将工作流拆分为更小的部分](break-workflows-into-smaller-parts.md)
* [转换为子工作流](convert-to-sub-workflows.md)
* [妥善处理错误](handle-errors-gracefully.md)
