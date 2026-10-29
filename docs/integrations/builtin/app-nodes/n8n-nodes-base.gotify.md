---
title: Gotify 节点文档
description: 了解如何在 n8n 中使用 Gotify 节点，并按照技术文档将 Gotify 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Gotify 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gotify.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gotify 节点 <a href="#gotify-node" id="gotify-node"></a>

使用 Gotify 节点自动处理 Gotify 中的工作，并将其与其他应用集成。n8n 内置支持多种 Gotify 功能，包括创建、删除和获取消息。

本页列出了 Gotify 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Gotify 凭据](../credentials/gotify.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Message（消息）
    * Create（创建）
    * Delete（删除）
    * Get All（获取全部）

## 创建消息 <a id="create-message"></a>

创建消息时，可配置以下内容：

### 附加字段 <a id="additional-fields"></a>

- **Priority**（优先级）：消息的优先级，默认为 1。
- **Title**（标题）：消息标题。

### 选项 <a id="options"></a>

- **Content Type**（内容类型）：消息的内容类型，可选择：
    - **Plain**（纯文本）：消息以纯文本呈现，为默认选项。
    - **Markdown**：消息以 Markdown 呈现。
- **Click URL**（点击 URL）：点击通知时打开此 URL。
- **Big Image URL**（大图 URL）：在通知中显示大图。
- **Intent URL**：通知送达后打开 Intent URL，仅限 Android。

/// note | 消息附加功能
**Options**（选项）中的字段（**Click URL**、**Big Image URL** 和 **Intent URL**）使用 Gotify 的消息附加功能，可自定义通知在 Gotify 客户端中的显示方式和行为。更多信息请参阅 [Gotify 的消息附加功能文档](https://gotify.net/docs/msgextras){:target="_blank" .external-link}。
///

## 模板与示例 <a id="templates-and-examples"></a>
## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Gotify 集成模板](https://n8n.io/integrations/gotify)，或[搜索所有模板](https://n8n.io/workflows/)
