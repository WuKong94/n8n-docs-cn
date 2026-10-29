---
title: 执行环境变量
description: 配置工作流执行相关设置的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 执行
originalFilePath: hosting/configuration/environment-variables/executions.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/executions
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 执行环境变量 <a href="#executions-environment-variables" id="executions-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

本页列出用于配置工作流执行设置的环境变量。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `EXECUTIONS_MODE` | 枚举字符串： `regular`, `queue` | `regular` | 执行应直接运行还是通过队列运行。<br><br>更多信息请参阅[队列模式](../../scaling/enable-queue-mode.md)。 |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | 为所有工作流设置默认超时，单位为秒，超时后 n8n 停止执行。用户可对单个工作流覆盖此值，但不能超过 `EXECUTIONS_TIMEOUT_MAX` 设置的时长。将 `EXECUTIONS_TIMEOUT` 设为 `-1` 可禁用超时。 |
| `EXECUTIONS_TIMEOUT_MAX` | Number | `3600` | 用户可以为单个工作流设置的最大执行时长，单位为秒。 |
| `N8N_AI_TIMEOUT_MAX` | Number | `3600000` | AI 和 LLM 节点，例如 OpenAI、Anthropic、Mistral、Ollama 的 HTTP 请求超时，单位为毫秒。控制 n8n 等待 AI 服务响应多久后超时，适用于较慢的本地 AI 服务或需要更长处理时间的复杂提示词。 |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | 枚举字符串： `all`, `none` | `all` | 是否在执行出错时保存执行数据。 |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | 枚举字符串： `all`, `none` | `all` | 是否在执行成功时保存执行数据。 |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | Boolean | `false` | 是否保存每个已执行节点的进度，true 表示保存，false 表示不保存。 |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | Boolean | `true` | 是否保存手动启动的执行数据。 |
| `N8N_EXECUTION_DATA_STORAGE_MODE` | 枚举字符串： `database`, `filesystem`, `s3`, `azure` | `database` | n8n 存储执行数据的位置。`s3` 和 `azure` 模式需要自托管商业版或企业版套餐。相关存储变量请参阅[外部数据存储](external-data-storage.md)。 |
| `N8N_STORAGE_PATH` | String | `N8N_USER_FOLDER/storage` | 文件系统存储的基础路径。当 `N8N_EXECUTION_DATA_STORAGE_MODE` 为 `filesystem` 时，n8n 在此存储执行数据；文件系统中的二进制数据也使用此路径。 |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | 是否滚动删除历史执行数据。 |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | 执行记录保留多久后删除，单位为小时。 |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | 数据库中保留的最大执行记录数，0 表示不限制。 |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | Number | `1` | 已完成的执行数据必须保留多久后才会被硬删除，单位为小时。默认的缓冲期会排除近期执行，因为用户构建工作流时可能仍需要这些数据。 |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | Number | `15` | 硬删除执行数据的频率，单位为分钟。 |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | Number | `60` | 软删除执行数据的频率，单位为分钟。 |
| `EXECUTIONS_DATA_MAX_DISPLAY_SIZE` | Number | `104857600` | 显示执行记录时，包括编辑器、执行详情和公共 API，n8n 加载的执行数据大小上限，单位为字节。较大的执行会省略数据，显示“too large to display（数据过大，无法显示）”，避免资源较少的实例耗尽内存。不影响重试或恢复执行，这些操作始终加载完整数据。设为 `0` 可禁用限制。 |
| `N8N_CONCURRENCY_PRODUCTION_LIMIT` | Number | `-1` | 常规模式和扩展模式下允许同时运行的生产执行数量上限。在常规模式下设为 `-1` 可禁用限制。 |
| `N8N_CONCURRENCY_EVALUATION_LIMIT` | Number | 许可证层级默认值 | 单次[评估](../../../../../build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md#run-test-cases-in-parallel)测试运行中，允许并行的测试用例数量上限。未设置时，按许可证层级确定：自托管社区版为 1，n8n Cloud Pro 为 1，自托管商业版为 3，n8n Cloud Enterprise 和自托管企业版为 5。设置此变量会覆盖层级默认值。 |
| `N8N_WORKFLOW_AUTODEACTIVATION_ENABLED` | Boolean | `false` | 工作流执行反复崩溃后，是否自动取消发布。 |
| `N8N_WORKFLOW_AUTODEACTIVATION_MAX_LAST_EXECUTIONS` | Number | `3` | 取消发布工作流前允许的执行崩溃次数。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
