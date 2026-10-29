---
title: Redis 触发器节点文档
description: 了解如何在 n8n 中使用 Redis 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Redis 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Redis 触发器节点 <a href="#redis-trigger-node" id="redis-trigger-node"></a>

[Redis](https://redis.io/) 是开源的内存数据结构存储系统，可用作数据库、缓存和消息代理。

使用 Redis Trigger 节点订阅 Redis 频道。频道每次收到新消息时，工作流都会启动。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Redis 凭据文档](../credentials/redis.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Redis Trigger 集成](https://n8n.io/integrations/redis-trigger/)页面。
{% endhint %}

