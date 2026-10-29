---
title: Azure Storage 凭据
description: Azure Storage 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Azure Storage 的身份验证。
contentType:
- integration
- reference
nodeTitle: Azure Storage 凭据
originalFilePath: integrations/builtin/credentials/azurestorage.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/azurestorage
url: https://docs.n8n.io/integrations/builtin/credentials/azurestorage
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Azure Storage 凭据 <a href="#azure-storage-credentials" id="azure-storage-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Azure Storage](../app-nodes/n8n-nodes-base.azurestorage.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Azure](https://azure.microsoft.com) 订阅。
* 创建 [Azure 存储账户](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2
* Shared Key（共享密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure Storage API 文档](https://learn.microsoft.com/en-us/rest/api/storageservices/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

自托管用户从头配置 OAuth2，主要需要两个步骤：

1. 向 Microsoft 标识平台注册[应用](#register-an-application)。
2. 为该应用[生成客户端密钥](#generate-a-client-secret)。

请按照下方各步骤的详细说明操作。Microsoft OAuth2 Web 流程的更多信息，请参阅 [Microsoft 身份验证与授权基础知识](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)。

### 注册应用 <a href="#register-an-application" id="register-an-application"></a>

向 Microsoft 标识平台注册应用：

1. 打开 [Microsoft 应用注册门户](https://aka.ms/appregistrations)。
2. 选择 **Register an application**（注册应用）。
3. 输入应用的 **Name**（名称）。
4. 在 **Supported account types**（支持的账户类型）中，选择 **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**（任何组织目录中的账户，任何 Azure AD 目录、多租户，以及个人 Microsoft 账户，例如 Skype、Xbox）。
5. 在 **Register an application**（注册应用）中：
    1. 从 n8n 凭据复制 **OAuth Callback URL**（OAuth 回调 URL）。
    2. 将其粘贴到 **Redirect URI (optional)**（重定向 URI，可选）字段。
    3. 选择 **Select a platform**（选择平台）> **Web**。
6. 选择 **Register**（注册），完成应用创建。
7. 复制 **Application (client) ID**（应用程序，客户端 ID），填入 n8n 的 **Client ID**（客户端 ID）。

更多信息，请参阅[向 Microsoft 标识平台注册应用](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成客户端密钥 <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

应用创建完成后，为其生成客户端密钥：

1. 在 Microsoft 应用页面的左侧导航栏，选择 **Certificates & secrets**（证书与秘密）。
1. 在 **Client secrets**（客户端密钥）中，选择 **+ New client secret**（新建客户端密钥）。
1. 输入客户端密钥的 **Description**（描述），例如 `n8n credential`。
1. 选择 **Add**（添加）。
1. 复制 **Value**（值）列中的 **Secret**（秘密值）。
1. 将其粘贴到 n8n 的 **Client Secret**（客户端密钥）。
1. 在 n8n 中选择 **Connect my account**（连接我的账户），完成连接设置。
1. 登录 Microsoft 账户，允许应用访问你的信息。

添加客户端密钥的更多信息，请参阅 Microsoft 的[添加凭据](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

也可使用证书（`private_key_jwt`）代替客户端密钥进行身份验证。将 **Authentication**（身份验证）设为 **Certificate**（证书），并提供私钥和证书。完整步骤，请参阅[使用证书进行身份验证](microsoft.md#authenticate-with-a-certificate)。

## 使用共享密钥 <a href="#using-shared-key" id="using-shared-key"></a>

配置此凭据需要：

* **Account**（账户）：Azure Storage 账户的名称。
* **Key**（密钥）：Azure Storage 账户的共享密钥。选择 **Security + networking**（安全性 + 网络），再选择 **Access keys**（访问密钥）。两个账户密钥均可使用。

更详细的步骤，请参阅[管理存储账户访问密钥 | Microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出 Azure Storage 凭据的已知常见错误和问题。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/microsoft-need-admin-approval.md" %}
