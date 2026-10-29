---
title: MySQL 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: MySQL 凭据
originalFilePath: integrations/builtin/credentials/mysql.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mysql
url: https://docs.n8n.io/integrations/builtin/credentials/mysql
description: MySQL 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MySQL 的身份验证。
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


# MySQL 凭据 <a id="mysql-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [MySQL](../app-nodes/n8n-nodes-base.mysql/README.md)
* [Agent（智能体）](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)

{% hint style="info" %}
**Agent 节点用户**

Agent 节点不支持 SSH 隧道。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [MySQL](https://www.mysql.com/) 服务器数据库上创建用户账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MySQL 文档](https://dev.mysql.com/doc/refman/8.3/en/)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据需要：

* 服务器 **Host**（主机）：数据库的主机名或 IP 地址。
* **Database**（数据库）名称。
* **User**（用户）名称。
* 该用户的 **Password**（密码）。
* MySQL 服务器使用的 **Port**（端口）号。
* **Connect Timeout**（连接超时）：初始数据库连接期间，发生超时前等待的毫秒数。
* **SSL**：数据库使用 SSL 时，开启此项，并添加 SSL 证书详情。
* **SSH Tunnel**（SSH 隧道）：选择是否通过 SSH 隧道连接。SSH 隧道允许未加密流量通过加密连接传输，使获授权用户可以远程访问受防火墙保护、无法从外部直接连接的服务器。

设置数据库连接凭据的步骤如下：

1. 将数据库主机名填入 n8n 凭据的 **Host**（主机）。运行以下查询，确认主机名：

    ```
    SHOW VARIABLES WHERE Variable_name = 'hostname';
    ```
2. 将数据库名称填入 n8n 凭据的 **Database**（数据库）。运行以下查询，确认数据库名称：

    ```
    SHOW DATABASES;
    ```
3. 输入数据库中 **User**（用户）的用户名。此用户应具有执行你希望 n8n 完成的各项操作所需的适当权限。
4. 输入该用户的 **Password**（密码）。
5. 输入 MySQL 服务器使用的 **Port**（端口）号（默认值为 `3306`）。运行以下查询，确认端口号：

    ```
    SHOW VARIABLES WHERE Variable_name = 'port';
    ```
6. 输入节点使用的 **Connect Timeout**（连接超时），即初始数据库连接期间，节点在超时前等待的毫秒数。n8n 默认使用 `10000`，即 MySQL 默认的 10 秒。如需匹配数据库的 `connect_timeout`，运行以下查询获取该值，再乘以 1000 后填入 n8n：

    ```
    SHOW VARIABLES WHERE Variable_name = 'connect_timeout';
    ```
7. 如果数据库使用 SSL，且希望连接使用 **SSL**，请在凭据中开启此选项。开启后，在以下字段中输入 MySQL SSL 证书的信息：
   1. 将 `ca.pem` 文件内容填入 **CA Certificate**（CA 证书）字段。
   2. 将 `client-key.pem` 文件内容填入 **Client Private Key**（客户端私钥）字段。
   3. 将 `client-cert.pem` 文件内容填入 **Client Certificate**（客户端证书）字段。
8. 如需使用 **SSH Tunnel**（SSH 隧道）连接，请在凭据中开启此选项；否则跳过。开启后：
   1. 通过 **SSH Authenticate with**（SSH 身份验证方式）选择要建立的 SSH 隧道类型：
      * 如需使用密码连接 SSH，选择 **Password**（密码）。
      * 如需使用身份文件（私钥）和口令连接 SSH，选择 **Private Key**（私钥）。
   2. 输入 **SSH Host**（SSH 主机）。n8n 使用此主机构建以下格式的 SSH URI：`[user@]host:port`。
   3. 输入 **SSH Port**（SSH 端口）。n8n 使用此端口构建以下格式的 SSH URI：`[user@]host:port`。
   4. 输入用于连接的 **SSH User**（SSH 用户）。n8n 使用此用户构建以下格式的 SSH URI：`[user@]host:port`。
   5. 如果 **SSH Authenticate with**（SSH 身份验证方式）选择了 **Password**（密码），请添加 **SSH Password**（SSH 密码）。
   6. 如果 **SSH Authenticate with**（SSH 身份验证方式）选择了 **Private Key**（私钥）：
      1. 添加 SSH 使用的 **Private Key**（私钥）或身份文件内容。这等同于使用 `ssh-identity-file` 选项运行 MySQL 的 `shell-connect()` 命令。
      2. 如果 **Private Key**（私钥）创建时设置了口令，请输入该 **Passphrase**（口令）。这等同于使用 `ssh-identity-pass` 选项运行 MySQL 的 `shell-connect()` 命令。如果私钥没有口令，将此字段留空。

在 MySQL 中使用 SSL 证书的更多信息，请参阅 [MySQL | 创建 SSL 和 RSA 证书及密钥](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-rsa-files.html)；在 MySQL 中使用 SSH 隧道的更多信息，请参阅 [MySQL | 使用 SSH 隧道](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-connection-ssh.html)。
