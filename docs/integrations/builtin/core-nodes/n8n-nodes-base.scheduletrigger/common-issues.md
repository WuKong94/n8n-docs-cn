---
title: Schedule Trigger 节点常见问题
contentType:
- integration
- reference
priority: critical
nodeTitle: Schedule Trigger 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues
description: 了解 n8n 中 Schedule Trigger 节点的常见问题、排查步骤及建议的解决方法。
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


# 常见问题 <a id="common-issues"></a>

本页介绍 [Schedule Trigger 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 无效的 cron 表达式 <a href="#invalid-cron-expression" id="invalid-cron-expression"></a>

将 **Trigger Interval**（触发间隔）设为 **Custom (Cron)**（自定义 Cron），但 n8n 无法理解 cron 表达式时，会出现此错误。可能是表达式有误，或使用了不兼容的语法。

排查时，请检查：

* cron 表达式是否符合 [cron 示例](./README.md#custom-cron-interval)中的语法。
* 去掉[秒字段](./README.md#why-there-are-six-asterisks-in-the-cron-expression)后，cron 表达式是否能通过 [crontab guru](https://crontab.guru/) 的校验。

## 定时工作流运行时间不正确 <a href="#scheduled-workflows-run-at-the-wrong-time" id="scheduled-workflows-run-at-the-wrong-time"></a>

如果 Schedule Trigger 节点的运行时间不正确，可能需要调整 n8n 使用的时区。

### 调整全局时区 <a href="#adjust-the-timezone-globally" id="adjust-the-timezone-globally"></a>

使用 [n8n Cloud](../../../../deploy/use-n8n-cloud/README.md) 时，请按[设置 Cloud 实例时区](../../../../deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md)中的说明配置，确保 n8n 按本地时间执行。

使用[自托管](../../../../deploy/host-n8n/README.md)部署时，通过 [`GENERIC_TIMEZONE` 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md)设置全局时区。

### 调整单个工作流的时区 <a href="#adjust-the-timezone-for-an-individual-workflow" id="adjust-the-timezone-for-an-individual-workflow"></a>

设置单个工作流时区的步骤：

1. 在画布上打开工作流。
2. 选择右上角的 <img src="../../../.gitbook/assets/three-dots-horizontal (2).png" alt="工作流菜单图标" data-size="line"> **Workflow menu**（工作流菜单）。
3. 选择 **Settings**（设置）。
4. 更改 **Timezone**（时区）。
5. 选择 **Save**（保存）。

### 变量未按预期生效 <a href="#variables-not-working-as-expected" id="variables-not-working-as-expected"></a>

定时触发器可以使用变量，但只会在工作流发布时求出变量值。发布后，在设置中更改变量值不会改变工作流运行频率。需要先停止，再发布工作流的新版本，才能应用更新后的变量值。

### 更改触发间隔 <a href="#changing-the-trigger-interval" id="changing-the-trigger-interval"></a>

可以随时更改定时触发间隔，但只有发布工作流时才会更新。工作流发布后，更改触发间隔不会立即生效，必须先取消发布，再发布工作流的新版本。

定时安排还会从工作流发布时刻开始。例如，原先每隔 1 小时运行，计划在 12:00 执行；改为每隔 2 小时，并在 11:30 发布新版本后，下次将于 13:30 执行，即发布后 2 小时。
