---
title: Google Workspace Admin 节点文档
description: 了解如何在 n8n 中使用 Google Workspace Admin 节点，并按照技术文档将 Google Workspace Admin
  节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Google Workspace Admin 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Workspace Admin 节点 <a href="#google-workspace-admin-node" id="google-workspace-admin-node"></a>

使用 Google Workspace Admin 节点自动处理 Google Workspace Admin 中的工作，并将其与其他应用集成。n8n 内置支持多种 Google Workspace Admin 功能，包括创建、更新、删除和获取用户、群组及 ChromeOS 设备。

本页列出了 Google Workspace Admin 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Google 凭据](../credentials/google/README.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* ChromeOS Device（ChromeOS 设备）
    * Get a ChromeOS device（获取 ChromeOS 设备）
    * Get many ChromeOS devices（获取多个 ChromeOS 设备）
    * Update a ChromeOS device（更新 ChromeOS 设备）
    * Change the status of a ChromeOS device（更改 ChromeOS 设备的状态）
* Group（群组）
    * Create a group（创建群组）
    * Delete a group（删除群组）
    * Get a group（获取群组）
    * Get many groups（获取多条群组）
    * Update a group（更新群组）
* User（用户）
    * Add an existing user to a group（将已有用户添加到群组）
    * Create a user（创建用户）
    * Delete a user（删除用户）
    * Get a user（获取用户）
    * Get many users（获取多条用户）
    * Remove a user from a group（将用户从群组移除）
    * Update a user（更新用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Workspace Admin 集成模板](https://n8n.io/integrations/google-workspace-admin)，或[搜索所有模板](https://n8n.io/workflows/)

## 控制获取用户的哪些自定义字段 <a href="#how-to-control-which-custom-fields-to-fetch-for-a-user" id="how-to-control-which-custom-fields-to-fetch-for-a-user"></a>

获取用户信息时，可通过三种方式控制要获取的自定义字段。使用 **Custom Fields**（自定义字段）参数选择以下选项之一：

- **Don't Include**（不包含）：不包含任何自定义字段。
- **Custom**（自定义）：包含 **Custom Schema Names or IDs**（自定义架构名称或 ID）中指定架构的自定义字段。
- **Include All**（包含全部）：包含与用户关联的所有字段。

包含自定义字段的步骤：

1. 从 **Custom Fields**（自定义字段）下拉菜单中选择 **Custom**（自定义）。
2. 在 **Custom Schema Names or IDs**（自定义架构名称或 ID）下拉菜单中选择要包含的架构名称。
