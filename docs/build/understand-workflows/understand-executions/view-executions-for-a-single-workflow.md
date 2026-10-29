---
description: 查看和筛选当前画布中工作流的全部执行。
contentType: howto
nodeTitle: 查看单个工作流的执行
originalFilePath: workflows/executions/single-workflow-executions.md
originalUrl: https://docs.n8n.io/workflows/executions/single-workflow-executions
url: https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流级别的执行列表 <a href="#workflow-level-executions-list" id="workflow-level-executions-list"></a>

工作流中的 **Executions（执行）** 列表显示该工作流的全部执行。

{% hint style="info" %}
**已删除的工作流**

删除工作流时，n8n 也会删除其执行历史，因此无法查看已删除工作流的执行。
{% endhint %}

{% hint style="info" %}
**执行历史与工作流历史**

不要将执行列表与[工作流历史](../../manage-workflows/view-change-history.md)混淆。

执行是指工作流的运行。通过执行列表，可以查看当前版本工作流之前的运行记录。可以将以往执行复制到编辑器，在当前工作流中[调试并重新运行](debug-executions.md)。

工作流历史保存的是工作流的旧版本，例如使用不同节点或不同参数设置的版本。
{% endhint %}


## 查看单个工作流的执行 <a href="#view-executions-for-a-single-workflow" id="view-executions-for-a-single-workflow"></a>

在工作流中，选择顶部菜单中的 **Executions（执行）** 标签页，即可预览该工作流的全部执行。

{% hint style="info" %}
**使用最终用户凭据的执行**

执行使用[最终用户凭据](../../../administer/manage-credentials/end-user-credentials.md)时，只有通过自己已连接账号运行该节点的用户，才能查看节点数据。其他所有人（包括管理员）看到的输出都会被隐藏。
{% endhint %}

## 筛选执行 <a href="#filter-executions" id="filter-executions"></a>

可以筛选执行列表。

1. 在工作流中选择 **Executions（执行）**。
2. 选择 **Filters（筛选）**。
3. 输入筛选条件。可以按以下字段筛选：
	* **Status（状态）**：选择 **Failed（失败）**、**Running（运行中）**、**Success（成功）** 或 **Waiting（等待中）**。
	* **Execution start（执行开始时间）**：查看在指定时间范围内开始的执行。
	* **Saved custom data（已保存的自定义数据）**：在工作流中通过 Code 节点创建的数据。输入键和值进行筛选。添加此类数据的方法，请参阅[自定义执行数据](customize-executions-data.md)。

		{% include "../../../reusable-content/.gitbook/includes/workflows/executions/custom-execution-data-availability.md" %}


## 重试失败的工作流 <a href="#retry-failed-workflows" id="retry-failed-workflows"></a>

工作流执行失败时，可以重试。重试失败工作流的步骤如下：

1. 打开 **Executions（执行）** 列表。
2. 在要重试的工作流执行上，选择 **Refresh（刷新）** <img src="../../.gitbook/assets/refresh.png" alt="刷新图标" data-size="line">。
{% include "../../../reusable-content/.gitbook/includes/workflows/executions/retry-options.md" %}

## 相关资源 <a id="related-resources"></a>

* [理解执行](./)
* [手动执行、部分执行与生产执行](types-of-executions.md)
* [查看所有执行](view-all-executions.md)
* [调试并重新运行以往执行](debug-executions.md)
* [自定义执行数据](customize-executions-data.md)
* [流式传输实时响应](stream-real-time-responses.md)
* [脏节点](understand-dirty-nodes.md)
