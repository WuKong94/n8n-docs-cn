---
title: Microsoft Outlook 节点文档
description: 了解如何在 n8n 中使用 Microsoft Outlook 节点，并按照技术文档将 Microsoft Outlook 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: Microsoft Outlook 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Outlook 节点 <a href="#microsoft-outlook-node" id="microsoft-outlook-node"></a>

使用 Microsoft Outlook 节点自动处理 Microsoft Outlook 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft Outlook 功能，包括创建、更新、删除和获取文件夹、消息及草稿。

本页列出了 Microsoft Outlook 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的 **Authentication**（身份验证）下拉菜单提供三个选项：

- **Outlook OAuth2**：专用于 Microsoft Outlook 的 OAuth2 凭据，为默认选项。
- **Microsoft OAuth2 (Graph)**：通用 Microsoft Graph 凭据，可在其他 Microsoft 节点中复用。选择此选项时，确保凭据获得该节点所需的作用域，例如 `Mail.ReadWrite`、`Mail.Send`、`Calendars.ReadWrite` 和 `Contacts.ReadWrite`。
- **Microsoft Entra Service Principal (App-Only)**：通过 Microsoft Entra 应用注册提供仅应用访问，无需用户登录，从节点版本 2 起可用。配置方法和所需应用权限，请参阅 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)。

有关身份验证设置，请参阅 [Microsoft 凭据](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（美国政府、美国国防部或中国），请确保在 Microsoft 凭据配置中选择正确的 **Microsoft Graph API Base URL（Microsoft Graph API 基础 URL）**。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Calendar（日历）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Contact（联系人）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Draft（草稿）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Send（发送）
	* Update（更新）
* Event（事件）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Folder（文件夹）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Update（更新）
* Folder Message（文件夹中的消息）
    * Get Many（获取多条）
* Message（消息）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）
	* Move（移动）
	* Reply（回复）
	* Send（发送）
	* Send and Wait for Response（发送并等待回复）
	* Update（更新）
* Message Attachment（消息附件）
	* Add（添加）
	* Download（下载）
	* Get（获取）
	* Get Many（获取多条）

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/send-and-wait-operation.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Outlook 集成模板](https://n8n.io/integrations/microsoft-outlook)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Outlook API 文档](https://learn.microsoft.com/en-us/outlook/rest/get-started)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
