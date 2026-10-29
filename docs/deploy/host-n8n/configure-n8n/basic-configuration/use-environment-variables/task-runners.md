---
title: 任务运行器环境变量
description: 配置自托管 n8n 实例任务运行器的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 任务运行器
originalFilePath: hosting/configuration/environment-variables/task-runners.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/task-runners
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 任务运行器环境变量 <a href="#task-runner-environment-variables" id="task-runner-environment-variables"></a>

{% hint style="info" %}
**通过文件配置**

与 n8n 主镜像不同，任务运行器镜像**不支持**通过文件配置密钥。因此，添加 `_FILE` 后缀的变量不会被识别。
{% endhint %}

[任务运行器](../../set-up-task-runners.md)执行 [Code 节点](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)中定义的代码。

## n8n 实例环境变量 <a href="#n8n-instance-environment-variables" id="n8n-instance-environment-variables"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_ENABLED` （**已弃用**） | Boolean | `false` | 是否启用任务运行器。自 n8n 2.0 起**弃用**。 |
| `N8N_RUNNERS_MODE` | 枚举字符串： `internal` （**已弃用**）, `external` | `internal` | 任务运行器的启动和运行方式。`internal` 表示由 n8n 以子进程方式启动运行器。**已弃用**：内部模式将在未来版本移除。`external` 表示由外部编排器启动运行器。参阅[外部模式](../../set-up-task-runners.md#external-mode)。 |
| `N8N_RUNNERS_AUTH_TOKEN` | String | 随机字符串 | 任务运行器向 n8n 验证身份所用的共享密钥。使用 `external` 模式时必需。 |
| `N8N_RUNNERS_BROKER_PORT` | Number | `5679` | 任务代理监听运行器连接的端口。 |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` | String | `127.0.0.1` | 任务代理监听的地址。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | 任务代理与运行器之间通信的负载大小上限，单位为字节。 |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | 任务运行器使用的 `--max-old-space-size` 选项，单位为 MB。Node.js 默认根据可用内存设置。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | 单个任务运行器同时执行的任务数量。 |
| `N8N_RUNNERS_TASK_TIMEOUT` | Number | `300` | 任务最长运行时长，单位为秒。超过后运行器停止任务并重启。必须大于 0。 |
| `N8N_RUNNERS_HEARTBEAT_INTERVAL` | Number | `30` | 运行器向任务代理发送心跳的间隔，单位为秒。未及时发送心跳时，任务停止，运行器重启。必须大于 0。 |
| `N8N_RUNNERS_INSECURE_MODE` | Boolean | `false` | 是否关闭任务运行器的全部安全措施，以兼容依赖不安全 JavaScript 特性的模块。**不建议在生产环境使用。** |
| `N8N_RUNNERS_TASK_REQUEST_TIMEOUT` | Number | `60` | 任务请求等待可用运行器的最长时长，单位为秒，超过后超时，避免无运行器可用时工作流无限挂起。必须大于 0。 |

## 任务运行器启动器环境变量 <a href="#task-runner-launcher-environment-variables" id="task-runner-launcher-environment-variables"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_LAUNCHER_LOG_LEVEL` | 枚举字符串： `debug`, `info`, `warn`, `error` | `info` | 显示哪些日志消息。 |
| `N8N_RUNNERS_AUTH_TOKEN` | String | - | 向 n8n 验证身份所用的共享密钥。 |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | 空闲运行器关闭前等待的秒数。 |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | 任务代理服务器，即 n8n 实例的 URI。 |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | 启动器健康检查服务器的端口。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | 任务代理与运行器之间通信的负载大小上限，单位为字节。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | 单个任务运行器同时执行的任务数量。 |

## 任务运行器环境变量（所有语言） <a href="#task-runner-environment-variables-all-languages" id="task-runner-environment-variables-all-languages"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_GRANT_TOKEN` | String | 随机字符串 | 运行器向任务代理验证身份所用的令牌，由启动器自动提供。 |
| `N8N_RUNNERS_ID` | String | 随机字符串 | 运行器向任务代理标识自身的 ID。在 `internal` 模式下，由 n8n 为每个启动的运行器设置。在 `external` 模式下，除非需要代理日志中的 ID 稳定，否则请勿设置。每个运行器必须使用唯一值，两个运行器共用 ID 会不断互相挤掉连接。应按运行器类型设置为 `env-override`，放在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中，不要作为容器环境变量设置。自 n8n 2.35.0 起提供。 |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | 空闲运行器关闭前等待的秒数。 |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | 任务代理服务器，即 n8n 实例的 URI。 |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | 启动器健康检查服务器的端口。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | 任务代理与运行器之间通信的负载大小上限，单位为字节。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | 单个任务运行器同时执行的任务数量。 |

## 任务运行器环境变量（JavaScript） <a href="#task-runner-environment-variables-javascript" id="task-runner-environment-variables-javascript"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | 允许用户在 Code 节点中导入指定的内置模块，使用 * 允许全部。n8n 默认禁用模块导入。在外部模式下，请在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中设置为 `env-override`，不要作为容器环境变量设置。 |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | 允许用户在 Code 节点中导入指定的外部模块，来源为 `n8n/node_modules`。n8n 默认禁用模块导入。在外部模式下，请在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中设置为 `env-override`，不要作为容器环境变量设置。 |
| `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION` | Boolean | `false` | 是否允许外部库修改原型。设为 `true`，可使用依赖运行时原型修改的模块，例如 [`puppeteer`](https://pptr.dev/)，但会降低安全限制。 |
| `GENERIC_TIMEZONE` | * | `America/New_York` | 与 [n8n 实例配置的默认时区相同](timezone-and-localization.md)。 |
| `NODE_OPTIONS` | String | - | Node.js 的[选项](https://nodejs.org/api/cli.html#node_optionsoptions)。 |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | 任务运行器使用的 `--max-old-space-size` 选项，单位为 MB。Node.js 默认根据可用内存设置。 |

## 任务运行器环境变量（Python） <a href="#task-runner-environment-variables-python" id="task-runner-environment-variables-python"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_STDLIB_ALLOW` | String | - | Code 节点允许使用的 Python 标准库模块，包括子模块。使用 `*` 可允许全部标准库模块。n8n 默认禁用所有 Python 标准库导入。在外部模式下，请在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中设置为 `env-override`，不要作为容器环境变量设置。 |
| `N8N_RUNNERS_EXTERNAL_ALLOW` | String | - | Code 节点允许使用的第三方 Python 模块，包括子模块。使用 `*` 可允许全部外部模块。n8n 默认禁用全部第三方 Python 模块。模块必须[包含](../../set-up-task-runners.md#adding-extra-dependencies)在 `n8nio/runners` 镜像中。在外部模式下，请在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中设置为 `env-override`，不要作为容器环境变量设置。 |
| `N8N_RUNNERS_ALLOW_TRANSITIVE_IMPORTS` | Boolean | `false` | 允许列表中包自身代码执行的导入，是否跳过 `N8N_RUNNERS_EXTERNAL_ALLOW` 和 `N8N_RUNNERS_STDLIB_ALLOW` 两项导入允许列表。设为 `true`，允许这些包加载其传递依赖和标准库，而无需逐一列出模块。适用于内部导入还会引入其他模块的包，例如 `pandas` 导入 `pytz`，或 `boto3` 导入 `dateutil`。你在 Code 节点中编写的导入仍会检查允许列表。启用后信任的是所有已安装包的导入行为，而非仅指定的包；被入侵的依赖可能引入原本会被阻止的模块，因此只有信任运行器镜像中全部已安装包时才应启用。在外部模式下，请在[运行器配置文件](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中设置为 `env-override`，不要作为容器环境变量设置。 |
| `N8N_RUNNERS_BUILTINS_DENY` | String | `eval,exec,compile,open,input,breakpoint,getattr,object,type,vars,setattr,delattr,hasattr,dir,memoryview,__build_class__,globals,locals` | Code 节点中禁止使用的 Python 内置项。设为空字符串可允许全部内置项。 |
| `N8N_BLOCK_RUNNER_ENV_ACCESS` | Boolean | `true` | 是否禁止 Python 代码任务访问运行器环境。设为 `false`，允许所有 Python Code 节点用户通过 `os.environ` 访问运行器环境。出于安全原因，默认禁止访问环境变量。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
