---
title: Discord 节点文档
description: 了解如何在 n8n 中使用 Discord 节点，并按照技术文档将 Discord 节点集成到工作流中。
contentType:
- integration
- reference
priority: high
nodeTitle: n8n-nodes-base.discord
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Discord 节点 <a href="#discord-node" id="discord-node"></a>

使用 Discord 节点自动处理 Discord 中的工作，并将其与其他应用集成。n8n 内置支持多种 Discord 功能，包括向 Discord 频道发送消息及管理频道。

本页列出了 Discord 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Discord 凭据](../../credentials/discord.md)。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/hitl-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>



- Channel（频道）
    - Create（创建）
    - Delete（删除）
    - Get（获取）
    - Get Many（获取多项）
    - Update（更新）
- Message（消息）
    - Delete（删除）
    - Get（获取）
    - Get Many（获取多项）
    - React with Emoji（添加表情回应）
    - Send（发送）
    * Send and Wait for Response（发送并等待响应）
- Member（成员）
    - Ban（封禁）
    - Get Many（获取多项）
    - Kick（踢出）
    - Role Add（添加角色）
    - Role Remove（移除角色）
    - Timeout（禁言）
    - Unban（解除封禁）

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/send-and-wait-operation.md" %}



## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.discord 集成模板](https://n8n.io/integrations/discord)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Discord 文档](https://discord.com/developers/docs/intro)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见错误或问题及建议的解决步骤，请参阅[常见问题](common-issues.md)。
