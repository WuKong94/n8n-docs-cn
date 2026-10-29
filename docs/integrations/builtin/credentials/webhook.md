---
title: Webhook 凭据
contentType:
- integration
- reference
priority: critical
nodeTitle: Webhook 凭据
originalFilePath: integrations/builtin/credentials/webhook.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/webhook
url: https://docs.n8n.io/integrations/builtin/credentials/webhook
description: Webhook 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Webhook 的身份验证。
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


# Webhook 凭据 <a id="webhook-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Webhook](../core-nodes/n8n-nodes-base.webhook/README.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

必须使用要查询的应用或服务所要求的身份验证方式。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Basic auth（基本身份验证）
* Header auth（请求头身份验证）
* JWT auth（JWT 身份验证）
* None（无）

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/basic-auth.md" %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/generic-auth/header-auth.md" %}

## 使用 JWT 身份验证 <a href="#using-jwt-auth" id="using-jwt-auth"></a>

[**JWT Auth**](https://jwt.io/introduction/) 是一种使用 JSON Web Token（JWT）对数据进行数字签名的身份验证方式。它使用 **JWT credential**（JWT 凭据），密钥类型可选择 **Passphrase**（口令）或 **PEM Key**（PEM 密钥）。更多信息请参阅 [JWT 凭据](jwt.md)。
