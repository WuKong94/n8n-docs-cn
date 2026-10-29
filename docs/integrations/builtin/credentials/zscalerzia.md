---
title: Zscaler ZIA 凭据
description: Zscaler ZIA 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zscaler ZIA 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Zscaler ZIA 凭据
originalFilePath: integrations/builtin/credentials/zscalerzia.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zscalerzia
url: https://docs.n8n.io/integrations/builtin/credentials/zscalerzia
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zscaler ZIA 凭据 <a href="#zscaler-zia-credentials" id="zscaler-zia-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Zscaler Internet Access (ZIA)](https://www.zscaler.com/products/zscaler-internet-access) 云实例中创建管理员账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth and API key combo（基本身份验证与 API 密钥组合）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zscaler ZIA 文档](https://help.zscaler.com/zia/getting-started-zia-api)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/zscaler-zia/)。

## 使用基本身份验证与 API 密钥组合 <a href="#using-basic-auth-and-api-key-combo" id="using-basic-auth-and-api-key-combo"></a>

配置此凭据需要：

- **Base URL**（基础 URL）：输入 Zscaler ZIA 云名称对应的基础 URL。登录 ZIA Admin Portal（ZIA 管理门户），进入 **Administration > Cloud Service API Security**（管理 > 云服务 API 安全）获取。在 **Cloud Service API Key**（云服务 API 密钥）和 **OAuth 2.0 Authorization Servers**（OAuth 2.0 授权服务器）标签页中均会显示基础 URL。
- **Username**（用户名）：输入 ZIA 管理员用户名。
- **Password**（密码）：输入 ZIA 管理员密码。
- **Api Key**（API 密钥）：在 **Administration > Cloud Service API Security > Cloud Service API Key**（管理 > 云服务 API 安全 > 云服务 API 密钥）中创建。

详细步骤请参阅[关于 Cloud Service API Key](https://help.zscaler.com/zia/about-cloud-service-api-key)。
