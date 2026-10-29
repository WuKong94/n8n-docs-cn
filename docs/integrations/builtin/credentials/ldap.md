---
title: LDAP 凭据
description: LDAP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 LDAP 的身份验证。
contentType:
- integration
- reference
nodeTitle: LDAP 凭据
originalFilePath: integrations/builtin/credentials/ldap.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ldap
url: https://docs.n8n.io/integrations/builtin/credentials/ldap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# LDAP 凭据 <a href="#ldap-credentials" id="ldap-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [LDAP](../core-nodes/n8n-nodes-base.ldap.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用轻量目录访问协议（LDAP）创建服务器目录。

常见的 LDAP 提供商包括：

* [Jumpcloud](https://jumpcloud.com/blog/how-to-connect-your-application-to-ldap)
* [Azure ADDS](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/tutorial-configure-ldaps)
* [Okta](https://help.okta.com/en-us/Content/Topics/Directory/LDAP-interface-connection-settings.htm)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **LDAP server details**（LDAP 服务器详情）：使用 **Binding DN**（绑定 DN）和 **Binding Password**（绑定密码），通过简单绑定连接。

n8n 仅支持简单绑定，不支持 SASL 绑定，包括 GSSAPI 和 Kerberos。如果 LDAP 服务器要求基于 Kerberos 的绑定（在 Active Directory 环境中较常见），则无法使用此凭据连接。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

详细信息，请参阅 LDAP 提供商自己的文档。

LDAP 的一般信息，请参阅[基本 LDAP 概念](https://ldap.com/basic-ldap-concepts/)获取基础概览；绑定操作及身份验证的工作方式，请参阅 [LDAP 绑定操作](https://ldap.com/the-ldap-bind-operation/)。

## 使用 LDAP 服务器详情 <a href="#using-ldap-server-details" id="using-ldap-server-details"></a>

配置此凭据需要：

- **LDAP Server Address**（LDAP 服务器地址）：使用 LDAP 服务器的 IP 地址或域名。
- **LDAP Server Port**（LDAP 服务器端口）：使用连接 LDAP 服务器的端口号。
- **Binding DN**（绑定 DN）：使用 LDAP 服务器的绑定可分辨名称（Bind DN），即凭据应使用的登录账户。如果使用 Active Directory，其格式可能类似 `cn=administrator, cn=Users, dc=n8n, dc=io`。如何确定此 DN 及其对应密码，请参阅 LDAP 提供商文档。
- **Binding Password**（绑定密码）：使用 **Binding DN**（绑定 DN）用户的密码。
- 选择 **Connection Security**（连接安全性），可选：
    - `None`
    - `TLS`
    - `STARTTLS`
- 选择 `TLS` 或 `STARTTLS` 时，会显示另外两项设置：
    - **Ignore SSL/TLS Issues**（忽略 SSL/TLS 问题）：开启后，即使 LDAP 服务器的 SSL/TLS 证书检查失败，仍会连接。
    - **CA Certificate**（CA 证书）：粘贴 LDAP 服务器的证书颁发机构证书。
- _可选：_ 输入以秒为单位的数值，设置 **Timeout**（超时）。默认值为 300。

