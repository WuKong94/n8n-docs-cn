---
title: Microsoft Outlook 触发器节点文档
description: 了解如何在 n8n 中使用 Microsoft Outlook 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Outlook 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Outlook 触发器节点 <a href="#microsoft-outlook-trigger-node" id="microsoft-outlook-trigger-node"></a>

使用 Microsoft Outlook Trigger 节点响应 [Microsoft Outlook](https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook) 中的事件，并将其与其他应用集成。

本页列出了 Microsoft Outlook Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的 **Authentication**（身份验证）下拉菜单提供三个选项：

- **Outlook OAuth2**：专用于 Microsoft Outlook 的 OAuth2 凭据，为默认选项。
- **Microsoft OAuth2 (Graph)**：通用 Microsoft Graph 凭据，可在其他 Microsoft 节点中复用。选择此选项时，确保凭据获得该节点所需的作用域，例如 `Mail.ReadWrite`。
- **Microsoft Entra Service Principal (App-Only)**：通过 Microsoft Entra 应用注册提供仅应用访问，无需用户登录。配置方法和所需应用权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

此节点的身份验证信息，请参阅 [Microsoft 凭据文档](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（US Government、US Government DOD 或 China），请在 Microsoft 凭据配置中选择适当的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Microsoft Outlook 集成](https://n8n.io/integrations/microsoft-outlook-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Message Received（已收到消息）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft Outlook 提供应用节点。更多信息请参阅 [Microsoft Outlook 节点文档](../app-nodes/n8n-nodes-base.microsoftoutlook.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/microsoft-outlook-trigger/)。

