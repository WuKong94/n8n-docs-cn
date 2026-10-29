---
title: AMQP 凭据
description: AMQP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 AMQP 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: AMQP 凭据
originalFilePath: integrations/builtin/credentials/amqp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/amqp
url: https://docs.n8n.io/integrations/builtin/credentials/amqp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AMQP 凭据 <a href="#amqp-credentials" id="amqp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [AMQP Sender（发送器）](../app-nodes/n8n-nodes-base.amqp.md)
- [AMQP Trigger（触发器）](../trigger-nodes/n8n-nodes-base.amqptrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

安装兼容 AMQP 1.0 的消息代理，例如 [ActiveMQ](https://activemq.apache.org/)。可选产品列表，请参阅 [AMQP 产品](https://www.amqp.org/about/examples.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- AMQP connection（连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

高级消息队列协议（AMQP）是面向消息的中间件所使用的开放标准应用层协议，主要特性包括面向消息、队列、路由、可靠性及安全性。更多信息，请参阅 [OASIS AMQP 1.0 版本标准](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html)。

有关该服务的更多信息，请参阅提供商的文档，例如 [ActiveMQ API 文档](https://activemq.apache.org/components/classic/documentation/rest)。

## 使用 AMQP 连接 <a href="#using-amqp-connection" id="using-amqp-connection"></a>

配置此凭据需要：

- **Hostname**（主机名）：输入 AMQP 消息代理的主机名。
- **Port**（端口）：输入连接使用的端口号。
- **User**（用户）：输入建立连接时使用的用户名。
    - 例如，ActiveMQ 的默认用户名为 `admin`。
- **Password**（密码）：输入该用户的密码。
    - 例如，ActiveMQ 的默认密码为 `admin`。
- _可选：_ **Transport Type**（传输类型）：输入 `tcp` 或 `tls`。

更详细的说明，请参阅提供商的文档。
