---
contentType: explanation
nodeTitle: 选择节点类型
originalFilePath: integrations/creating-nodes/plan/node-types.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/plan/node-types
url: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-type
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点类型：触发器与操作 <a href="#node-types-trigger-and-action" id="node-types-trigger-and-action"></a>

可以为 n8n 构建两类节点：触发节点和操作节点。

两种类型都能与外部服务集成。

## 触发节点 <a href="#trigger-nodes" id="trigger-nodes"></a>

[触发节点](#user-content-fn-1)[^1]启动工作流并提供初始数据。工作流可包含多个触发节点，但每次执行只会根据触发事件运行其中一个。

n8n 中有三种触发节点：

| 类型 | 说明 | 示例节点 |
| --- | --- | --- |
| Webhook | 用于支持 Webhook 的服务。监听事件并实时触发工作流。 | [Zendesk Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Zendesk)、[Telegram Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Telegram)、[Brevo Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Brevo) |
| 轮询 | 用于不支持 Webhook 的服务。定期检查新数据，发现更新时触发工作流。 | [Airtable Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable)、[Gmail Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Gmail)、[Google Sheet Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Sheet)、[RssFeed Read Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/RssFeedRead) |
| 其他 | 处理与 HTTP 请求或轮询无关的实时响应，包括消息队列节点和基于时间的触发器。 | [AMQP Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Amqp)、[RabbitMQ Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/RabbitMQ)、[MQTT Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/MQTT)、[Schedule Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Schedule)、[Email Trigger (IMAP)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/EmailReadImap) |

## 操作节点 <a href="#action-nodes" id="action-nodes"></a>

操作节点在工作流中执行具体操作，包括处理数据以及在其他系统中触发事件。

<a id="user-content-fn-1"></a>
[^1]: 触发节点是一类特殊节点，负责在满足特定条件时启动工作流。所有生产工作流都需要至少一个触发器，用于确定工作流何时运行。

## 相关资源 <a id="related-resources"></a>

* [规划节点](./)
* [选择节点开发方式](choose-a-node-building-style.md)
* [节点界面设计](node-ui-design.md)
* [选择节点文件结构](choose-node-file-structure.md)
