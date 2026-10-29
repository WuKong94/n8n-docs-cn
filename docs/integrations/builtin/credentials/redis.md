---
title: Redis 凭据
description: Redis 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Redis 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Redis 凭据
originalFilePath: integrations/builtin/credentials/redis.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/redis
url: https://docs.n8n.io/integrations/builtin/credentials/redis
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Redis 凭据 <a href="#redis-credentials" id="redis-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Redis](../app-nodes/n8n-nodes-base.redis.md)
- [Redis Chat Memory（聊天记忆）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)
- [Redis Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Redis 开发者文档](https://redis.readthedocs.io/en/stable/index.html)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

你需要一个 [Redis](https://redis.io/) 服务器上的用户账户，以及：

- 一个 **Password（密码）**
- **Host**（主机）名称
- **Port**（端口）号
- **Database Number**（数据库编号）
- **SSL**

配置此凭据的步骤如下：

1. 输入用户账户的 **Password**（密码）。
2. 输入 Redis 服务器的 **Host**（主机）名称，默认值为 `localhost`。
3. 输入连接使用的 **Port**（端口）号，默认值为 `6379`。
    - 此编号应与 `tcp_port` 一致，该值列于 `INFO` 命令的输出中。
4. 输入 **Database Number**（数据库编号），默认值为 `0`。
5. 如果连接应使用 SSL，请开启 **SSL** 开关。关闭时，连接仅使用 TCP。
6. 启用 **SSL** 后，可选择 **disable TLS verification**（禁用 TLS 验证），以便使用自签名证书。警告：这样会降低连接的安全性。

更多信息，请参阅[连接到 Redis | 通用客户端](https://redis.readthedocs.io/en/stable/connections.html)。
