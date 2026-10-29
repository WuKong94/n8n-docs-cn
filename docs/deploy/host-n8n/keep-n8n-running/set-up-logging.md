---
contentType: howto
nodeTitle: 设置日志
originalFilePath: hosting/logging-monitoring/logging.md
originalUrl: https://docs.n8n.io/hosting/logging-monitoring/logging
url: https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 日志 <a href="#logging-in-n8n" id="logging-in-n8n"></a>

日志是调试的重要功能。n8n 使用 [winston](https://www.npmjs.com/package/winston) 日志库。

{% hint style="info" %}
**功能可用范围**

本文介绍的所有日志选项，日志流除外，可用于：

- **n8n Cloud：**所有套餐。
- **自托管：**所有版本。

[日志流](../../../administer/observe-and-log/stream-logs-to-external-systems.md)可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

{% endhint %}

## 如何在 n8n 中设置日志？ <a href="#setup" id="setup"></a>

要在 n8n 中设置日志，需要设置以下环境变量，也可以在[配置文件](../configure-n8n/basic-configuration/use-environment-variables/README.md)中设置相应值。

| 配置文件中的设置 | 使用环境变量 | 说明 |
|-----------------------------------|-----------------------------|-------------|
| n8n.log.level | N8N_LOG_LEVEL | 日志输出级别，可用选项从低到高为 error、warn、info 和 debug，默认值为 `info`。这些选项的更多信息，请参阅[日志级别](#log-levels)。 |
| n8n.log.output | N8N_LOG_OUTPUT | 日志输出位置，可用选项为 `console` 和 `file`，可使用逗号（`,`）分隔多个值，默认使用 `console`。 |
| n8n.log.file.location | N8N_LOG_FILE_LOCATION | 日志文件位置，仅在日志输出设为文件时使用，默认为 `<n8nFolderPath>/logs/n8n.log`。 |
| n8n.log.file.fileSizeMax | N8N_LOG_FILE_SIZE_MAX | 每个日志文件的最大大小，单位为 MB，默认 16 MB。 |
| n8n.log.file.fileCountMax | N8N_LOG_FILE_COUNT_MAX | 保留日志文件的最大数量，默认 100。使用工作进程时应设置此值。 |


```bash
# Set the logging level to 'debug' <a href="#set-the-logging-level-to-debug" id="set-the-logging-level-to-debug"></a>
export N8N_LOG_LEVEL=debug

# Set log output to both console and a log file <a href="#set-log-output-to-both-console-and-a-log-file" id="set-log-output-to-both-console-and-a-log-file"></a>
export N8N_LOG_OUTPUT=console,file

# Set a save location for the log file <a href="#set-a-save-location-for-the-log-file" id="set-a-save-location-for-the-log-file"></a>
export N8N_LOG_FILE_LOCATION=/home/jim/n8n/logs/n8n.log

# Set a 50 MB maximum size for each log file <a href="#set-a-50-mb-maximum-size-for-each-log-file" id="set-a-50-mb-maximum-size-for-each-log-file"></a>
export N8N_LOG_FILE_SIZE_MAX=50

# Set 60 as the maximum number of log files to be kept <a href="#set-60-as-the-maximum-number-of-log-files-to-be-kept" id="set-60-as-the-maximum-number-of-log-files-to-be-kept"></a>
export N8N_LOG_FILE_COUNT_MAX=60
```

### 日志级别 <a href="#log-levels" id="log-levels"></a>

n8n 使用标准日志级别报告信息：

- `silent`：不输出任何内容。
- `error`：仅输出错误。
- `warn`：输出错误和警告消息。
- `info`：包含进度相关的有用信息。
- `debug`：最详细的输出，n8n 输出大量信息来帮助调试问题。


## 如何在开发期间添加日志？ <a href="#development" id="development"></a>

开发期间添加日志消息是良好实践，有助于调试错误。按以下指南配置开发日志。

### 实现细节 <a href="#implementation-details" id="implementation-details"></a>

n8n 使用 `LoggerProxy` 类，该类位于 `workflow` 包中。使用前，调用 `LoggerProxy.init()` 并传入 `Logger` 实例来初始化此类。

初始化仅发生一次。[`start.ts`](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) 文件已完成此过程。如果从头创建新命令，需要初始化 `LoggerProxy` 类。

创建 `Logger` 在 `cli` 包中的实现后，可以调用所导出模块的 `getInstance` 便捷方法获取它。

请查看 [start.ts](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) 文件，了解此过程的工作方式。

### 添加日志 <a href="#adding-logs" id="adding-logs"></a>

在项目中初始化 `LoggerProxy` 类后，就可以将其导入其他文件并添加日志。

所有日志级别都提供便捷方法，可以随时按 `Logger.<logLevel>('<message>', ...meta)` 格式添加日志。其中 `meta` 表示在 `message` 之外所需的附加属性。

上例使用[前文](#log-levels)介绍的标准日志级别。`message` 参数为字符串，`meta` 为数据对象。

```js
// You have to import the LoggerProxy. We rename it to Logger to make it easier

import {
	LoggerProxy as Logger
} from 'n8n-workflow';

// Info-level logging of a trigger function, with workflow name and workflow ID as additional metadata properties

Logger.info(`Polling trigger initiated for workflow "${workflow.name}"`, {workflowName: workflow.name, workflowId: workflow.id});
```

创建新日志记录器时，请遵循以下有用规范：

- 尽量使日志消息便于阅读，例如始终用引号包裹名称。
- 在日志消息和元数据中重复相同信息可能有帮助，例如上例的工作流名称：消息更易搜索，元数据更便于筛选。
- 在各处日志中包含多个 ID，例如 `executionId`、`workflowId` 和 `sessionId`。
- 使用节点类型而非节点名称，或同时包含两者，使记录更一致，也更易搜索。

## 是否提供前端日志？ <a href="#front-end-logs" id="front-end-logs"></a>

目前不提供前端日志。使用 `Logger` 或 `LoggerProxy` 会在 `editor-ui` 包中产生错误，未来版本将实现此功能。

## 相关资源 <a id="related-resources"></a>

* [保持 n8n 运行](./)
* [监控 n8n](monitor-n8n.md)
* [使用 Grafana 可视化指标](visualize-metrics-with-grafana.md)
* [备份与恢复](backup-and-restore.md)
* [更新 n8n](update-n8n.md)
* [使用 OpenTelemetry 跟踪执行](trace-executions-with-opentelemetry.md)
