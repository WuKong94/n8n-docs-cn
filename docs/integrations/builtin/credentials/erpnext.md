---
title: ERPNext 凭据
description: ERPNext 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 ERPNext 的身份验证。
contentType:
- integration
- reference
nodeTitle: ERPNext 凭据
originalFilePath: integrations/builtin/credentials/erpnext.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/erpnext
url: https://docs.n8n.io/integrations/builtin/credentials/erpnext
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ERPNext 凭据 <a href="#erpnext-credentials" id="erpnext-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [ERPNext](../app-nodes/n8n-nodes-base.erpnext.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [ERPNext](https://erpnext.com) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ERPNext 文档](https://docs.erpnext.com/docs/user/manual/en/introduction)。

使用该框架的更多信息，请参阅 [ERPNext 开发者文档](https://frappeframework.com/docs/user/en/introduction)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在你自己的 ERPNext 用户账户中，进入 **Settings > My Settings > API Access**（设置 > 我的设置 > API 访问）生成。
- **API Secret**（API 密钥对应的秘密值）：与 API key 一同生成。
- ERPNext 的 **Environment**（环境）：
    - 对于 **Cloud-hosted**（云托管）：
        - ERPNext 的 **Subdomain**（子域名）：请参阅[常见问答](#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account)。
        - **Domain**（域名）：选择 `erpnext.com` 或 `frappe.cloud`。
    - 对于 **Self-hosted**（自托管）：
        - 托管 ERPNext 的完全限定 **Domain**（域名）
- 选择是否 **Ignore SSL Issues**（忽略 SSL 问题）：启用后，即使无法验证 SSL 证书，n8n 仍会连接。

如果你是 ERPNext 系统管理员，也可为其他用户生成 API 密钥及秘密值。更多信息，请参阅 [ERPNext 添加用户文档](https://docs.erpnext.com/docs/user/manual/en/adding-users)。

## 如何查找 ERPNext 云托管账户的子域名 <a href="#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account" id="how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account"></a>

可通过浏览器地址栏查找 ERPNext 子域名。`https://` 与 `.erpnext.com` 或 `frappe.cloud` 之间的字符串就是子域名。

例如，地址栏中的 URL 为 `https://n8n.erpnext.com` 时，子域名为 `n8n`。

