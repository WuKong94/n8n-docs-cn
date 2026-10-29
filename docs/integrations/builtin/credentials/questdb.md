---
title: QuestDB 凭据
description: QuestDB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 QuestDB 的身份验证。
contentType:
- integration
- reference
nodeTitle: QuestDB 凭据
originalFilePath: integrations/builtin/credentials/questdb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/questdb
url: https://docs.n8n.io/integrations/builtin/credentials/questdb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# QuestDB 凭据 <a href="#questdb-credentials" id="questdb-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [QuestDB](../app-nodes/n8n-nodes-base.questdb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [QuestDB](https://questdb.io/) 实例上创建用户账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [QuestDB 文档](https://questdb.io/docs)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据需要：

- **Host**（主机）：输入服务器的主机名或 IP 地址。
- **Database**（数据库）：输入数据库名称，例如 `qdb`。
- 一个 **User**（用户）：输入用户账户的用户名，其配置项为 `pg.user` 或 `pg.readonly.user`，位于 `server.conf` 中。默认值为 `admin`。
- 一个 **Password**（密码）：输入用户账户的密码，其配置项为 `pg.password` 或 `pg.readonly.password`，位于 `server.conf` 中。默认值为 `quest`。
- **SSL**：选择连接是否使用 SSL，此项设置 `sslmode` 参数。可选：
    - **Allow**（允许）
    - **Disable**（禁用）
    - **Require**（要求）
- **Port**（端口）：输入连接使用的端口号，默认为 `8812`。

更多信息请参阅[支持的连接属性列表](https://questdb.io/docs/reference/api/postgres/#list-of-supported-connection-properties)。
