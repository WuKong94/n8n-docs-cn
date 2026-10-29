---
contentType: howto
nodeTitle: 配置工作流设置
originalFilePath: workflows/settings.md
originalUrl: https://docs.n8n.io/workflows/settings
url: https://docs.n8n.io/build/manage-workflows/configure-workflow-settings
description: 管理单个工作流的设置。
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


# 配置工作流设置 <a id="configure-workflow-settings"></a>

通过工作流设置，可以为单个工作流自定义行为。

## 打开工作流设置 <a href="#access-workflow-settings" id="access-workflow-settings"></a>

打开设置的步骤如下：

1. 打开工作流。
2. 选择右上角的 **Workflow menu（工作流菜单）** <img src="../.gitbook/assets/three-dots-horizontal (1).png" alt="工作流菜单图标" data-size="line">。
3. 选择 **Settings（设置）**。n8n 会打开 **Workflow settings（工作流设置）** 弹窗。

## 可用设置 <a href="#available-settings" id="available-settings"></a>

提供以下设置：

### Execution order（执行顺序） <a href="#execution-order" id="execution-order"></a>

选择多分支工作流的执行顺序：

**v1（推荐）** 依次执行各个分支，完成一个分支后再开始下一个。n8n 根据分支在画布[^1]上的位置，从上到下排序。如果两个分支高度相同，则先执行最左侧的分支。

**v0（旧版）** 先执行每个分支的第一个节点，再执行每个分支的第二个节点，依此类推。

### Error Workflow（当前工作流出错时用于通知的错误工作流） <a href="#error-workflow-to-notify-when-this-one-errors" id="error-workflow-to-notify-when-this-one-errors"></a>

选择当前工作流失败时要触发的工作流。更多详情请参阅[错误工作流](../flow-logic/handle-errors-gracefully.md)。

### This workflow can be called by（允许调用此工作流的工作流） <a href="#this-workflow-can-be-called-by" id="this-workflow-can-be-called-by"></a>

选择哪些其他工作流可以调用此工作流。

### Timezone（时区） <a href="#timezone" id="timezone"></a>

设置此工作流的时区。时区设置对于 Schedule Trigger 节点很重要。

可以通过设置 n8n 实例时区，配置工作流使用的默认时区：

* [设置 n8n Cloud 实例时区](../../deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md)
* [配置自托管实例的时区](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md)

如果未配置工作流或实例时区，n8n 默认使用 EDT（纽约）时区。

### Save failed production executions（保存失败的生产执行） <a href="#save-failed-production-executions" id="save-failed-production-executions"></a>

控制 n8n 是否保存已发布工作流中失败的执行。

### Save successful production executions（保存成功的生产执行） <a href="#save-successful-production-executions" id="save-successful-production-executions"></a>

控制 n8n 是否保存已发布工作流中成功的执行。

### Save manual executions（保存手动执行） <a href="#save-manual-executions" id="save-manual-executions"></a>

控制 n8n 是否保存在编辑器中由用户启动的工作流执行。

### Save execution progress（保存执行进度） <a href="#save-execution-progress" id="save-execution-progress"></a>

控制 n8n 是否保存每个节点的执行数据。

设为 **Save（保存）** 后，发生错误时，工作流会从停止处恢复。这可能增加延迟。

### Timeout Workflow（工作流超时） <a href="#timeout-workflow" id="timeout-workflow"></a>

控制 n8n 是否在经过一定时间后取消当前工作流执行。

启用后会显示 **Timeout After（超时时间）** 选项，可以设置工作流应在多长时间后超时，单位为小时、分钟和秒。对于 n8n Cloud 用户，n8n 会按套餐限制最大可设置的超时时间。

### Redact production execution data（隐藏生产执行数据） <a href="#redact-production-execution-data" id="redact-production-execution-data"></a>

控制 n8n 是否隐藏生产执行（非手动触发）的数据。设为 **Redact（隐藏）** 后，n8n 会隐藏每个节点的输入和输出数据，并用已隐藏标记代替。

### Redact manual execution data（隐藏手动执行数据） <a href="#redact-manual-execution-data" id="redact-manual-execution-data"></a>

控制 n8n 是否隐藏手动触发执行的数据。设为 **Redact（隐藏）** 后，n8n 会隐藏每个节点的输入和输出数据，并用已隐藏标记代替。

如果实例管理员[在整个实例中强制启用数据隐藏](../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md#instance-level-enforcement)，n8n 会将强制范围内的设置锁定为 **Redact（隐藏）**，无法在此关闭。

有关隐藏策略、查看被隐藏数据和权限要求的详情，请参阅[执行数据隐藏](../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md)。

### Estimated time saved（预计节省时间） <a href="#estimated-time-saved" id="estimated-time-saved"></a>

估计此工作流每次执行能为你节省的分钟数。

设置后，n8n 可以在[洞察](../../administer/observe-and-log/track-usage-with-insights.md)中计算节省的时间。

### Custom span attributes（自定义 Span 属性） <a href="#custom-span-attributes" id="custom-span-attributes"></a>

为工作流的 OpenTelemetry Span 添加自定义键值属性。详情请参阅[自定义 Span 属性](../../deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry.md#custom-span-attributes)。

[^1]: 画布是 n8n 编辑器中构建工作流的主要界面。你可以在画布上添加并连接节点，组成工作流。

## 相关资源 <a id="related-resources"></a>

* [管理工作流](./)
* [为工作流添加标签](tag-workflows.md)
* [收藏项目](favorite-items.md)
* [查看更改历史](view-change-history.md)
* [审核工作流](workflow-reviews.md)
* [导出和导入](export-and-import.md)
* [n8n 软件包](n8n-packages/README.md)
* [与他人共享](share-with-others.md)
