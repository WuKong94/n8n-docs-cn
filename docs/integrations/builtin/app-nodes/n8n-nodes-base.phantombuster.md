---
title: PhantomBuster 节点文档
description: 了解如何在 n8n 中使用 PhantomBuster 节点，并按照技术文档将 PhantomBuster 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: PhantomBuster 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.phantombuster.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# PhantomBuster 节点 <a href="#phantombuster-node" id="phantombuster-node"></a>

使用 PhantomBuster 节点自动处理 PhantomBuster 中的工作，并将其与其他应用集成。n8n 内置支持多种 PhantomBuster 功能，包括添加、删除和获取 Agent（自动化代理）。

本页列出了 PhantomBuster 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [PhantomBuster 凭据](../credentials/phantombuster.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Agent（自动化代理）
    * Delete an agent by ID.（按 ID 删除 Agent）
    * Get an agent by ID.（按 ID 获取 Agent）
    * Get all agents of the current user's organization.（获取当前用户所属组织的全部 Agent）
    * Get the output of the most recent container of an agent.（获取 Agent 最近一个容器的输出）
    * Add an agent to the launch queue.（将 Agent 加入启动队列）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 PhantomBuster 集成模板](https://n8n.io/integrations/phantombuster)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
