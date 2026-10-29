---
title: WhatsApp 触发器节点文档
contentType:
- integration
- reference
priority: high
nodeTitle: WhatsApp 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger
description: 了解如何在 n8n 中使用 WhatsApp 触发器节点，并按照技术文档将其集成到工作流中。
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


# WhatsApp 触发器 <a id="whatsapp-trigger"></a>

使用 WhatsApp Trigger 节点响应 WhatsApp 中的事件，并将其与其他应用集成。n8n 内置支持多种 WhatsApp 事件，包括账户、消息和电话号码事件。

本页列出了 WhatsApp Trigger 节点可响应的事件，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [WhatsApp Business Cloud 凭据文档](../credentials/whatsapp.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [WhatsApp 集成](https://n8n.io/integrations/whatsapp-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Account Review Update（账户审核更新）
* Account Update（账户更新）
* Business Capability Update（业务能力更新）
* Message Template Quality Update（消息模板质量更新）
* Message Template Status Update（消息模板状态更新）
* Messages（消息）
* Phone Number Name Update（电话号码名称更新）
* Phone Number Quality Update（电话号码质量更新）
* Security（安全）
* Template Category Update（模板类别更新）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 WhatsApp 提供应用节点。更多信息请参阅 [WhatsApp Business Cloud 节点文档](../app-nodes/n8n-nodes-base.whatsapp/README.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/whatsapp-trigger/)。

API 的详细信息，请参阅 [WhatsApp 文档](https://developers.facebook.com/docs/whatsapp/cloud-api)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 WhatsApp Trigger 节点的常见错误和问题，以及解决或排查步骤。

### 工作流只能在测试或生产环境之一正常运行 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

WhatsApp 每个应用只允许注册一个 Webhook。因此，每次在测试 URL 和生产 URL 之间切换，WhatsApp 都会覆盖已注册的 Webhook URL。

测试已发布的工作流时，可能因此遇到问题。WhatsApp 只会将事件发送到两个 Webhook URL 中的一个，另一个始终收不到事件通知。

一种解决办法是在测试时停用工作流：

{% hint style="warning" %}
**会中断生产流量**

此方法会为了测试暂时停用生产工作流。取消发布期间，工作流将不再接收生产流量。
{% endhint %}

1. 进入工作流页面。
2. 从工作流设置下拉菜单中点击 **Unpublish**（取消发布），暂时停用工作流。
3. 使用测试 Webhook URL 测试工作流。
4. 测试完成后，点击 **Publish**（发布）。生产 Webhook URL 应恢复工作。

### 收到 WhatsApp 消息时工作流不运行 <a id="workflow-doesnt-run-when-whatsapp-messages-arrive"></a>

Meta 只会向已订阅相应 WhatsApp Business Account（WABA，商业账户）的应用发送该账户的 WhatsApp Webhook。发布包含 WhatsApp Trigger 节点的工作流时，n8n 会将 Webhook URL 注册到你的 Meta 应用，但不会为该应用订阅 WABA。

如果应用未订阅你的 WABA，发送到 WhatsApp 号码的消息就无法到达 n8n。工作流不会启动，n8n 也不会显示失败执行。Meta 应用控制台发送的测试事件仍可能到达 n8n，因此测试通过并不能排除这一问题。

检查订阅并修复问题：

1. 在 [Meta for Developers 应用控制台](https://developers.facebook.com/apps/)中选择你的应用，然后进入 **WhatsApp** > **API Setup**（API 设置）。复制 **WhatsApp Business Account ID**（商业账户 ID），不要使用 **Phone number ID**（电话号码 ID）。
2. 获取与你的 n8n WhatsApp Trigger 凭据对应同一个 Meta 应用的访问令牌。步骤 4 的请求会为令牌所属的应用建立订阅。令牌需要 `whatsapp_business_management` 权限。例如，在 Meta 的 [Graph API Explorer](https://developers.facebook.com/tools/explorer/) 中，在 **Meta App** 下选择你的应用，添加此权限并生成令牌。
3. 列出已订阅你的 WABA 的应用：

    ```bash
    curl -X GET 'https://graph.facebook.com/<api-version>/<business-account-id>/subscribed_apps' \
    	-H 'Authorization: Bearer <access-token>'
    ```

    每个已订阅的应用都列在 `data` 数组中，其 ID 位于 `whatsapp_business_api_data.id`。你的应用 ID 就是 n8n 凭据中的 **Client ID**（客户端 ID）。如果响应为 `{"data": []}`，或者没有任何 ID 与你的应用匹配，则应用尚未订阅。

    如果应用条目还包含 `override_callback_uri`，Meta 会将此 WABA 的消息 Webhook 发送到该 URL，而不是应用的 Webhook URL。在企业电话号码上设置的覆盖地址优先于这两个地址。请检查 URL 是否符合预期。
4. 仅当应用尚未订阅，或其条目中有你希望移除的 `override_callback_uri` 时，才发送此请求。不带请求体的 `POST` 会为应用建立订阅，并移除订阅中的任何 `override_callback_uri`。如果应用已订阅，且你希望保留其覆盖地址，请跳过此步骤。此请求不需要请求体：

    ```bash
    curl -X POST 'https://graph.facebook.com/<api-version>/<business-account-id>/subscribed_apps' \
    	-H 'Authorization: Bearer <access-token>'
    ```

    请求成功时返回 `{"success": true}`。
5. 如果发送了步骤 4 的请求，请再次运行步骤 3 的请求。确认应用 ID 已列出，且其条目中没有 `override_callback_uri`。如果消息仍发送到错误的 URL，请检查企业电话号码上是否设置了覆盖地址。
6. 向你的 WhatsApp 号码发送消息，以测试已发布的工作流。

{% hint style="warning" %}
**不要通过删除订阅来解决 Webhook 冲突**

`already has a webhook subscription` 错误涉及应用的 Webhook URL，而不是 WABA 订阅。不要通过 `DELETE` 请求访问 `subscribed_apps` 来清除此错误。该请求会取消应用对 WABA 的订阅，Meta 也会停止发送该账户的 Webhook。
{% endhint %}

更多信息请参阅 Meta 的 [Subscribed Apps API](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/subscribed-apps-api/) 参考文档和 [Webhook 覆盖地址](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/override/)。
