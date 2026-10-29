---
title: Schema Registry 凭据
description: Schema Registry 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Schema Registry 的身份验证。
contentType:
- integration
- reference
priority: medium
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Schema Registry 凭据 <a id="schema-registry-credentials"></a>

启用 **Use Schema Registry**（使用 Schema Registry）时，这些凭据可用于以下节点的身份验证：

- [Kafka](../app-nodes/n8n-nodes-base.kafka.md)
- [Kafka Trigger（触发器）](../trigger-nodes/n8n-nodes-base.kafkatrigger.md)

Kafka 节点和 Kafka Trigger 使用 Schema Registry 对 Avro 消息进行编码和解码。此凭据与 [Kafka 凭据](kafka.md)分开：注册表具有独立的端点和身份验证，与 Kafka 消息代理不同。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- None（无）
- Basic Auth（基本身份验证，用户名和密码），例如 Confluent Cloud Schema Registry 的 API key 和 secret

## 相关资源 <a id="related-resources"></a>

有关该服务使用方法的更多信息，请参阅 [Confluent Schema Registry 文档](https://docs.confluent.io/platform/current/schema-registry/index.html)。

## 设置凭据 <a id="setting-up-the-credential"></a>

配置此凭据需要 Schema Registry 的 URL；如果要求身份验证，还需要相应访问凭据。

1. 在 **URL** 字段中输入 Schema Registry 的基础 URL，例如 `https://psrc-xxxxx.region.aws.confluent.cloud`。
2. 选择 **Authentication**（身份验证）方式：
    - **None**（无）：用于不要求身份验证的 Schema Registry。
    - **Basic Auth**（基本身份验证）：用于要求 HTTP 基本身份验证的 Schema Registry，例如 Confluent Cloud。然后添加：
        1. **Username**（用户名）：对于 Confluent Cloud，此值是 Schema Registry API key。
        2. **Password**（密码）：对于 Confluent Cloud，此值是 Schema Registry API secret。
3. 选择 **Save**（保存）。n8n 会调用注册表的 `/subjects` 端点，测试凭据。

使用此凭据时，打开 Kafka 或 Kafka Trigger 节点，启用 **Use Schema Registry**（使用 Schema Registry），然后选择该凭据。