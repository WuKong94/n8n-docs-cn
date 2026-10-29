---
title: Intercom 凭据
description: Intercom 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Intercom 的身份验证。
contentType:
- integration
- reference
nodeTitle: Intercom 凭据
originalFilePath: integrations/builtin/credentials/intercom.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/intercom
url: https://docs.n8n.io/integrations/builtin/credentials/intercom
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Intercom 凭据 <a href="#intercom-credentials" id="intercom-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Intercom](../app-nodes/n8n-nodes-base.intercom.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Intercom](https://www.intercom.com/) 开发者账号。
- 在开发者中心[创建应用](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Intercom API 文档](https://developers.intercom.com/docs/references/introduction/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：Intercom 会在你[创建应用](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/)时自动生成 **Access Token（访问令牌）**。将此 **Access Token** 填入 n8n 的 **API Key** 字段。详细说明请参阅[如何获取访问令牌](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/#how-to-get-your-access-token)。
