---
title: Nextcloud 凭据
description: Nextcloud 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Nextcloud 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Nextcloud 凭据
originalFilePath: integrations/builtin/credentials/nextcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/nextcloud
url: https://docs.n8n.io/integrations/builtin/credentials/nextcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Nextcloud 凭据 <a href="#nextcloud-credentials" id="nextcloud-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Nextcloud](../app-nodes/n8n-nodes-base.nextcloud.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Nextcloud API 文档](https://nextcloud-server.netlify.app/)。

安装和配置 Nextcloud 的更多信息，请参阅 [Nextcloud 用户手册](https://docs.nextcloud.com/server/stable/user_manual/en/contents.html)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要一个 [Nextcloud](https://nextcloud.com/) 账号，以及：

- **WebDAV URL**
- **User**（用户）名称
- **Password**（密码）或应用密码

设置步骤如下：

1. 创建 **WebDAV URL**：如果 Nextcloud 安装在域名根目录中，输入访问 Nextcloud 的 URL，再添加 `/remote.php/webdav/`。例如，通过 `https://cloud.n8n.com` 访问 Nextcloud 时，WebDAV URL 为 `https://cloud.n8n.com/remote.php/webdav`。
    - 如果 Nextcloud 安装在子目录中，输入访问 Nextcloud 的 URL，再添加 `/<subdirectory>/remote.php/webdav/`，并将 `<subdirectory>` 替换为 Nextcloud 所在的子目录。
    - 构建 WebDAV URL 的更多信息，请参阅 Nextcloud 的[第三方 WebDAV 客户端](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients)文档。
2. 输入 **User**（用户）名称。
3. 在 **Password**（密码）字段中，Nextcloud 建议使用应用密码，而非用户密码。创建应用密码的步骤如下：
    1. 在 Nextcloud Web 界面中，选择右上角的头像，再选择 **Personal settings**（个人设置）。
    2. 在左侧菜单选择 **Security**（安全）。
    3. 向下滚动到 **App Password**（应用密码）部分，创建新应用密码。
    4. 复制该应用密码，填入 n8n 的 **Password**（密码）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Nextcloud](https://nextcloud.com/) 账号，以及：

- **Authorization URL**（授权 URL）和 **Access Token URL**（访问令牌 URL）：取决于访问 Nextcloud 所用的 URL。
- **Client ID**（客户端 ID）：在 **Administrator Security Settings**（管理员安全设置）中添加 OAuth2 客户端应用后生成。
- **Client Secret**（客户端密钥）：在 **Administrator Security Settings**（管理员安全设置）中添加 OAuth2 客户端应用后生成。
- **WebDAV URL**：取决于访问 Nextcloud 所用的 URL。

设置步骤如下：

1. 在 Nextcloud 中打开 **Administrator Security Settings**（管理员安全设置）。
2. 在 **OAuth 2.0 clients**（OAuth 2.0 客户端）下找到 **Add client**（添加客户端）部分。
3. 输入客户端的 **Name**（名称），例如 `n8n integration`。
4. 从 n8n 复制 **OAuth Callback URL**（OAuth 回调 URL），填入 **Redirection URI**（重定向 URI）。
5. 然后在 Nextcloud 中选择 **Add**（添加）。
6. 在 n8n 中更新 **Authorization URL**（授权 URL），将 `https://nextcloud.example.com` 替换为访问 Nextcloud 的 URL。例如，通过 `https://cloud.n8n.com` 访问 Nextcloud 时，Authorization URL 为 `https://cloud.n8n.com/apps/oauth2/authorize`。
7. 在 n8n 中更新 **Access Token URL**（访问令牌 URL），将 `https://nextcloud.example.com` 替换为访问 Nextcloud 的 URL。例如，通过 `https://cloud.n8n.com` 访问 Nextcloud 时，Access Token URL 为 `https://cloud.n8n.com/apps/oauth2/api/v1/token`。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Pretty URL 配置</strong></p><p><strong>Authorization URL（授权 URL）</strong> 和 <strong>Access Token URL（访问令牌 URL）</strong> 假设 Nextcloud 已配置为使用<a href="https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#pretty-urls">Pretty URLs</a>。如果未配置，必须添加 <code>/index.php/</code>，放在 Nextcloud URL 与 <code>/apps/oauth2</code> 部分之间，例如：<code>https://cloud.n8n.com/index.php/apps/oauth2/api/v1/token</code>。</p></div>
    
8. 复制 Nextcloud 为 OAuth2 客户端生成的 **Client Identifier**（客户端标识符），填入 n8n 的 **Client ID**（客户端 ID）。
9. 复制 Nextcloud 的 **Secret**（秘密值），填入 n8n 的 **Client Secret**（客户端密钥）。
10. 在 n8n 中创建 **WebDAV URL**：如果 Nextcloud 安装在域名根目录中，输入访问 Nextcloud 的 URL，再添加 `/remote.php/webdav/`。例如，通过 `https://cloud.n8n.com` 访问 Nextcloud 时，WebDAV URL 为 `https://cloud.n8n.com/remote.php/webdav`。
    - 如果 Nextcloud 安装在子目录中，输入访问 Nextcloud 的 URL，再添加 `/<subdirectory>/remote.php/webdav/`，并将 `<subdirectory>` 替换为 Nextcloud 所在的子目录。
    - 构建 WebDAV URL 的更多信息，请参阅 Nextcloud 的[第三方 WebDAV 客户端](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients)文档。

更详细的说明，请参阅 Nextcloud 的 [OAuth2 配置文档](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/oauth2.html)。
