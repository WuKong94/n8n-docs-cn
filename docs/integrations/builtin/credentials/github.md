---
title: GitHub 凭据
description: GitHub 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 GitHub 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitHub 凭据
originalFilePath: integrations/builtin/credentials/github.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/github
url: https://docs.n8n.io/integrations/builtin/credentials/github
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitHub 凭据 <a href="#github-credentials" id="github-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [GitHub](../app-nodes/n8n-nodes-base.github.md)
- [GitHub Trigger（触发器）](../trigger-nodes/n8n-nodes-base.githubtrigger.md)
- [GitHub Document Loader（文档加载器）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)：此节点不支持 OAuth。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [GitHub](https://github.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）：可用于任何 GitHub 节点。
- OAuth2：仅用于 [GitHub](../app-nodes/n8n-nodes-base.github.md) 和 [GitHub Trigger（触发器）](../trigger-nodes/n8n-nodes-base.githubtrigger.md)节点，不用于 [GitHub Document Loader（文档加载器）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GitHub API 文档](https://docs.github.com/en/rest)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [GitHub](https://github.com/) 账户。

设置此凭据需要两个步骤：

1. [生成 GitHub 个人访问令牌](#generate-personal-access-token)。
2. [设置凭据](#set-up-the-credential)。

详细说明，请参阅下方各节。

### 生成个人访问令牌 <a href="#generate-personal-access-token" id="generate-personal-access-token"></a>

{% hint style="info" %}
**建议的访问令牌类型**

n8n 建议使用经典个人访问令牌。GitHub 的细粒度个人访问令牌可将访问限定到特定仓库和权限，但有一些[限制](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#fine-grained-personal-access-tokens-limitations)。
{% endhint %}

生成个人访问令牌的步骤如下：

1. 如果尚未验证电子邮箱地址，请先在 GitHub 中完成验证。更多信息，请参阅[验证电子邮箱地址](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address)。
2. 打开 GitHub 个人资料的[设置](https://github.com/settings/profile)。
3. 在左侧导航栏选择 [**Developer settings**（开发者设置）](https://github.com/settings/apps)。
4. 在左侧导航栏的 **Personal access tokens**（个人访问令牌）下，选择 **Tokens (classic)**（经典令牌）。
5. 选择 **Generate new token > Generate new token (classic)**（生成新令牌 > 生成新的经典令牌）。
6. 在 **Note**（备注）字段中输入有描述性的令牌名称，例如 `n8n integration`。
7. 选择令牌的 **Expiration**（有效期），或选择 **No expiration**（永不过期）。
8. 为令牌选择 **Scopes**（作用域）。对于大多数 n8n GitHub 节点，添加 `repo` 作用域。
    - 未分配作用域的令牌只能访问公开信息。
9. 选择 **Generate token**（生成令牌）。
10. 复制令牌。

更多信息，请参阅[创建经典个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)；GitHub 作用域的更多信息，请参阅 [OAuth 应用作用域](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes)。

### 设置凭据 <a href="#set-up-the-credential" id="set-up-the-credential"></a>

然后在 n8n 凭据中：

1. 未使用 GitHub Enterprise Server 时，不要修改 **GitHub server**（GitHub 服务器）的 URL。
    - 使用 [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.9/admin/overview/about-github-enterprise-server) 时，更新 **GitHub server**（GitHub 服务器），使其与服务器 URL 一致。
2. 按照 GitHub 个人资料中显示的名称，输入 **User**（用户）名称。
3. 输入上面生成的 **Access Token**（访问令牌）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

如果[自托管 n8n](../../../deploy/host-n8n/README.md)，请创建新的 GitHub [OAuth 应用](https://docs.github.com/en/apps/oauth-apps)：

1. 打开 GitHub 个人资料的[设置](https://github.com/settings/profile)。
2. 在左侧导航栏选择 [**Developer settings**（开发者设置）](https://github.com/settings/apps)。
3. 在左侧导航栏选择 **OAuth apps**（OAuth 应用）。
4. 选择 **New OAuth App**（新建 OAuth 应用）。
    - 如果此前未创建过应用，可能显示 **Register a new application**（注册新应用），请选择此项。
5. 输入 **Application name**（应用名称），例如 `n8n integration`。
6. 输入应用网站的 **Homepage URL**（主页 URL）。
7. 可填写可选的 **Application description**（应用描述），GitHub 会向最终用户显示。
8. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），粘贴到 GitHub 的 **Authorization callback URL**（授权回调 URL）。
9. 选择 **Register application**（注册应用）。
10. 复制生成的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据。

授权过程的更多信息，请参阅 [GitHub 授权 OAuth 应用文档](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps)。
