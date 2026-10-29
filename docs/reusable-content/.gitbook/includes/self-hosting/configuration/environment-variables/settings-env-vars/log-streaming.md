---
title: 日志流
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_LOG_STREAMING_MANAGED_BY_ENV` | Boolean | `false` | 设为 `true`，通过环境变量管理日志流。当值为 `true` 时，n8n 会在每次启动时应用日志流变量，并锁定对应的界面控件。 |
| `N8N_LOG_STREAMING_DESTINATIONS` | JSON 字符串 | - | 日志流目标的 JSON 数组。每个目标是一个对象，包含 `type` 字段，其值为 `webhook`、`syslog` 或 `sentry`，以及该类型对应的配置。 |
