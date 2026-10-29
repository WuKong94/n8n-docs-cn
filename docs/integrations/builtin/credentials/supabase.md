---
title: Supabase 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Supabase 凭据
originalFilePath: integrations/builtin/credentials/supabase.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/supabase
url: https://docs.n8n.io/integrations/builtin/credentials/supabase
description: Supabase 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Supabase 的身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Supabase 凭据 <a id="supabase-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Supabase](../app-nodes/n8n-nodes-base.supabase/README.md)：使用秘密密钥或 OAuth2。
* [Supabase Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md)：使用秘密密钥。

还可使用 OAuth2 凭据，从 [MCP 服务器](../../../build/integrate-ai/mcp-servers.md)注册表连接 Supabase MCP 服务器。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Supabase](https://supabase.com/dashboard/sign-up) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）
* OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Supabase API 文档](https://supabase.com/docs/guides/api)。

## 使用秘密密钥 <a href="#using-secret-key" id="using-secret-key"></a>

配置此凭据需要：

* **Host**（主机）
* **Secret Key**（秘密密钥）

凭据通过 Supabase [Data API](https://supabase.com/docs/guides/api) 连接项目，因此必须启用 Data API。可在项目的 [Data API 设置](https://supabase.com/dashboard/project/_/integrations/data_api/overview)中检查并启用。

生成秘密密钥的步骤如下：

1. 在 Supabase 账户中进入 **Dashboard**（控制台），创建或选择要为其创建 API 密钥的项目。
2. 进入 [**Integrations > Data API**（集成 > Data API）](https://supabase.com/dashboard/project/_/integrations/data_api/overview)，复制 **Project URL**（项目 URL），填入 n8n 的 **Host**（主机），省略末尾的 `/rest/v1` 路径（使用 `https://your_project.supabase.co`，不要使用 `https://your_project.supabase.co/rest/v1`）。
3. 进入 [**Project Settings > API Keys**（项目设置 > API 密钥）](https://supabase.com/dashboard/project/_/settings/api-keys)，查看项目的 API 密钥。
4. 创建或显示 **secret key**（秘密密钥），填入 n8n 的 **Secret Key**（秘密密钥）。更多信息，请参阅[理解 API 密钥](https://supabase.com/docs/guides/getting-started/api-keys)。

{% hint style="info" %}
使用旧版 `service_role` 秘密值的现有凭据仍可工作，但 Supabase 正在[逐步淘汰旧版 API 密钥](https://supabase.com/docs/guides/getting-started/migrating-to-new-api-keys)。请在旧密钥于 2026 年底停用之前，将其替换为新的秘密密钥。
{% endhint %}

## 使用 OAuth2 <a id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

托管 OAuth2 使用权限表中 **Supabase node and MCP server**（Supabase 节点与 MCP 服务器）列的权限。使用自定义 OAuth2 时，请创建 Supabase OAuth 应用，并将客户端凭据填入 n8n。

### OAuth2 前置条件 <a id="oauth2-prerequisites"></a>

开始之前，请确保：

* 使用 Supabase 节点的项目已启用 Supabase [Data API](https://supabase.com/docs/guides/api)。
* 使用自定义 OAuth2 时，Supabase 账户具有组织的 **Owner**（所有者）或 **Administrator**（管理员）角色。Supabase 要求拥有其中一种角色，才能发布 OAuth 应用。
* Supabase 账户具有每个所连接项目的 **Owner**（所有者）或 **Administrator**（管理员）角色。n8n 需要此权限来创建托管秘密密钥。

组织及项目角色的更多信息，请参阅 Supabase 的[访问控制文档](https://supabase.com/docs/guides/platform/access-control)。

根据 OAuth 凭据的使用方式，配置应用权限：

| Scope（作用域） | Supabase node only（仅 Supabase 节点） | Supabase node and MCP server（Supabase 节点与 MCP 服务器） |
| --- | --- | --- |
| Analytics（分析） | 无访问权限 | 只读 |
| Database（数据库） | 无访问权限 | 读写 |
| Edge Functions（边缘函数） | 无访问权限 | 读写 |
| Environment（环境） | 无访问权限 | 读写 |
| Organizations（组织） | 无访问权限 | 只读 |
| Projects（项目） | 只读 | 读写 |
| Secrets（秘密值） | 读写 | 读写 |
| Storage（存储） | 无访问权限 | 读写 |

将表中未列出的全部作用域保持为 **No access**（无访问权限）。**Supabase node and MCP server**（Supabase 节点与 MCP 服务器）列中的额外权限由 Supabase MCP 工具需要，Supabase 节点本身不需要。

配置自定义 OAuth2 的步骤如下：

1. 在 n8n 中创建 **Supabase OAuth2 API** 凭据，复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
2. 在 [Supabase 控制台](https://supabase.com/dashboard)中选择组织，进入 **Organization Settings > OAuth Apps**（组织设置 > OAuth 应用）。
3. 选择 **Publish OAuth app**（发布 OAuth 应用）。
4. 输入 **Application name**（应用名称）和 **Website URL**（网站 URL）。
5. 在 **Authorization callback URLs**（授权回调 URL）中，输入 n8n 的 **OAuth Redirect URL**（OAuth 重定向 URL）。
6. 根据凭据的使用方式，使用对应表格列设置应用权限。
7. 选择 **Confirm**（确认）。
8. 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。Supabase 只显示一次客户端密钥。
9. 将 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）填入 n8n 凭据。
10. 选择 **Connect my account**（连接我的账户），再选择并授权 Supabase 组织。

n8n 会创建或复用名为 `n8n_managed_data_api` 的专用 Supabase 秘密密钥，访问 Data API。如需保持 Supabase 节点正常工作，请勿删除此密钥。

如果修改 OAuth 应用权限，请重新连接 n8n 凭据，以应用新权限。

更多信息，请参阅 Supabase 的 [OAuth 应用指南](https://supabase.com/docs/guides/integrations/build-a-supabase-oauth-integration)和 [OAuth 作用域文档](https://supabase.com/docs/guides/integrations/build-a-supabase-oauth-integration/oauth-scopes)。
