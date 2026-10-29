---
title: Microsoft Foundry 凭据
description: Microsoft Foundry 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft Foundry 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Foundry 凭据
originalFilePath: integrations/builtin/credentials/azureopenai.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/azureopenai
url: https://docs.n8n.io/integrations/builtin/credentials/azureopenai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Foundry 凭据 <a href="#azure-openai-credentials" id="azure-openai-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Microsoft Foundry Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)
- [Microsoft Foundry Embeddings（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md)

这些凭据此前称为 **Azure OpenAI credentials**（API 密钥）和 **Azure Entra ID (Azure Active Directory) API**（Entra ID）。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 [Azure](https://azure.microsoft.com) 订阅。
- 在该订阅中具有 Azure OpenAI 或 Microsoft Foundry 的访问权限。如果组织尚无 Azure OpenAI 访问权限，可能需要[申请访问](https://aka.ms/oai/access)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- Microsoft Foundry（Entra ID）：应用使用客户端 ID 和密钥登录，无需用户登录。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure OpenAI API 文档](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)。

## 端点类型 <a href="#endpoint-type" id="endpoint-type"></a>

两种凭据类型都有 **Endpoint Type**（端点类型）设置，用于决定节点调用哪个 Azure 端点。

* **Classic**（经典）：用于位于 `*.openai.azure.com` 的 Azure OpenAI 资源。凭据需要 **Resource Name**（资源名称）和 **API Version**（API 版本），还可填写可选的 **Endpoint**（端点）。
* **Microsoft Foundry**：用于位于 `*.services.ai.azure.com` 的 Microsoft Foundry 资源。凭据需要完整的 **Endpoint**（端点）URL，例如 `https://<resource>.services.ai.azure.com/openai/v1`，还可填写可选的 [**Project**（项目）](#project)。

### Project（项目） <a id="project"></a>

**Project**（项目）字段可选，仅在 **Microsoft Foundry** 端点类型下显示。输入拥有部署的 Microsoft Foundry 项目名称，可在 Foundry 门户的项目概览页查看。

n8n 使用此项目列出部署。Chat Model 节点自身的 **Project**（项目）字段会覆盖此值。将节点字段留空，可使用凭据中的项目。

部分 Chat Model 节点功能需要 **Microsoft Foundry** 端点类型，包括部署列表、Claude 模型和 Responses API。详情请参阅 [Microsoft Foundry Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Endpoint Type**（端点类型）：**Classic**（经典）或 **Microsoft Foundry**。
- **API key**（API 密钥）：可使用 **Key 1**，部署前可在 **Keys and Endpoint**（密钥与端点）中获取。
- 对于 **Classic**（经典）端点类型：
    - **Resource Name**（资源名称）：你为资源设置的 **Name**（名称）。
    - 凭据应使用的 **API Version**（API 版本）。Azure OpenAI API 版本管理的更多信息，请参阅 [Azure OpenAI API 预览生命周期文档](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation)。
- 对于 **Microsoft Foundry** 端点类型：资源的完整 **Endpoint**（端点）URL，以及可选的 **Project**（项目）。

如需获取上述信息，请创建并部署资源：

- **Classic**（经典）：[创建并部署 Azure OpenAI Service 资源](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource)。
- **Microsoft Foundry**：[创建 Microsoft Foundry 资源](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources)，并在其中部署模型。

{% hint style="info" %}
**Microsoft Foundry 节点的模型名称**

部署资源后，在使用此凭据的 Microsoft Foundry 节点中，将 **Deployment name**（部署名称）用作模型名称。
{% endhint %}

## 使用 Microsoft Foundry（Entra ID） <a href="#using-azure-entra-id-oauth2" id="using-azure-entra-id-oauth2"></a>

Microsoft Foundry（Entra ID）凭据以 Entra 应用的身份登录，使用客户端凭据授权，无需通过浏览器登录，也没有 **Connect**（连接）按钮或重定向 URI。

配置此凭据需要：

- **Endpoint Type**（端点类型）及对应端点字段。请参阅[端点类型](#endpoint-type)。
- **Tenant ID**（租户 ID）：应用注册的 **Directory (tenant) ID**（目录，租户 ID），没有默认值。
- 应用注册的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。

按以下步骤操作：

1. 向 Microsoft 标识平台注册[应用](#register-an-application)。
2. 为该应用[生成客户端密钥](#generate-a-client-secret)。
3. [授予应用访问资源的权限](#give-the-application-access)。

现有凭据仍可使用。**Connect**（连接）按钮和作用域设置不再显示，已存储的登录令牌也不再使用。

### 注册应用 <a href="#register-an-application" id="register-an-application"></a>

向 Microsoft 标识平台注册应用：

1. 打开 [Microsoft 应用注册门户](https://aka.ms/appregistrations)。
2. 选择 **Register an application**（注册应用）。
3. 输入应用的 **Name**（名称）。
4. 在 **Supported account types**（支持的账户类型）中，选择包含你的租户的选项。
5. 选择 **Register**（注册），完成应用创建，无需 **Redirect URI**（重定向 URI）。
6. 复制 **Application (client) ID**（应用程序，客户端 ID），填入 n8n 的 **Client ID**（客户端 ID）。
7. 复制 **Directory (tenant) ID**（目录，租户 ID），填入 n8n 的 **Tenant ID**（租户 ID）。

更多信息，请参阅[向 Microsoft 标识平台注册应用](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成客户端密钥 <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

应用创建完成后，为其生成客户端密钥：

1. 在 Microsoft 应用页面的左侧导航栏，选择 **Certificates & secrets**（证书与秘密）。
1. 在 **Client secrets**（客户端密钥）中，选择 **+ New client secret**（新建客户端密钥）。
1. 输入客户端密钥的 **Description**（描述），例如 `n8n credential`。
1. 选择 **Add**（添加）。
1. 复制 **Value**（值）列中的 **Secret**（秘密值）。
1. 将其粘贴到 n8n 的 **Client Secret**（客户端密钥）。

添加客户端密钥的更多信息，请参阅 Microsoft 的[添加凭据](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

### 授予应用访问权限 <a href="#give-the-application-access" id="give-the-application-access"></a>

应用需要具有 Azure 资源上的角色。缺少角色时，模型调用会失败并返回 `403` 错误。角色分配最多可能需要五分钟才生效。

在 Azure 门户中打开资源，进入 **Access control (IAM)**（访问控制，IAM），为应用分配角色，成员类型选择 **User, group, or service principal**（用户、组或服务主体）。

* **Classic**（经典）端点类型：分配 **Cognitive Services OpenAI User** 角色。
* **Microsoft Foundry** 端点类型：在 Foundry 资源上分配 **Foundry User** 角色。Microsoft 此前将其命名为 **Azure AI User**，门户中可能仍显示旧名称。

更多信息，请参阅 Microsoft 文档中的 [Azure OpenAI 的 Entra ID 身份验证](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/managed-identity)和 [Microsoft Foundry 的基于角色的访问控制](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry)。
