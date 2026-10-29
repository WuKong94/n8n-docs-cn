---
title: Postgres 触发器节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Postgres 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger
description: 了解如何在 n8n 中使用 Postgres 触发器节点，并按照技术文档将其集成到工作流中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Postgres 触发器 <a id="postgres-trigger"></a>

使用 Postgres Trigger 节点响应 [Postgres](https://www.postgresql.org/) 中的事件，并将其与其他应用集成。n8n 内置支持响应插入、更新和删除事件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Postgres 凭据文档](../credentials/postgres.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Postgres Trigger 集成](https://n8n.io/integrations/postgres-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

可以配置节点监听事件的方式。

* 选择 **Listen and Create Trigger Rule**（监听并创建触发器规则），然后选择要监听的事件：
  * Insert（插入）
  * Update（更新）
  * Delete（删除）
* 选择 **Listen to Channel**（监听频道），然后输入要监控的频道名称。

{% hint style="info" %}
**Postgres 事件监听器与所需数据库权限**

* 为监听触发器事件，n8n 会在目标表上自动创建 Postgres 触发器。发布工作流时添加此触发器，取消发布时移除。
* 如果工作流尚未发布，测试工作流时也会添加触发器，并在停止监听测试事件后移除。
* Postgres 触发器会调用自动创建的过程，向 n8n 通知事件。
* Postgres 凭据中的用户必须拥有创建和执行触发器及过程的权限。在 PostgreSQL 中，需要超级用户权限、表所有权或 TRIGGER 权限，并且还需对过程所在 schema 拥有 CREATE 权限。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Postgres 提供应用节点。更多信息请参阅 [Postgres 节点文档](../app-nodes/n8n-nodes-base.postgres/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/postgres-trigger/)。
