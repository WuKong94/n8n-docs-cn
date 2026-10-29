---
description: 为 n8n Assistant 和已连接的 MCP 客户端提供可复用上下文，说明你和团队在 n8n 中的构建方式。
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
  anchors:
    visible: true
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 智能体上下文管理 <a id="agentic-context-management"></a>

智能体上下文管理可以向 n8n 中的 AI 工具提供可复用上下文，例如命名规则和首选节点，无需在每条提示词中重复说明。

{% hint style="info" %}
**预览状态**

智能体上下文管理处于预览阶段，未来版本中可能变化。请避免在生产环境中依赖此功能。
{% endhint %}

{% include "../../reusable-content/.gitbook/includes/agent-search-endpoint.md" %}

## 上下文如何传递给 AI 工具 <a id="how-context-reaches-ai-tools"></a>

在 **Settings（设置）** > **Context（上下文）** 中管理上下文。n8n 只存储一份，再传递给所有读取它的 AI 功能：

* **n8n Assistant** 会在每条消息中读取上下文，因此编辑从下一条消息起生效。
* 连接 [n8n MCP 服务器](../../connect/connect-to-n8n-mcp-server.md)的 **MCP 客户端**，会在每次调用相关 MCP 工具时读取上下文。

上下文遵循 n8n 的权限规则。每个人只能收到有权查看的上下文，只有具备相应角色的人才能修改适用于他人的上下文。

## 上下文类型 <a id="types-of-context"></a>

目前 n8n 支持一种上下文：[偏好设置](preferences.md)。偏好是简短指令，例如“始终连接错误工作流”，AI 工具每次为你构建工作流和智能体时都会应用。可以为自己、某个项目或实例中的所有人保存偏好。

## 相关资源 <a id="related-resources"></a>

* [构建](../)
* [构建工作流的方式](../ways-of-building-workflows/)
* [构建和管理智能体](../build-and-manage-agents/)
* [集成 AI](../integrate-ai/)
* [管理工作流](../manage-workflows/)
* [流程逻辑](../flow-logic/)
* [处理数据](../work-with-data/)
* [在 n8n 中编写代码](../code-in-n8n/)
* [键盘快捷键](../keyboard-shortcuts.md)
