---
title: Strapi 凭据
description: Strapi 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Strapi 的身份验证。
contentType:
- integration
- reference
nodeTitle: Strapi 凭据
originalFilePath: integrations/builtin/credentials/strapi.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/strapi
url: https://docs.n8n.io/integrations/builtin/credentials/strapi
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Strapi 凭据 <a href="#strapi-credentials" id="strapi-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Strapi](../app-nodes/n8n-nodes-base.strapi.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建具有以下条件的 [Strapi](https://strapi.io/) 管理员账户：

- 可以访问现有 Strapi 项目。
- 项目中至少有一个集合类型。
- 该集合类型中包含已发布的数据。

更多信息，请参阅 Strapi 开发者[快速入门指南](https://docs.strapi.io/dev-docs/quick-start)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API user account（API 用户账户）：需要具有适当内容权限的用户账户。
- API token（API 令牌）：需要管理员账户。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Strapi 文档](https://docs.strapi.io/dev-docs/api/rest)。

## 使用 API 用户账户 <a href="#using-api-user-account" id="using-api-user-account"></a>

配置此凭据需要：

- 用户 **Email**（电子邮箱）：必须属于用户账户，而非管理员账户。详细说明见下文。
- 用户 **Password**（密码）：必须属于用户账户，而非管理员账户。详细说明见下文。
- **URL**：使用 Strapi 服务器的公开 URL，即在 `./config/server.js` 中作为 `url` 参数定义的值。Strapi 建议使用绝对 URL。
    - 对于 Strapi Cloud 项目，使用云项目的 URL，例如：`https://my-strapi-project-name.strapiapp.com`
- **API Version**（API 版本）：选择调用使用的 API 版本，可选：
    - **Version 3**（版本 3）
    - **Version 4**（版本 4）

在 Strapi 中配置需要两个步骤：

1. [配置角色](#configure-a-role)。
2. [创建用户账户](#create-a-user-account)。

各步骤的详细说明如下。

### 配置角色 <a href="#configure-a-role" id="configure-a-role"></a>

API 访问使用 **Settings > Users & Permissions Plugin**（设置 > 用户与权限插件）中的 Users & Permissions Plugin。

插件的更多信息，请参阅[配置用户与权限插件](https://docs.strapi.io/user-docs/settings/configuring-users-permissions-plugin-settings)；角色的更多信息，请参阅[配置最终用户角色](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles)。

用于 n8n 凭据的用户，必须具有授予其访问集合类型 API 权限的角色。可选择：

* 更新默认 **Authenticated**（已验证）角色，加入相应权限，再将用户分配到该角色。更多信息，请参阅[配置角色权限](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#configuring-roles-permissions)。
* 创建包含相应权限的新角色，再将用户分配到该角色。更多信息，请参阅[创建新角色](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#creating-a-new-role)。

无论选择哪种方式，打开角色后：

1. 进入 **Permissions**（权限）部分。
2. 打开对应集合类型的部分。
3. 选择角色应具有的集合类型权限，可选：
    - `create`（POST）
    - `find` 和 `findone`（GET）
    - `update`（PUT）
    - `delete`（DELETE）
4. 对所有相关集合类型重复操作。
5. 保存角色。

权限选项的更多信息，请参阅[端点](https://docs.strapi.io/dev-docs/api/rest#endpoints)。

### 创建用户账户 <a href="#create-a-user-account" id="create-a-user-account"></a>

配置适当角色后，创建最终用户账户，并为其分配该角色：

1. 进入 **Content Manager > Collection Types > User**（内容管理器 > 集合类型 > 用户）。
2. 选择 **Add new entry**（添加新条目）。
3. 填写用户详情。n8n 凭据要求以下字段，Strapi 项目可能还包含其他自定义必填字段：
    - **Username**（用户名）：所有 Strapi 用户均必填。
    - **Email**（电子邮箱）：在 Strapi 中输入，并用作 n8n 凭据的 **Email**（电子邮箱）。
    - **Password**（密码）：在 Strapi 中输入，并用作 n8n 凭据的 **Password**（密码）。
    - **Role**（角色）：选择前一步设置的角色。

更多信息，请参阅[管理最终用户账户](https://docs.strapi.io/user-docs/users-roles-permissions/managing-end-users)。


## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- **API Token**（API 令牌）：在 **Settings > Global Settings > API Tokens**（设置 > 全局设置 > API 令牌）中创建。创建及重新生成 API 令牌的更多详情，请参阅 Strapi 的[创建新 API 令牌文档](https://docs.strapi.io/user-docs/settings/API-tokens#creating-a-new-api-token)。<br>
    
    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>API 令牌权限</strong></p><p>如果在 <strong>Global settings（全局设置）</strong>中未看到 <strong>API tokens（API 令牌）</strong>选项，说明账户不具有 <strong>API tokens &gt; Read</strong>（API 令牌 > 读取）权限。</p></div>
    
- **URL**：使用 Strapi 服务器的公开 URL，即在 `./config/server.js` 中作为 `url` 参数定义的值。Strapi 建议使用绝对 URL。
    - 对于 Strapi Cloud 项目，使用云项目的 URL，例如：`https://my-strapi-project-name.strapiapp.com`
- **API Version**（API 版本）：选择调用使用的 API 版本，可选：
    - **Version 3**（版本 3）
    - **Version 4**（版本 4）
