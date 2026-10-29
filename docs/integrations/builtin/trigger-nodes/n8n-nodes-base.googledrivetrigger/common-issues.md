---
title: Google Drive 触发器节点常见问题
description: 工作流自动化平台 n8n 中 Google Drive 触发器节点的常见错误和问题，包括问题详情及建议的解决办法。
contentType:
- integration
- reference
priority: medium
nodeTitle: Google Drive 触发器节点常见问题
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Drive 触发器节点常见问题 <a href="#google-drive-trigger-node-common-issues" id="google-drive-trigger-node-common-issues"></a>

以下列出 [Google Drive 触发器节点](README.md)的常见错误和问题，以及解决或排查步骤。


## 401 未授权错误 <a href="#401-unauthorized-error" id="401-unauthorized-error"></a>

完整错误信息如下：

```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```


所用凭据及其作用域或权限存在问题时，会出现此错误。

解决步骤：

1. 使用 [OAuth2](../../credentials/google/oauth-single-service.md) 凭据时，确保已在 **APIs & Services > Library**（API 与服务 > 库）中启用 Google Drive API。更多信息请参阅 [Google OAuth2 单服务凭据：启用 API](../../credentials/google/oauth-single-service.md#enable-apis)。
2. 使用[服务账户](../../credentials/google/service-account.md)凭据时：
    1. [启用全域委派](../../credentials/google/service-account.md#enable-domain-wide-delegation)。
    2. 确保在全域委派配置中添加 Google Drive API。

## 处理多个文件变更 <a href="#handling-more-than-one-file-change" id="handling-more-than-one-file-change"></a>

Google Drive Trigger 节点按设定间隔轮询 Google Drive 的变更，默认每分钟一次。

如果轮询间隔内发生多个符合 **Watch For**（监控目标）条件的变更，会触发单个 Google Drive Trigger 事件，并将这些变更作为数据项包含在其中。因此，工作流必须能够处理数据包含多个数据项的情况。

可以使用 [If 节点](../../core-nodes/n8n-nodes-base.if.md)或 [Switch 节点](../../core-nodes/n8n-nodes-base.switch.md)，根据 Google Drive Trigger 节点的数据包含单个还是多个数据项，调整工作流行为。
