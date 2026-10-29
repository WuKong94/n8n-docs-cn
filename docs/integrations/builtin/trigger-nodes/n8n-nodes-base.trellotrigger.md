---
title: Trello 触发器节点文档
description: 了解如何在 n8n 中使用 Trello 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Trello 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Trello 触发器节点 <a href="#trello-trigger-node" id="trello-trigger-node"></a>

[Trello](https://trello.com/) 是 Atlassian 旗下基于网页的看板式列表应用。用户可以创建包含不同列的任务看板，并在列之间移动任务。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Trello 凭据文档](../credentials/trello.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Trello Trigger 集成](https://n8n.io/integrations/trello-trigger/)页面。
{% endhint %}

## 查找 Model ID <a href="#find-the-model-id" id="find-the-model-id"></a>

Model ID 是 Trello 中任意模型的 ID，具体取决于使用场景，例如 User ID、List ID 等。

在此示例中，List ID 将用作 Model ID：

1. 打开包含所需列表的 Trello 看板。
2. 如果列表中没有卡片，先添加一张卡片。
3. 打开卡片，在 URL 末尾添加 `.json`，然后按 Enter。
4. 在 JSON 文件中找到名为 `idList` 的字段。
5. 复制 `idList`，粘贴到 n8n 的 **Model ID** 字段。

