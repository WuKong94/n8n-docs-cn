---
title: AlienVault 凭据
description: AlienVault 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 AlienVault 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: AlienVault 凭据
originalFilePath: integrations/builtin/credentials/alienvault.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/alienvault
url: https://docs.n8n.io/integrations/builtin/credentials/alienvault
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AlienVault 凭据 <a href="#alienvault-credentials" id="alienvault-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [AlienVault](https://otx.alienvault.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AlienVault 文档](https://otx.alienvault.com/api)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/alienvault/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **OTX Key（OTX 密钥）**：创建 AlienVault 账号后，可以在 **Settings（设置）** 中查看 **OTX Key**。
