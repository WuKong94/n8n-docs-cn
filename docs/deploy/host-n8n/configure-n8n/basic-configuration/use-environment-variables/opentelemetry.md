---
title: OpenTelemetry 环境变量
description: 通过环境变量配置自托管 n8n 实例的 OpenTelemetry 追踪。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: OpenTelemetry
originalFilePath: hosting/configuration/environment-variables/opentelemetry.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/opentelemetry
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenTelemetry 环境变量 <a href="#opentelemetry-environment-variables" id="opentelemetry-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

n8n 可以通过 OTLP，将工作流和节点执行追踪导出到 OpenTelemetry 收集器。详情请参阅 [OpenTelemetry 追踪](../../../keep-n8n-running/trace-executions-with-opentelemetry.md)。

| 变量 | 类型 | 默认值 | 说明 | 起始版本 |
| :------- | :--- | :------ | :---------- | :------
| `N8N_OTEL_ENABLED` | Boolean | `false` | 是否启用 OpenTelemetry 追踪。设为 `false` 时，n8n 不加载 OpenTelemetry SDK。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` | String | `http://localhost:4318` | 接收导出追踪的 OTLP 端点基础 URL，必须为 `http://` 或 `https://` URL，否则 n8n 会记录警告并使用默认值。对于 `http/protobuf`，n8n 会将 `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` 的值追加到此 URL。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_PROTOCOL` | String | `http/protobuf` | 导出追踪所用的 OTLP 传输协议，可选值为 `http/protobuf` 和 `grpc`。名称和值与上游 [`OTEL_EXPORTER_OTLP_PROTOCOL`](https://opentelemetry.io/docs/specs/otel/protocol/exporter/) 规范一致。选择方法请参阅[选择 OTLP 协议](../../../keep-n8n-running/trace-executions-with-opentelemetry.md#choose-the-otlp-protocol)。 | 2.39.0 |
| `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` | String | `/v1/traces` | 导出追踪时追加到 `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` 的路径。`N8N_OTEL_EXPORTER_OTLP_PROTOCOL` 为 `grpc` 时，n8n 忽略此变量，因为 gRPC 端点不使用 URL 路径。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_HEADERS` | String | - | 每次 OTLP 请求发送的 HTTP 请求头，以逗号分隔的 `key=value` 键值对表示。可用于身份验证令牌或租户请求头，例如 `authorization=Bearer <token>,x-tenant=acme`。使用 `grpc` 协议时，n8n 将其作为 gRPC 元数据发送，并把键转换为小写。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_SERVICE_NAME` | String | `n8n` | 导出的 span 中，`service.name` 资源属性的值。 | 2.19.0 |
| `N8N_OTEL_TRACES_SAMPLE_RATE` | Number | `1.0` | 导出追踪的比例，介于 `0` 和 `1` 之间。n8n 按追踪 ID 比例采样，因此同一追踪中的所有 span 会一起被采样或丢弃。 | 2.19.0 |
| `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` | Boolean | `true` | 是否为每次节点执行生成 `node.execute` span。设为 `false`，仅导出工作流级 span。 | 2.19.0 |
| `N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES` | String | - | 用于修改或移除自定义 span 属性键前缀的 JSON 对象，例如 `{"project":"","node":""}`。参阅[更改属性前缀](../../../keep-n8n-running/trace-executions-with-opentelemetry.md#change-the-attribute-prefixes)。 | 2.46.0 |
| `N8N_OTEL_TRACES_EMIT_WORKFLOW_START_SPAN` | Boolean | `false` | 是否在工作流执行开始时发送时长为 0 毫秒的 `workflow.execute.started` span。参阅[开始 span](../../../keep-n8n-running/trace-executions-with-opentelemetry.md#start-spans)。 | 2.44.0 |
| `N8N_OTEL_TRACES_EMIT_NODE_START_SPAN` | Boolean | `false` | 是否在节点执行开始时发送时长为 0 毫秒的 `node.execute.started` span。需要将 `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` 设为 `true`。参阅[开始 span](../../../keep-n8n-running/trace-executions-with-opentelemetry.md#start-spans)。 | 2.44.0 |
| `N8N_OTEL_TRACES_PRODUCTION_ONLY` | Boolean | `true` | 是否仅导出[生产执行](../../../../../build/understand-workflows/understand-executions/types-of-executions.md)的追踪。设为 `false`，导出所有工作流执行的追踪。 | 2.25.2 |
| `N8N_OTEL_TRACES_INJECT_OUTBOUND` | Boolean | `true` | 是否向使用 n8n HTTP 辅助函数的节点发出的出站 HTTP 请求中，注入 W3C `traceparent`/`tracesstate` 请求头。 | 2.19.0 |
| `N8N_OTEL_STARTUP_CONNECTIVITY_TIMEOUT_MS` | Number | `2000` | 启动时检查 OTLP 端点连接的超时，单位为毫秒。期限内无法访问端点时，n8n 会记录错误。 | 2.19.0 |
| `N8N_AGENTS_TRACING_ENABLED` | Boolean | `true` | 智能体运行是否生成 OpenTelemetry span。继承 `N8N_OTEL_*` 的端点、请求头、采样和传输设置。配置 OTel 提供商前，span 没有发送目标；如需只追踪工作流，不生成智能体 span，可将此变量设为 `false`。 | 2.33.0 |
| `N8N_AGENTS_TRACING_RECORD_INPUTS` | Boolean | `true` | 智能体追踪是否记录提示词、工具参数等输入。设为 `false`，从追踪中排除敏感输入数据。 | 2.33.0 |
| `N8N_AGENTS_TRACING_RECORD_OUTPUTS` | Boolean | `true` | 智能体追踪是否记录响应、工具结果等输出。设为 `false`，从追踪中排除敏感输出数据。 | 2.33.0 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
