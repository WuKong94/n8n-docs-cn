---
title: Dropbox 凭据
description: Dropbox 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Dropbox 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Dropbox 凭据
originalFilePath: integrations/builtin/credentials/dropbox.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/dropbox
url: https://docs.n8n.io/integrations/builtin/credentials/dropbox
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Dropbox 凭据 <a href="#dropbox-credentials" id="dropbox-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）：Dropbox 建议用于以你自己的账户进行测试，以及向少量用户授予访问权限。
- OAuth2：Dropbox 建议用于生产环境，或超过 50 个用户的测试。

{% hint style="info" %}
**复用应用**

可在 n8n 中创建使用同一应用的新 OAuth2 凭据，将应用从 API 访问令牌方式迁移到 OAuth2。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Dropbox 开发者文档](https://www.dropbox.com/developers/documentation)。

## 使用访问令牌 <a href="#using-access-token" id="using-access-token"></a>

配置此凭据需要一个 [Dropbox](https://www.dropbox.com/developers) 开发者账户，以及：

- **Access Token**（访问令牌）：创建 Dropbox 应用后生成。
- **App Access Type**（应用访问类型）

设置此凭据需要创建 Dropbox 应用：

1. 在 Dropbox 开发者门户中打开[应用控制台](https://www.dropbox.com/developers/apps)。
2. 选择 **Create app**（创建应用）。
3. 在 **Choose an API**（选择 API）中，选择 **Scoped access**（基于作用域的访问）。
4. 在 **Choose the type of access you need**（选择所需访问类型）中，选择最符合 [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md) 节点用途的选项：
    - **App Folder**（应用文件夹）：授予对专门为应用创建的单个文件夹的访问权限。
    - **Full Dropbox**（完整 Dropbox）：授予对用户 Dropbox 中全部文件和文件夹的访问权限。
    - 更多信息，请参阅 [DBX Platform 开发者指南](https://www.dropbox.com/developers/reference/developer-guide)。
5. 在 **Name your app**（为应用命名）中输入应用名称，例如 `n8n integration`。
6. 勾选复选框，同意 **Dropbox API Terms and Conditions**（Dropbox API 条款与条件）。
7. 选择 **Create app**（创建应用），随后打开应用的 **Settings**（设置）。
8. 在 **OAuth 2** 部分的 **Generated access token**（生成的访问令牌）中，选择 **Generate**（生成）。
9. 复制访问令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。
10. 在 n8n 中选择与应用相同的 **App Access Type**（应用访问类型）。

更多信息，请参阅 [Dropbox 应用控制台设置文档](https://www.dropbox.com/developers/reference/getting-started)。

{% hint style="warning" %}
**用户数量限制**

在 **Settings**（设置）选项卡中，即使使用访问令牌方式，也可为应用添加其他用户。应用关联达到 50 个 Dropbox 用户后，你有两周时间申请并获得生产状态批准，否则 Dropbox 会禁止应用继续关联更多用户。
{% endhint %}

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

Cloud 用户需要选择 **App Access Type**（应用访问类型）：

- **App Folder**（应用文件夹）：授予对专门为应用创建的单个文件夹的访问权限。
- **Full Dropbox**（完整 Dropbox）：授予对用户 Dropbox 中全部文件和文件夹的访问权限。
- 更多信息，请参阅 [DBX Platform 开发者指南](https://www.dropbox.com/developers/reference/developer-guide)。

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要手动配置 OAuth2：

1. 在 Dropbox 开发者门户中打开[应用控制台](https://www.dropbox.com/developers/apps)。
2. 选择 **Create app**（创建应用）。
3. 在 **Choose an API**（选择 API）中，选择 **Scoped access**（基于作用域的访问）。
4. 在 **Choose the type of access you need**（选择所需访问类型）中，选择最符合 [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md) 节点用途的选项：
    - **App Folder**（应用文件夹）：授予对专门为应用创建的单个文件夹的访问权限。
    - **Full Dropbox**（完整 Dropbox）：授予对用户 Dropbox 中全部文件和文件夹的访问权限。
    - 更多信息，请参阅 [DBX Platform 开发者指南](https://www.dropbox.com/developers/reference/developer-guide)。
5. 在 **Name your app**（为应用命名）中输入应用名称，例如 `n8n integration`。
6. 勾选复选框，同意 **Dropbox API Terms and Conditions**（Dropbox API 条款与条件）。
7. 选择 **Create app**（创建应用），随后打开应用的 **Settings**（设置）。
8. 复制 **App key**（应用密钥），填入 n8n 凭据的 **Client ID**（客户端 ID）。
9. 复制 **Secret**（秘密值），填入 n8n 凭据的 **Client Secret**（客户端密钥）。
10. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Dropbox 的 **Redirect URIs**（重定向 URI）。
11. 在 n8n 中选择与应用相同的 **App Access Type**（应用访问类型）。

更多信息，请参阅 [Dropbox 实现 OAuth 文档](https://developers.dropbox.com/oauth-guide#implementing-oauth)中的说明。

内部工具和有限使用场景可保持应用私有。如果希望超过 50 个用户使用应用，或希望分发应用，则需要完成 Dropbox 的生产审批流程。更多信息，请参阅 [DBX Platform 开发者指南](https://www.dropbox.com/developers/reference/developer-guide)中的 **Production Approval**（生产审批）。

{% hint style="warning" %}
**用户数量限制**

在 **Settings**（设置）选项卡中可为应用添加其他用户。应用关联达到 50 个 Dropbox 用户后，你有两周时间申请并获得生产状态批准，否则 Dropbox 会禁止应用继续关联更多用户。
{% endhint %}
