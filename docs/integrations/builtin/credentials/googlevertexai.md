---
description: 通过服务账户、Google Cloud 项目和区域配置 Google Vertex AI 凭据。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Vertex AI 凭据 <a id="google-vertex-ai-credentials"></a>

使用 Google Vertex AI 凭据，通过服务账户、项目和区域将 n8n 连接到 Vertex AI。

这些凭据可用于以下节点：

* [Google Vertex Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md)
* [Embeddings Google Vertex（向量嵌入）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md)

## 前置条件 <a id="prerequisites"></a>

* 一个 [Google Cloud](https://cloud.google.com/) 账户。
* 已启用结算和 Vertex AI API（`aiplatform.googleapis.com`）的 Google Cloud 项目。请参阅 [Google 项目设置指南](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal)。
* 在该项目中具有 Vertex AI 访问权限的服务账户。为服务账户授予 `roles/aiplatform.user` 角色，或包含所需 Vertex 权限的自定义角色。请参阅 [Google 访问控制文档](https://cloud.google.com/vertex-ai/docs/general/access-control)。
* 服务账户的 JSON 密钥。组织必须允许使用服务账户密钥。请参阅[创建服务账户密钥](https://cloud.google.com/iam/docs/keys-create-delete#creating)。

服务账户可属于其他项目。请在凭据所选择的项目中授予其 Vertex AI 权限。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

* 服务账户邮箱和私钥。

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 [Google Vertex AI 文档](https://cloud.google.com/vertex-ai/generative-ai/docs)。

## 使用服务账户 <a id="using-a-service-account"></a>

在 n8n 中创建 **Google Vertex AI** 凭据。打开服务账户的 JSON 密钥文件，填写以下字段：

| 字段 | 值 |
| --- | --- |
| **Region**（区域） | 支持所用模型的位置。默认值为 **Global (multi-region) - global**（全球，多区域）。请参阅 [Google 模型位置](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)。 |
| **Service Account Email**（服务账户邮箱） | JSON 密钥文件中的 `client_email` 值。 |
| **Private Key**（私钥） | JSON 密钥文件中完整的 `private_key` 值，包括 `BEGIN PRIVATE KEY` 和 `END PRIVATE KEY` 两行，不要包含 JSON 两侧的引号。 |
| **Project**（项目） | 选择列表中的项目，或选择 **Custom**（自定义）以输入项目 ID。默认值为 **Custom**。加载列表前，请先填写邮箱和私钥。 |
| **Project ID**（项目 ID） | Google Cloud 项目 ID，例如 `my-project-id`。当 **Project**（项目）为 **Custom**（自定义）时显示此字段。请使用项目 ID，不要使用显示名称或项目编号。 |

选择 **Save**（保存）以保存凭据。

### 选择项目 <a id="select-a-project"></a>

项目列表使用服务账户的访问权限，而非你的个人 Google 账户。Google 会返回服务账户具有 `resourcemanager.projects.get` 权限的项目。请参阅 [Google 项目搜索文档](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search)。

如果项目列表为空或加载失败，请选择 **Custom**（自定义）并输入 **Project ID**（项目 ID）。项目查找是可选步骤，服务账户仍须对所选项目具有 Vertex AI 访问权限。

项目出现在列表中并不代表可访问 Vertex 模型，仍取决于项目已启用的 API、权限和模型可用性。

### 在工作流中使用凭据 <a id="use-the-credential-in-a-workflow"></a>

1. 打开 **Google Vertex Chat Model** 或 **Embeddings Google Vertex** 节点。
2. 将 **Authentication**（身份验证）设为 **Google Vertex AI**。
3. 选择 **Google Vertex AI** 凭据。
4. 选择在项目和区域中可用的模型。

使用此身份验证方式时，节点从凭据中读取项目，凭据还提供默认区域。节点的 **Region**（区域）设置可覆盖凭据中的区域。

现有工作流可继续使用 **Google Service Account**（Google 服务账户）身份验证。使用该方式时，项目仍在节点中设置。具体设置请参阅 [Google 服务账户凭据](google/service-account.md)。

## 常见问题 <a id="common-issues"></a>

### 项目查找失败 <a id="project-lookup-fails"></a>

如果 Google 报告 [Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com) 已禁用，请在错误中指出的项目中启用它。检查服务账户是否对要选择的项目具有 `resourcemanager.projects.get` 权限。解决查找访问权限问题期间，可通过 **Custom**（自定义）手动填写项目。

### Vertex 返回权限错误 <a id="vertex-returns-a-permission-error"></a>

检查服务账户在凭据所选项目中的角色。服务账户在自身所属项目中的角色不会授予其他项目的访问权限。还需为所选项目启用结算和 Vertex AI API。

### 模型不可用 <a id="the-model-is-unavailable"></a>

检查模型是否支持凭据的 **Region**（区域），或节点覆盖后的 **Region**。支持的端点请参阅 [Google 模型位置](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations)。项目查找不会检查模型可用性。
