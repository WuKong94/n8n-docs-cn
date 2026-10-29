---
title: Microsoft OneDrive 触发器节点文档
description: 了解如何在 n8n 中使用 Microsoft OneDrive 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft OneDrive 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft OneDrive 触发器节点 <a href="#microsoft-onedrive-trigger-node" id="microsoft-onedrive-trigger-node"></a>

使用 Microsoft OneDrive Trigger 节点响应 [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage) 中的事件，并将其与其他应用集成。n8n 内置支持 OneDrive 的文件和文件夹事件。

本页列出了 Microsoft OneDrive Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Microsoft 凭据文档](../credentials/microsoft.md)。它也支持 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)，可在没有用户登录的情况下提供仅应用访问；在 **Authentication**（身份验证）下拉菜单中选择 **Microsoft Entra Service Principal (App-Only)**。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（US Government、US Government DOD 或 China），请在 Microsoft 凭据配置中选择适当的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Microsoft OneDrive 集成](https://n8n.io/integrations/microsoft-onedrive-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* On File Created（文件已创建时）
* On File Updated（文件已更新时）
* On Folder Created（文件夹已创建时）
* On Folder Updates（文件夹更新时）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft OneDrive 提供应用节点。更多信息请参阅 [Microsoft OneDrive 节点文档](../app-nodes/n8n-nodes-base.microsoftonedrive.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/microsoft-onedrive-trigger/)。

该服务的更多信息，请参阅 [Microsoft OneDrive API 文档](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)。
