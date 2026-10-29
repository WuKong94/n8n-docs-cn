---
title: Salesforce 触发器节点文档
description: 了解如何在 n8n 中使用 Salesforce 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Salesforce 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Salesforce 触发器节点 <a href="#salesforce-trigger-node" id="salesforce-trigger-node"></a>

使用 Salesforce Trigger 节点响应 [Salesforce](https://login.salesforce.com/) 中的事件，并将其与其他应用集成。n8n 内置支持多种 Salesforce 事件。

本页列出了 Salesforce Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Salesforce 凭据文档](../credentials/salesforce.md)。
{% endhint %}
{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Salesforce Trigger 集成](https://n8n.io/integrations/salesforce-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* On Account Created（账户创建时）
* On Account Updated（账户更新时）
* On Attachment Created（附件创建时）
* On Attachment Updated（附件更新时）
* On Case Created（服务工单创建时）
* On Case Updated（服务工单更新时）
* On Contact Created（联系人创建时）
* On Contact Updated（联系人更新时）
* On Custom Object Created（自定义对象创建时）
* On Custom Object Updated（自定义对象更新时）
* On Lead Created（销售线索创建时）
* On Lead Updated（销售线索更新时）
* On Opportunity Created（商机创建时）
* On Opportunity Updated（商机更新时）
* On Task Created（任务创建时）
* On Task Updated（任务更新时）
* On User Created（用户创建时）
* On User Updated（用户更新时）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Salesforce 提供应用节点。更多信息请参阅 [Salesforce 节点文档](../app-nodes/n8n-nodes-base.salesforce.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/salesforce-trigger/)。
