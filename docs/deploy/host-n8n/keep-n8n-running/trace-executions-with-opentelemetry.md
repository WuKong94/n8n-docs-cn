---
title: OpenTelemetry 跟踪
description: 将 n8n 的工作流和节点执行跟踪发送到 OpenTelemetry 收集器。
contentType: howto
nodeTitle: 使用 OpenTelemetry 跟踪执行
originalFilePath: hosting/logging-monitoring/opentelemetry.md
originalUrl: https://docs.n8n.io/hosting/logging-monitoring/opentelemetry
url: https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry
layout:
  description:
    visible: false
status: preview
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenTelemetry 跟踪 <a href="#opentelemetry-tracing" id="opentelemetry-tracing"></a>
{% hint style="info" %}
**预览状态**

OpenTelemetry 跟踪自 n8n 2.19.0 起处于预览阶段，未来版本可能更改。请避免在生产工作流中依赖此功能。n8n 计划在后续版本中增加 OpenTelemetry 格式的指标。
{% endhint %}

n8n 可以为工作流和节点执行生成 [OpenTelemetry](https://opentelemetry.io/) 跟踪。使用这些跟踪，可以监控执行延迟、调试故障，并在可观测性系统中跨服务跟踪请求。

观看 n8n OpenTelemetry 跟踪概览：

{% embed url="https://www.youtube.com/embed/xOi8K_-GLRM" %}

## 可获得的内容 <a href="#what-you-get" id="what-you-get"></a>

启用跟踪后，n8n 会为每次执行导出两类 span（跟踪片段）：

- **`workflow.execute`**：每次工作流执行生成一个 span，记录工作流 ID、名称、版本、项目、节点数量、执行模式、状态和错误类型。
- **`node.execute`**：每次节点执行生成一个 span，嵌套在所属工作流 span 中，记录节点 ID、名称、类型、版本、输入和输出条目数量，以及所属执行、工作流和项目。

n8n 在 span 结束时导出它。要在运行仍进行时查看，请启用[开始 span](#start-spans)。

每个 span 都包含用于标识 n8n 实例的资源属性：

- `service.name`，默认为 `n8n`。
- `service.version`，即 n8n 版本。
- `n8n.instance.id`
- `n8n.instance.role`，例如 `main`、`worker` 或 `webhook`。

n8n 也会处理跟踪上下文传播：

- **入站**：如果 webhook 请求包含 [W3C `traceparent` 标头](https://www.w3.org/TR/trace-context/)，n8n 会将其作为工作流 span 的父级，将 n8n 工作流跟踪与上游调用方关联。
- **出站**：HTTP Request 节点及其他使用 n8n HTTP 辅助方法的节点，可以在出站请求中注入 `traceparent` 标头。支持 W3C 跟踪上下文的下游服务即可继续此跟踪。
- **子工作流**：子工作流的 span 使用父工作流的 span 作为父级。
- **恢复的工作流**：工作流从等待中恢复时，新的 span 通过 span link 关联到之前的 span。

## 在界面中启用跟踪 <a href="#enable-tracing-in-the-ui" id="enable-tracing-in-the-ui"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.27.0 起，可以在界面中配置 OpenTelemetry 跟踪。需要实例所有者或管理员身份。
{% endhint %}

可以在 **Settings > OpenTelemetry**（设置 > OpenTelemetry）中配置跟踪，无需设置环境变量。n8n 会直接应用更改，无需重启，并在[队列模式](../configure-n8n/scaling/enable-queue-mode.md)下将配置重新加载到各工作进程和 webhook 处理器。

要配置跟踪：

1. 选择 **Settings > OpenTelemetry**（设置 > OpenTelemetry）。
1. 打开 **Enable OpenTelemetry**（启用 OpenTelemetry）。
1. 在 **Collector connection**（收集器连接）下，填写 **OTLP endpoint**（OTLP 端点）和其他连接信息。
1. 在 **Tracing**（跟踪）下设置采样和 span 选项。
1. 选择 **Save settings**（保存设置）。

要检查 n8n 能否访问收集器，请在 **Verify configuration**（验证配置）下选择 **Send test trace**（发送测试跟踪）。n8n 会发送单个测试 span，并报告收集器是否接受。保存前后都可以测试。

每个字段都对应一个环境变量，字段提示中会显示该变量。完整列表请参阅 [OpenTelemetry 环境变量](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)。

{% hint style="info" %}
**环境变量优先**

如果通过环境变量设置某个选项，n8n 会使用该值，并禁用界面中的对应字段。要从界面管理设置，请不要设置其环境变量。n8n 重启时，环境变量会覆盖界面保存的值。
{% endhint %}

## 通过环境变量启用跟踪 <a href="#enable-tracing-with-environment-variables" id="enable-tracing-with-environment-variables"></a>

在每个需要启用工作流跟踪的 n8n 实例上设置以下环境变量，包括主实例、工作进程和 webhook 处理器：

```bash
export N8N_OTEL_ENABLED=true
export N8N_OTEL_EXPORTER_OTLP_ENDPOINT=http://<your-collector-host>:4318
```

重启 n8n。实例会使用 Protobuf 编码，通过 OTLP HTTP 导出 span。要改用 gRPC 导出，请参阅[选择 OTLP 协议](#choose-the-otlp-protocol)。

n8n 默认会在端点后追加 `/v1/traces`。请将 `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` 指向收集器的基础 URL，而非跟踪路径。端点必须使用 `http://` 或 `https://` URL。如果使用其他协议或未指定协议，n8n 会记录警告并使用默认端点。

如果收集器需要身份验证，请将 `N8N_OTEL_EXPORTER_OTLP_HEADERS` 设为以逗号分隔的 `key=value` 键值对列表：

```bash
export N8N_OTEL_EXPORTER_OTLP_HEADERS="authorization=Bearer <your-token>,x-tenant=acme"

// For added protection - It is recommended to use the `_FILE` postfix if you are putting a token in here:
export N8N_OTEL_EXPORTER_OTLP_HEADERS_FILE=/mnt/otel-headers
```

完整的受支持变量列表，请参阅 [OpenTelemetry 环境变量](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)。

{% hint style="info" %}
**队列模式**

在[队列模式](../configure-n8n/scaling/enable-queue-mode.md)下，必须在所有实例上设置 OpenTelemetry 变量。跟踪上下文会在实例间传播。
{% endhint %}

## 选择 OTLP 协议 <a id="choose-the-otlp-protocol"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.39.0 起，提供 OTLP gRPC 协议、**Protocol**（协议）设置和 `N8N_OTEL_EXPORTER_OTLP_PROTOCOL` 环境变量。
{% endhint %}

n8n 可以通过两种 OTLP 传输方式导出跟踪：

- **`http/protobuf`**，默认选项：通过 HTTP 传输 OTLP，使用 Protobuf 编码。收集器通常在端口 4318 监听。可通过不支持 HTTP/2 的代理、Ingress 和防火墙，调试也更简单。
- **`grpc`**：通过 gRPC 传输 OTLP。收集器通常在端口 4317 监听。HTTP/2 多路复用和二进制分帧降低了每次导出的开销，span 数量很大时差异最明显。此方式要求端到端支持 HTTP/2，部分代理和负载均衡器需要显式配置 HTTP/2。

除非收集器仅接受 gRPC，或你通过支持 HTTP/2 的基础设施导出大量跟踪，否则请保留默认的 `http/protobuf`。

要选择协议，请设置 **Settings > OpenTelemetry**（设置 > OpenTelemetry）中的 **Protocol**（协议）字段，或设置环境变量：

```bash
export N8N_OTEL_EXPORTER_OTLP_PROTOCOL=grpc
```

变量名及其值（`http/protobuf` 和 `grpc`）与上游 [`OTEL_EXPORTER_OTLP_PROTOCOL`](https://opentelemetry.io/docs/specs/otel/protocol/exporter/) 规范一致。与 **Settings > OpenTelemetry** 中的其他字段一样，设置环境变量后，n8n 会禁用 **Protocol** 字段。

### TLS <a id="tls"></a>

两种协议都通过端点 URL 的协议部分控制 TLS。`https://` 启用 TLS，`http://` 禁用 TLS。n8n 不接受 `grpc://` 协议。

要信任自定义证书颁发机构，或提供客户端证书进行双向 TLS（mTLS），请使用上游 OpenTelemetry 变量 `OTEL_EXPORTER_OTLP_CERTIFICATE`、`OTEL_EXPORTER_OTLP_CLIENT_KEY` 和 `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`。对于 `http/protobuf` 协议，`NODE_EXTRA_CA_CERTS` 也有效。n8n 本身没有证书设置。

### gRPC 行为 <a id="grpc-behavior"></a>

`grpc` 协议与 `http/protobuf` 有以下区别：

- **在端点中包含端口。**未显式指定端口的 gRPC 端点会连接到 gRPC 默认端口 443，而非 4317。请写为 `http://<your-collector-host>:4317`。
- **gRPC 端点不包含 URL 路径。**n8n 会忽略 **Trace path**（跟踪路径）设置（`N8N_OTEL_EXPORTER_OTLP_TRACING_PATH`），并在界面中隐藏该行。n8n 保留已保存的值，切回 `http/protobuf` 时会重新应用。
- **自定义标头转换为 gRPC 元数据。**n8n 会将键转为小写。对于 gRPC 拒绝的条目，包括带 `-bin` 后缀但值为文本的键，n8n 会跳过并记录警告，而不是导致启动失败。
- **启动连接检查会等待 gRPC 通道就绪。**通道就绪证明 n8n 能打开 TCP 连接、在 `https://` 下完成 TLS 握手，并建立 HTTP/2 连接，但不能证明端点提供 OTLP。请使用 **Settings > OpenTelemetry** 中的 **Send test trace**（发送测试跟踪），确认收集器收到 span。此检查不会阻止启动。

## 采样 <a href="#sampling" id="sampling"></a>

默认情况下，n8n 导出每条跟踪。要减少繁忙实例的数据量，请将 `N8N_OTEL_TRACES_SAMPLE_RATE` 设为 `0` 到 `1` 之间的值：

```bash
# Export 10% of traces <a href="#export-10percent-of-traces" id="export-10percent-of-traces"></a>
export N8N_OTEL_TRACES_SAMPLE_RATE=0.1
```

n8n 使用基于跟踪 ID 比例的采样器，因此同一跟踪 ID 下的所有 span 要么全部采样，要么全部丢弃。

{% hint style="info" %}
n8n 默认仅为[生产执行](../../../build/understand-workflows/understand-executions/types-of-executions.md)输出跟踪。要为所有工作流执行输出跟踪，请设置 `N8N_OTEL_TRACES_PRODUCTION_ONLY=false`。
{% endhint %}

## 减少 span 数量 <a href="#reduce-span-volume" id="reduce-span-volume"></a>

工作流中的每个节点都会生成自己的 span，节点很多时，产生的数据可能超出需要。要仅导出工作流级 span，请设置：

```bash
export N8N_OTEL_TRACES_INCLUDE_NODE_SPANS=false
```

要停止 n8n 向出站 HTTP 请求注入 `traceparent` 标头，请设置：

```bash
export N8N_OTEL_TRACES_INJECT_OUTBOUND=false
```

## 开始 span <a id="start-spans"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.44.0 起提供开始 span。
{% endhint %}

长时间运行的工作流或节点，在其 span 结束前不会显示在观测后端中。启用开始 span 后，n8n 还会在工作流或节点开始的瞬间发送一个 0 毫秒的子 span。开始 span 携带父 span 在该时刻的相同属性，让你立即知道哪些任务正在运行，以及所属工作流和项目。

| 开始 span | 父级 | 设置 | 环境变量 |
| :--------- | :----- | :------ | :------------------- |
| `workflow.execute.started` | `workflow.execute` | **Send workflow start spans**（发送工作流开始 span） | `N8N_OTEL_TRACES_EMIT_WORKFLOW_START_SPAN` |
| `node.execute.started` | `node.execute` | **Send node start spans**（发送节点开始 span） | `N8N_OTEL_TRACES_EMIT_NODE_START_SPAN` |

两者默认均关闭。可以在 **Settings > OpenTelemetry > Tracing**（设置 > OpenTelemetry > 跟踪）下启用，或将环境变量设为 `true`。节点开始 span 还需要启用 **Include node spans**（包含节点 span，`N8N_OTEL_TRACES_INCLUDE_NODE_SPANS`）。队列模式下，请在主实例和每个工作进程上设置变量。

要使用公共 API，请调用 `PUT /api/v1/settings/otel`，传入 `emitWorkflowStartSpan` 和 `emitNodeStartSpan`，并使用具有 `otel:manage` 权限范围的 API 密钥。此调用会替换所有 OpenTelemetry 设置。缺少必填字段的请求体会被 n8n 拒绝。如果省略可选字段 `exporterProtocol`、`emitWorkflowStartSpan` 或 `emitNodeStartSpan`，n8n 会将其重置为默认值。

## 崩溃的执行 <a id="crashed-executions"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.42.0 起，崩溃的执行也会产生 span。
{% endhint %}

运行执行的 n8n 实例未记录结果就停止时，例如因内存不足被终止或容器被驱逐，执行即处于 `crashed` 状态。n8n 发现执行无法完成后，会将其标记为 `crashed`。在 n8n 2.42.0 之前，这些执行不产生 span，因此跟踪后端的错误率会漏掉所有这类平台故障。自 n8n 2.42.0 起，崩溃的执行会产生一个 `workflow.execute` span。

### 接收崩溃 span <a id="receive-crashed-spans"></a>

span 由发现崩溃的实例发出，而非运行该执行的实例。在[队列模式](../configure-n8n/scaling/enable-queue-mode.md)下，这是主实例，因此需要在主实例启用 OpenTelemetry，不能仅在工作进程启用。常规模式下，单个主实例运行并检查自身执行，因此正常配置即可覆盖。

### 阅读崩溃 span <a id="read-a-crashed-span"></a>

崩溃 span 携带通常的[工作流 span 属性](#workflow-span-workflowexecute)，并增加：

| 属性 | 值 |
| :-------- | :---- |
| `n8n.execution.status` | `crashed` |
| `n8n.execution.error_type` | `WorkflowCrashedError` |
| `n8n.execution.crash.detector` | 哪种检查发现了崩溃。参阅 [n8n 如何检测崩溃](#how-n8n-detects-a-crash)。 |
| `n8n.execution.reconstructed` | n8n 结束原 span 时为 `false`，重建 span 时为 `true`。参阅[跟踪中的 span 与重建的 span](#tracked-and-rebuilt-spans)。 |

span 状态为 error，并带有 `exception` 事件。

### n8n 如何检测崩溃 <a id="how-n8n-detects-a-crash"></a>

| 检测器 | 含义 |
| :------- | :------ |
| `stall` | 队列模式下，工作进程停止续订其作业锁。 |
| `queue-recovery` | 队列模式下，定期检查发现有正在运行的执行，但队列中不存在对应作业。 |
| `startup-recovery` | n8n 重启后，发现执行仍标记为正在运行。 |
| `start-failure` | 执行无法启动。 |
| `workflow-deactivation` | 执行仍在进行时，有人取消发布了工作流。 |

### 跟踪中的 span 与重建的 span <a id="tracked-and-rebuilt-spans"></a>

启动执行的实例会打开其 `workflow.execute` span。如果同一实例检测到崩溃，就直接结束该 span，并设置 `n8n.execution.reconstructed=false`。span 保留启动时设置的全部属性。该实例上仍未结束的节点 span 会以 `n8n.node.termination_reason=workflow_crashed` 结束。

如果由其他实例检测到崩溃，例如主实例已重启，就不存在尚未结束的 span。n8n 会使用执行中存储的跟踪上下文，在同一跟踪中重建一个 `workflow.execute` span，并设置 `n8n.execution.reconstructed=true`。重建的 span 包含工作流 ID、工作流名称、工作流版本 ID、项目 ID、项目和工作流的[自定义 span 属性](#custom-span-attributes)、执行 ID、执行模式、`n8n.execution.is_retry` 和 `n8n.execution.retry_of`，但不包含：

- `n8n.workflow.node_count`.
- 自身的节点 span。崩溃前已导出的节点 span 仍保留在跟踪中，实例停止时正在运行的节点没有 span。
- 执行曾从等待中恢复时，指向之前 span 的 span link。

其工作流自定义属性来自工作流当前设置，而非实际运行的版本。

### 崩溃执行的注意事项 <a id="crashed-execution-caveats"></a>

- **时长表示检测延迟，而非运行时间。**崩溃 span 在 n8n 检测到崩溃时结束，而非实例停止时。对于 `stall`，延迟为一至两分钟；对于 `queue-recovery`，到下次定期检查时才发现；对于 `startup-recovery`，到下次重启时才发现。延迟指标应排除带 `n8n.execution.status=crashed` 的 span，仅在错误率指标中计入它们。
- **重建的 span 会显示父级缺失。**存储的跟踪上下文是原 span 的 ID，而 OpenTelemetry 不能复用 span ID。重建的 span 成为从未结束的 span 的子级，因此 Jaeger 等后端会标记父级缺失。这是预期警告。
- **停滞队列作业的状态发生变化。**在 n8n 2.42.0 之前，工作进程停止的作业以 `error` 结束；自 n8n 2.42.0 起，以 `crashed` 结束，检测器为 `stall`。仅匹配 `n8n.execution.status=error` 的告警会漏掉这些情况。

## 智能体跟踪 <a href="#agent-tracing" id="agent-tracing"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.33.0 起提供智能体跟踪。
{% endhint %}

n8n 也可以为使用 Agents 功能构建的智能体运行生成详细 span，与工作流跟踪使用同一跟踪器。覆盖从工作流、聊天集成和计划任务启动的智能体运行。

{% hint style="warning" %}
**旧版 AI Agent 节点**

本节介绍新 Agents 功能的跟踪。较早的 AI Agent（LangChain）节点与其他节点一样，仅产生标准 `node.execute` span，不生成 `gen_ai.*` 智能体运行或工具调用 span。
{% endhint %}

智能体跟踪依赖 OTel 模块。启用 `N8N_OTEL_ENABLED` 后，添加：

```bash
export N8N_AGENTS_TRACING_ENABLED=true
```

将其设为 `false`，即可保留工作流和节点 span，同时不生成智能体 span。

默认情况下，智能体跟踪会记录提示词、工具参数、响应和工具结果。要排除敏感输入或输出数据：

```bash
export N8N_AGENTS_TRACING_RECORD_INPUTS=false
export N8N_AGENTS_TRACING_RECORD_OUTPUTS=false
```

完整变量列表请参阅 [OpenTelemetry 环境变量](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)。

### 可获得的内容 <a href="#what-you-get-agents" id="what-you-get-agents"></a>

每次智能体运行生成一个根 span，根据是否流式返回响应，命名为 `<agent name>.generate` 或 `<agent name>.stream`。智能体的每次工具调用生成一个嵌套的 `execute_tool <tool name>` span。

这些 span 使用 OpenTelemetry 的 [GenAI 语义约定](https://opentelemetry.io/docs/specs/semconv/gen-ai/)，即 `gen_ai.*` 属性，因此任何 OTLP 后端都能读取，不限于为 LangSmith 构建的工具。

## 自定义 span 属性 <a href="#custom-span-attributes" id="custom-span-attributes"></a>

可以为项目、工作流和节点 span 添加自定义属性。n8n 将每个自定义属性作为 OpenTelemetry span 属性导出到已配置的可观测性后端。

{% hint style="info" %}
**功能可用范围**

自定义 span 属性可用于：

- **自托管：**企业版。

n8n Cloud 不提供此功能。

项目和工作流自定义 span 属性自 n8n 2.24.0 起提供，节点自定义 span 属性自 n8n 2.22.0 起提供。
{% endhint %}

请勿在属性值中包含密钥、个人数据或其他敏感值。

n8n 支持以下自定义属性级别：

| 级别 | 配置位置 | 导出的 span | 默认属性前缀 |
| :---- | :----------- | :------------ | :--------------- |
| 项目 | **Project settings**（项目设置） | `workflow.execute` | `n8n.project.custom.<key>` |
| 工作流 | **Workflow settings**（工作流设置） | `workflow.execute` | `n8n.workflow.custom.<key>` |
| 节点 | 节点的 **Settings**（设置）选项卡 | `node.execute` | `n8n.node.custom.<key>` |

### 添加项目 span 属性 <a href="#add-project-span-attributes" id="add-project-span-attributes"></a>

要添加项目级 span 属性：

1. 打开项目。
1. 选择 **Project settings**（项目设置）。
1. 在 **Custom Span Attributes**（自定义 span 属性）下，添加一个或多个 span 属性。
1. 选择 **Save**（保存）。

项目属性值请使用纯文本。

### 添加工作流 span 属性 <a href="#add-workflow-span-attributes" id="add-workflow-span-attributes"></a>

要添加工作流级 span 属性：

1. 打开工作流。
1. 打开 **Workflow settings**（工作流设置）。
1. 在 **Custom Span Attributes**（自定义 span 属性）下选择 **Configure**（配置）。
1. 添加一个或多个 span 属性。
1. 选择 **Save**（保存）。

工作流属性值请使用纯文本。

### 添加节点 span 属性 <a href="#add-node-span-attributes" id="add-node-span-attributes"></a>

要添加节点级 span 属性：

1. 打开节点，选择 **Settings**（设置）选项卡。
1. 在 **Custom Span Attributes**（自定义 span 属性）下选择 **Add Attribute**（添加属性）。
1. 输入 **Key**（键），键必须为纯文本。
1. 输入 **Value**（值），可以是纯文本或表达式，例如 `={{ $json.environment }}`。

节点属性值必须解析为字符串、数字或布尔值。

### 在自定义节点中通过代码添加属性 <a href="#add-attributes-programmatically-in-a-custom-node" id="add-attributes-programmatically-in-a-custom-node"></a>

如果正在[构建自定义节点](../../../connect/create-nodes/overview.md)，可以通过代码添加自定义键值对。调用 `setMetadata`，位置是节点的 `execute` 方法：

```typescript
async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
	this.setMetadata({
		tracing: {
			'llm.model': 'gpt-4o',
			'llm.token.input': 1500,
			'llm.token.output': 340,
		},
	});

	return [this.getInputData()];
}
```

默认情况下，n8n 为每个键添加 `n8n.node.custom.` 前缀。可以[更改属性前缀](#change-the-attribute-prefixes)。值必须为字符串、数字或布尔值。

Code 节点不能使用此 API。此 API 面向希望用领域相关数据丰富 span 的节点作者。

如果节点通过此方式设置的属性键，也配置为[自定义节点 span 属性](#add-node-span-attributes)，则代码设置的值优先。

### 更改属性前缀 <a id="change-the-attribute-prefixes"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.46.0 起提供自定义属性前缀。
{% endhint %}

n8n 会为自定义属性键添加前缀。要更改或移除前缀，请将 `N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES` 设为 JSON 对象。此对象接受以下键，每个键的值都为字符串：

| 键 | 设置哪类属性的前缀 | 默认前缀 |
| :-- | :------------------ | :------------- |
| `project` | 项目属性 | `n8n.project.custom.` |
| `workflow` | 工作流属性 | `n8n.workflow.custom.` |
| `node` | 节点属性 | `n8n.node.custom.` |

空字符串会移除前缀。省略的键保留默认前缀。请在主实例、工作进程和 webhook 处理器上设置相同的值。

要移除这两个前缀，使属性名称与界面中输入的名称完全一致：

```bash
# A project attribute named team becomes team
export N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES='{"project":"","node":""}'
```

设置自定义前缀：

```bash
# A project attribute named team becomes acme.project.team
export N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES='{"project":"acme.project.","node":"acme.node."}'
```

仅更改一个前缀：

```bash
# A project attribute named team becomes acme.team
# Node attributes keep their default prefix
export N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES='{"project":"acme."}'
```

如果值不是有效 JSON、使用其他键，或存在非字符串值，n8n 会记录警告，并在所有级别使用默认前缀。

{% hint style="warning" %}
**OpenTelemetry 标准属性**

n8n 不会将自定义键与 [OpenTelemetry 语义约定](https://opentelemetry.io/docs/specs/semconv/)对照检查。如果键与标准属性匹配，例如 `user.id` 或 `http.request.method`，后端会将你的值作为该属性读取。除非值符合标准含义，否则请避免使用标准键。
{% endhint %}

## 使用 Jaeger 试用 <a href="#try-it-out-with-jaeger" id="try-it-out-with-jaeger"></a>

可以将跟踪发送到本地 [Jaeger](https://www.jaegertracing.io/) 实例，查看实际效果。

1. 将以下内容保存为 `docker-compose.yml`：

```yaml
services:
  jaeger:
    image: jaegertracing/jaeger:latest
    ports:
      - "16686:16686" # UI
      - "4317:4317"   # OTLP gRPC
      - "4318:4318"   # OTLP HTTP
```

2. 启动 Jaeger：

```bash
docker compose up -d
```

3. 启用跟踪，将目标指向 Jaeger，然后启动 n8n。设置详情请参阅[启动 n8n](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md)：

```bash
N8N_OTEL_ENABLED=true N8N_OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4318 n8n start
```

5. 运行工作流，然后在 [http://localhost:16686](http://localhost:16686) 打开 Jaeger 界面。选择“n8n”作为 service（服务），点击“Find traces”（查找跟踪），查看 n8n 生成的 OpenTelemetry 跟踪。

## Span 属性 <a href="#span-attributes" id="span-attributes"></a>

工作流和节点 span 包含以下 n8n 专用属性。

### 工作流 span（`workflow.execute`）<a href="#workflow-span-workflowexecute" id="workflow-span-workflowexecute"></a>

| 属性 | 说明 |
| :-------- | :---------- |
| `n8n.workflow.id` | 工作流 ID。 |
| `n8n.workflow.name` | 工作流名称。 |
| `n8n.workflow.version_id` | 工作流版本 ID。 |
| `n8n.workflow.node_count` | 工作流中的节点数量。崩溃执行的[重建 span](#tracked-and-rebuilt-spans) 中不包含。 |
| `n8n.project.id` | 项目 ID，自 n8n 2.23.0 起提供。 |
| `n8n.project.name` | 项目名称。仅用于团队项目：个人项目名称包含所有者姓名和邮箱，因此 n8n 不包含此值。自 n8n 2.44.0 起提供。 |
| `n8n.execution.id` | 执行 ID。 |
| `n8n.execution.mode` | 执行模式，例如 `manual`、`webhook`、`trigger`、`retry`。 |
| `n8n.execution.status` | 最终执行状态，包括[崩溃执行](#crashed-executions)的 `crashed`。 |
| `n8n.execution.is_retry` | 执行为重试时，值为 `true`。 |
| `n8n.execution.retry_of` | 执行为重试时，记录原始执行 ID。 |
| `n8n.execution.error_type` | 错误类名，执行失败时设置；崩溃时为 `WorkflowCrashedError`。 |
| `n8n.execution.crash.detector` | 发现崩溃的检查：`stall`、`queue-recovery`、`startup-recovery`、`start-failure` 或 `workflow-deactivation`。参阅 [n8n 如何检测崩溃](#how-n8n-detects-a-crash)。自 n8n 2.42.0 起提供。 |
| `n8n.execution.reconstructed` | n8n 在崩溃后重建 span 时为 `true`，结束原 span 时为 `false`。参阅[跟踪中的 span 与重建的 span](#tracked-and-rebuilt-spans)。自 n8n 2.42.0 起提供。 |
| `n8n.continuation.reason` | 工作流从等待中恢复时，在 span link 上设置。 |
| `n8n.project.custom.<key>` | 通过[项目级自定义 span 属性](#custom-span-attributes)设置的自定义属性。 |
| `n8n.workflow.custom.<key>` | 通过[工作流级自定义 span 属性](#custom-span-attributes)设置的自定义属性。 |

### 节点 span（`node.execute`）<a href="#node-span-nodeexecute" id="node-span-nodeexecute"></a>

| 属性 | 说明 |
| :-------- | :---------- |
| `n8n.node.id` | 节点 ID。 |
| `n8n.node.name` | 节点名称。 |
| `n8n.node.type` | 节点类型，例如 `n8n-nodes-base.httpRequest`。 |
| `n8n.node.type_version` | 节点类型版本。 |
| `n8n.node.items.input` | 节点收到的输入条目数量。 |
| `n8n.node.items.output` | 节点生成的输出条目数量。 |
| `n8n.node.termination_reason` | 节点 span 未正常完成就结束的原因，例如 `workflow_cancelled` 或 `workflow_crashed`。 |
| `n8n.node.custom.<key>` | 在节点设置中通过[节点级自定义 span 属性](#custom-span-attributes)，或在自定义节点代码中通过 `metadata.tracing` 设置的自定义属性。 |

自 n8n 2.44.0 起，节点 span 还包含 `n8n.execution.id`、`n8n.workflow.id`、`n8n.workflow.name`、`n8n.project.id` 和 `n8n.project.name`，值与所属工作流 span 相同。要在 Jaeger 中查找某次执行的全部 span，请搜索标签 `n8n.execution.id=<execution-id>`。

节点失败时，n8n 会在 span 上记录 `exception` 事件，并包含标准 OpenTelemetry 异常属性（`exception.type`、`exception.message`、`exception.stacktrace`）。

### 智能体运行 span（`<agent name>.generate` 或 `<agent name>.stream`）<a href="#agent-run-span" id="agent-run-span"></a>

| 属性 | 说明 |
| :-------- | :---------- |
| `gen_ai.operation.name` | 始终为 `invoke_agent`。 |
| `gen_ai.agent.name` | 智能体名称。 |
| `gen_ai.request.model` | 已知时记录模型 ID，格式为 `<provider>/<model name>`。 |
| `gen_ai.conversation.id` | 对话线程 ID。 |
| `gen_ai.prompt` | 序列化提示词、工具数量和工具目录。`N8N_AGENTS_TRACING_RECORD_INPUTS` 为 `false` 时省略。 |
| `agent_id` | 智能体 ID。 |
| `project_id` | 项目 ID。 |
| `thread_id` | 对话线程 ID。 |
| `source` | 运行启动的来源，例如 `workflow` 或聊天集成名称。 |
| `user_id` | 已知时记录用户 ID。 |
| `model_id` | 已知时记录模型 ID，格式为 `<provider>/<model name>`。 |
| `execution_id` | 由工作流触发的运行所对应的执行 ID。 |
| `workflow_id` | 由工作流触发的运行所对应的工作流 ID。 |
| `node_id` | 由工作流触发的运行所对应的节点 ID。 |

### 工具调用 span（`execute_tool <tool name>`）<a href="#tool-call-span" id="tool-call-span"></a>

| 属性 | 说明 |
| :-------- | :---------- |
| `gen_ai.operation.name` | 始终为 `execute_tool`。 |
| `gen_ai.tool.name` | 工具名称。 |
| `gen_ai.tool.call.id` | 工具调用 ID。 |
| `gen_ai.agent.name` | 智能体名称。 |
| `gen_ai.tool.call.arguments` | 工具调用参数。`N8N_AGENTS_TRACING_RECORD_INPUTS` 为 `false` 时省略。 |
| `gen_ai.tool.call.result` | 工具调用结果。`N8N_AGENTS_TRACING_RECORD_OUTPUTS` 为 `false` 时省略。 |

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 后端未显示任何跟踪 <a href="#no-traces-appear-in-your-backend" id="no-traces-appear-in-your-backend"></a>

如果 n8n 启动时无法访问 OTLP 端点，会记录以下错误：

```
Failed to connect to OpenTelemetry OTLP endpoint during startup
```

请检查：

- `N8N_OTEL_ENABLED` 已设为 `true`。
- `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` 指向收集器的基础 URL，而非 `/v1/traces` 路径。
- n8n 容器或主机能访问收集器。
- 已设置所有必需的 `N8N_OTEL_EXPORTER_OTLP_HEADERS`，例如身份验证令牌。

如果使用 `grpc` 协议，还需检查端点是否显式包含端口。未指定时，n8n 连接端口 443，而非 4317。

n8n 默认以 `warn` 级别记录 OpenTelemetry 诊断信息。设置 `N8N_LOG_LEVEL=debug` 可查看更详细的信息。

### 使用 gRPC 和私有 CA 时出现启动连接错误 <a id="startup-connectivity-error-with-grpc-and-a-private-ca"></a>

`grpc` 协议的启动连接检查使用默认 TLS 信任库，不读取 `OTEL_EXPORTER_OTLP_CERTIFICATE`、`OTEL_EXPORTER_OTLP_CLIENT_KEY` 或 `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE`，但导出器会采用这些变量。使用私有证书颁发机构，或要求 mTLS 的收集器，可能出现检查失败并记录 `Failed to connect to OpenTelemetry OTLP endpoint during startup`，但实际导出正常。此检查不会阻止启动。请在 **Settings > OpenTelemetry** 中使用 **Send test trace**（发送测试跟踪），确认收集器收到 span。

### 缺少自定义 span 属性 <a href="#custom-span-attributes-are-missing" id="custom-span-attributes-are-missing"></a>

请检查：

- 你拥有 Enterprise 许可证。
- 已将 `N8N_OTEL_ENABLED` 设为 `true`。
- 对于节点级 span 属性，`N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` 未设为 `false`。
- 如果设置了 `N8N_OTEL_TRACES_CUSTOM_ATTRIBUTE_PREFIXES`，请搜索新键。n8n 会丢弃与内置属性匹配的键。参阅[更改属性前缀](#change-the-attribute-prefixes)。

### 崩溃的执行没有 span <a id="a-crashed-execution-has-no-span"></a>

请在主实例启用 OpenTelemetry。队列模式下，由主实例检测崩溃并发出 span，因此仅在工作进程启用不会生成崩溃 span。请在所有类型的实例上设置相同变量，使工作进程 span 保留父级上下文。

实例停止时正在运行的节点没有 span。崩溃前已导出的节点 span 仍保留在跟踪中。参阅[崩溃的执行](#crashed-executions)。

### 重建的 span 显示父级缺失警告 <a id="a-rebuilt-span-shows-a-missing-parent-warning"></a>

n8n 使用执行中存储的跟踪上下文重建 span。该上下文是从未结束的原 span 的 ID，而 OpenTelemetry 不能复用 span ID。因此，重建的 span 成为后端从未收到的 span 的子级。这是预期警告。span 带有 `n8n.execution.reconstructed=true`。参阅[注意事项](#crashed-execution-caveats)。

### 工作进程跟踪缺少父级上下文 <a href="#worker-traces-are-missing-parent-context" id="worker-traces-are-missing-parent-context"></a>

队列模式下，工作进程从数据库读取父级跟踪上下文。如果仅在主实例设置 OpenTelemetry 环境变量，工作进程 span 就无法关联到父工作流跟踪。请在所有类型的实例上设置相同变量。

### 没有智能体 span <a href="#no-agent-spans-appear" id="no-agent-spans-appear"></a>

智能体 span 依赖 OTel 模块。请检查：

- `N8N_OTEL_ENABLED` 已设为 `true`。
- `N8N_AGENTS_TRACING_ENABLED` 已设为 `true`。

当 `N8N_OTEL_ENABLED` 设为 `false` 时，智能体运行正常完成，但 n8n 不为其生成 span，即使 `N8N_AGENTS_TRACING_ENABLED` 已设为 `true`。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

- [保持 n8n 运行](./)
- [n8n 日志](set-up-logging.md)
- [监控](monitor-n8n.md)
- [使用 Grafana 可视化指标](visualize-metrics-with-grafana.md)
- [备份与恢复](backup-and-restore.md)
- [更新 n8n](update-n8n.md)
- [OpenTelemetry 环境变量](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)
- [W3C Trace Context 规范](https://www.w3.org/TR/trace-context/)
- [OpenTelemetry Collector 文档](https://opentelemetry.io/docs/collector/)
