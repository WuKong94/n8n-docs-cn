---
title: Postgres 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Postgres 凭据
originalFilePath: integrations/builtin/credentials/postgres.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/postgres
url: https://docs.n8n.io/integrations/builtin/credentials/postgres
description: Postgres 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Postgres 的身份验证。
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


# Postgres 凭据 <a id="postgres-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Postgres](../app-nodes/n8n-nodes-base.postgres/README.md)
* [Agent（智能体）](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)
* [Postgres Chat Memory（聊天记忆）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md)
* [PGVector Vector Store（PGVector 向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md)

{% hint style="info" %}
**Agent 节点用户**

Agent 节点不支持 SSH 隧道。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 Postgres 服务器上[创建用户账户](https://www.postgresql.org/docs/current/sql-createuser.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Postgres 文档](https://www.postgresql.org/docs/16/index.html)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据需要：

* 服务器的 **Host**（主机）或域名。
* **Database**（数据库）名称。
* **User**（用户）名称。
* 用户 **Password**（密码）。
* **Ignore SSL Issues**（忽略 SSL 问题）：设置 SSL 验证失败时，凭据是否仍进行连接。
* **SSL**：选择连接是否使用 SSL。
* 连接使用的 **Port**（端口）号。
* **SSH Tunnel**（SSH 隧道）：选择是否使用 SSH，加密与 Postgres 服务器之间的网络连接。

设置数据库连接的步骤如下：

1. 输入 Postgres 服务器的 **Host**（主机）或域名。可运行 `/conninfo` 命令确认主机名，也可运行以下查询：

    ```
    SELECT inet_server_addr();
    ```
2. 输入 **Database**（数据库）名称。运行 `/conninfo` 命令可确认数据库名称。
3. 输入要用于连接的用户的 **User**（用户）名称。
4. 输入该用户的 **Password（密码）**。
5. **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 验证失败，凭据仍会连接。
6. **SSL**：选择连接是否使用 SSL。更多信息，请参阅 Postgres 的 [SSL 支持](https://www.postgresql.org/docs/16/libpq-ssl.html)。可选：
   * **Allow**（允许）：将 `ssl-mode` 参数设为 `allow`。先尝试非 SSL 连接，失败后再尝试 SSL 连接。
   * **Disable**（禁用）：将 `ssl-mode` 参数设为 `disable`，仅尝试非 SSL 连接。
   * **Require**（要求）：将 `ssl-mode` 参数设为 `require`，仅尝试 SSL 连接。如果存在根 CA 文件，则验证服务器证书是否由可信的证书颁发机构（CA）签发。
7. 输入连接使用的 **Port**（端口）号。可运行 `/conninfo` 命令确认主机名，也可运行以下查询：

    ```
    SELECT inet_server_port();
    ```
8. **SSH Tunnel**（SSH 隧道）：开启此设置，通过 SSH 连接数据库。使用 SSH 的相关指引，请参阅 [SSH 隧道限制](postgres.md#ssh-tunnel-limitations)。开启后，需要：
   1. 通过 **SSH Authenticate with**（SSH 身份验证方式）选择要建立的 SSH 隧道类型：
      * 如需使用密码连接 SSH，选择 **Password**（密码）。
      * 如需使用身份文件（私钥）和口令连接 SSH，选择 **Private Key**（私钥）。
   2. 将要连接的远程绑定地址填入 **SSH Host**（SSH 主机）。
   3. **SSH Port**（SSH 端口）：输入 SSH 隧道的本地端口号。
   4. **SSH Postgres Port**（SSH Postgres 端口）：输入隧道远端数据库服务器使用的端口号。
   5. **SSH User**（SSH 用户）：输入登录使用的用户名。
   6. 如果 SSH Authenticate with（SSH 身份验证方式）选择了 **Password**（密码），请添加该用户的 **SSH Password**（SSH 密码）。
   7. 如果 **SSH Authenticate with**（SSH 身份验证方式）选择了 **Private Key**（私钥）：
      1. 添加 SSH 使用的 **Private Key**（私钥）或身份文件的内容。
      2. 如果 **Private Key**（私钥）创建时设置了口令，请输入该 **Passphrase**（口令）。如果 **Private Key**（私钥）没有口令，将此字段留空。

更多信息，请参阅[使用 SSH 隧道的安全 TCP/IP 连接](https://www.postgresql.org/docs/16/ssh-tunnels.html)。

### SSH 隧道限制 <a href="#ssh-tunnel-limitations" id="ssh-tunnel-limitations"></a>

仅在满足以下条件时使用 **SSH Tunnel**（SSH 隧道）设置：

* 此凭据用于 [Postgres](../app-nodes/n8n-nodes-base.postgres/README.md) 节点（Agent 节点不支持 SSH 隧道）。
* SSH 服务器与 Postgres 服务器运行在同一台机器上。
* 你具有可通过 `ssh` 登录的用户账户。
