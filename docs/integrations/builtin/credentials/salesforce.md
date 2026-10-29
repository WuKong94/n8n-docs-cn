---
title: Salesforce 凭据
description: Salesforce 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Salesforce 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Salesforce 凭据
originalFilePath: integrations/builtin/credentials/salesforce.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/salesforce
url: https://docs.n8n.io/integrations/builtin/credentials/salesforce
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Salesforce 凭据 <a href="#salesforce-credentials" id="salesforce-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Salesforce](../app-nodes/n8n-nodes-base.salesforce.md)
- [Salesforce trigger（触发器）](../trigger-nodes/n8n-nodes-base.salesforcetrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- JWT
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Salesforce 开发者文档](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro.htm)。

{% hint style="warning" %}
**功能可用范围**

Salesforce 正在弃用 Connected Apps（连接应用），改用 External Client Apps（外部客户端应用）。退役时间表请查阅 Salesforce 自身文档。两种方式均可用于 n8n；新建集成请使用外部客户端应用，现有连接应用仍可继续工作。
{% endhint %}

## 使用 JWT <a href="#using-jwt" id="using-jwt"></a>

配置此凭据需要一个 [Salesforce](https://www.salesforce.com/) 账号，以及：

- **Environment Type**（环境类型）：Production（生产）或 Sandbox（沙盒）
- **Client ID**（客户端 ID）：创建外部客户端应用或连接应用时生成。
- Salesforce 的 **Username**（用户名）
- 自签名数字证书的 **Private Key**（私钥）

### 创建外部客户端应用（推荐） <a href="#create-an-external-client-app-recommended" id="create-an-external-client-app-recommended"></a>

设置时，先创建私钥和证书，再创建外部客户端应用：

1. 在 n8n 中选择连接的 **Environment Type**（环境类型），从 **Production**（生产）或 **Sandbox**（沙盒）中选择最符合实际环境的选项。
2. 输入 Salesforce **Username（用户名）**。
3. 在 Salesforce 中登录组织。
4. 需要私钥和由证书颁发机构签发的证书。可使用自己的密钥及证书，也可通过 OpenSSL 创建密钥和自签名数字证书。具体说明，请参阅 Salesforce 的[创建私钥和自签名数字证书文档](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm)。
5. 在 Salesforce 的 **Setup**（设置）中，在 Quick Find（快速查找）框输入 `App Manager`，再选择 **App Manager**（应用管理器）。
6. 在应用管理器页面选择 **New External Client App**（新建外部客户端应用）。
7. 填写外部客户端应用所需的 **Basic Info**（基本信息），包括 **Name**（名称）和 **Contact Email address**（联系邮箱地址）。
8. 在 **API (Enable OAuth Settings)**（API，启用 OAuth 设置）下，选择 **Enable OAuth**（启用 OAuth）。
9. 在 **Callback URL**（回调 URL）框中添加 `http://localhost:1717/OauthRedirect`；自托管时，使用你的 n8n 实例 URL。
10. 在 **OAuth Scopes**（OAuth 作用域）部分，选择以下作用域：
    - **Full access (full)**（完整访问）
    - **Perform requests at any time (refresh_token, offline_access)**（随时执行请求）
11. 在 **Flow Enablement**（流程启用）部分，选择 **Enable JWT Bearer Flow**（启用 JWT Bearer 流程）。
12. 选择 **Upload Files**（上传文件），上传包含数字证书的文件，例如 `server.crt`。
13. 在 **OAuth Policies**（OAuth 政策）下，确保以下设置均**未勾选**：
    - **Require Secret for Web Server Flow**（Web 服务器流程要求密钥）
    - **Require Secret for Refresh Token Flow**（刷新令牌流程要求密钥）
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**（对支持的授权流程要求 PKCE 扩展）
14. 选择 **Save**（保存），再选择 **Continue**（继续）。
15. 复制 **Consumer Key**（消费者密钥），填入 n8n 凭据的 **Client ID**（客户端 ID）。
16. 将私钥文件的内容填入 n8n 的 **Private Key**（私钥）。
    - 使用 n8n 的多行编辑器。
    - 按标准 PEM 密钥格式输入私钥：
        ```
        -----BEGIN PRIVATE KEY-----
        KEY DATA GOES HERE
        -----END PRIVATE KEY-----
        ```

更多信息，请参阅 Salesforce 的[外部客户端应用基础知识](https://help.salesforce.com/s/articleView?id=sf.external_client_app_about.htm&type=5)文档。

### 创建连接应用（旧版） <a href="#create-a-connected-app-legacy" id="create-a-connected-app-legacy"></a>

{% hint style="warning" %}
**功能可用范围**

Salesforce 正在弃用 Connected Apps（连接应用），改用 External Client Apps（外部客户端应用）。退役时间表请查阅 Salesforce 自身文档；新建集成请改用外部客户端应用。
{% endhint %}

设置时，先创建私钥和证书，再创建连接应用：

1. 在 n8n 中选择连接的 **Environment Type**（环境类型），从 **Production**（生产）或 **Sandbox**（沙盒）中选择最符合实际环境的选项。
2. 输入 Salesforce **Username（用户名）**。
3. 在 Salesforce 中登录组织。
4. 需要私钥和由证书颁发机构签发的证书。可使用自己的密钥及证书，也可通过 OpenSSL 创建密钥和自签名数字证书。具体说明，请参阅 Salesforce 的[创建私钥和自签名数字证书文档](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm)。
5. 在 Salesforce 的 **Setup**（设置）中，在 Quick Find（快速查找）框输入 `App Manager`，再选择 **App Manager**（应用管理器）。
6. 在应用管理器页面选择 **New Connected App**（新建连接应用）。
7. 填写连接应用所需的 **Basic Info**（基本信息），包括 **Name**（名称）和 **Contact Email address**（联系邮箱地址）。更多信息，请参阅 Salesforce 的[配置连接应用基本设置](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5)文档。
8. 勾选 **Enable OAuth Settings**（启用 OAuth 设置）。
9. 在 **Callback URL**（回调 URL）中输入 `http://localhost:1717/OauthRedirect`。
10. 勾选 **Use digital signatures**（使用数字签名）。
11. 选择 **Choose File**（选择文件），上传包含数字证书的文件，例如 `server.crt`。
12. 添加以下 **OAuth scopes**（OAuth 作用域）：
    - **Full access (full)**（完整访问）
    - **Perform requests at any time (refresh_token, offline_access)**（随时执行请求）
13. 选择 **Save**（保存），再选择 **Continue**（继续）。**Manage Connected Apps**（管理连接应用）页面应打开刚创建的应用。
14. 在 **API (Enable OAuth Settings)**（API，启用 OAuth 设置）部分，选择 **Manage Consumer Details**（管理消费者详情）。
15. 复制 **Consumer Key**（消费者密钥），填入 n8n 凭据的 **Client ID**（客户端 ID）。
16. 将私钥文件的内容填入 n8n 的 **Private Key**（私钥）。
    - 使用 n8n 的多行编辑器。
    - 按标准 PEM 密钥格式输入私钥：
        ```
        -----BEGIN PRIVATE KEY-----
        KEY DATA GOES HERE
        -----END PRIVATE KEY-----
        ```

以上是 n8n 侧所需步骤。Salesforce 还建议设置刷新令牌政策、会话政策和 OAuth 政策：

17. 在 Salesforce 中选择 **Back to Manage Connected Apps**（返回管理连接应用）。
18. 选择 **Manage**（管理）。
19. 选择 **Edit Policies**（编辑政策）。
20. 查看 **Refresh Token Policy**（刷新令牌政策）字段。Salesforce 建议将刷新令牌设为 90 天后过期。
21. 在 **Session Policies**（会话政策）部分，Salesforce 建议将 **Timeout Value**（超时值）设为 15 分钟。
22. 在 **OAuth Policies**（OAuth 政策）部分，将 **Permitted Users**（允许的用户）设为 **Admin approved users are pre-authorized for permitted users**（管理员批准的用户已预先获准），再选择 **OK**（确定）。
23. 选择 **Save**（保存）。
24. 选择 **Manage Profiles**（管理简档），选择预先获准使用此连接应用的简档，再选择 **Save**（保存）。
25. 选择 **Manage Permission Sets**（管理权限集），选择权限集，必要时创建。

更多信息，请参阅 Salesforce 的[在组织中创建连接应用](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)文档。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要一个 [Salesforce](https://www.salesforce.com/) 账户。

需要选择 **Environment Type**（环境类型），可选 **Production**（生产）或 **Sandbox**（沙盒）。

### 创建外部客户端应用（推荐） <a href="#create-an-external-client-app-recommended" id="create-an-external-client-app-recommended"></a>

如果[自托管](../../../deploy/host-n8n/README.md) n8n，需要创建外部客户端应用，从头配置 OAuth2：

1. 在 n8n 中选择连接的 **Environment Type**（环境类型），从 **Production**（生产）或 **Sandbox**（沙盒）中选择最符合实际环境的选项。
2. 输入 Salesforce **Username（用户名）**。
3. 在 Salesforce 中登录组织。
4. 在 Salesforce 的 **Setup**（设置）中，在 Quick Find（快速查找）框输入 `App Manager`，再选择 **App Manager**（应用管理器）。
5. 在应用管理器页面选择 **New External Client App**（新建外部客户端应用）。
6. 填写外部客户端应用所需的 **Basic Info**（基本信息），包括 **Name**（名称）和 **Contact Email address**（联系邮箱地址）。
7. 在 **API (Enable OAuth Settings)**（API，启用 OAuth 设置）下，选择 **Enable OAuth**（启用 OAuth）。
8. 在 **Callback URL**（回调 URL）框中添加 n8n OAuth 回调 URL，例如 `https://your-n8n-instance.com/rest/oauth2-credential/callback`。对于 n8n Cloud，此值为 `https://oauth.n8n.cloud/oauth2/callback`。
9. 在 **OAuth Scopes**（OAuth 作用域）部分，选择以下作用域：
    - **Full access (full)**（完整访问）
    - **Perform requests at any time (refresh_token, offline_access)**（随时执行请求）
10. 在 **Flow Enablement**（流程启用）部分，选择 **Enable Authorization Code and Credentials Flow**（启用授权码与凭据流程）。
11. 在 **OAuth Policies**（OAuth 政策）下，确保以下设置均**已勾选**：
    - **Require Secret for Web Server Flow**（Web 服务器流程要求密钥）
    - **Require Secret for Refresh Token Flow**（刷新令牌流程要求密钥）
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**（对支持的授权流程要求 PKCE 扩展）
12. 选择 **Save**（保存），再选择 **Continue**（继续）。
13. 复制 **Consumer Key**（消费者密钥），填入 n8n 凭据的 **Client ID**（客户端 ID）。
14. 复制 **Consumer Secret**（消费者秘密值），填入 n8n 凭据的 **Client Secret**（客户端密钥）。

更多信息，请参阅 Salesforce 的[外部客户端应用基础知识](https://help.salesforce.com/s/articleView?id=sf.external_client_app_about.htm&type=5)文档。

### 创建连接应用（旧版） <a href="#create-a-connected-app-legacy" id="create-a-connected-app-legacy"></a>

{% hint style="warning" %}
**功能可用范围**

Salesforce 正在弃用 Connected Apps（连接应用），改用 External Client Apps（外部客户端应用）。退役时间表请查阅 Salesforce 自身文档；新建集成请改用外部客户端应用。
{% endhint %}

如果[自托管](../../../deploy/host-n8n/README.md) n8n，也可创建连接应用来配置 OAuth2：

1. 在 n8n 中选择连接的 **Environment Type**（环境类型），从 **Production**（生产）或 **Sandbox**（沙盒）中选择最符合实际环境的选项。
2. 输入 Salesforce **Username（用户名）**。
3. 在 Salesforce 中登录组织。
4. 在 Salesforce 的 **Setup**（设置）中，在 Quick Find（快速查找）框输入 `App Manager`，再选择 **App Manager**（应用管理器）。
5. 在应用管理器页面选择 **New Connected App**（新建连接应用）。
6. 填写连接应用所需的 **Basic Info**（基本信息），包括 **Name**（名称）和 **Contact Email address**（联系邮箱地址）。更多信息，请参阅 Salesforce 的[配置连接应用基本设置](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5)文档。
7. 勾选 **Enable OAuth Settings**（启用 OAuth 设置）。
8. 在 **Callback URL**（回调 URL）中输入 `http://localhost:1717/OauthRedirect`。
9. 添加以下 **OAuth scopes**（OAuth 作用域）：
    - **Full access (full)**（完整访问）
    - **Perform requests at any time (refresh_token, offline_access)**（随时执行请求）
10. 确保以下设置均未勾选：
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**（对支持的授权流程要求 PKCE 扩展）
    - **Require Secret for Web Server Flow**（Web 服务器流程要求密钥）
    - **Require Secret for Refresh Token Flow**（刷新令牌流程要求密钥）
11. 选择 **Save**（保存），再选择 **Continue**（继续）。**Manage Connected Apps**（管理连接应用）页面应打开刚创建的应用。
12. 在 **API (Enable OAuth Settings)**（API，启用 OAuth 设置）部分，选择 **Manage Consumer Details**（管理消费者详情）。
13. 复制 **Consumer Key**（消费者密钥），填入 n8n 凭据的 **Client ID**（客户端 ID）。
14. 复制 **Consumer Secret**（消费者秘密值），填入 n8n 凭据的 **Client Secret**（客户端密钥）。

以上是 n8n 侧所需步骤。Salesforce 还建议设置刷新令牌政策和会话政策：

15. 在 Salesforce 中选择 **Back to Manage Connected Apps**（返回管理连接应用）。
16. 选择 **Manage**（管理）。
17. 选择 **Edit Policies**（编辑政策）。
18. 查看 **Refresh Token Policy**（刷新令牌政策）字段。Salesforce 建议将刷新令牌设为 90 天后过期。
19. 在 **Session Policies**（会话政策）部分，Salesforce 建议将 **Timeout Value**（超时值）设为 15 分钟。

更多信息，请参阅 Salesforce 的[在组织中创建连接应用](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### 从 n8n Cloud 向 Salesforce 进行身份验证时的连接问题 <a href="#connection-issues-when-authenticating-with-salesforce-from-n8n-cloud" id="connection-issues-when-authenticating-with-salesforce-from-n8n-cloud"></a>

从 n8n Cloud 向 Salesforce 进行身份验证时，如果遇到连接问题，可能需要在 Salesforce 用户简档中启用特定系统权限：

1. 在 Salesforce 中进入 **Setup**（设置）。
2. 在 **Quick Find**（快速查找）框中搜索 `Profiles`。
3. 选择连接到 n8n 的用户所用简档，例如 System Administrator（系统管理员）或其他相关简档。
4. 点击 **Edit**（编辑），或使用新版 **Profile**（简档）界面（如果可用）。
5. 找到 **Administrative Permissions**（管理权限）部分。
6. 勾选 **Approve Connected Apps for Non-Admins**（为非管理员批准连接应用）。根据 Salesforce 的语言或译文，此项也可能显示为 **Approve apps connected not installed**。
7. 点击 **Save**（保存）。

默认情况下，即使管理员简档也未启用此权限，需要手动开启。缺少此权限时，将 n8n 连接到 Salesforce 可能出现身份验证失败。
