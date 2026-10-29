---
title: Databricks 凭据
description: Databricks 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Databricks 的身份验证。
contentType:
- integration
- reference
nodeTitle: Databricks 凭据
originalFilePath: integrations/builtin/credentials/databricks.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/databricks
url: https://docs.n8n.io/integrations/builtin/credentials/databricks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks 凭据 <a href="#databricks-credentials" id="databricks-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Databricks](../app-nodes/n8n-nodes-base.databricks.md)
- [Databricks AI Agent](../cluster-nodes/root-nodes/n8n-nodes-langchain.databricksaiagent.md)（仅支持 OAuth2，用于导出 MLflow 追踪记录）
- [Databricks Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdatabricks.md)（仅支持 OAuth2）
- [Databricks Genie One MCP server](../cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie.md)（仅支持通过用户登录的 OAuth2）
- [Databricks Lakebase Chat Memory](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorylakebasechat.md)（仅支持 OAuth2）
- [Databricks Trigger（触发器）](../trigger-nodes/n8n-nodes-base.databrickstrigger.md)
- [Databricks Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoredatabricks/README.md)（仅支持 OAuth2）
- [Embeddings Databricks](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsdatabricks.md)（仅支持 OAuth2）

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 位于 AWS、Azure 或 GCP 上的 [Databricks](https://www.databricks.com/) 工作区。
- 使用用户登录的 OAuth2：需要一名能够在账户控制台创建自定义 OAuth 应用连接的 Databricks 账户管理员。
- 使用服务主体的 OAuth2：需要一名能够创建服务主体并为其生成 OAuth 密钥的 Databricks 管理员。
- 用于身份验证的身份执行所需操作时必需的[权限](#required-databricks-privileges)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [个人访问令牌](#using-a-personal-access-token)：绑定到一个 Databricks 用户的令牌。仅 Databricks 节点支持，且该节点的 **Lakebase** 资源不支持。
- [通过用户登录的 OAuth2](#using-oauth2-with-user-login)：在浏览器中登录 Databricks 账户来连接凭据。操作使用该用户的权限执行，并以其身份记录到 Databricks 审计日志。每位用户都可创建自己的凭据，让工作流以自己的账户运行。Databricks 建议将此方式用于有人参与的交互场景。
- [使用服务主体的 OAuth2](#using-oauth2-service-principal)：n8n 使用客户端 ID 和密钥以服务主体身份进行身份验证，无需用户交互。Databricks 建议将此方式用于无人值守场景，例如完全自动化的生产工作流。

## 所需的 Databricks 权限 <a id="required-databricks-privileges"></a>

凭据用于身份验证的身份（已登录用户或服务主体）需要在 Databricks 中拥有以下权限，具体取决于执行的操作：

| 操作 | 所需权限 |
|------------|--------------------|
| 全部 | **Workspace access**（工作区访问）授权 |
| Databricks SQL（Execute Query，执行查询） | **Databricks SQL access**（Databricks SQL 访问）授权，以及 SQL 仓库的 **CAN USE** 权限 |
| Job（作业）：Get、Get Run、Get Run Output（获取作业、获取运行、获取运行输出） | 作业的 **CAN VIEW** 权限 |
| Job（作业）：Run（运行） | 作业的 **CAN MANAGE RUN** 权限 |
| Lakebase | 在项目分支上创建的 Postgres 角色，并将其授予 `authenticator`；该角色还需拥有操作所需的表和函数权限。请参阅[为 Data API 设置 Lakebase](#set-up-lakebase-for-the-data-api) |
| 读取或写入 Unity Catalog 数据 | 目录的 **USE CATALOG** 权限、架构的 **USE SCHEMA** 权限，以及所查询表或视图的 **SELECT** 权限。函数和模型还需要 **EXECUTE** 权限 |
| Genie Agent（Databricks 节点） | Genie Agent 的 **CAN RUN** 权限及其 SQL 仓库的 **CAN USE** 权限 |
| Genie One MCP server | 对 Genie One 应据以回答问题的每个 Genie Agent 拥有 **CAN RUN** 权限，并对至少一个 SQL 仓库拥有 **CAN USE** 权限 |
| Model Serving（模型服务）：Query Endpoint（查询端点） | 服务端点的 **CAN QUERY** 权限 |
| Unity AI Gateway 模型服务（Databricks Chat Model、Embeddings Databricks） | 对模型服务所在的目录和架构拥有 **USE CATALOG** 和 **USE SCHEMA** 权限，并对模型服务拥有 **EXECUTE** 权限。Databricks 默认向所有用户授予 `system.ai` 服务的 **EXECUTE** 权限 |
| 搜索向量搜索索引（Databricks Vector Store：Get Many、Retrieve Documents、Retrieve as Tool，即获取多项、检索文档、作为工具检索） | 目录的 **USE CATALOG** 权限、架构的 **USE SCHEMA** 权限及索引的 **SELECT** 权限。对于同步全部列的 Delta Sync 索引，对源表拥有 **SELECT** 权限后，节点才能列出这些列。自管理索引还需要为 Embeddings Databricks 节点授予上文所述的模型服务权限。**Metadata Filter**（元数据筛选）需要对 Vector Search 端点的读取权限 |
| 插入文档（Databricks Vector Store：Insert Documents） | 搜索所需权限，以及索引的 **MODIFY** 权限。仅 Direct Access 索引接受插入 |
| 将追踪记录导出到 MLflow（Databricks AI Agent） | 实验的 **CAN EDIT** 权限。节点在 `/Shared` 下创建的默认实验无需额外授权，因为所有工作区用户默认拥有 `/Shared` 文件夹的 **CAN MANAGE** 权限 |
| 监视作业或流水线（Databricks Trigger） | 作业或流水线的 **CAN VIEW** 权限 |

{% hint style="info" %}
**新建服务主体最初没有任何权限**

刚创建的服务主体没有任何授权，因此首次执行操作会因权限不足而失败，错误中会指出缺失的授权。请先分配上述权限，再运行工作流。
{% endhint %}

更多信息，请参阅 [Databricks 授权](https://docs.databricks.com/aws/en/security/auth/entitlements)、[访问控制列表](https://docs.databricks.com/aws/en/security/auth/access-control/)和 [Unity Catalog 权限](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Databricks 身份验证文档](https://docs.databricks.com/aws/en/dev-tools/auth/)。

## 使用个人访问令牌 <a href="#using-a-personal-access-token" id="using-a-personal-access-token"></a>

配置此凭据需要：

- **Host**（主机）：Databricks 工作区的 URL，例如 `https://adb-1234567890123456.7.azuredatabricks.net`。
- **Access Token**（访问令牌）：在 Databricks 工作区中生成的个人访问令牌。

生成个人访问令牌的步骤如下：

1. 在 Databricks 工作区中选择右上角的用户名，再选择 **Settings**（设置）。
2. 选择 **Developer**（开发者）。
3. 在 **Access tokens**（访问令牌）旁选择 **Manage**（管理）。
4. 选择 **Generate new token**（生成新令牌）。
5. 可选：输入 **Comment**（备注）以标识令牌，再选择 **Generate**（生成）。
6. 复制令牌并妥善保存。关闭此对话框后，将无法再次查看该令牌。
7. 将令牌填入 n8n 凭据的 **Access Token**（访问令牌）。

{% hint style="info" %}
**令牌格式**

个人访问令牌以 `dapi` 开头，例如 `dapi1234abcd5678efgh`。
{% endhint %}

更多信息，请参阅 [Databricks 个人访问令牌身份验证](https://docs.databricks.com/en/dev-tools/auth/pat.html)。

## 通过用户登录使用 OAuth2 <a id="using-oauth2-with-user-login"></a>

此方式使用 Databricks OAuth 用户到机器（U2M）流程。在浏览器中登录 Databricks 来连接凭据，操作以你的权限执行。共享凭据以连接该凭据的用户身份运行，因此不同身份应创建各自的凭据。

配置此凭据需要：

- **Host**（主机）：Databricks 工作区的 URL，例如 `https://adb-1234567890123456.7.azuredatabricks.net`。
- **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）：来自 Databricks 账户管理员在账户控制台中创建的自定义 OAuth 应用连接。

设置此凭据需要三个步骤：

1. [在 Databricks 中创建自定义 OAuth 应用连接](#create-a-custom-oauth-app-connection)。
2. 可选：[配置令牌有效期](#configure-token-lifetimes)。
3. [在 n8n 中设置凭据](#set-up-the-credential-in-n8n)。

{% hint style="info" %}
**需要账户控制台访问权限**

创建自定义 OAuth 应用连接需要访问 Databricks 账户控制台。Databricks Free Edition 不提供账户控制台访问权限，因此 Free Edition 工作区应使用[服务主体](#using-oauth2-service-principal)或[个人访问令牌](#using-a-personal-access-token)。
{% endhint %}

### 创建自定义 OAuth 应用连接 <a id="create-a-custom-oauth-app-connection"></a>

Databricks 账户管理员需要完成以下步骤：

1. 在 n8n 中打开 Databricks 凭据，复制 **OAuth Redirect URL**（OAuth 重定向 URL），其格式为 `https://<your-n8n-instance>/rest/oauth2-credential/callback`。
2. 登录所用云平台的 Databricks 账户控制台（[AWS](https://accounts.cloud.databricks.com/)、[Azure](https://accounts.azuredatabricks.net/) 或 [GCP](https://accounts.gcp.databricks.com/)），选择侧栏中的 **Settings**（设置）图标。
3. 在 **App connections**（应用连接）选项卡中选择 **Add connection**（添加连接）。
4. 输入连接名称，例如 `n8n`。
5. 将从 n8n 复制的 **OAuth Redirect URL**（OAuth 重定向 URL）添加为重定向 URL。
6. 选择连接所需的访问作用域。**Databricks** 节点和 **Databricks Chat Model** 节点需要 **All APIs**（所有 API）。如果连接仅供 [Genie One MCP server](../cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie.md) 使用，则选择 `genie`：这样连接无法访问其他 Databricks API，用户同意授予的权限范围也更小。Databricks 会自动允许 n8n 保持连接所需的 `offline_access` 作用域。在 n8n 的测试中，**All APIs** 也涵盖 `genie` 作用域；如果连接该服务卡片时出现作用域错误，请[添加 `genie` 作用域](#add-the-genie-scope-for-the-genie-mcp-server)。
7. 启用客户端密钥生成。n8n 是机密客户端，因此需要密钥。
8. 保存连接，复制 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。Databricks 仅显示一次密钥。

将客户端 ID 和密钥提供给需要创建凭据的 n8n 用户。所有用户复用同一个 OAuth 应用连接，但每位用户都创建并连接自己的 n8n 凭据，以各自的身份运行。

更多信息，请参阅[启用或禁用合作伙伴 OAuth 应用](https://docs.databricks.com/aws/en/integrations/enable-disable-oauth)。

### 为 Genie MCP server 添加 genie 作用域 <a id="add-the-genie-scope-for-the-genie-mcp-server"></a>

[Databricks Genie One MCP server](../cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie.md) 服务卡片会请求 `genie` 和 `offline_access` 作用域。在 n8n 的测试中，具有 **All APIs**（所有 API）的应用连接无需显式添加 `genie` 作用域即可满足请求。对于无法满足请求的账户，用户在服务卡片上选择 **Connect my account**（连接我的账户）时会看到以下错误：

```text
access_denied: Scopes 'genie' are not assigned to the client <client-id>
```

要解决此问题，Databricks 账户管理员需向应用连接添加 `genie` 作用域。如果账户控制台的连接页面在 **Add scope**（添加作用域）选择器中提供 `genie`，就在其中添加。否则，使用已通过账户身份验证的 [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/)。CLI 更新会替换整个作用域列表，因此必须包含应用所需的全部作用域。同时供 Databricks 节点、Databricks Chat Model 节点和 Genie One MCP server 使用的应用连接需要以下三个作用域：

```bash
databricks account custom-app-integration update <integration-id> \
	--json '{"scopes": ["all-apis", "genie", "offline_access"]}'
```

`<integration-id>` 可通过 `databricks account custom-app-integration list` 查找，也可在账户控制台的连接详情页找到。API 参考请参阅[更新自定义 OAuth 应用集成](https://docs.databricks.com/api/account/customappintegration/update)。

Databricks 的授权同意页面显示分配给应用连接的作用域，而不是 n8n 请求的较小作用域集合。用户通过 **All APIs**（所有 API）应用连接 Genie One MCP server 时，授权页面显示 **All APIs**，即使 n8n 收到的令牌仅限于 `genie offline_access` 作用域。

如果应用连接仅供 Genie One MCP server 使用，请将作用域设为 `["genie", "offline_access"]`。这样用户看到并同意的权限范围更小，客户端也无法访问其他 Databricks API。

### 配置令牌有效期 <a id="configure-token-lifetimes"></a>

应用连接的令牌访问策略决定用户与 n8n 的连接可保持有效多长时间：

- **Access token TTL**（访问令牌有效期）：每个访问令牌的有效时长，默认为 60 分钟。n8n 会使用刷新令牌自动续期已过期的访问令牌，因此可以保留默认值。
- **Refresh token TTL**（刷新令牌有效期）：刷新令牌的有效时长，默认为 10080 分钟（7 天），最长为 129600 分钟（90 天）。刷新令牌过期后，凭据将停止工作，直到用户在 n8n 中打开凭据并重新登录。

Databricks 账户管理员还可通过[账户 API 或 CLI](https://docs.databricks.com/aws/en/integrations/manage-oauth) 设置绝对会话有效期和一次性刷新令牌。达到绝对会话有效期时，即使刷新令牌仍然有效，会话也会结束。

{% hint style="warning" %}
**较短有效期会要求用户重新连接**

较短的刷新令牌有效期或绝对会话有效期意味着用户必须定期在 n8n 中重新打开凭据并登录；在重新登录前，使用此凭据的工作流会失败。对于运行定时工作流的凭据，请设置较长有效期，或改用[服务主体](#using-oauth2-service-principal)。
{% endhint %}

### 在 n8n 中设置凭据 <a id="set-up-the-credential-in-n8n"></a>

1. 将工作区 URL 填入 **Host**（主机）。
2. 将 **Grant Type**（授权类型）设为 **Authorization Code (User)**（授权码，用户）。
3. 输入自定义 OAuth 应用连接的 **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
4. 选择 **Connect my account**（连接我的账户），使用 Databricks 账户登录。

凭据默认请求 `all-apis` 和 `offline_access` 作用域。`offline_access` 作用域让连接在一小时后仍保持有效，因此始终包含在请求中：如果启用 **Custom Scopes**（自定义作用域）并将其从列表中移除，n8n 会自动将其加回。

## 使用 OAuth2（服务主体） <a href="#using-oauth2-service-principal" id="using-oauth2-service-principal"></a>

此方式使用 Databricks 服务主体和 OAuth M2M（机器到机器）流程。它不需要用户交互，因此是自动化工作流的推荐方式。

配置此凭据需要：

- **Host**（主机）：Databricks 工作区的 URL，例如 `https://adb-1234567890123456.7.azuredatabricks.net`。
- **Client ID**（客户端 ID）：服务主体的应用程序 ID。
- **Client Secret**（客户端密钥）：为服务主体生成的 OAuth 密钥。

设置此凭据需要两个步骤：

1. [在 Databricks 中创建服务主体和 OAuth 密钥](#create-a-service-principal-and-oauth-secret)。
2. [在 n8n 中设置凭据](#set-up-the-oauth2-credential)。

### 创建服务主体和 OAuth 密钥 <a href="#create-a-service-principal-and-oauth-secret" id="create-a-service-principal-and-oauth-secret"></a>

1. 在 Databricks 账户控制台中选择 **User management**（用户管理）。
2. 选择 **Service principals**（服务主体），再选择 **Add service principal**（添加服务主体）。
3. 输入服务主体名称，选择 **Add**（添加）。
4. 打开服务主体，进入 **Configuration**（配置）选项卡，授予其所需的工作区访问授权。
5. 进入 **Secrets**（密钥）选项卡，选择 **Generate secret**（生成密钥）。
6. 设置密钥有效期，单位为天，最长 730 天，再选择 **Generate**（生成）。
7. 复制显示的 **Secret**（密钥）和 **Client ID**（客户端 ID，与应用程序 ID 相同）。密钥仅显示一次。

{% hint style="info" %}
**工作区分配**

必须将服务主体分配到其要访问的工作区，并授予 **Workspace access**（工作区访问）授权。仅存在于账户级别的服务主体访问工作区令牌端点时会收到 `invalid_client` 错误，看起来像是客户端密钥错误。进入 **Permissions**（权限）选项卡，授权所需的用户或组管理和使用此服务主体。
{% endhint %}

{% hint style="warning" %}
**OAuth 密钥会过期**

服务主体密钥的有效期最长为 730 天。密钥过期后，凭据将停止工作，使用它的工作流也会失败。请记录到期日，在到期前生成新密钥，并更新 n8n 凭据的 **Client Secret**（客户端密钥）。
{% endhint %}

更多信息，请参阅[使用 OAuth 授权服务主体访问 Databricks](https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html)。

### 设置 OAuth2 凭据 <a href="#set-up-the-oauth2-credential" id="set-up-the-oauth2-credential"></a>

在 n8n 凭据中：

1. 将 **Authentication**（身份验证）设为 **OAuth2**。
2. 将工作区 URL 填入 **Host**（主机）。
3. 将 **Grant Type**（授权类型）设为 **Client Credentials (Service Principal)**（客户端凭据，服务主体）。这是默认值。
4. 输入从服务主体复制的 **Client ID**（客户端 ID）。
5. 输入生成的 **Client Secret**（客户端密钥）。

## 为 Data API 设置 Lakebase <a id="set-up-lakebase-for-the-data-api"></a>

[Databricks 节点](../app-nodes/n8n-nodes-base.databricks.md#lakebase-operations)的 **Lakebase** 资源通过 Lakebase Data API 读写行。此 API 默认关闭，且凭据用于身份验证的身份必须拥有 Postgres 角色，操作才能成功。请按以下顺序执行。各步骤的作用范围不同：每个项目启用一次 Data API 和 OpenAPI 规范；每个分支创建一次 Postgres 角色并将其授予 `authenticator`；节点访问的每个数据库都需安装 `databricks_auth` 扩展并授予表和函数权限。

{% hint style="info" %}
**Data API 不接受个人访问令牌**

节点会在调用 Data API 前检查这一点，因此使用个人访问令牌会出现 `Lakebase requires OAuth2 authentication` 错误，而不会收到 Databricks 返回的错误。将节点的 **Authentication**（身份验证）设为 **OAuth2**，并使用[通过用户登录的 OAuth2](#using-oauth2-with-user-login) 或[使用服务主体的 OAuth2](#using-oauth2-service-principal)。
{% endhint %}

### 启用 Data API <a id="enable-the-data-api"></a>

在 Databricks 中打开 Lakebase 项目，依次选择 **App Backend**（应用后端）> **Data API** > **Enable Data API**（启用 Data API）。此步骤没有对应的 API 或 CLI。Databricks 会创建下文授权步骤所需的 `authenticator` 角色。

此 API 默认仅公开 `public` 架构。如需访问其他架构，请在同一设置中添加。

### 启用 OpenAPI 规范 <a id="turn-on-the-openapi-specification"></a>

在同一项目中依次选择 **Data API** > **API** > **Advanced settings**（高级设置）> **OpenAPI specification**（OpenAPI 规范），再选择 **Follow privileges**（遵循权限）。选择 **Save**（保存）应用更改，更改会立即生效。

节点会读取此文档，以列出表、函数、表的列和函数的参数。没有它，**Table**（表）、**Function**（函数）和列列表会报错，**Columns**（列）及 **Arguments**（参数）映射器会保持为空并显示提示。每条消息都会指出同一个设置：

```text
Data API > API > Advanced settings > OpenAPI specification
```

**Follow privileges**（遵循权限）仅列出已连接身份可使用的对象。**Ignore privileges**（忽略权限）会列出所有对象，包括 Databricks 创建的内部表和函数。

### 为 n8n 使用的身份创建 Postgres 角色 <a id="create-a-postgres-role-for-the-n8n-identity"></a>

使用能够管理项目的身份，在 Lakebase SQL 编辑器中运行以下内容：

```sql
CREATE EXTENSION IF NOT EXISTS databricks_auth;
SELECT databricks_create_role('<identity>', 'SERVICE_PRINCIPAL');
```

`<identity>` 是服务主体的应用程序 ID。对于用户身份，请改为传入电子邮件地址和 `'USER'`。

Postgres 扩展属于单个数据库。请在节点访问的每个数据库中运行 `CREATE EXTENSION`。角色覆盖整个分支，而非单个数据库。在尚未为该身份创建角色的任何分支上，都需再次运行 `databricks_create_role`。如果分支中没有对应角色，Data API 会返回 `invalid token permissions`（`PGRST301`）。

即使该身份已显示在 Databricks 界面中，也应以此方式创建角色。下一步仅适用于通过 `databricks_create_role` 创建的角色。

### 将角色授予 authenticator <a id="grant-the-role-to-authenticator"></a>

`<role>` 是传入 `databricks_create_role` 的身份。服务主体使用应用程序 ID，用户则使用电子邮件地址。

```sql
GRANT "<role>" TO authenticator;
```

以创建该角色的身份运行此语句。没有此授权，任何角色都无法访问 Data API。执行前，操作都会因 `permission denied to set role` 而失败。

然后像其他 Postgres 角色一样，授予此角色访问数据所需的权限。在每个包含节点所用表或函数的数据库中运行以下语句：

```sql
GRANT USAGE ON SCHEMA <schema> TO "<role>";
GRANT SELECT, INSERT, UPDATE, DELETE ON <table> TO "<role>";
GRANT USAGE ON ALL SEQUENCES IN SCHEMA <schema> TO "<role>";
GRANT EXECUTE ON FUNCTION <function>(<argument-types>) TO "<role>";
```

架构级 `USAGE` 权限对除 `public` 外的所有架构都很重要。没有序列授权，向 `serial` 列插入数据时会出现 `permission denied for sequence` 错误。

{% hint style="warning" %}
**不要以项目所有者身份连接**

Databricks 按设计不允许数据库所有者访问 Data API。所有者无法将自己的角色授予 `authenticator`，授权操作会因 `permission denied to grant role` 而失败。请使用不拥有该项目的身份。
{% endhint %}
