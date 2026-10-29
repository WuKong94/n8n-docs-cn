---
title: Redis 节点文档
description: 了解如何在 n8n 中使用 Redis 节点，并按照技术文档将 Redis 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Redis 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.redis.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Redis 节点 <a href="#redis-node" id="redis-node"></a>

使用 Redis 节点自动处理 Redis 中的工作，并将其与其他应用集成。n8n 内置支持多种 Redis 功能，包括删除键、获取键值、设置键值，以及向 Redis 频道发布消息。

本页列出了 Redis 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Redis 凭据](../credentials/redis.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* 从 Redis 删除键。
* 从 Redis 获取键的值。
* 返回 Redis 实例的基本信息。
* 以原子方式将键的值递增 1；键不存在时创建该键。
* 返回匹配指定模式的全部键。
* 在 Redis 中设置键的值。
* 向 Redis 频道发布消息。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Redis 集成模板](https://n8n.io/integrations/redis)，或[搜索所有模板](https://n8n.io/workflows/)
