---
title: Venafi TLS Protect Datacenter 凭据
description: Venafi TLS Protect Datacenter 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Venafi TLS
  Protect Datacenter 的身份验证。
contentType:
- integration
- reference
nodeTitle: Venafi TLS Protect Datacenter 凭据
originalFilePath: integrations/builtin/credentials/venafitlsprotectdatacenter.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter
url: https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Venafi TLS Protect Datacenter 凭据 <a href="#venafi-tls-protect-datacenter-credentials" id="venafi-tls-protect-datacenter-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Venafi TLS Protect Datacenter 节点](../app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 Venafi [TLS Protect Datacenter](https://venafi.com/) 账户。
- 设置令牌的到期和刷新时间。更多信息请参阅[设置令牌身份验证](https://docs.venafi.com/Docs/current/TopNav/Content/SDK/AuthSDK/t-SDKa-Setup-OAuth.php)。
- 在 **API > Integrations**（API > 集成）中创建 [API 集成](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/c-APIAppIntegrations-about.php)。详细步骤请参阅[将其他系统与 Venafi 产品集成](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php)。
    - 记下集成的 Client ID（客户端 ID）。
    - 根据要在 n8n 中执行的操作选择所需作用域。可用作用域的详情，请参阅[将其他系统与 Venafi 产品集成](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php)中的作用域表。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API integration（API 集成）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Venafi API 集成文档](https://docs.venafi.com/Docs/currentSDK/TopNav/Content/SDK/WebSDK/c-sdk-AboutThisGuide.php)。

## 使用 API 集成 <a href="#using-api-integration" id="using-api-integration"></a>

配置此凭据需要：

- 一个 **Domain**（域名）：输入你的 Venafi TLS Protect Datacenter 域名。
- 一个 **Client ID**（客户端 ID）：输入 API 集成中的 **Client ID**。创建 API 集成的更多信息，请参阅[前置条件](#prerequisites)中的说明和链接。
- 一个 **Username**（用户名）：输入你的用户名。
- **Password**（密码）：输入密码。
- **Allow Self-Signed Certificates**（允许自签名证书）：开启后，此凭据将允许自签名证书。


