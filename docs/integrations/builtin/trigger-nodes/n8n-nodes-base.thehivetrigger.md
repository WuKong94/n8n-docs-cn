---
title: TheHive 触发器节点文档
description: 了解如何在 n8n 中使用 TheHive 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: TheHive 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TheHive 触发器节点 <a href="#thehive-trigger-node" id="thehive-trigger-node"></a>

本页列出了 TheHive Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个节点。要使用 TheHive 的版本 3 或 4 API，请使用此节点（TheHive Trigger）；要使用版本 5，请使用 [TheHive 5 Trigger](n8n-nodes-base.thehive5trigger.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [TheHive Trigger 集成](https://n8n.io/integrations/thehive-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Alert（警报）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Case（案件）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Log（日志）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Observable（可观测项）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）
* Task（任务）
    * Created（已创建）
    * Deleted（已删除）
    * Updated（已更新）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 提供应用节点。更多信息请参阅 [TheHive 节点文档](../app-nodes/n8n-nodes-base.thehive.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/thehive-trigger/)。

该服务的更多信息，请参阅 TheHive 的文档：

* [版本 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)
* [版本 4](https://docs.thehive-project.org/cortex/api/api-guide/)


## 在 TheHive 中配置 Webhook <a href="#configure-a-webhook-in-thehive" id="configure-a-webhook-in-thehive"></a>

为 TheHive 实例配置 Webhook：

1. 从 TheHive Trigger 节点复制测试和生产 Webhook URL。
2. 将以下内容添加到 `application.conf` 文件中。这是 TheHive 的配置文件：

	```
	notification.webhook.endpoints = [
		{
			name: TESTING_WEBHOOK_NAME
			url: TESTING_WEBHOOK_URL
			version: 0
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		},
		{
			name: PRODUCTION_WEBHOOK_NAME
			url: PRODUCTION_WEBHOOK_URL
			version: 0
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		}
	]
	```

3. 将 `TESTING_WEBHOOK_URL` 和 `PRODUCTION_WEBHOOK_URL` 替换为上一步复制的 URL。
4. 将 `TESTING_WEBHOOK_NAME` 和 `PRODUCTION_WEBHOOK_NAME` 替换为你希望使用的端点名称。
5. 将 `ORGANIZATION_NAME` 替换为你的组织名称。
6. 执行以下 cURL 命令以启用通知：
	```sh
	curl -XPUT -uTHEHIVE_USERNAME:THEHIVE_PASSWORD -H 'Content-type: application/json' THEHIVE_URL/api/config/organisation/notification -d '
	{
		"value": [
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "TESTING_WEBHOOK_NAME" }
			},
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "PRODUCTION_WEBHOOK_NAME" }
			}
		]
	}'
	```
