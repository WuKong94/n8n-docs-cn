---
contentType: reference
nodeTitle: 选择 n8n 的数据库
originalFilePath: hosting/configuration/supported-databases-settings.md
originalUrl: https://docs.n8n.io/hosting/configuration/supported-databases-settings
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 支持的数据库 <a href="#supported-databases" id="supported-databases"></a>

n8n 默认使用 SQLite 保存凭据、历史执行记录和工作流，也支持 PostgresDB。n8n 的 PostgreSQL 版本支持策略请参阅[支持的 PostgreSQL 版本](#supported-postgresql-versions)。

## 不同 n8n 安装方式使用的数据库类型 <a href="#database-type-by-n8n-installation" id="database-type-by-n8n-installation"></a>

数据库类型取决于 n8n 的安装方式：

### 自托管 n8n <a href="#self-hosted-n8n" id="self-hosted-n8n"></a>
自托管安装默认使用 **SQLite**。也可以通过相应环境变量配置 PostgreSQL，参阅 [PostgresDB 配置](#postgresdb)。

### n8n Cloud <a href="#n8n-cloud" id="n8n-cloud"></a>

n8n Cloud 根据套餐层级使用不同的数据库：

- **SQLite**：Starter、Pro 和旧版 Enterprise 套餐。
- **PostgreSQL**：仅 Enterprise Scaling 套餐。

## 共享设置 <a href="#shared-settings" id="shared-settings"></a>

以下环境变量适用于所有数据库：

 - `DB_TABLE_PREFIX`（默认值：-）— 表名前缀。

## PostgresDB <a href="#postgresdb" id="postgresdb"></a>

### 支持的 PostgreSQL 版本 <a href="#supported-postgresql-versions" id="supported-postgresql-versions"></a>

n8n 支持：

- 最新的两个仍受积极维护的 PostgreSQL 大版本，截至 2026 年 7 月为 **17** 和 **18**。
- 额外支持一个大版本以保持兼容，即 **16**。

请运行所用大版本下的最新小版本。

Amazon Aurora PostgreSQL 属于**实验性支持**。n8n 的托管模板为高可用部署提供了此选项，因为主数据库故障时 Aurora 恢复更快。但 n8n 不对 Aurora 进行测试或认证，PostgreSQL 版本支持范围也不适用于 Aurora。除非明确需要 Aurora 的特性，否则请使用上游 PostgreSQL。

n8n 不支持其他兼容 PostgreSQL 的衍生产品，例如 AlloyDB、CockroachDB 或 YugabyteDB。

PostgreSQL 项目每年 11 月会停止维护最旧的大版本，并发布新版本，因此 n8n 支持的版本范围每年会调整。请在本页查看当前支持的版本，不要仅依赖在其他地方看到的特定版本号。

要使用 PostgresDB，可以提供以下环境变量：

 - `DB_TYPE=postgresdb`
 - `DB_POSTGRESDB_DATABASE`（默认值：'n8n'）
 - `DB_POSTGRESDB_HOST`（默认值：'localhost'）
 - `DB_POSTGRESDB_PORT`（默认值：5432）
 - `DB_POSTGRESDB_USER`（默认值：'postgres'）
 - `DB_POSTGRESDB_PASSWORD`（默认值：空）
 - `DB_POSTGRESDB_SCHEMA`（默认值：'public'）
 - `DB_POSTGRESDB_SSL_CA`（默认值：undefined）：用于验证连接的服务器 CA 证书路径，不支持机会式加密。
 - `DB_POSTGRESDB_SSL_CERT`（默认值：undefined）：客户端 TLS 证书路径。
 - `DB_POSTGRESDB_SSL_KEY`（默认值：undefined）：与证书对应的客户端私钥路径。
 - `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`（默认值：true）：是否拒绝验证失败的 TLS 连接。

```bash
export DB_TYPE=postgresdb
export DB_POSTGRESDB_DATABASE=n8n
export DB_POSTGRESDB_HOST=postgresdb
export DB_POSTGRESDB_PORT=5432
export DB_POSTGRESDB_USER=n8n
export DB_POSTGRESDB_PASSWORD=n8n
export DB_POSTGRESDB_SCHEMA=n8n

# optional: <a href="#optional" id="optional"></a>
export DB_POSTGRESDB_SSL_CA_FILE=$(pwd)/ca.crt
export DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false

n8n start
```

### 所需权限 <a href="#required-permissions" id="required-permissions"></a>

n8n 需要创建和修改其所用数据表的结构。

建议授予以下权限：

```sql
CREATE DATABASE n8n-db;
CREATE USER n8n-user WITH PASSWORD 'random-password';
GRANT ALL PRIVILEGES ON DATABASE n8n-db TO n8n-user;
```

### TLS <a href="#tls" id="tls"></a>

可以选择以下配置：

- 不声明，采用默认配置：以 `SSL=off` 连接。
- 仅声明 CA 和 unauthorized 标志：以 `SSL=on` 连接，并验证服务器签名。
- 在上述配置基础上声明 `_{CERT,KEY}`：使用证书和密钥进行客户端 TLS 身份验证。

## SQLite <a href="#sqlite" id="sqlite"></a>

未指定数据库时，默认使用 SQLite。

数据库文件位于：
`~/.n8n/database.sqlite`

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
