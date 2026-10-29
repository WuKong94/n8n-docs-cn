---
title: 测试节点
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

可通过 [`n8n-node` 工具](../../../../../connect/create-nodes/build-your-node/using-the-n8n-node-tool.md)，在本地 n8n 实例中运行节点，边开发边测试。`n8n-node` 包含 n8n，因此无需全局安装 n8n。

1. 在项目根目录运行 `dev` 命令：
	```shell
	npm run dev
	```
	此命令运行 `n8n-node dev`，构建节点并将其链接到 n8n 自定义节点目录，随后启动加载该节点的本地 n8n 实例，并在文件更改时重建节点。

	{% hint style="info" %}
	**自定义节点目录**

	`n8n-node dev` 使用独立的 n8n 用户目录 `.n8n-node-cli`，不会影响已有的 n8n 安装。默认位置取决于操作系统：
	- Windows：`C:\Users\<username>\.n8n-node-cli\.n8n\custom`
	- Linux：`/home/<username>/.n8n-node-cli/.n8n/custom`
	- macOS：`/Users/<username>/.n8n-node-cli/.n8n/custom`

	要针对自己运行的 n8n 实例测试，请传入 `--external-n8n`，并将 `--custom-user-folder <path>` 设为该实例的用户目录，即其 `.n8n` 目录的父目录。在该实例中设置 `N8N_DEV_RELOAD=true`，使其加载更改。

	注意：`.n8n-node-cli` 和 `.n8n` 为隐藏目录，文件浏览器可能不显示它们。
	{% endhint %}
2. 在浏览器中打开 `http://localhost:5678`，登录 n8n 实例。
3. 打开工作流，在节点面板中搜索你的节点。

	{% hint style="info" %}
	**节点名称**

	请使用节点名称搜索，而不是软件包名称。例如，npm 软件包名为 `n8n-nodes-weather-nodes`，其中包含 `rain`、`sun`、`snow` 三个节点时，应搜索 `rain`，而非 `weather-nodes`。
	{% endhint %}

将节点添加到工作流，在开发过程中测试。要停止 n8n，请按 `ctrl` + `c`。
