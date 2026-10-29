---
title: RabbitMQ 凭据
description: RabbitMQ 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 RabbitMQ 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: RabbitMQ 凭据
originalFilePath: integrations/builtin/credentials/rabbitmq.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/rabbitmq
url: https://docs.n8n.io/integrations/builtin/credentials/rabbitmq
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# RabbitMQ 凭据 <a href="#rabbitmq-credentials" id="rabbitmq-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [RabbitMQ](../app-nodes/n8n-nodes-base.rabbitmq.md)
- [RabbitMQ Trigger（触发器）](../trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- User connection（用户连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [RabbitMQ 连接文档](https://www.rabbitmq.com/docs/connections)。

## 使用用户连接 <a href="#using-user-connection" id="using-user-connection"></a>

配置此凭据需要已安装的 [RabbitMQ 消息代理](https://www.rabbitmq.com/)，以及：

1. 输入 RabbitMQ 消息代理的 **Hostname**（主机名）。
2. 输入连接使用的 **Port**（端口）。
3. 输入连接用于登录的 **User**（用户）。
    - 默认值为 `guest`。RabbitMQ 建议生产环境使用其他用户。更多信息，请参阅[访问控制 | 基础知识](https://www.rabbitmq.com/docs/access-control#basics)。如果使用 `guest` 账户进行非 localhost 连接，排查方法请参阅下方的 [`guest` 用户问题](#guest-user-issues)。
4. 输入该用户的 **Password（密码）**。
    - `guest` 用户的默认密码为 `guest`。
5. 将连接使用的[虚拟主机](https://www.rabbitmq.com/docs/vhosts)填入 **Vhost**，默认虚拟主机为 `/`。
6. 选择连接是否使用 **SSL**。开启时，还需要设置：
    - **Passwordless**（无密码）：选择是否使用基于证书的无密码连接，即 SASL 机制 EXTERNAL。开启时，还需输入：
        - **Client Certificate**（客户端证书）：粘贴要使用的 SSL 客户端证书文本。
        - **Client Key**（客户端密钥）：粘贴要使用的 SSL 客户端密钥。
        - **Passphrase**（口令）：粘贴要使用的 SSL 口令。
    - **CA Certificates**（CA 证书）：粘贴要使用的 SSL CA 证书文本。

## guest 用户问题 <a href="#guest-user-issues" id="guest-user-issues"></a>

如果在凭据中使用 `guest` 用户并尝试访问远程主机，可能遇到连接错误。RabbitMQ 日志中会显示类似以下内容的错误：

    [error] <0.918.0> PLAIN login refused: user 'guest' can only connect via localhost

这是因为 RabbitMQ 禁止默认 `guest` 用户从远程主机连接，该用户只能通过 `localhost` 连接。

解决此错误的方法包括：

- 更新 `guest` 用户，允许其访问远程主机。
- 创建或使用其他用户连接远程主机。只有 `guest` 用户默认受此限制。

更多信息，请参阅 [guest 用户只能从 localhost 连接](https://www.rabbitmq.com/docs/access-control#loopback-users)。

