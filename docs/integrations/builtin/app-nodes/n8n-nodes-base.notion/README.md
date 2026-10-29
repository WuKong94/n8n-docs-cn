---
title: Notion 节点文档
description: 了解如何在 n8n 中使用 Notion 节点，并按照技术文档将 Notion 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.notion
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.notion/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Notion 节点 <a href="#notion-node" id="notion-node"></a>

使用 Notion 节点自动处理 Notion 中的工作，并将其与其他应用集成。n8n 内置支持多种 Notion 功能，包括获取和搜索数据库、创建页面及获取用户。

本页列出了 Notion 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Notion 凭据](../../credentials/notion.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Block（块）
    * Append After（在后方追加）
    * Get Many（获取多项）
    * Get Markdown（获取 Markdown）
* Data Source（数据源）
    * Get（获取）
    * Search（搜索）
* Database（数据库）
    * Get（获取）
* Database Page（数据库页面）
    * Create（创建）
    * Get（获取）
    * Get Many（获取多项）
    * Update（更新）
* Page（页面）
    * Archive（归档）
    * Create（创建）
    * Get Markdown（获取 Markdown）
    * Search（搜索）
    * Update Markdown（更新 Markdown）
* User（用户）
    * Get（获取）
    * Get Many（获取多项）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.notion 集成模板](https://n8n.io/integrations/notion)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 提供 Notion 触发器节点。更多信息，请参阅 [Notion Trigger 节点文档](../../trigger-nodes/n8n-nodes-base.notiontrigger.md)。

有关 API 的详细信息，请参阅 [Notion 文档](https://developers.notion.com/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
