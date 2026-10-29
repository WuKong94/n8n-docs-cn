---
title: Oracle Database 凭据
contentType:
- integration
- reference
priority: high
nodeTitle: Oracle Database 凭据
originalFilePath: integrations/builtin/credentials/oracledb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/oracledb
url: https://docs.n8n.io/integrations/builtin/credentials/oracledb
description: Oracle Database 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Oracle Database 的身份验证。
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


# Oracle Database 凭据 <a id="oracle-database-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [OracleDB](../app-nodes/n8n-nodes-base.oracledb.md)
* [Agent（智能体）](../cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md)
* [Oracle Database Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md)
* [Embeddings Oracle Database（嵌入模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md)

{% hint style="info" %}
这些节点不支持 SSH 隧道，要求 Oracle Database **19c 或更高版本**。使用透明应用连续性（TAC）和分片等 Oracle Database 高级功能时，还需要 Oracle Client Libraries **19c 或更高版本**。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Oracle Database](https://www.oracle.com/pls/topic/lookup?ctx=dblatest\&id=GUID-F0246961-558F-480B-AC0F-14B50134621C) 服务器上创建用户账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Oracle Database 文档](https://docs.oracle.com/en/database/oracle/oracle-database)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据需要：

* **User**（用户）名称。
* 该用户的 **Password**（密码）。
* **Connection String**（连接字符串）：要连接的 Oracle Database 实例，可使用 Easy Connect 字符串、tnsnames.ora 文件中的 TNS 别名，或 Oracle Database 实例。
* **Use Optional Oracle Client Libraries**（使用可选的 Oracle 客户端库）：如需使用 Oracle Database 高级功能，请开启此项。它在内部使用 node-oracledb Thick 模式，还需要额外设置才能启用该模式。更多信息，请参阅[启用 Thick 模式文档](https://node-oracledb.readthedocs.io/en/latest/user_guide/initialization.html#enabling-node-oracledb-thick-mode)。官方 n8n Docker 镜像不提供此选项。
* **Use SSL**（使用 SSL）：连接字符串使用 SSL 时，开启此项，并配置 SSL 身份验证的其他详情。
* **Wallet Password**（钱包密码）：用于解密采用隐私增强邮件（PEM）编码且已加密的私有证书的密码。
* **Wallet Content**（钱包内容）：与 Oracle Database 建立双向 TLS（mTLS）连接所需的安全凭据。
* **Distinguished Name**（可分辨名称）：应与证书 DN 匹配的可分辨名称（DN）。
* **Match Distinguished Name**（匹配可分辨名称）：是否在常规证书验证之外，额外匹配服务器证书 DN。
* **Allow Weak Distinguished Name Match**（允许弱可分辨名称匹配）：是否执行同时检查监听器和服务器证书的安全 DN 匹配行为。
* **Pool Min**（连接池最小连接数）：创建连接池时，与数据库建立的连接数量。
* **Pool Max**（连接池最大连接数）：连接池可增长到的最大连接数量。
* **Pool Increment**（连接池增量）：连接请求超过当前已打开的连接数量时，每次新打开的连接数量。
* **Pool Maximum Session Life Time**（连接池会话最大生命周期）：连接自首次创建起，可在池中存在的最长时间，单位为秒。
* **Pool Connection Idle Timeout**（连接池空闲连接超时）：池中连接空闲多少秒后可被终止。
* **Connection Class Name**（连接类名称）：DRCP/PRCP 连接类。更多信息，请参阅[启用 DRCP](https://docs.oracle.com/en/database/oracle/oracle-database/26/admin/managing-processes.html#GUID-BB76E57C-3F16-4C85-AEF6-BA14FC1B4777)。
* **Connection Timeout**（连接超时）：应用建立 Oracle Net 连接的超时时长，单位为秒。
* **Transport Connection Timeout**（传输连接超时）：等待建立到数据库主机的连接的最长秒数。
* **Keepalive Probe Interval**（保活探测间隔）：发送保活探测之间的分钟数。

设置数据库连接凭据的步骤如下：

1. 将数据库用户名填入 n8n 凭据的 **User**（用户）。
2. 输入该用户的 **Password**（密码）。
3. 将数据库连接字符串填入 n8n 凭据的 **Connection String**（连接字符串）。
4. 如果数据库使用 SSL，且希望为连接配置 **SSL**，请在凭据中开启此选项。开启后，在以下字段输入 Oracle Database SSL 证书的信息：
   1. 如果有钱包密码，请填入 **Wallet Password**（钱包密码）字段。
   2. 在 **Wallet Content**（钱包内容）字段的 Expanded（展开）布局中，输入 PEM 编码钱包文件 **ewallet.pem** 的内容，以保留钱包文件中的全部空白字符。直接粘贴到 **Wallet Content** 字段会移除空白字符，导致连接错误。

使用 TLS 连接的更多信息，请参阅 [node-oracledb](https://node-oracledb.readthedocs.io/en/latest/user_guide/connection_handling.html#mutual-tls-connections-to-oracle-cloud-autonomous-database)。
