---
title: GitLab 凭据
description: GitLab 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 GitLab 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitLab 凭据
originalFilePath: integrations/builtin/credentials/gitlab.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/gitlab
url: https://docs.n8n.io/integrations/builtin/credentials/gitlab
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitLab 凭据 <a href="#gitlab-credentials" id="gitlab-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [GitLab](../app-nodes/n8n-nodes-base.gitlab.md)
- [GitLab Trigger（触发器）](../trigger-nodes/n8n-nodes-base.gitlabtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）
- OAuth2（推荐）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GitLab API 文档](https://docs.gitlab.com/ee/api/rest/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [GitLab](https://gitlab.com/) 账号，以及：

- **GitLab Server**（GitLab 服务器）的 URL
- 一个 **Access Token（访问令牌）**

设置凭据的步骤如下：

1. 在 GitLab 中选择头像，再选择 **Edit profile**（编辑个人资料）。
2. 在左侧边栏选择 **Access tokens**（访问令牌）。
3. 选择 **Add new token**（添加新令牌）。
4. 输入令牌的 **Name**（名称），例如 `n8n integration`。
5. 输入令牌的 **expiry date**（到期日期）。未输入时，GitLab 会自动将其设为当前日期之后 365 天。
    - 令牌在该到期日期的 UTC 午夜失效。
6. 选择所需的 **Scopes**（作用域）。对于 [GitLab](../app-nodes/n8n-nodes-base.gitlab.md) 节点，可使用 `api` 作用域，方便地授予节点全部功能的访问权限；也可参阅[个人访问令牌作用域](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)，选择所需功能的作用域。
7. 选择 **Create personal access token**（创建个人访问令牌）。
8. 复制所生成的访问令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。
9. 将 **GitLab Server**（GitLab 服务器）的 URL 填入 n8n 凭据。

更多信息，请参阅 GitLab 的[创建个人访问令牌文档](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要一个 [GitLab](https://gitlab.com/) 账户，然后创建新的 GitLab 应用：

1. 在 GitLab 中选择头像，再选择 **Edit profile**（编辑个人资料）。
2. 在左侧边栏选择 **Applications**（应用）。
3. 选择 **Add new application**（添加新应用）。
4. 输入应用的 **Name**（名称），例如 `n8n integration`。
5. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 GitLab 的 **Redirect URI**（重定向 URI）。
6. 选择所需的 **Scopes**（作用域）。对于 [GitLab](../app-nodes/n8n-nodes-base.gitlab.md) 节点，可使用 `api` 作用域，方便地授予节点全部功能的访问权限；也可参阅[个人访问令牌作用域](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)，选择所需功能的作用域。
6. 选择 **Save application**（保存应用）。
7. 复制 **Application ID**（应用 ID），填入 n8n 凭据的 **Client ID**（客户端 ID）。
8. 复制 **Secret**（秘密值），填入 n8n 凭据的 **Client Secret**（客户端密钥）。

更多信息，请参阅 GitLab 的[将 GitLab 配置为 OAuth 2.0 身份验证提供商](https://docs.gitlab.com/ee/integration/oauth_provider.html)文档。OAuth2 与 GitLab 的更多信息，请参阅 [GitLab OAuth 2.0 身份提供商 API 文档](https://docs.gitlab.com/ee/api/oauth2.html)。
