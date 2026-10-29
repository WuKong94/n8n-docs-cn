---
title: Segment 节点文档
description: 了解如何在 n8n 中使用 Segment 节点，并按照技术文档将 Segment 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Segment 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.segment.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Segment 节点 <a href="#segment-node" id="segment-node"></a>

使用 Segment 节点自动处理 Segment 中的工作，并将其与其他应用集成。n8n 内置支持多种 Segment 功能，包括将用户加入群组、创建身份标识和跟踪活动。

本页列出了 Segment 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Segment 凭据](../credentials/segment.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Group（群组）
    * Add a user to a group（将用户添加到群组）
* Identify（识别身份）
    * Create an identity（创建身份标识）
* Track（跟踪）
    * 记录用户执行的操作。每项操作都会触发一个事件，事件也可以包含关联属性。
    * 记录网站的页面浏览情况，并可附加所浏览页面的额外信息。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Segment 集成模板](https://n8n.io/integrations/segment)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
