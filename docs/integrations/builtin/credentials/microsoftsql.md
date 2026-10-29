---
title: Microsoft SQL 凭据
description: Microsoft SQL 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft SQL 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft SQL 凭据
originalFilePath: integrations/builtin/credentials/microsoftsql.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/microsoftsql
url: https://docs.n8n.io/integrations/builtin/credentials/microsoftsql
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft SQL 凭据 <a href="#microsoft-sql-credentials" id="microsoft-sql-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Microsoft SQL](../app-nodes/n8n-nodes-base.microsoftsql.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Microsoft SQL 服务器](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server)数据库上创建用户账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- SQL database connection（SQL 数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

连接该服务的更多信息，请参阅 [Microsoft 连接到 SQL Server 文档](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver16&tabs=sqldb#connect-to-sql-server)。

## 使用 SQL 数据库连接 <a href="#using-sql-database-connection" id="using-sql-database-connection"></a>

配置此凭据需要：

- **Server**（服务器）名称
- **Database**（数据库）名称
- **User**（用户）账户或 ID
- 你的 **Password**（密码）
- 连接使用的 **Port**（端口）
- **Domain**（域）名称
- 是否使用 **TLS**
- 是否 **Ignore SSL Issues**（忽略 SSL 问题）
- **Connect Timeout**（连接超时）
- **Request Timeout**（请求超时）
- 连接使用的 **TDS Version**（TDS 版本）

设置数据库连接的步骤如下：

1. 将 SQL Server 主机名填入 **Server**（服务器）。现有 SQL Server 连接中，主机名位于实例名之前，格式为 `HOSTNAME\INSTANCENAME`。可在以下位置查找主机名：
    - **Object Explorer**（对象资源管理器）窗格中数据库的顶层对象。
    - 查询窗口的页脚。
    - 查看当前连接的 **Properties**（属性），查找 **Name**（名称）或 **Display Name**（显示名称）。
    - 更多信息，请参阅[查找 SQL Server 实例名 | 已连接到 SQL Server 时](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#when-youre-connected-to-sql-server)。也可在[错误日志](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server)中查找。
2. 在 **Database**（数据库）中输入要连接的数据库名称。数据库名称与 SQL Server 实例名不同，不应将实例名作为此字段的值。
    - 如果这些位置都没有显示实例名，则数据库使用默认的 `MSSQLSERVER` 实例名。
3. 输入 **User**（用户）账户名称或 ID。
4. 输入 **Password**（密码）。
5. 对于 **Port**（端口）：
    - SQL Server 默认使用 `1433`。
    - 如果无法通过端口 1433 连接，请在[错误日志](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server)中查找 `Server is listening on`，确定应输入的端口号。
6. 仅当多个域中的用户访问数据库时，才需要输入 **Domain**（域）名称。运行以下 SQL 查询获取域名：

    ```sql
    SELECT DEFAULT_DOMAIN()[DomainName];
    ```

7. 选择是否使用 **TLS**。
8. 选择是否 **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，凭据仍会连接。
9. 在 **Connect Timeout**（连接超时）中输入 n8n 尝试完成初始连接、断开前等待的毫秒数。更多信息，请参阅 [SqlConnection.ConnectionTimeout 属性文档](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectiontimeout)。
    - SQL Server 以秒存储此超时值，n8n 以毫秒存储。如果复制 SQL Server 的默认值，请先乘以 1000，再填入此处。
10. 在 **Request Timeout**（请求超时）中输入 n8n 等待某个请求完成的毫秒数，超过此时长即超时。它本质上是查询超时参数。更多信息，请参阅[排查查询超时错误](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-query-timeouts#explanation)。
11. 从 **TDS Version**（TDS 版本）下拉列表中选择要使用的表格数据流（TDS）协议。如果服务器不支持所选版本，连接会协商使用另一版本。不同 SQL Server 版本及 .NET 框架的 TDS 兼容性详情，请参阅[附录 A：产品行为](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tds/135d0ebe-5c4c-4a94-99bf-1811eccb9f4a)。可选：
    - **7_4 (SQL Server 2012 ~ 2019)**：TDS 版本 7.4。
    - **7_3_B (SQL Server 2008R2)**：TDS 版本 7.3.B。
    - **7_3_A (SQL Server 2008)**：TDS 版本 7.3.A。
    - **7_2 (SQL Server 2005)**：TDS 版本 7.2。
    - **7_1 (SQL Server 2000)**：TDS 版本 7.1。
