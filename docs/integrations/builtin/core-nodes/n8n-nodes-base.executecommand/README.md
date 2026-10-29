---
title: Execute Command 节点
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.executecommand
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executecommand/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand
description: 了解 n8n 中 Execute Command 节点的用法，并查看相关示例。
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


# Execute Command（执行命令） <a id="execute-command"></a>

Execute Command 节点在运行 n8n 的主机上执行 shell 命令。

{% hint style="warning" %}
**安全注意事项**

在存在不可信用户的环境中，Execute Command 节点可能带来较大的安全风险，因此从 n8n 2.0 起默认[禁用](../../../../deploy/host-n8n/configure-n8n/security/block-specific-nodes.md#exclude-nodes)。
{% endhint %}

{% hint style="info" %}
**由哪个 shell 运行命令？**

此节点使用主机的默认 shell 执行命令，例如 Windows 上的 `cmd` 和 macOS 上的 `zsh`。

如果使用 Docker 运行 n8n，命令在 n8n 容器中执行，而不是在 Docker 宿主机上执行。

使用[队列模式](../../../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md)时，生产执行中的命令会在实际处理任务的工作进程上运行。手动执行时，命令在主实例上运行，除非将 `OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS` 设为 `true`。
{% endhint %}

{% hint style="info" %}
**功能可用性**

Execute Command 节点可用于：

- **自托管：** 所有版本

n8n Cloud 不提供此节点。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Execute Once（只执行一次） <a href="#execute-once" id="execute-once"></a>

开启时，节点只执行一次；关闭时，每收到一个输入数据项就执行一次。

### Command（命令） <a href="#command" id="command"></a>

输入要在主机上执行的命令。运行[多条命令](./README.md#run-multiple-commands)和 [cURL 命令](./README.md#run-curl-command)的示例见下文。

#### 运行多条命令 <a href="#run-multiple-commands" id="run-multiple-commands"></a>

可使用以下两种方式之一，在同一个 Execute Command 节点中运行多条命令：

*   将命令写在同一行，用 `&&` 分隔。例如，使用 `&&` 将切换目录命令 cd 与列出目录内容的 ls 组合起来。

    ```bash
    cd bin && ls
    ```
*   将每条命令写在单独一行。例如，在切换目录命令 cd 之后，另起一行写入 ls。

    ```bash
    cd bin
    ls
    ```

#### 运行 cURL 命令 <a href="#run-curl-command" id="run-curl-command"></a>

也可以使用 [HTTP Request](../n8n-nodes-base.httprequest/README.md) 节点发起 cURL 请求。

要在 Execute Command 节点中运行 curl，需要基于现有 n8n 镜像构建 Docker 镜像。默认 n8n Docker 镜像使用 Alpine Linux。

{% hint style="info" %}
**n8n 镜像不包含 `apk`**

官方 n8n Docker 镜像已移除 `apk` 包管理器。安装 `curl` 等软件包前，需要先从新的 Alpine 基础镜像恢复 `apk`，如下所示。
{% endhint %}

1. 创建名为 `Dockerfile` 的文件。
2. 将以下代码片段添加到 Dockerfile。

```shell
   FROM n8nio/n8n
   USER root

   # Restore the apk package manager (removed from the base image)
   COPY --from=alpine:3.22 /sbin/apk /sbin/apk
   COPY --from=alpine:3.22 /lib/apk /lib/apk
   COPY --from=alpine:3.22 /usr/lib/libapk* /usr/lib/

   RUN apk add --no-cache curl
   USER node
```
3. 在同一文件夹中执行以下命令，构建 Docker 镜像。

```shell
   docker build -t n8n-curl .
```
4. 替换之前使用的 Docker 镜像。例如，将 `n8nio/n8n` 替换为 `n8n-curl`。
5. 运行新创建的 Docker 镜像，之后便可通过 Execute Command 节点执行 curl。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-base.executecommand 集成模板](https://n8n.io/integrations/execute-command)，或[搜索所有模板](https://n8n.io/workflows/)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见疑问或问题及建议的解决方法，请参阅[常见问题](common-issues.md)。
