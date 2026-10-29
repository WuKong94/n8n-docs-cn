---
title: Airtable 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Airtable 凭据
originalFilePath: integrations/builtin/credentials/airtable.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/airtable
url: https://docs.n8n.io/integrations/builtin/credentials/airtable
description: Airtable 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Airtable 的身份验证。
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


# Airtable 凭据 <a id="airtable-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Airtable](../app-nodes/n8n-nodes-base.airtable/README.md)
* [Airtable Trigger（触发器）](../trigger-nodes/n8n-nodes-base.airtabletrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Airtable](https://airtable.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Personal Access Token（个人访问令牌，PAT）
* OAuth2

{% hint style="warning" %}
**功能可用范围**

n8n 此前为 Airtable 提供的 API 密钥身份验证方式已弃用。Airtable 于 2024 年 2 月[完全弃用了这些密钥](https://support.airtable.com/v1/docs/airtable-api-deprecation-guidelines)。如果此前使用 Airtable API 凭据，请替换为 Airtable Personal Access Token 或 Airtable OAuth2 凭据。n8n 建议使用个人访问令牌。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Airtable API 文档](https://airtable.com/developers/web/api/authentication)。

## 使用个人访问令牌 <a href="#using-personal-access-token" id="using-personal-access-token"></a>

配置此凭据需要：

* 个人 **Access Token**（访问令牌，PAT）

创建 PAT 的步骤如下：

1. 打开 Airtable Builder Hub 的[个人访问令牌](https://airtable.com/create/tokens)页面。
2. 选择 **+ Create new token**（创建新令牌），Airtable 会打开 **Create personal access token**（创建个人访问令牌）页面。
3. 输入令牌的 **Name**（名称），例如 `n8n credential`。
4. 为令牌添加 **Scopes**（作用域）。更多信息，请参阅 Airtable 的[作用域](https://airtable.com/developers/web/api/scopes)指南。n8n 建议使用以下作用域：
   * `data.records:read`
   * `data.records:write`
   * `schema.bases:read`
5. 选择令牌的 **Access**（访问范围）。可选择单个数据库、多个数据库（可跨工作区）、你拥有的某个工作区内当前及未来的所有数据库，或你拥有的任意工作区中的所有数据库，包括未来新增的数据库和工作区。
6. 选择 **Create token**（创建令牌）。
7. Airtable 打开显示令牌的弹窗。复制此令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。

更多信息，请参阅 Airtable 的[查找和创建 PAT 文档](https://support.airtable.com/v1/docs/creating-personal-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自行托管 n8n](../../../deploy/host-n8n/README.md)，你需要：

* **OAuth Redirect URL**（OAuth 重定向 URL）
* **Client ID**（客户端 ID）
* **Client Secret**（客户端密钥）

如需生成这些信息，请注册新的 Airtable 集成：

1. 打开 Airtable Builder Hub 的 [**OAuth integrations**（OAuth 集成）](https://airtable.com/create/oauth)页面。
2. 选择 **Register new OAuth integration**（注册新 OAuth 集成）按钮。
3. 输入 OAuth 集成的名称。
4. 从 n8n 凭据复制 **OAuth Redirect URL**（OAuth 重定向 URL）。
5. 在 Airtable 中，将该重定向 URL 填入 **OAuth redirect URL**（OAuth 重定向 URL）。
6. 选择 **Register integration**（注册集成）。
7. 在下一页，从 Airtable 复制 **Client ID**（客户端 ID），粘贴到 n8n 凭据的 **Client ID**（客户端 ID）。
8. 在 Airtable 中选择 **Generate client secret**（生成客户端密钥）。
9. 复制客户端密钥，粘贴到 n8n 凭据的 **Client Secret**（客户端密钥）。
10. 在 Airtable 中选择以下作用域：
    * `data.records:read`
    * `data.records:write`
    * `schema.bases:read`
11. 在 Airtable 中选择 **Save changes**（保存更改）。
12. 在 n8n 凭据中选择 **Connect my account**（连接我的账户），随后打开 **Grant access**（授予访问权限）弹窗。
13. 按照说明，选择要操作的数据库（或全部数据库）。
14. 选择 **Grant access**（授予访问权限），完成连接。

注册新 OAuth 集成的步骤，请参阅 [Airtable 注册新集成文档](https://airtable.com/developers/web/guides/oauth-integrations)。
