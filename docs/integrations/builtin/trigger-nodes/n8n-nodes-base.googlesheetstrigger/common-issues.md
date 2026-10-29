---
title: Google Sheets 触发器节点常见问题
description: 工作流自动化平台 n8n 中 Google Sheets 触发器节点的常见错误和问题，包括问题详情及建议的解决办法。
contentType:
- integration
- reference
priority: high
nodeTitle: Google Sheets 触发器节点常见问题
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Sheets 触发器节点常见问题 <a href="#google-sheets-trigger-node-common-issues" id="google-sheets-trigger-node-common-issues"></a>

以下列出 [Google Sheets 触发器节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 卡在等待触发事件的状态 <a href="#stuck-waiting-for-trigger-event" id="stuck-waiting-for-trigger-event"></a>

使用 **Execute step**（执行步骤）或 **Execute workflow**（执行工作流）按钮测试 Google Sheets Trigger 节点时，执行可能看似卡住，且无法停止监听事件。出现此情况时，可能需要退出工作流后重新打开，以重置画布。

一直停留在监听事件状态，通常与 n8n 外部的网络配置有关，尤其是通过反向代理运行 n8n、却未配置 WebSocket 代理时。

请检查反向代理配置，例如 Nginx、Caddy、Apache HTTP Server 或 Traefik，启用 WebSocket 支持。

## 日期和时间列显示为数字 <a href="#date-and-time-columns-are-rendering-as-numbers" id="date-and-time-columns-are-rendering-as-numbers"></a>

Google Sheets 支持以多种方式显示日期和时间。

[**序列号格式**](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption)由 Lotus 1-2-3 推广，许多电子表格软件都采用此格式，用小数表示日期。整数部分（小数点左侧）表示自 1899 年 12 月 30 日以来的天数；小数部分（小数点右侧）表示一天 24 小时中的时间比例，例如 `.5` 表示中午。

要为日期和时间值使用其他格式，请调整 Google Sheets Trigger 节点中的格式。**Trigger On**（触发条件）设为 **Row Added**（已添加行）时，可以配置此选项：

1. 在画布中打开 Google Sheets Trigger 节点。
2. 选择 **Add option**（添加选项）。
3. 选择 **DateTime Render**（日期时间呈现方式）。
4. 将 **DateTime Render** 改为 **Formatted String**（格式化字符串）。

此后，Google Sheets Trigger 节点会按照数字格式，将日期、时间、日期时间和时长字段格式化为字符串。

数字格式取决于电子表格的地区设置。打开电子表格，选择 **File > Settings**（文件 > 设置）。在 **General**（常规）标签页中，将 **Locale**（地区设置）改为所需地区，再选择 **Save settings**（保存设置）。
