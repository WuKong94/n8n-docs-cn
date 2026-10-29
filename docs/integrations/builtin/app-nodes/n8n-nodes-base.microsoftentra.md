---
title: Microsoft Entra ID 节点文档
description: 了解如何在 n8n 中使用 Microsoft Entra ID 节点，并按照技术文档将 Microsoft Entra ID 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Microsoft Entra ID 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Entra ID 节点 <a href="#microsoft-entra-id-node" id="microsoft-entra-id-node"></a>

使用 Microsoft Entra ID 节点自动处理 Microsoft Entra ID 中的工作，并将其与其他应用集成。n8n 内置支持多种 Microsoft Entra ID 功能，包括创建、获取、更新和删除用户及群组，以及将用户添加到群组或从中移除。

本页列出了 Microsoft Entra ID 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

该节点的身份验证信息，请参阅 [Microsoft Entra ID 凭据文档](../credentials/microsoftentra.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（US Government、US Government DOD 或 China），请在 Microsoft Entra ID 凭据配置中选择适当的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Group**（群组）
    * **Create**（创建）：创建新群组。
    * **Delete**（删除）：删除已有群组。
    * **Get**（获取）：获取指定群组的数据。
    * **Get Many**（获取多条）：获取群组列表。
    * **Update**（更新）：更新群组。
* **User**（用户）
    * **Create**（创建）：创建新用户。
    * **Delete**（删除）：删除已有用户。
    * **Get**（获取）：获取指定用户的数据。
    * **Get Many**（获取多条）：获取用户列表。
    * **Update**（更新）：更新用户。
    * **Add to Group**（添加到群组）：将用户添加到群组。
    * **Remove from Group**（从群组移除）：将用户从群组移除。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Microsoft Entra ID 集成模板](https://n8n.io/integrations/microsoft-entra-id-azure-active-directory)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [Microsoft Entra ID 文档](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0)。


{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Microsoft Entra ID 节点的常见错误和问题，以及解决或排查步骤。

### 更新 Allow External Senders 和 Auto Subscribe New Members 选项失败 <a href="#updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails" id="updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails"></a>

创建新群组后，无法立即更新 **Allow External Senders**（允许外部发件人）和 **Auto Subscribe New Members**（自动订阅新成员）选项。必须在创建群组后等待一段时间，才能更改这些选项的值。

设计工作流，使用多个 Microsoft Entra ID 节点先创建群组再更新这些选项时，请在两个操作之间添加 [Wait](../core-nodes/n8n-nodes-base.wait.md) 节点。将 Wait 节点配置为暂停至少两秒，为群组完成初始化留出时间。等待后，更新操作即可完成而不报错。
