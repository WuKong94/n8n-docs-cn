---
title: Cisco Secure Endpoint 凭据
description: Cisco Secure Endpoint 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cisco Secure Endpoint
  的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Cisco Secure Endpoint 凭据
originalFilePath: integrations/builtin/credentials/ciscosecureendpoint.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint
url: https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cisco Secure Endpoint 凭据 <a href="#cisco-secure-endpoint-credentials" id="cisco-secure-endpoint-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cisco DevNet 开发者账号](https://developer.cisco.com)。
- 拥有 [Cisco Secure Endpoint 许可证](https://www.cisco.com/site/us/en/products/security/endpoint-security/secure-endpoint/index.html)的使用权限。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cisco Secure Endpoint 文档](https://developer.cisco.com/docs/secure-endpoint/introduction/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/cisco-secure-endpoint/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- Cisco Secure Endpoint 所在的 **Region**（地区），可选项：
    - Asia Pacific, Japan, and China（亚太、日本和中国）
    - Europe（欧洲）
    - North America（北美）
- **Client ID**（客户端 ID）：注册 SecureX API 客户端时提供。
- **Client Secret**（客户端密钥）：注册 SecureX API 客户端时提供。

要获取 Client ID 和 Client Secret，需先注册 SecureX API 客户端。详细步骤请参阅 [Cisco Secure Endpoint 身份验证文档](https://developer.cisco.com/docs/secure-endpoint/authentication/#authentication)。将 SecureX 的 **Client Password**（客户端密码）填入 n8n 凭据的 **Client Secret**。

