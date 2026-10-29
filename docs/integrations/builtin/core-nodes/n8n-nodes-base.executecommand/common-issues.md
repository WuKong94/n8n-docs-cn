---
title: Execute Command 节点常见问题
description: 了解 n8n 中 Execute Command 节点的常见问题、排查步骤和建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: Execute Command 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Execute Command 节点常见问题 <a href="#execute-command-node-common-issues" id="execute-command-node-common-issues"></a>

本页介绍 [Execute Command 节点](README.md)的常见错误和问题，以及解决或排查步骤。


## Command failed: &lt;command&gt; /bin/sh: &lt;command&gt;: not found（命令失败：找不到命令） <a href="#command-failed-andltcommandandgt-binsh-andltcommandandgt-not-found" id="command-failed-andltcommandandgt-binsh-andltcommandandgt-not-found"></a>


shell 环境找不到 **Command**（命令）参数中的某条命令时，会出现此错误。

请检查以下内容：

* **Command**（命令）参数中的命令及参数是否存在拼写错误。
* 命令是否位于运行 n8n 的用户的 `PATH` 中。
* 如果使用 Docker 运行 n8n，尝试在容器内手动运行命令，检查其是否可用。容器未包含所需命令时，可能需要基于官方 n8n 镜像创建包含该命令的[自定义镜像](https://docs.docker.com/build/building/base-images/)。
    * n8n 已运行时：
		```sh
		# Find n8n's container ID, it will be the first column
		docker ps | grep n8n
		# Try to execute the command within the running container
		docker container exec <container_ID> <command_to_run>
		```
    * n8n 未运行时：
		```sh
		# Start up a new container that runs the command instead of n8n
		# Use the same image and tag that you use to run n8n normally
		docker run -it --rm --entrypoint /bin/sh n8nio/n8n -c <command_to_run>
		```


## Error: stdout maxBuffer length exceeded（标准输出超过最大缓冲区长度） <a href="#error-stdout-maxbuffer-length-exceeded" id="error-stdout-maxbuffer-length-exceeded"></a>


命令返回的输出超过 Execute Command 节点单次能够处理的数量时，会出现此错误。

减少命令输出可以避免此错误。查看命令手册或文档，确认是否有用于限制或筛选输出的参数。如果没有，可能需要通过管道将输出传给其他命令，去掉不需要的信息。


## PowerShell 命令在换行处被截断 <a id="powershell-commands-get-truncated-at-line-breaks"></a>

在 Windows 上，Execute Command 节点将 **Command**（命令）参数作为单个字符串传给系统 shell。命令中包含换行时，shell 只执行第一行，并忽略其余行。

这是 Windows shell 的限制，底层 `cmd.exe` 进程将每个换行视为命令结束。

将 PowerShell 命令写在单行中可以解决此问题。命令较复杂时，用分号连接各条语句：

```powershell
powershell -Command "Get-ChildItem C:\Data; Write-Output 'Done'"
```

对于较长的脚本，将其保存为文件，再使用 `-File` 参数运行：

```powershell
powershell -File C:\Scripts\my-script.ps1
```