---
title: RSS Feed Trigger（RSS 订阅源触发器） 节点文档
description: 了解如何在 n8n 中使用 RSS Feed Trigger（RSS 订阅源触发器） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: RSS Feed Trigger（RSS 订阅源触发器） 节点文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# RSS Feed Trigger（RSS 订阅源触发器） 节点 <a href="#rss-feed-trigger-node" id="rss-feed-trigger-node"></a>

RSS Feed Trigger 节点支持在 RSS 订阅源发布新条目时启动 n8n 工作流。

本页列出了 RSS Feed Trigger 节点支持的操作，并提供更多资源的链接。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Poll Times**（轮询时间）：选择轮询 **Mode**（模式）以设置轮询触发频率。所选模式会添加或移除相应字段。各模式的参数配置，请参阅下方各节。
* **Feed URL**（订阅源 URL）：输入要轮询的 RSS 订阅源 URL。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/poll-modes.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 RSS Feed Trigger（RSS 订阅源触发器） 集成模板](https://n8n.io/integrations/rss-feed-trigger)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 RSS 订阅源提供应用节点。更多信息请参阅 [RSS Read 节点文档](n8n-nodes-base.rssfeedread.md)。
