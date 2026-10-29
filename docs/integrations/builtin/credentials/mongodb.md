---
title: MongoDB 凭据
description: MongoDB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MongoDB 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: MongoDB 凭据
originalFilePath: integrations/builtin/credentials/mongodb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mongodb
url: https://docs.n8n.io/integrations/builtin/credentials/mongodb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MongoDB 凭据 <a href="#mongodb-credentials" id="mongodb-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [MongoDB](../app-nodes/n8n-nodes-base.mongodb.md)
- [MongoDB Atlas Vector Store（Atlas 向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md)
- [MongoDB Chat Memory（聊天记忆）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [MongoDB](https://www.mongodb.com/) 服务器上创建具有适当权限的用户账户。
- 以项目所有者身份，将全部 [n8n IP 地址](../../../deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses.md)添加到项目 **Network Access**（网络访问）的 IP 访问列表条目中。详细说明，请参阅[添加 IP 访问列表条目](https://www.mongodb.com/docs/atlas/security/ip-access-list/#add-ip-access-list-entries)。

如果从头设置 MongoDB，请创建集群和数据库。详细步骤，请参阅 [MongoDB Atlas 文档](https://www.mongodb.com/docs/atlas/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection - Connection string（数据库连接，连接字符串）
- Database connection - Values（数据库连接，字段值）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MongoDB Atlas 文档](https://www.mongodb.com/docs/atlas/)。

## 使用数据库连接：连接字符串 <a href="#using-database-connection-connection-string" id="using-database-connection-connection-string"></a>

配置此凭据需要满足上述[前置条件](#prerequisites)，然后：

1. 将 **Configuration Type**（配置类型）设为 **Connection String**（连接字符串）。
2. 输入 MongoDB **Connection String**（连接字符串）。在 MongoDB 中，进入 **Database > Connect**（数据库 > 连接）获取此字符串。
    1. 选择 **Drivers**（驱动程序）。
    2. 复制 **Add your connection string into your application code**（将连接字符串添加到应用代码）中显示的代码，格式类似：`mongodb+srv://yourName:yourPassword@clusterName.mongodb.net/?retryWrites=true&w=majority`。
    3. 将连接字符串中的 `<password>` 和 `<username>` 替换为要使用的数据库用户的凭据信息。
    4. 将该连接字符串填入 n8n。
    5. 查找和格式化连接字符串的相关信息，请参阅[连接字符串](https://www.mongodb.com/docs/manual/reference/connection-string/)。
3. 输入 **Database**（数据库）名称，即连接字符串所填用户要登录的数据库的名称。
4. 选择是否 **Use TLS**（使用 TLS）：开启时使用 TLS。必须先将 MongoDB 数据库配置为使用 TLS，并生成 x.509 证书。在 n8n 中添加以下证书字段的信息：
    - **CA Certificate**（CA 证书）
    - **Public Client Certificate**（客户端公钥证书）
    - **Private Client Key**（客户端私钥）
    - **Passphrase**（口令）

使用 x.509 证书的更多信息，请参阅 [MongoDB x.509 文档](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements)。

## 使用数据库连接：字段值 <a href="#using-database-connection-values" id="using-database-connection-values"></a>

配置此凭据需要满足上述[前置条件](#prerequisites)，然后：

1. 将 **Configuration Type**（配置类型）设为 **Values**（字段值）。
2. 输入数据库的 **Host**（主机）名称或地址。
3. 输入 **Database**（数据库）名称。
4. 输入登录使用的 **User**（用户）。
5. 输入该用户的 **Password**（密码）。
6. 输入连接使用的 **Port**（端口），即服务器监听传入连接的端口号。
7. 选择是否 **Use TLS**（使用 TLS）：开启时使用 TLS。必须先将 MongoDB 数据库配置为使用 TLS，并生成 x.509 证书。在 n8n 中添加以下证书字段的信息：
    - **CA Certificate**（CA 证书）
    - **Public Client Certificate**（客户端公钥证书）
    - **Private Client Key**（客户端私钥）
    - **Passphrase**（口令）

使用 x.509 证书的更多信息，请参阅 [MongoDB x.509 文档](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements)。
