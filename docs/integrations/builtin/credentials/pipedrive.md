---
title: Pipedrive 凭据
description: Pipedrive 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Pipedrive 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Pipedrive 凭据
originalFilePath: integrations/builtin/credentials/pipedrive.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/pipedrive
url: https://docs.n8n.io/integrations/builtin/credentials/pipedrive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Pipedrive 凭据 <a href="#pipedrive-credentials" id="pipedrive-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Pipedrive](../app-nodes/n8n-nodes-base.pipedrive.md)
- [Pipedrive Trigger（触发器）](../trigger-nodes/n8n-nodes-base.pipedrivetrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Pipedrive 开发者文档](https://pipedrive.readme.io/docs/getting-started)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要一个 [Pipedrive](https://pipedrive.com/) 账号，以及：

- 一个 **API Token（API 令牌）**

获取 API 令牌：

1. 打开 [**API Personal Preferences**（API 个人偏好设置）](https://app.pipedrive.com/settings/api)。
2. 复制 **Your personal API token**（你的个人 API 令牌），填入 n8n 凭据。

如果有多家公司，需要先选择正确的公司：

1. 选择账户名称，确保当前查看的是正确的公司。
2. 然后选择 **Company Settings**（公司设置）。
2. 选择 **Personal Preferences**（个人偏好设置）。
3. 选择 **API** 选项卡。
4. 复制 **Your personal API token**（你的个人 API 令牌），填入 n8n 凭据。

更多信息，请参阅[如何查找 API 令牌](https://pipedrive.readme.io/docs/how-to-find-the-api-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Pipedrive 开发者沙盒账户](https://developers.pipedrive.com/)，以及：

- 一个 **Client ID（客户端 ID）**
- 一个 **Client Secret（客户端密钥）**

如需获取这两项，需要注册新应用：

1. 选择右上角的个人资料名称。
2. 找到沙盒账户的公司名称，选择 **Developer Hub**（开发者中心）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>没有 Developer Hub</strong></p><p>如果账户下拉列表中未显示 <strong>Developer Hub（开发者中心）</strong>，请注册<a href="https://developers.pipedrive.com/">开发者沙盒账户</a>。</p></div>

3. 选择 **Create an app**（创建应用）。
4. 选择 **Create public app**（创建公开应用），随后打开应用的 **Basic info**（基本信息）选项卡。
5. 输入应用的 **App name**（应用名称），例如 `n8n integration`。
6. 从 n8n 复制 **OAuth Redirect URL**（OAuth 重定向 URL），添加为应用的 **Callback URL**（回调 URL）。
7. 选择 **Save**（保存），随后打开应用的 **OAuth & access scopes**（OAuth 与访问作用域）选项卡。
8. 为应用开启适当的 **Scopes**（作用域）。更多指引，请参阅下方 [Pipedrive 节点作用域](#pipedrive-node-scopes)和 [Pipedrive Trigger 节点作用域](#pipedrive-trigger-node-scopes)。
8. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
9. 复制 **Client Secret**（客户端密钥），填入 n8n 凭据。

更多信息，请参阅[注册公开应用](https://pipedrive.readme.io/docs/marketplace-registering-the-app)。

### Pipedrive 节点作用域 <a href="#pipedrive-node-scopes" id="pipedrive-node-scopes"></a>

应用应添加哪些作用域，取决于你要在 n8n 中使用哪些节点，以及通过这些节点完成哪些操作。

[Pipedrive](../app-nodes/n8n-nodes-base.pipedrive.md) 节点可能需要以下作用域：

| **对象** | **节点操作** | **界面作用域** | **实际作用域** |
| --- | --- | --- | --- |
| 活动 | 获取活动数据 <br> 获取全部活动数据 | **Activities: Read only**（活动：只读） 或 <br> **Activities: Full Access**（活动：完整访问） | `activities:read` 或 <br> `activities:full` |
| 活动 | 创建 <br> 删除 <br> 更新 | **Activities: Full Access**（活动：完整访问） | `activities:full` |
| 交易 | 获取交易数据 <br> 获取全部交易数据 <br> 搜索交易 | **Deals: Read only**（交易：只读） 或 <br> **Deals: Full Access**（交易：完整访问） | `deals:read` 或 <br> `deals:full` |
| 交易 | 创建 <br> 删除 <br> 复制 <br> 更新 | **Deals: Full Access**（交易：完整访问） | `deals:full` |
| 交易活动 | 获取交易的全部活动 | **Activities: Read only**（活动：只读） 或 <br> **Activities: Full Access**（活动：完整访问） | `activities:read` 或 <br> `activities:full` |
| 交易产品 | 获取交易的全部产品 | **Products: Read Only**（产品：只读） 或 <br> **Products: Full Access**（产品：完整访问） | `products:read` 或 <br> `products:full` |
| 文件 | 下载 <br> 获取文件数据 | 请参阅下方说明 | 请参阅下方说明 |
| 文件 | 创建 <br> 删除 | 请参阅下方说明 | 请参阅下方说明 |
| 潜在客户 | 获取潜在客户数据 <br> 获取全部潜在客户数据 | **Leads: Read only**（潜在客户：只读） 或 <br> **Leads: Full access**（潜在客户：完整访问） | `leads:read` 或 <br> `leads:full` |
| 潜在客户 | 创建 <br> 删除 <br> 更新 | **Leads: Full access**（潜在客户：完整访问） | `leads:full` |
| 备注 | 获取备注数据 <br> 获取全部备注数据 | 请参阅下方说明 | 请参阅下方说明 |
| 备注 | 创建 <br> 删除 <br> 更新 | 请参阅下方说明 | 请参阅下方说明 |
| 组织 | 获取组织数据 <br> 获取全部组织数据 <br> 搜索 | **Contacts: Read Only**（联系人：只读） 或 <br> **Contacts: Full Access**（联系人：完整访问） | `contacts:read` 或 <br> `contacts:full` |
| 组织 | 创建 <br> 删除 <br> 更新 | **Contacts: Full Access**（联系人：完整访问） | `contacts:full` |
| 联系人 | 获取联系人数据 <br> 获取全部联系人数据 <br> 搜索 | **Contacts: Read Only**（联系人：只读） 或 <br> **Contacts: Full Access**（联系人：完整访问） | `contacts:read` 或 <br> `contacts:full` |
| 联系人 | 创建 <br> 删除 <br> 更新 | **Contacts: Full Access**（联系人：完整访问） | `contacts:full` |
| 产品 | 获取全部产品数据 | **Products: Read Only**（产品：只读） | `products:read` |

{% hint style="info" %}
**文件与备注**

文件和备注需要的作用域，取决于它们关联的对象：

- 文件关联交易、活动或联系人。
- 备注关联交易或联系人。

请参阅这些对象的作用域。
{% endhint %}

Pipedrive 节点还支持自定义 API 调用，请为计划执行的自定义调用添加相应作用域。

更多信息，请参阅[作用域与权限说明](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations)。

### Pipedrive Trigger 节点作用域 <a href="#pipedrive-trigger-node-scopes" id="pipedrive-trigger-node-scopes"></a>

[Pipedrive Trigger（触发器）](../trigger-nodes/n8n-nodes-base.pipedrivetrigger.md)节点需要 **Webhooks: Full access**（Webhook：完整访问，`webhooks:full`）作用域。
