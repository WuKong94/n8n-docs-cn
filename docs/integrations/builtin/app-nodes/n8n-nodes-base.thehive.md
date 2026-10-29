---
title: TheHive 节点文档
description: 了解如何在 n8n 中使用 TheHive 节点，并按照技术文档将 TheHive 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: TheHive 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.thehive.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TheHive 节点 <a href="#thehive-node" id="thehive-node"></a>

使用 TheHive 节点自动处理 TheHive 中的工作，并将其与其他应用集成。n8n 内置支持多种 TheHive 功能，包括创建告警，以及统计任务日志、案件和可观测对象。

本页列出了 TheHive 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个节点。如果使用 TheHive 的版本 3 或 4 API，请使用此节点（TheHive）；如果使用版本 5，请使用 [TheHive 5](n8n-nodes-base.thehive5.md)。
{% endhint %}
{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [TheHive 凭据](../credentials/thehive.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

可用操作取决于 API 版本。先创建凭据并选择 API 版本，再返回节点，选择所需资源，n8n 就会显示该 API 版本支持的操作。

* Alert（告警）
* Case（案件）
* Log（日志）
* Observable（可观测对象）
* Task（任务）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 TheHive 集成模板](https://n8n.io/integrations/thehive)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 提供触发器节点。更多信息请参阅 [TheHive Trigger 节点文档](../trigger-nodes/n8n-nodes-base.thehivetrigger.md)。

该服务的更多信息，请参阅 TheHive 文档：

* [版本 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)
* [版本 4](https://docs.thehive-project.org/cortex/api/api-guide/)
