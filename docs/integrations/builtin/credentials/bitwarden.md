---
title: Bitwarden 凭据
description: Bitwarden 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Bitwarden 的身份验证。
contentType:
- integration
- reference
nodeTitle: Bitwarden 凭据
originalFilePath: integrations/builtin/credentials/bitwarden.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/bitwarden
url: https://docs.n8n.io/integrations/builtin/credentials/bitwarden
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Bitwarden 凭据 <a href="#bitwarden-credentials" id="bitwarden-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Bitwarden](../app-nodes/n8n-nodes-base.bitwarden.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Bitwarden](https://vault.bitwarden.com/#/register?org=teams) Teams 或 Enterprise 组织账户。Bitwarden Public API 仅对这些[组织](https://bitwarden.com/help/about-organizations/)方案开放。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Bitwarden Public API 文档](https://bitwarden.com/help/public-api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Client ID**（客户端 ID）：生成 API 密钥时提供。
- **Client Secret**（客户端密钥）：生成 API 密钥时提供。
- **Environment**（环境）：
    - 如果不是自行托管 Bitwarden，选择 **Cloud-hosted**（云托管），无需其他配置。
    - 如果在自己的服务器上托管 Bitwarden，选择 **Self-hosted**（自托管），并在对应字段输入 **Self-hosted domain**（自托管域名）。

Client ID 和 Client Secret 必须来自 **Organization API Key**（组织 API 密钥），不能使用 Personal API Key（个人 API 密钥）。生成组织 API 密钥的步骤，请参阅 [Bitwarden Public API 身份验证文档](https://bitwarden.com/help/public-api/#authentication)。

