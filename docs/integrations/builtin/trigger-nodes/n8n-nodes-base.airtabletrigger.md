---
title: Airtable 触发器节点文档
contentType:
- integration
- reference
priority: medium
nodeTitle: Airtable 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger
description: 了解如何在 n8n 中使用 Airtable 触发器节点，并按照技术文档将其集成到工作流中。
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


# Airtable 触发器 <a id="airtable-trigger"></a>

[Airtable](https://airtable.com/) 融合了电子表格和数据库，将数据库功能应用于电子表格。Airtable 表中的字段类似于电子表格的单元格，但具有“复选框”“电话号码”和“下拉列表”等类型，还可引用图片等文件附件。

本页列出了 Airtable Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Airtable 凭据文档](../credentials/airtable.md)。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **New Airtable event**（新的 Airtable 事件）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Airtable 提供应用节点。更多信息请参阅 [Airtable 节点文档](../app-nodes/n8n-nodes-base.airtable/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/airtable-trigger/)。

API 的详细信息，请参阅 [Airtable 文档](https://airtable.com/developers/web/api/introduction)。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Poll Times（轮询时间） <a href="#poll-times" id="poll-times"></a>

n8n 的 Airtable 节点通过轮询检查所配置的 Airtable 资源是否更新。**Poll Times**（轮询时间）参数用于配置查询频率：

* Every Minute（每分钟）
* Every Hour（每小时）
* Every Day（每天）
* Every Week（每周）
* Every Month（每月）
* **Every X**（每隔指定时间）：每隔指定的分钟数或小时数检查更新。
* **Custom**（自定义）：提供 [cron 表达式](https://en.wikipedia.org/wiki/Cron)来自定义轮询间隔。

使用 **Add Poll Time**（添加轮询时间）按钮添加更多轮询间隔。

### Base（数据库） <a href="#base" id="base"></a>

要检查更新的 [Airtable 数据库](https://support.airtable.com/docs/airtable-bases-overview)。可提供数据库的 URL 或 [base ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls)。

### Table（表） <a href="#table" id="table"></a>

要检查更新的 Airtable 数据库中的[表](https://support.airtable.com/docs/tables-overview)。可提供表的 URL 或 [table ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls)。

### Trigger Field（触发字段） <a href="#trigger-field" id="trigger-field"></a>

表中的创建时间或最后修改时间字段。Airtable Trigger 节点使用此字段判断自上次检查以来发生了哪些更新。

### Download Attachments（下载附件） <a href="#download-attachments" id="download-attachments"></a>

是否从表中下载附件。启用后，使用 **Download Fields**（下载字段）参数指定附件字段。

### Download Fields（下载字段） <a href="#download-fields" id="download-fields"></a>

启用 **Download Attachments**（下载附件）开关后，此字段指定要下载哪些表字段。字段名称区分大小写，多个字段名称用逗号分隔。

### Additional Fields（附加字段） <a href="#additional-fields" id="additional-fields"></a>

使用 **Add Field**（添加字段）按钮添加以下参数：

* **Fields**（字段）：要在输出中包含的字段列表，以逗号分隔。如果留空，输出将只包含 **Trigger Field**（触发字段）。
* **Formula**（公式）：用于进一步筛选结果的 [Airtable 公式](https://support.airtable.com/docs/formula-field-reference)。可用它为触发工作流的事件添加额外条件。公式值仅在生产轮询时生效，手动执行时不会考虑。
* **View ID**（视图 ID）：表视图的名称或 ID。设置后，仅返回指定视图中的记录。
