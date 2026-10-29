---
title: SyncroMSP 凭据
description: SyncroMSP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SyncroMSP 的身份验证。
contentType:
- integration
- reference
nodeTitle: SyncroMSP 凭据
originalFilePath: integrations/builtin/credentials/syncromsp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/syncromsp
url: https://docs.n8n.io/integrations/builtin/credentials/syncromsp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SyncroMSP 凭据 <a href="#syncromsp-credentials" id="syncromsp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SyncroMSP](../app-nodes/n8n-nodes-base.syncromsp.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SyncroMSP](https://syncromsp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SyncroMSP API 文档](https://api-docs.syncromsp.com/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：在 SyncroMSP 中称为 **API token（API 令牌）**。进入 **user menu > Profile/Password > API Tokens（用户菜单 > 个人资料/密码 > API 令牌）**，选择 **Create New Token（创建新令牌）**。选择 **Custom Permissions（自定义权限）**，输入令牌名称，并按需求调整权限。
- 你的 **Subdomain（子域名）**：输入 SyncroMSP 子域名，即 SyncroMSP URL 中位于 `https://` 与 `.syncromsp.com` 之间的部分。如果完整 URL 为 `https://n8n-instance.syncromsp.com`，子域名应填 `n8n-instance`。

创建新令牌的更多信息，请参阅 [API 令牌](https://docs.syncromsp.com/imported/api-tokens)。
