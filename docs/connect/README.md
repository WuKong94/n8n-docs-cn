---
contentType: guide
nodeTitle: 连接
originalFilePath: api/n8n-cli/index.md
originalUrl: https://docs.n8n.io/api/n8n-cli
url: https://docs.n8n.io/connect/
description: 使用 API、CLI 和 MCP 服务器，以编程方式连接 n8n。
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 连接 <a id="connect"></a>

通过代码、脚本和 AI 工具连接 n8n。

如果你需要在编辑器之外使用 n8n，请查阅本节文档。你可以调用公共 API、使用 CLI 编写脚本，或连接兼容 MCP 的客户端。

本节包含 n8n API 指南与参考资料、n8n CLI 参考，以及内置 n8n MCP 服务器文档。内容还涵盖身份验证、连接设置，以及将不同客户端的工具和智能体连接到 n8n 的具体说明。

{% hint style="info" %}
选择适合你工作流程的接口。每种方式采用不同的访问模型，适合不同任务。
{% endhint %}

{% tabs %}
{% tab title="n8n API" %}
通过 HTTP 以编程方式管理 n8n。

适合：

* 基于 n8n 构建平台和工具
* 从外部系统触发和监控执行
* 自动管理工作流和凭据

从 [n8n API](n8n-api/README.md) 开始。
{% endtab %}

{% tab title="n8n CLI" %}
直接通过终端控制 n8n。

适合：

* 导入和导出工作流
* 在脚本和 CI 流水线中运行执行任务
* 本地开发和调试

从 [n8n CLI](n8n-cli.md) 开始。
{% endtab %}

{% tab title="MCP 服务器" %}
将 AI 智能体和 MCP 客户端直接连接到你的 n8n 实例。

适合：

* Claude Code、Claude Desktop、Lovable 等工具
* 通过 AI 智能体发现和执行工作流
* 通过 MCP 客户端管理工作流

从[连接 n8n MCP 服务器](connect-to-n8n-mcp-server.md)开始。
{% endtab %}
{% endtabs %}

你也可以将 MCP 客户端连接到 [n8n 文档 MCP 服务器](connect-to-n8n-docs-mcp-server.md)，让 AI 工具能够搜索文档；或[创建自己的节点](create-nodes/README.md)，为 n8n 添加自定义集成。
