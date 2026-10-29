---
title: 操作不受支持时的处理方式
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## 所需操作不受支持时怎么办 <a href="#what-to-do-if-your-operation-isnt-supported" id="what-to-do-if-your-operation-isnt-supported"></a>

如果该节点不支持你需要的操作，可以通过 [HTTP Request 节点](../../../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)调用服务 API。

你可以在 HTTP Request 节点中使用已经为该服务创建的凭据：

1. 在 HTTP Request 节点中，选择 **Authentication（身份验证）> Predefined Credential Type（预定义凭据类型）**。
1. 选择要连接的服务。
1. 选择对应凭据。

更多信息请参阅[自定义 API 操作](../../../../../../integrations/builtin/custom-api-actions-for-existing-nodes.md)。
