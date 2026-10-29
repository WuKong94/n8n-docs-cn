---
title: Gmail 节点常见问题
description: 了解 n8n 工作流自动化平台中 Gmail 节点的常见错误和问题，包括问题详情及建议的解决方法。
contentType:
- integration
- reference
priority: critical
nodeTitle: Gmail 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gmail 节点常见问题 <a href="#gmail-node-common-issues" id="gmail-node-common-issues"></a>

以下介绍 [Gmail 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 从已发送消息中移除 n8n 标识 <a href="#remove-the-n8n-attribution-from-sent-messages" id="remove-the-n8n-attribution-from-sent-messages"></a>

使用节点[发送消息](message-operations.md#send-a-message)或[回复消息](message-operations.md#reply-to-a-message)时，节点会在邮件末尾附加以下声明：

> This email was sent automatically with n8n（此电子邮件由 n8n 自动发送）

要移除此标识：

1. 在节点的 **Options**（选项）部分选择 **Add option**（添加选项）。
2. 选择 **Append n8n attribution**（附加 n8n 标识）。
3. 关闭开关。

更多信息，请参阅[发送选项](message-operations.md#send-options)和[回复选项](message-operations.md#reply-options)。

## Forbidden - perhaps check your credentials（禁止访问，请检查凭据） <a href="#forbidden-perhaps-check-your-credentials" id="forbidden-perhaps-check-your-credentials"></a>

此错误显示在节点的某些下拉菜单旁，例如 **Label Names or IDs**（标签名称或 ID）。完整错误文本类似于：

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

最常见的原因是使用了 Google 服务账户凭据，但未开启凭据中的 **Impersonate a User**（模拟用户）。

更多信息，请参阅 [Google 服务账户：完成 n8n 凭据设置](../../credentials/google/service-account.md#finish-your-n8n-credential)。

## 401 unauthorized（未授权）错误 <a href="#401-unauthorized-error" id="401-unauthorized-error"></a>

完整错误文本如下：

```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```


所用凭据及其作用域或权限存在问题时，会出现此错误。

解决方法：

1. 对于 [OAuth2](../../credentials/google/oauth-single-service.md) 凭据，请确认已在 **APIs & Services > Library**（API 和服务 > 库）中启用 Gmail API。更多信息，请参阅 [Google OAuth2 单服务：启用 API](../../credentials/google/oauth-single-service.md#enable-apis)。
2. 对于[服务账户](../../credentials/google/service-account.md)凭据：
    1. [启用全域委派](../../credentials/google/service-account.md#enable-domain-wide-delegation)。
    2. 确认已将 Gmail API 添加到全域委派配置中。

## Bad request - please check your parameters（请求无效，请检查参数） <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

此错误通常是因为输入的消息 ID、邮件线程 ID 或标签 ID 不存在。

尝试使用该 ID 执行 **Get**（获取）操作，确认其是否存在。
