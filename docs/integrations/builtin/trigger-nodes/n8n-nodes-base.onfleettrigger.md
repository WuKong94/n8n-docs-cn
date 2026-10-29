---
title: Onfleet 触发器节点文档
description: 了解如何在 n8n 中使用 Onfleet 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Onfleet 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Onfleet 触发器节点 <a href="#onfleet-trigger-node" id="onfleet-trigger-node"></a>

[Onfleet](https://onfleet.com/) 是提供最后一公里配送解决方案的物流平台。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Onfleet 凭据文档](../credentials/onfleet.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Onfleet Trigger 集成](https://n8n.io/integrations/onfleet-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

在以下情况触发工作流：

* SMS recipient opt out（短信收件人退订）
* SMS recipient response missed（短信收件人回复缺失）
* Task arrival（任务到达）
* Task assigned（任务已分配）
* Task cloned（任务已克隆）
* Task completed（任务已完成）
* Task created（任务已创建）
* Task delayed（任务已延迟）
* Task ETA（任务预计到达时间）
* Task failed（任务失败）
* Task started（任务已开始）
* Task unassigned（任务已取消分配）
* Task updated（任务已更新）
* Worker created（工作人员已创建）
* Worker deleted（工作人员已删除）
* Worker duty（工作人员值勤）

