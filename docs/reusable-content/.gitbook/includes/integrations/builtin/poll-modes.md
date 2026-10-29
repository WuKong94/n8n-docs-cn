---
title: 轮询模式
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

### Every Hour（每小时）模式 <a href="#every-hour-mode" id="every-hour-mode"></a>

在 **Minute**（分钟）中输入每小时触发轮询的分钟数，范围为 `0` 至 `59`。

### Every Day（每天）模式 <a href="#every-day-mode" id="every-day-mode"></a>

* 在 **Hour**（小时）中，以 24 小时制输入每天触发轮询的小时数，范围为 `0` 至 `23`。
* 在 **Minute**（分钟）中输入每小时触发轮询的分钟数，范围为 `0` 至 `59`。

### Every Week（每周）模式 <a href="#every-week-mode" id="every-week-mode"></a>

* 在 **Hour**（小时）中，以 24 小时制输入当天触发轮询的小时数，范围为 `0` 至 `23`。
* 在 **Minute**（分钟）中输入触发轮询的分钟数，范围为 `0` 至 `59`。
* 在 **Weekday**（星期几）中选择触发轮询的星期几。

### Every Month（每月）模式 <a href="#every-month-mode" id="every-month-mode"></a>

* 在 **Hour**（小时）中，以 24 小时制输入当天触发轮询的小时数，范围为 `0` 至 `23`。
* 在 **Minute**（分钟）中输入触发轮询的分钟数，范围为 `0` 至 `59`。
* 在 **Day of the Month**（每月第几天）中输入触发轮询的日期，范围为 `0` 至 `31`。

### Every X（每隔一段时间）模式 <a href="#every-x-mode" id="every-x-mode"></a>

* 在 **Value**（数值）中输入轮询触发间隔，以分钟或小时为单位。
* 在 **Unit**（单位）中选择数值的单位，支持 **Minutes**（分钟）和 **Hours**（小时）。

### Custom（自定义）模式 <a href="#custom-mode" id="custom-mode"></a>

输入自定义 **Cron Expression**（Cron 表达式）触发轮询，使用以下值和范围：

* 秒：`0` - `59`
* 分钟：`0` - `59`
* 小时：`0` - `23`
* 每月第几天：`1` - `31`
* 月份：`0` - `11`（一月至十二月）
* 星期几：`0` - `6`（星期日至星期六）

可以使用 [crontab guru](https://crontab.guru) 生成 Cron 表达式，再将结果粘贴到 n8n 的 **Cron Expression** 字段。

#### 示例 <a href="#examples" id="examples"></a>

要在每天 04:08:30 触发工作流，在 **Cron Expression** 字段中输入以下内容。
```
30 8 4 * * *
```

要在每天 04:08 触发工作流，在 **Cron Expression** 字段中输入以下内容。
```
8 4 * * *
```

#### 为什么 Cron 表达式中有六个星号 <a href="#why-there-are-six-asterisks-in-the-cron-expression" id="why-there-are-six-asterisks-in-the-cron-expression"></a>

六字段 Cron 表达式的第一个字段表示秒。该字段可选，即使不设置秒值，节点也会执行。

|  *  |  *  |  *  |  *  |  *  |  *  |
|:--:|:--:|:--:|:--:|:--:|:--:|
|秒|分钟|小时|每月第几天|月份|星期几|
