---
title: 日志环境变量
description: 配置日志记录和诊断数据的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 日志
originalFilePath: hosting/configuration/environment-variables/logs.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/logs
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 日志环境变量 <a href="#logs-environment-variables" id="logs-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

本页列出用于配置调试日志的环境变量。详情请参阅 [n8n 中的日志记录](../../../keep-n8n-running/set-up-logging.md)。

## n8n 日志 <a href="#n8n-logs" id="n8n-logs"></a>


| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_LOG_LEVEL` | 枚举字符串： `info`, `warn`, `error`, `debug` | `info` | 日志输出级别。详情请参阅[日志级别](../../../keep-n8n-running/set-up-logging.md#log-levels)。 |
| `N8N_LOG_OUTPUT` | 枚举字符串： `console`, `file` | `console` | 日志输出位置。多个值以逗号分隔。 |
| `N8N_LOG_FORMAT` | 枚举字符串： `text`, `json` | `text` | 使用的日志格式。`text` 输出适合人阅读的消息；`json` 每行输出一个 JSON 对象，包含消息、级别、时间戳和全部元数据，适合生产监控及调试。 |
| `N8N_LOG_CRON_ACTIVE_INTERVAL` | Number | `0` | 记录当前激活 cron 任务的间隔，单位为分钟。设为 `0` 可禁用。 |
| `N8N_LOG_FILE_COUNT_MAX` | Number | `100` | 保留的日志文件数量上限。 |
| `N8N_LOG_FILE_SIZE_MAX` | Number | `16` | 每个日志文件的大小上限，单位为 MB。 |
| `N8N_LOG_FILE_LOCATION` | String | `<n8n-directory-path>/logs/n8n.log` | 日志文件位置。需要将 N8N_LOG_OUTPUT 设为 `file`。 |
| `DB_LOGGING_ENABLED` | Boolean | `false` | 是否启用数据库专用日志。 |
| `DB_LOGGING_OPTIONS` | 枚举字符串： `query`, `error`, `schema`, `warn`, `info`, `log` | `error` | 数据库日志输出级别。要启用全部日志，指定 `all`。参阅 [TypeORM 日志选项](https://orkhan.gitbook.io/typeorm/docs/docs/advanced-topics/5-logging#logging-options)。 |
| `DB_LOGGING_MAX_EXECUTION_TIME` | Number | `1000` | 超过指定执行时长后，n8n 会记录警告，单位为毫秒。设为 `0` 可禁用长查询警告。 |
| `CODE_ENABLE_STDOUT` | Boolean | `false` | 设为 `true`，将 Code 节点中 `console.log` 或 `print` 产生的日志发送到进程标准输出，仅适用于生产执行。 |
| `NO_COLOR` | any | `undefined` | 设置任意值，以不带 ANSI 颜色的方式输出日志。更多信息请参阅 [no-color.org 网站](https://no-color.org/)。 |


## 日志流 <a href="#log-streaming" id="log-streaming"></a>

此功能的更多信息请参阅[日志流](../../../../../administer/observe-and-log/stream-logs-to-external-systems.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_EVENTBUS_CHECKUNSENTINTERVAL` | Number | `0` | 检查未发送事件消息的频率，单位为毫秒。极少数情况下可能重复发送消息。设为 `0` 可禁用。 |
| `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS` | Boolean | `false` | 是否在线程内同步执行所有文件访问，true 表示同步，false 表示不同步。 |
| `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT` | Number | `3` | 保留的事件日志文件数量。 |
| `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB` | Number | `10240` | 创建新事件日志文件前，单个文件允许的最大大小，单位为 KB。 |
| `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` | String | `n8nEventLog` | 事件日志文件的基础名称。设置 `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` 时忽略此值。 |
| `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` | String | `''` | 事件日志文件的绝对路径，必须以 `.log` 结尾。设置后会原样使用此路径，覆盖 `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` 和默认的进程后缀。多个进程共享可写文件系统时，可用此设置为每个 n8n 进程指定独立日志路径。详情请参阅[每个进程独立的事件日志文件](../../../../../administer/observe-and-log/stream-logs-to-external-systems.md#per-process-event-log-files)。 |
| `N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE` | Number | `500000` | 恢复时从单个事件日志文件解析的最大行数。当文件包含大量无效行时，用于限制内存使用。 |

### 通过环境变量管理日志流目标 <a href="#manage-log-streaming-destinations-from-environment-variables" id="manage-log-streaming-destinations-from-environment-variables"></a>

将 `N8N_LOG_STREAMING_MANAGED_BY_ENV` 设为 `true`，通过环境变量管理日志流目标。启用机制请参阅[通过环境变量管理实例设置](../../manage-settings-using-environment-variables.md)，各类目标的 JSON 结构请参阅[通过环境变量配置日志流目标](../../../../../administer/observe-and-log/stream-logs-to-external-systems.md#configure-using-environment-variables)。

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/log-streaming.md" %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
