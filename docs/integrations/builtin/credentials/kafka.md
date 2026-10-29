---
title: Kafka 凭据
description: Kafka 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Kafka 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Kafka 凭据
originalFilePath: integrations/builtin/credentials/kafka.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/kafka
url: https://docs.n8n.io/integrations/builtin/credentials/kafka
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Kafka 凭据 <a href="#kafka-credentials" id="kafka-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Kafka](../app-nodes/n8n-nodes-base.kafka.md)
- [Kafka Trigger（触发器）](../trigger-nodes/n8n-nodes-base.kafkatrigger.md)

{% hint style="info" %}
**Schema Registry（架构注册表）**

这些凭据用于 Kafka 消息代理的身份验证。如需连接要求身份验证的 Confluent Schema Registry，以对 Avro 消息进行编码和解码，请使用独立的 [Schema Registry 凭据](schemaregistry.md)。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Client ID（客户端 ID）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务使用方法的更多信息，请参阅 [Kafka 文档](https://kafka.apache.org/documentation/)。

如果初次接触 Kafka，初始设置请参阅 [Apache Kafka 快速入门](https://kafka.apache.org/quickstart)。

在 Kafka 中使用 SSL 的方法，请参阅[使用 SSL 加密与身份验证](https://kafka.apache.org/documentation/#security_ssl)。

## 使用客户端 ID <a href="#using-client-id" id="using-client-id"></a>

配置此凭据需要一个正在运行的 Kafka 环境，以及：

- 一个 **Client ID（客户端 ID）**
- 相关 **Brokers**（消息代理）列表
- 如果 Kafka 环境使用身份验证，需要用户名和密码等身份验证信息

设置步骤如下：

1. 在凭据的 **Client ID**（客户端 ID）字段中，输入客户端或消费者组的 `CLIENT-ID`。
2. 以逗号分隔的 `<broker-service-name>:<port>` 格式输入凭据使用的相关 **Brokers**（消息代理）列表。请使用在 `services` 列表中定义消息代理时指定的名称。例如，`kafka-1:9092,kafka-2:9092` 将添加消息代理 `kafka-1` 和 `kafka-2`，端口为 `9092`。
3. 如果 Kafka 环境不使用 SSL，请关闭 **SSL** 开关。
4. 如果在 Kafka 环境中启用了 SASL 身份验证，请开启 **Authentication**（身份验证）开关，然后添加：
    1. **Username**（用户名）
    2. **Password**（密码）
    3. 选择消息代理配置的 **SASL Mechanism**（SASL 机制）。更多信息，请参阅 [SASL 配置](https://kafka.apache.org/documentation/#security_sasl_config)。可选：
        - `Plain`
        - `scram-sha-256`
        - `scram-sha-512`

