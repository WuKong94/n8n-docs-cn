---
title: Splunk 节点文档
description: 了解如何在 n8n 中使用 Splunk 节点，并按照技术文档将 Splunk 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Splunk 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.splunk.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.splunk
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.splunk
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Splunk 节点 <a href="#splunk-node" id="splunk-node"></a>

使用 Splunk 节点自动处理 Splunk 中的工作，并将其与其他应用集成。n8n 内置支持多种 Splunk 功能，包括获取已触发告警的报告，以及删除和获取搜索配置。

本页列出了 Splunk 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Splunk 凭据](../credentials/splunk.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Fired Alert（已触发告警）
    * Get a fired alerts report（获取已触发告警报告）
* Search Configuration（搜索配置）
    * Delete a search configuration（删除搜索配置）
    * Get a search configuration（获取搜索配置）
    * Get many search configurations（获取多条搜索配置）
* Search Job（搜索任务）
    * Create a search job（创建搜索任务）
    * Delete a search job（删除搜索任务）
    * Get a search job（获取搜索任务）
    * Get many search jobs（获取多个搜索任务）
* Search Result（搜索结果）
    * Get many search results（获取多条搜索结果）
* User（用户）
    * Create a user（创建用户）
    * Delete a user（删除用户）
    * Get a user（获取用户）
    * Get many users（获取多条用户）
    * Update a user（更新用户）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Splunk 集成模板](https://n8n.io/integrations/splunk)，或[搜索所有模板](https://n8n.io/workflows/)
