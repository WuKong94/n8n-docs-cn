---
title: Demio 凭据
description: Demio 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Demio 的身份验证。
contentType:
- integration
- reference
nodeTitle: Demio 凭据
originalFilePath: integrations/builtin/credentials/demio.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/demio
url: https://docs.n8n.io/integrations/builtin/credentials/demio
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Demio 凭据 <a href="#demio-credentials" id="demio-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Demio](../app-nodes/n8n-nodes-base.demio.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Demio](https://demio.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Demio API 文档](https://publicdemioapi.docs.apiary.io/#)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**
- 一个 **API Secret（API 密钥）**

必须拥有 Demio 的 Owner（所有者）身份，才能生成 API 密钥和机密值。进入 **Account Settings > API（账号设置 > API）**，即可查看和生成。详细步骤请参阅 [Demio 账号所有者设置文档](https://help.demio.com/en/articles/6456716-account-owner-settings)。

