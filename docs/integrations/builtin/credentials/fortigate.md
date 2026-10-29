---
title: Fortinet FortiGate 凭据
description: Fortinet FortiGate 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Fortinet FortiGate 的身份验证。
contentType:
- integration
- reference
nodeTitle: Fortinet FortiGate 凭据
originalFilePath: integrations/builtin/credentials/fortigate.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/fortigate
url: https://docs.n8n.io/integrations/builtin/credentials/fortigate
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Fortinet FortiGate 凭据 <a href="#fortinet-fortigate-credentials" id="fortinet-fortigate-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Fortinet FortiGate](https://www.fortinet.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Fortinet FortiGate API 文档](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/fortinet-fortigate/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 API **Access Token（访问令牌）**：创建 [REST API 管理员](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/399023/rest-api-administrator)以生成令牌。

有关 FortiGate 基于令牌的身份验证，请参阅 [Fortinet FortiGate 的使用 API 文档](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis)。
