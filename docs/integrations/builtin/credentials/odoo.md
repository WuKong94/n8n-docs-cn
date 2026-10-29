---
title: Odoo 凭据
description: Odoo 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Odoo 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Odoo 凭据
originalFilePath: integrations/builtin/credentials/odoo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/odoo
url: https://docs.n8n.io/integrations/builtin/credentials/odoo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Odoo 凭据 <a href="#odoo-credentials" id="odoo-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Odoo](../app-nodes/n8n-nodes-base.odoo.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥，推荐）
- Password（密码）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Odoo 外部 API 文档](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html)。

如果初次接触 Odoo，请参阅 Odoo 的[入门教程](https://www.odoo.com/slides/getting-started-15)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Odoo](https://www.odoo.com/) 数据库上的用户账户，以及：

- **Site URL**（站点 URL）
- **Username**（用户名）
- **API key**（API 密钥）
- **Database name**（数据库名称）

使用 API 密钥设置凭据的步骤如下：

1. 将 Odoo 服务器或站点的 URL 填入 **Site URL**（站点 URL）。
2. 输入 Odoo 的 **Change password**（更改密码）页面显示的 **Username**（用户名）。
4. 如需使用 API 密钥，进入 **Your Profile > Preferences > Account Security > Developer API Keys**（你的个人资料 > 偏好设置 > 账户安全 > 开发者 API 密钥）。
    - 如果没有此选项，可能需要升级 Odoo 方案。更多信息，请参阅[所需方案类型](#required-plan-type)。
5. 选择 **New API Key**（新建 API 密钥）。
6. 输入密钥的 **Description**（描述），例如 `n8n integration`。
7. 选择 **Generate Key**（生成密钥）。
8. 复制密钥，填入 n8n 凭据的 **Password or API key**（密码或 API 密钥）。
9. 输入 Odoo 的 **Database name**（数据库名称），也称为实例名称。

更多信息，请参阅 [Odoo API 密钥](https://www.odoo.com/documentation/15.0/developer/reference/external_api.html?#api-keys)。

## 使用密码 <a href="#using-password" id="using-password"></a>

配置此凭据需要一个 [Odoo](https://www.odoo.com/) 数据库上的用户账户，以及：

- **Site URL**（站点 URL）
- **Username**（用户名）
- 你的 **Password**（密码）
- **Database name**（数据库名称）

使用密码设置凭据的步骤如下：

1. 将 Odoo 服务器或站点的 URL 填入 **Site URL**（站点 URL）。
2. 输入 Odoo 的 **Change password**（更改密码）页面显示的 **Username**（用户名）。
3. 如需使用密码，将用户密码填入 **Password or API key**（密码或 API 密钥）字段。
4. 输入 Odoo 的 **Database name**（数据库名称），也称为实例名称。

{% hint style="info" %}
**密码兼容性**

如果使用密码凭据时，某个节点功能无法正常工作，可尝试切换为 API 密钥。Odoo 的某些模块或设置要求使用 API 密钥。
{% endhint %}

## 所需方案类型 <a href="#required-plan-type" id="required-plan-type"></a>

{% hint style="info" %}
**所需方案类型**

只有 **Custom**（自定义）Odoo 方案提供外部 API 访问权限。One App Free 或 Standard 方案不提供此权限。

更多信息，请参阅 [Odoo 价格方案](https://www.odoo.com/pricing-plan)。
{% endhint %}
