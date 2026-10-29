---
title: Venafi TLS Protect Cloud 凭据
description: Venafi TLS Protect Cloud 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Venafi TLS Protect
  Cloud 的身份验证。
contentType:
- integration
- reference
nodeTitle: Venafi TLS Protect Cloud 凭据
originalFilePath: integrations/builtin/credentials/venafitlsprotectcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud
url: https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Venafi TLS Protect Cloud 凭据 <a href="#venafi-tls-protect-cloud-credentials" id="venafi-tls-protect-cloud-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Venafi TLS Protect Cloud 节点](../app-nodes/n8n-nodes-base.venafitlsprotectcloud.md)
* [Venafi TLS Protect Cloud Trigger（触发器）节点](../trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 Venafi [TLS Protect Cloud](https://venafi.com/tls-protect/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Venafi TLS Protect Cloud API 文档](https://docs.venafi.cloud/api/vaas-rest-api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Region（区域）**：选择符合业务需求的区域。如果位于欧盟，选择 **EU**；否则选择 **US**。
- 一个 **API Key（API 密钥）**：进入 **avatar > Preferences > API Keys（头像 > 偏好设置 > API 密钥）** 获取。也可以使用 VCert 获取 API 密钥。更多信息请参阅[获取 API 密钥](https://docs.venafi.cloud/api/obtaining-api-key/)。
