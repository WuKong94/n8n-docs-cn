---
title: Snowflake 凭据
description: Snowflake 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Snowflake 的身份验证。
contentType:
- integration
- reference
nodeTitle: Snowflake 凭据
originalFilePath: integrations/builtin/credentials/snowflake.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/snowflake
url: https://docs.n8n.io/integrations/builtin/credentials/snowflake
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Snowflake 凭据 <a href="#snowflake-credentials" id="snowflake-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Snowflake](../app-nodes/n8n-nodes-base.snowflake.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Snowflake](https://www.snowflake.com/en/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [Password（密码）](#using-password-authentication)
- [Key-pair（密钥对）](#using-key-pair-authentication)
- [OAuth2](#using-oauth2-authentication)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Snowflake API 文档](https://docs.snowflake.com/en/api-reference)和 [SQL 命令参考](https://docs.snowflake.com/en/sql-reference-commands)。

## 通用配置字段 <a href="#common-configuration-fields" id="common-configuration-fields"></a>

两种身份验证方式都需要以下字段：

- **Account**（账户）名称：Snowflake URL 中位于 `https://` 与 `snowflakecomputing.com` 之间的字符串。例如，Snowflake 账户 URL 为 `https://abc.eu-central-1.snowflakecomputing.com` 时，账户名称为 `abc.eu-central-1`。
- **Database**（数据库）：输入此凭据应连接的[数据库](https://docs.snowflake.com/en/sql-reference/sql/use-database)名称。
- **Warehouse**（仓库）：输入连接后会话使用的默认虚拟[仓库](https://docs.snowflake.com/en/sql-reference/sql/use-warehouse)名称。n8n 使用此仓库执行查询、加载数据等操作。
- **Schema**（架构）：输入连接后使用的[架构](https://docs.snowflake.com/en/sql-reference/sql/use-schema)。
- **Role**（角色）：输入连接后使用的安全[角色](https://docs.snowflake.com/en/sql-reference/sql/use-role)。
- **Client Session Keep Alive**（客户端会话保活）：默认情况下，客户端连接通常在最近一次执行查询的三到四小时后超时。开启此设置会将 `clientSessionKeepAlive` 参数设为 true：即使不执行查询，服务器也会无限期保持客户端连接。

这些设置的更多信息，请参阅[会话命令](https://docs.snowflake.com/en/sql-reference/commands-session)。

## 使用密码身份验证 <a href="#using-password-authentication" id="using-password-authentication"></a>

除[通用配置字段](#common-configuration-fields)外，密码身份验证还需要：

- 一个 **Username（用户名）**
- 一个 **Password（密码）**

## 使用密钥对身份验证 <a href="#using-key-pair-authentication" id="using-key-pair-authentication"></a>

密钥对身份验证可替代基于密码的身份验证，提供更高安全性，使用公钥和私钥对进行验证。

除[通用配置字段](#common-configuration-fields)外，密钥对身份验证还需要：

- **Username**（用户名）：已为其分配公钥的 Snowflake 用户。
- **Private Key**（私钥）：PEM 格式（PKCS#8）的私钥。应包含私钥文件的完整内容，包括 `-----BEGIN ENCRYPTED PRIVATE KEY-----` 和 `-----END ENCRYPTED PRIVATE KEY-----` 分隔标记（未加密密钥则为 `-----BEGIN PRIVATE KEY-----` 和 `-----END PRIVATE KEY-----`）。
- **Passphrase**（口令，可选）：私钥已加密时，输入用于加密的口令；使用未加密私钥时，将此字段留空。

生成和配置密钥对的更多信息，请参阅 [Snowflake 密钥对身份验证文档](https://docs.snowflake.com/en/user-guide/key-pair-auth)。

## 使用 OAuth2 身份验证 <a id="using-oauth2-authentication"></a>

OAuth2 身份验证使用独立的 **Snowflake OAuth2 API** 凭据，需要先在 Snowflake 中设置 OAuth 安全集成。

使用 `ACCOUNTADMIN` 角色，或具有 `CREATE INTEGRATION` 权限的角色，在 Snowflake 中运行以下命令：

```sql
CREATE SECURITY INTEGRATION n8n_oauth_integration
  TYPE = OAUTH
  ENABLED = TRUE
  OAUTH_CLIENT = CUSTOM
  OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
  OAUTH_REDIRECT_URI = '<your-redirect-url>'
  OAUTH_ALLOW_NON_TLS_REDIRECT_URI = TRUE
  OAUTH_ISSUE_REFRESH_TOKENS = TRUE
  OAUTH_REFRESH_TOKEN_VALIDITY = 7776000
  OAUTH_USE_SECONDARY_ROLES = IMPLICIT
  OAUTH_ENFORCE_PKCE = TRUE;
```

将 `<your-redirect-url>` 替换为 n8n 凭据显示的 **OAuth Redirect URL**（OAuth 重定向 URL）。通过 HTTPS 连接时，可移除 `OAUTH_ALLOW_NON_TLS_REDIRECT_URI` 行。

然后获取客户端 ID 和密钥：

```sql
SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('N8N_OAUTH_INTEGRATION');
```

更多信息，请参阅 Snowflake 的[自定义客户端 OAuth](https://docs.snowflake.com/en/user-guide/oauth-custom)文档。

除 **Role**（角色）以外的通用配置字段外，OAuth2 身份验证还需要：

- **Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）：来自上方创建的安全集成。

如需快速查找 Account、Warehouse 和 Schema 的值，在 Snowflake 中选择用户名，进入 **Account**（账户），为目标账户选择 **View Account Details**（查看账户详情）。选择 **Config File**（配置文件），再选择 **Warehouse**（仓库）和 **Schema**（架构），即可查看所需连接详情。

在 n8n 中选择 **Connect my account**（连接我的账户），开始 OAuth2 流程。n8n 会重定向到 Snowflake，供你登录并授权应用，然后携带令牌重定向回 n8n。

OAuth2 凭据没有独立的 **Role**（角色）字段，n8n 会在 OAuth 作用域中请求角色。默认作用域为 `refresh_token session:role:SYSADMIN`，因此 Snowflake 用户必须获授 `SYSADMIN` 角色。如果用户具有其他角色，或需要额外作用域，请在连接前开启 **Custom Scopes**（自定义作用域），编辑 **Enabled Scopes**（已启用的作用域），将 `session:role:SYSADMIN` 替换为该用户获授角色对应的 `session:role:<your-role>`。移除默认作用域可能导致节点无法正常工作。