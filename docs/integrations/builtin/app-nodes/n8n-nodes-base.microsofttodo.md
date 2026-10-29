---
title: Microsoft To Do 节点文档
description: 了解如何在 n8n 中使用 Microsoft To Do 节点，并按照技术文档将 Microsoft To Do 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft To Do 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft To Do 节点 <a href="#microsoft-to-do-node" id="microsoft-to-do-node"></a>

使用 Microsoft To Do 节点自动处理 Microsoft To Do 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft To Do 功能，包括创建、更新、删除和获取关联资源、列表和任务。

本页列出了 Microsoft To Do 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。该节点也支持通过 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)进行无需用户登录的仅应用访问：在 **Authentication（身份验证）** 下拉列表中选择 **Microsoft Entra Service Principal (App-Only)**。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Linked Resource（关联资源）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）
* List（列出）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）
* Task（任务）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft To Do 集成模板](https://n8n.io/integrations/microsoft-to-do)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
