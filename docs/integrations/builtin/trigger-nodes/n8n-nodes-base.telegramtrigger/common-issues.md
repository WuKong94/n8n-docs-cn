---
title: Telegram 触发器节点常见问题
description: 工作流自动化平台 n8n 中 Telegram 触发器节点的常见错误和问题，包括问题详情及建议的解决办法。
contentType:
- integration
- reference
priority: critical
nodeTitle: Telegram 触发器节点常见问题
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Telegram 触发器节点常见问题 <a href="#telegram-trigger-node-common-issues" id="telegram-trigger-node-common-issues"></a>

以下列出 [Telegram 触发器节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 卡在等待触发事件的状态 <a href="#stuck-waiting-for-trigger-event" id="stuck-waiting-for-trigger-event"></a>

使用 **Execute step**（执行步骤）或 **Execute workflow**（执行工作流）按钮测试 Telegram Trigger 节点时，执行可能看似卡住，且无法停止监听事件。出现此情况时，可能需要退出工作流后重新打开，以重置画布。

一直停留在监听事件状态，通常与 n8n 外部的网络配置有关，尤其是通过反向代理运行 n8n、却未配置 WebSocket 代理时。

请检查反向代理配置，例如 Nginx、Caddy、Apache HTTP Server 或 Traefik，启用 WebSocket 支持。


## Bad request: bad webhook: An HTTPS URL must be provided for webhook（请求错误：Webhook 必须提供 HTTPS URL） <a href="#bad-request-bad-webhook-an-https-url-must-be-provided-for-webhook" id="bad-request-bad-webhook-an-https-url-must-be-provided-for-webhook"></a>


通过反向代理运行 n8n，且实例的 Webhook URL 存在问题时，会出现此错误。

通过反向代理运行 n8n 时，必须将 [`WEBHOOK_URL` 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy.md)配置为 n8n 实例所在的公开 URL。对于 Telegram，此 URL 必须使用 HTTPS。

解决方法是在反向代理中配置 TLS/SSL 终止，然后更新 `WEBHOOK_URL` 环境变量，使用 HTTPS 地址。

## 工作流只能在测试或生产环境之一正常运行 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

Telegram 每个应用只允许注册一个 Webhook。因此，每次在测试 URL 和生产 URL 之间切换，Telegram 都会覆盖已注册的 Webhook URL。

测试已发布的工作流时，可能因此遇到问题。Telegram 机器人只会将事件发送到两个 Webhook URL 中的一个，另一个始终收不到事件通知。

一种解决办法是在测试时停用工作流，或者为测试和生产环境分别创建 Telegram 机器人。

要创建独立的测试 Telegram 机器人，请重复创建第一个机器人的过程。更多信息请参阅 [Telegram 机器人文档](https://core.telegram.org/bots)和 [Telegram Bot API 参考](https://core.telegram.org/bots/api)。

测试时停用工作流的步骤如下：

{% hint style="warning" %}
**会中断生产流量**

此方法会为了测试暂时停用生产工作流。取消发布期间，工作流将不再接收生产流量。
{% endhint %}

1. 进入工作流页面。
2. 从工作流设置下拉菜单中点击 **Unpublish**（取消发布），暂时停用工作流。
3. 使用测试 Webhook URL 测试工作流。
4. 测试完成后，点击 **Publish**（发布）。生产 Webhook URL 应恢复工作。
