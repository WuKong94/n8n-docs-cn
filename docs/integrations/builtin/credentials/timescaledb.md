---
title: TimescaleDB 凭据
description: TimescaleDB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 TimescaleDB 的身份验证。
contentType:
- integration
- reference
nodeTitle: TimescaleDB 凭据
originalFilePath: integrations/builtin/credentials/timescaledb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/timescaledb
url: https://docs.n8n.io/integrations/builtin/credentials/timescaledb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TimescaleDB 凭据 <a href="#timescaledb-credentials" id="timescaledb-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [TimescaleDB](../app-nodes/n8n-nodes-base.timescaledb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

一个可用的 [TimescaleDB](https://www.timescale.com/) 实例。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Timescale 文档](https://docs.timescale.com/)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据需要：

- **Host**（主机）：TimescaleDB 服务器的完全限定服务器名称或 IP 地址。
- **Database**（数据库）：要连接的数据库名称。
- 一个 **User**（用户）：要用于登录的用户名。
- 一个 **Password**（密码）：输入所连接数据库用户的密码。
- **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，n8n 仍会连接，此时不会显示 **SSL** 选择器。
- **SSL**：此设置控制连接的 `ssl-mode` 连接字符串，可选：
    - **Allow**（允许）：将 `ssl-mode` 参数设为 `allow`。先尝试非 SSL 连接，失败后再尝试 SSL 连接。
    - **Disable**（禁用）：将 `ssl-mode` 参数设为 `disable`，仅尝试非 SSL 连接。
    - **Require**（要求）：将 `ssl-mode` 参数设为 `require`，这是 TimescaleDB 连接字符串的默认值。仅尝试 SSL 连接。如果存在根 CA 文件，则验证服务器证书是否由可信的证书颁发机构（CA）签发。
- **Port**（端口）：TimescaleDB 服务器的端口号。

非 SSL 字段的更多信息，请参阅 [Timescale 连接设置文档](https://docs.tigerdata.com/integrations/latest/find-connection-details/)。SSL 选项的更多信息，请参阅[使用更严格的 SSL 连接](https://docs.tigerdata.com/use-timescale/latest/security/strict-ssl/)。
