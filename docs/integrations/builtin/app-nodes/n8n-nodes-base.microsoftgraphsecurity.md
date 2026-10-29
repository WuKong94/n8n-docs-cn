---
title: Microsoft Graph Security 节点文档
description: 了解如何在 n8n 中使用 Microsoft Graph Security 节点，并按照技术文档将 Microsoft Graph Security
  节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft Graph Security 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Graph Security 节点 <a href="#microsoft-graph-security-node" id="microsoft-graph-security-node"></a>

使用 Microsoft Graph Security 节点自动处理 Microsoft Graph Security 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft Graph Security 功能，包括获取和更新评分及配置文件。

本页列出了 Microsoft Graph Security 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Secure Score（安全评分）
    * Get（获取）
    * Get All（获取全部）
* Secure Score Control Profile（安全评分控制配置文件）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Graph Security 集成模板](https://n8n.io/integrations/microsoft-graph-security)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
