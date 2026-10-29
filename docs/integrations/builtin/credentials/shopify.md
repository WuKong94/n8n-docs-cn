---
title: Shopify 凭据
description: Shopify 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Shopify 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Shopify 凭据
originalFilePath: integrations/builtin/credentials/shopify.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/shopify
url: https://docs.n8n.io/integrations/builtin/credentials/shopify
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Shopify 凭据 <a href="#shopify-credentials" id="shopify-credentials"></a>

这些凭据可用于以下节点与 Shopify 之间的身份验证。

- [Shopify](../app-nodes/n8n-nodes-base.shopify.md)
- [Shopify Trigger（触发器）](../trigger-nodes/n8n-nodes-base.shopifytrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token（访问令牌，推荐）：用于私有应用或单个商店，普通管理员即可创建。
- OAuth2：用于公开应用，必须由合作伙伴账户创建。
- API key（API 密钥）：已弃用，请改用访问令牌。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Shopify 身份验证文档](https://shopify.dev/docs/apps/auth)。

## 使用访问令牌 <a href="#using-access-token" id="using-access-token"></a>

配置此凭据需要一个 [Shopify](https://shopify.com/) 管理员账户，以及：

- **Shop Subdomain**（商店子域名）
- **Access Token**（访问令牌）：创建自定义应用时生成。
- **APP Secret Key**（应用秘密密钥）：创建自定义应用时生成。

设置此凭据需要创建并安装自定义应用：

1. 输入 **Shop Subdomain**（商店子域名）。
    - 子域名位于 URL 中：`https://<subdomain>.myshopify.com`。例如，完整 URL 为 `https://n8n.myshopify.com` 时，商店子域名为 `n8n`。
2. 在 Shopify 中进入 **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps)（管理 > 设置 > 应用与销售渠道）。
3. 选择 **Develop apps**（开发应用）。
4. 选择 **Create a custom app**（创建自定义应用）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>未看到此选项？</strong></p><p>如果未看到此选项，商店可能尚未启用自定义应用开发。更多信息，请参阅<a href="#enable-custom-app-development">启用自定义应用开发</a>。</p></div>

5. 在弹窗中输入 **App name**（应用名称）。
6. 选择 **App developer**（应用开发者），可以是商店所有者，或具有 **Develop apps**（开发应用）权限的任意账户。
7. 选择 **Create app**（创建应用）。
8. 选择 **Select scopes**（选择作用域）。在 **Admin API access scopes**（Admin API 访问作用域）部分，为应用选择所需 API 作用域。
    - 如需使用 [Shopify](../app-nodes/n8n-nodes-base.shopify.md) 节点的全部功能，请添加 `read_orders`、`write_orders`、`read_products` 和 `write_products` 作用域。
    - 可用作用域的更多信息，请参阅 [Shopify API 访问作用域](https://shopify.dev/docs/api/usage/access-scopes)。
9. 选择 **Save**（保存）。
10. 选择 **Install app**（安装应用）。
11. 在弹窗中选择 **Install app**（安装应用）。
12. 打开应用的 **API Credentials**（API 凭据）部分。
13. 复制 **Admin API Access Token**（Admin API 访问令牌），填入 n8n 凭据的 **Access Token**（访问令牌）。
14. 复制 **API Secret Key**（API 秘密密钥），填入 n8n 凭据的 **APP Secret Key**（应用秘密密钥）。

这些步骤的更多信息，请参阅[创建自定义应用](https://help.shopify.com/en/manual/apps/app-types/custom-apps)和[在 Shopify 管理后台为自定义应用生成访问令牌](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/generate-app-access-tokens-admin)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Shopify 合作伙伴](https://www.shopify.com/partners)账户，以及：

- **Client ID**（客户端 ID）：创建自定义应用时生成。
- **Client Secret**（客户端密钥）：创建自定义应用时生成。
- **Shop Subdomain**（商店子域名）

设置此凭据需要创建并安装自定义应用：

{% hint style="info" %}
**自定义应用开发**

Shopify 提供创建新应用的模板。以下说明仅涉及设置 n8n 凭据所需的内容。构建应用及使用应用模板的更多信息，请参阅 Shopify 的[构建开发文档](https://shopify.dev/docs/apps/build)。
{% endhint %}

1. 打开 [Shopify Partner 控制台](https://partners.shopify.com/)。
2. 从左侧导航栏选择 **Apps**（应用）。
3. 选择 **Create app**（创建应用）。
4. 在 **Use Shopify Partners**（使用 Shopify Partners）部分，输入 **App name**（应用名称）。
6. 选择 **Create app（创建应用）**。
7. 打开应用详情后，复制 **Client ID**（客户端 ID），填入 n8n 凭据。
8. 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。
9. 在左侧菜单选择 **Configuration**（配置）。
10. 在 n8n 中复制 **OAuth Redirect URL**（OAuth 重定向 URL），粘贴到 **URLs** 部分的 **Allowed redirection URL(s)**（允许的重定向 URL）。
10. 在 **URLs** 部分，输入应用的 **App URL**（应用 URL）。此处主机必须与 **Allowed redirection URL(s)**（允许的重定向 URL）的主机一致，例如使用 n8n 实例的基础 URL。
8. 选择 **Save and release**（保存并发布）。
1. 从左侧菜单选择 **Overview**（概览）。此时可选择 **Test your app**（测试应用），将其安装到自己的某个商店中，或选择 **Choose distribution**（选择分发方式）公开分发应用。
1. 在 n8n 中输入已安装应用的商店的 **Shop Subdomain**（商店子域名），无论该应用用于测试还是分发。
    - 子域名位于 URL 中：`https://<subdomain>.myshopify.com`。例如，完整 URL 为 `https://n8n.myshopify.com` 时，商店子域名为 `n8n`。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

{% hint style="warning" %}
**功能可用范围**

Shopify 不再生成附带密码的 API 密钥，请改用[访问令牌](#using-access-token)方式。
{% endhint %}

配置此凭据需要：

- 一个 **API Key（API 密钥）**
- 一个 **Password（密码）**
- **Shop Subdomain**（商店子域名）：子域名位于 URL 中：`https://<subdomain>.myshopify.com`。例如，完整 URL 为 `https://n8n.myshopify.com` 时，商店子域名为 `n8n`。
- _可选：_ **Shared Secret**（共享秘密值）

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下列出设置 Shopify 凭据时的常见问题，以及解决或排查步骤。

### 启用自定义应用开发 <a href="#enable-custom-app-development" id="enable-custom-app-development"></a>

如果未看到 **Create a custom app**（创建自定义应用）选项，说明商店尚未启用自定义应用开发。

启用自定义应用开发，必须以商店所有者身份，或具有 **Enable app development**（启用应用开发）权限的用户身份登录：

1. 在 Shopify 中进入 **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps)（管理 > 设置 > 应用与销售渠道）。
2. 选择 **Develop apps**（开发应用）。
3. 选择 **Allow custom app development**（允许自定义应用开发）。
4. 阅读警告及提供的信息，选择 **Allow custom app development**（允许自定义应用开发）。

### Forbidden（禁止访问）凭据错误 <a href="#forbidden-credentials-error" id="forbidden-credentials-error"></a>


测试凭据时，如果出现 **Couldn't connect with these settings / Forbidden - perhaps check your credentials**（无法使用这些设置连接 / 禁止访问，请检查凭据）警告，可能与应用的[访问作用域](https://shopify.dev/docs/api/usage/access-scopes)依赖关系有关。例如，`read_orders` 作用域还需要 `read_products`。请检查已分配的作用域及要完成的操作。

