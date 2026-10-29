---
title: LinkedIn 凭据
description: LinkedIn 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 LinkedIn 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: LinkedIn 凭据
originalFilePath: integrations/builtin/credentials/linkedin.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/linkedin
url: https://docs.n8n.io/integrations/builtin/credentials/linkedin
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# LinkedIn 凭据 <a href="#linkedin-credentials" id="linkedin-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [LinkedIn](../app-nodes/n8n-nodes-base.linkedin.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 [LinkedIn](https://www.linkedin.com/) 账户。
* 创建 LinkedIn [公司主页](https://www.linkedin.com/help/linkedin/answer/a543852)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **Community Management OAuth2**（社区管理 OAuth2）：新 LinkedIn 用户或新建 LinkedIn 应用时，使用此方式。
- **OAuth2**：用于较旧的 LinkedIn 应用及用户账户。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LinkedIn Community Management API 文档](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview?view=li-lms-2024-04)。

此凭据适用于 API 版本 `202404`。

## 使用 Community Management OAuth2 <a href="#using-community-management-oauth2" id="using-community-management-oauth2"></a>

新 LinkedIn 用户或新建 LinkedIn 应用时，使用此方式。

配置此凭据需要一个 [LinkedIn](https://www.linkedin.com/) 账户、LinkedIn [公司主页](https://www.linkedin.com/help/linkedin/answer/a543852)，以及：

- **Client ID**（客户端 ID）：创建新开发者应用后生成。
- **Client Secret**（客户端密钥）：创建新开发者应用后生成。

创建新开发者应用并设置凭据的步骤如下：

1. 登录 LinkedIn，通过此链接[创建新开发者应用](https://www.linkedin.com/developers/apps/new)。
2. 输入应用的 **App name**（应用名称），例如 `n8n integration`。
3. 在 **LinkedIn Page**（LinkedIn 主页）中输入 LinkedIn [公司主页](https://www.linkedin.com/help/linkedin/answer/a543852)，或通过 **Create a new LinkedIn Page**（创建新的 LinkedIn 主页）链接即时创建。更多信息，请参阅[将应用关联到 LinkedIn 主页](https://www.linkedin.com/help/linkedin/answer/a548360)。
4. 添加 **App logo**（应用标志）。
5. 勾选复选框，同意 **Legal agreement**（法律协议）。
6. 选择 **Create app（创建应用）**。
7. 此时应打开 **Products**（产品）选项卡，选择要为应用启用的产品或 API。为使 LinkedIn 节点正常工作，必须添加并配置：
    - **Share on LinkedIn**（分享到 LinkedIn）
    - **Sign In with LinkedIn using OpenID Connect**（使用 OpenID Connect 登录 LinkedIn）
    - **Advertising API**（使用组织账户而非个人账户时需要）
8. 申请所需产品的访问权限后，打开 **Auth**（身份验证）选项卡。
9. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
10. 选择 **Copy**（复制）**Primary Client Secret**（主客户端密钥）的图标，将该值填入 n8n 凭据的 **Client Secret**（客户端密钥）。

{% hint style="info" %}
**以组织账户发布内容**

如需代表组织发布内容，应用必须通过 LinkedIn 的 [Community Management 应用审核](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review)流程。
{% endhint %}

作用域及权限的更多信息，请参阅[获取 LinkedIn API 访问权限](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)。

## 使用 Lead Sync API <a href="#using-lead-sync-api" id="using-lead-sync-api"></a>

LinkedIn Lead Sync API 可通过 webhook，将 LinkedIn 广告及自然流量表单（公司主页、活动、产品）的潜在客户表单回复同步到 n8n 工作流，需要额外设置及 LinkedIn 批准。

### 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- LinkedIn 开发者应用，按上方步骤创建
- 已关联到开发者应用的公司 LinkedIn 账户
- Lead Sync API 产品的访问权限，需要单独申请
- 可公开访问的 HTTPS webhook URL，即 n8n 工作流的 webhook URL

### 设置流程 <a href="#setup-process" id="setup-process"></a>

1. 按照上方 Community Management OAuth2 或 OAuth2 部分的步骤，**创建 LinkedIn 开发者应用**。
2. **关联公司账户**：通过 LinkedIn 开发者门户向 LinkedIn 提交请求，将公司 LinkedIn 账户关联到开发者应用。
3. **申请 Lead Sync API 访问权限**：
   - 在 [LinkedIn 开发者应用](https://www.linkedin.com/developers/apps/)中，打开 **Products**（产品）选项卡。
   - 申请 **Lead Sync API** 产品的访问权限。
4. **配置权限**：确保应用具有 `r_marketing_leadgen_automation` 权限，以便：
   - 访问已验证成员的广告表单和自然流量表单
   - 访问表单回复，即潜在客户信息
   - 管理潜在客户通知，即 webhook
5. **在 n8n 中设置 webhook**：
   - 在 n8n 中创建使用 Webhook 触发器节点的工作流。
   - 从 n8n 复制 webhook URL，必须使用 HTTPS。
   - webhook URL 必须可公开访问，接受 POST 请求，且不要求额外授权。
6. **处理质询请求**：
   - 向 LinkedIn 注册 webhook 时，LinkedIn 会发送包含 `challengeCode` 查询参数的 GET 请求。
   - n8n 工作流必须在 3 秒内返回包含以下内容的 JSON 载荷：
     - `challengeCode`：LinkedIn 发送的代码
     - `challengeResponse`：以应用 Client Secret 为键，对质询代码计算的 HMAC-SHA256 哈希
   - 响应格式示例：
     ```json
     {
       "challengeCode": "890e4665-4dfe-4ab1-b689-ed553bceeed0",
       "challengeResponse": "27b1d19678542072a7f1d0ce845d0c78cec22567f413697e25648f44fa3d1514"
     }
     ```
7. **创建潜在客户通知订阅**：
   - 使用 `leadNotifications` API 创建 webhook 订阅。
   - 可在不同级别创建订阅：
     - **Owner level**（所有者级别）：接收组织或赞助账户下全部表单的通知
     - **Form level**（表单级别）：仅接收特定表单的通知
     - **Associated entity level**（关联实体级别）：接收附属于广告、活动等特定实体的表单通知
   - API 调用示例：
     ```bash
     POST https://api.linkedin.com/rest/leadNotifications
     {
       "webhook": "https://your-n8n-instance.com/webhook/linkedin-leads",
       "owner": {"organization": "urn:li:organization:123456"},
       "leadType": "SPONSORED"
     }
     ```
8. **获取潜在客户表单回复**：
   - 设置 webhook 通知后，有新的潜在客户提交时便会收到通知。
   - 使用 `leadFormResponses` API 获取实际潜在客户数据：
     ```bash
     GET https://api.linkedin.com/rest/leadFormResponses?owner=(organization:urn%3Ali%3Aorganization%3A123456)&leadType=(leadType:SPONSORED)&q=owner
     ```

### 潜在客户类型 <a href="#lead-types" id="lead-types"></a>

LinkedIn 支持同步以下不同类型的潜在客户：

- **SPONSORED**：从赞助广告收集的潜在客户
- **COMPANY**：从公司主页收集的潜在客户\
- **EVENT**：从活动页面收集的潜在客户
- **ORGANIZATION_PRODUCT**：从组织产品页面收集的潜在客户

### Webhook 验证 <a href="#webhook-validation" id="webhook-validation"></a>

LinkedIn 每 2 小时定期重新验证 webhook 端点。如果连续验证失败 3 次，端点将被阻止，不再发送事件。请确保 webhook：

- 在 3 秒内响应质询请求
- 对全部通知返回 2xx HTTP 状态码
- 使用 HTTPS，不支持 HTTP URL
- 无需身份验证即可公开访问

### 安全 <a href="#security" id="security"></a>

验证通知是否来自 LinkedIn 的步骤如下：

1. 检查 POST 请求中的 `X-LI-Signature` 请求头。
2. 该请求头包含使用应用 Client Secret 对 JSON 编码的 POST 请求体计算得到的 HMAC-SHA256 哈希。
3. 在你这一侧计算相同哈希，验证是否匹配。
4. 丢弃签名不匹配的全部事件。

更多信息，请参阅 LinkedIn 的 [Lead Sync API 文档](https://learn.microsoft.com/en-us/linkedin/marketing/lead-sync/leadsync)和 [Webhook 验证指南](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

仅将此方式用于较旧的 LinkedIn 应用和用户账户。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cloud-oauth-button.md" %}

所有用户都必须选择：

- **Organization Support**（组织支持）：开启时，凭据通过 `w_organization_social` 作用域请求代表组织发布内容的权限。
    - 使用此选项，应用必须通过 LinkedIn 的 [Community Management 应用审核](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review)流程。
- **Legacy**（旧版）：开启时，凭据使用 `r_liteprofile` 和 `r_emailaddress` 的旧版作用域，代替较新的 `profile` 和 `email` 作用域。

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要创建新的开发者应用，从头配置 OAuth2：

1. 登录 LinkedIn，通过此链接[创建新开发者应用](https://www.linkedin.com/developers/apps/new)。
2. 输入应用的 **App name**（应用名称），例如 `n8n integration`。
3. 在 **LinkedIn Page**（LinkedIn 主页）中输入 LinkedIn [公司主页](https://www.linkedin.com/help/linkedin/answer/a543852)，或通过 **Create a new LinkedIn Page**（创建新的 LinkedIn 主页）链接即时创建。更多信息，请参阅[将应用关联到 LinkedIn 主页](https://www.linkedin.com/help/linkedin/answer/a548360)。
4. 添加 **App logo**（应用标志）。
5. 勾选复选框，同意 **Legal agreement**（法律协议）。
6. 选择 **Create app（创建应用）**。
7. 此时应打开 **Products**（产品）选项卡，选择要为应用启用的产品或 API。为使 LinkedIn 节点正常工作，必须添加：
    - **Share on LinkedIn**（分享到 LinkedIn）
    - **Sign In with LinkedIn using OpenID Connect**（使用 OpenID Connect 登录 LinkedIn）
8. 申请所需产品的访问权限后，打开 **Auth**（身份验证）选项卡。
9. 复制 **Client ID**（客户端 ID），填入 n8n 凭据。
10. 选择 **Copy**（复制）**Primary Client Secret**（主客户端密钥）的图标，将该值填入 n8n 凭据的 **Client Secret**（客户端密钥）。

{% hint style="info" %}
**以组织账户发布内容**

如需代表组织发布内容，应用必须通过 LinkedIn 的 [Community Management 应用审核](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review)流程。
{% endhint %}

作用域及权限的更多信息，请参阅[获取 LinkedIn API 访问权限](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)。
