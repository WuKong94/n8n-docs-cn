---
title: Notion 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Notion 凭据
originalFilePath: integrations/builtin/credentials/notion.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/notion
url: https://docs.n8n.io/integrations/builtin/credentials/notion
description: Notion 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Notion 的身份验证。
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


# Notion 凭据 <a id="notion-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Notion](../app-nodes/n8n-nodes-base.notion/README.md)
* [Notion Trigger（触发器）](../trigger-nodes/n8n-nodes-base.notiontrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建具有管理员级别权限的 [Notion](https://notion.so) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API integration token（API 集成令牌）：用于内部集成。
* OAuth2：用于公开集成。

{% hint style="info" %}
**集成类型**

不确定使用哪种集成类型？更多信息，请参阅下方[内部集成与公开集成](notion.md#internal-vs-public-integrations)。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Notion API 文档](https://developers.notion.com/reference/intro)。

## 使用 API 集成令牌 <a href="#using-api-integration-token" id="using-api-integration-token"></a>

配置此凭据需要：

* **Internal Integration Secret**（内部集成密钥）：创建 Notion 集成后生成。

生成集成密钥时，请先[创建 Notion 集成](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion)，再从 **Secrets**（密钥）选项卡获取：

1. 打开 Notion 的[集成控制台](https://www.notion.com/my-integrations)。
2. 选择 **+ New integration**（新建集成）按钮。
3. 输入集成的 **Name**（名称），例如 `n8n integration`。可按需添加 **Logo**（标志）。
4. 选择 **Submit**（提交），创建集成。
5. 打开 **Capabilities**（功能）选项卡，选择以下功能：
   * `Read content`
   * `Update content`
   * `Insert content`
   * `User information without email addresses`
6. 确保选择 **Save changes**（保存更改）。
7. 选择 **Secrets**（密钥）选项卡。
8. 复制 **Internal Integration Token**（内部集成令牌），填入 n8n 的 **Internal Integration Secret**（内部集成密钥）。

该服务的身份验证详情，请参阅[内部集成身份验证流程设置文档](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up)。

### 向集成共享 Notion 页面 <a href="#share-notion-pages-with-the-integration" id="share-notion-pages-with-the-integration"></a>

集成要与 Notion 交互，必须[授予集成页面权限](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)，使其能与 Notion 工作区中的页面交互：

1. 打开 Notion 工作区中的目标页面。
2. 选择页面右上角的三点菜单。
3. 在 **Connections**（连接）中选择 **Connect to**（连接到）。
4. 使用搜索栏，在下拉列表中找到并选择集成。

至少向集成共享一个页面后，即可开始发出 API 请求。如果未共享页面，API 请求将返回错误。

更多信息，请参阅[集成权限](https://developers.notion.com/docs/authorization#integration-permissions)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

* **Client ID**（客户端 ID）：配置公开集成后生成。
* **Client Secret**（客户端密钥）：配置公开集成后生成。

必须[创建 Notion 集成](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion)，并将其设为公开分发：

1. 打开 Notion 的[集成控制台](https://www.notion.so/my-integrations)。
2. 选择 **+ New integration**（新建集成）按钮。
3. 输入集成的 **Name**（名称），例如 `n8n integration`。可按需添加 **Logo**（标志）。
4. 选择 **Submit**（提交），创建集成。
5. 打开 **Capabilities**（功能）选项卡，选择以下功能：
   * `Read content`
   * `Update content`
   * `Insert content`
   * `User information without email addresses`
6. 选择 **Save changes**（保存更改）。
7. 打开 **Distribution**（分发）选项卡。
8. 开启 **Do you want to make this integration public?**（是否将此集成公开？）控件。
9. 在 **Organization Information**（组织信息）部分输入公司名称和网站。
10. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），填入 Notion 集成 **OAuth Domain & URLs**（OAuth 域名与 URL）部分的 **Redirect URI**（重定向 URI）。
11. 打开 **Secrets**（密钥）选项卡。
12. 复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥），填入 n8n 凭据。

该服务的身份验证详情，请参阅 Notion 的[公开集成身份验证流程设置](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up)。

## 内部集成与公开集成 <a href="#internal-vs-public-integrations" id="internal-vs-public-integrations"></a>

**Internal**（内部）集成具有以下特征：

* 专用于单个工作区。
* 仅该工作区成员可访问。
* 适合自定义工作区增强功能。

内部集成使用更简单的身份验证流程，即集成密钥，发布前无需安全审核。

**Public**（公开）集成具有以下特征：

* 可跨多个互不相关的 Notion 工作区使用。
* 任意 Notion 用户均可访问，不受所属工作区限制。
* 适合覆盖广泛使用场景。

公开集成使用 OAuth 2.0 协议进行身份验证，发布前需要经过 Notion 安全审核。

两种集成类型更详细的对比，请参阅 Notion 的[内部集成与公开集成文档](https://developers.notion.com/docs/getting-started#internal-vs-public-integrations)。
