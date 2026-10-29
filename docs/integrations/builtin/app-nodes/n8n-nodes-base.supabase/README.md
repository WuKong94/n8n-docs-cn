---
title: Supabase 节点文档
description: 了解如何在 n8n 中使用 Supabase 节点，并按照技术文档将 Supabase 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.supabase
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.supabase/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Supabase 节点 <a href="#supabase-node" id="supabase-node"></a>

使用 Supabase 节点自动处理 Supabase 中的工作，并将其与其他应用集成。n8n 内置支持多种 Supabase 功能，包括创建、删除及获取行。

本页列出了 Supabase 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Supabase 凭据](../../credentials/supabase.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Row（行）
    * Create a new row（创建新行）
    * Delete a row（删除行）
    * Get a row（获取行）
    * Get all rows（获取所有行）
    * Update a row（更新行）

## 使用自定义模式 <a href="#using-custom-schemas" id="using-custom-schemas"></a>

默认情况下，Supabase 节点仅获取 `public` 模式。要获取[自定义模式](https://supabase.com/docs/guides/api/using-custom-schemas)，请启用 **Use Custom Schema**（使用自定义模式）。

在新增的 **Schema**（模式）字段中，填写 Supabase 节点应使用的自定义模式。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.supabase 集成模板](https://n8n.io/integrations/supabase)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
