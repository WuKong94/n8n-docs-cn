---
title: Cal.com 凭据
description: Cal.com 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cal.com 的身份验证。
contentType:
- integration
- reference
nodeTitle: Cal.com 凭据
originalFilePath: integrations/builtin/credentials/cal.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cal
url: https://docs.n8n.io/integrations/builtin/credentials/cal
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cal.com 凭据 <a href="#calcom-credentials" id="calcom-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Cal.com Trigger（触发器）](../trigger-nodes/n8n-nodes-base.caltrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Cal.com](https://www.cal.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cal.com API 文档](https://cal.com/docs/enterprise-features/api#api-server-specifications)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：生成新密钥的方法，请参阅 [Cal.com API 文档](https://cal.com/docs/api-reference/v2/introduction)。
- 一个 **Host（主机地址）**：如果使用 Cal.com 云端版本，保留 Host 为 `https://api.cal.com`。如果自行托管 Cal.com，请填写对应实例的 **Host**。

