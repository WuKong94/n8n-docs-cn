---
description: 在 terraform-aws-n8n 模块中配置 S3 执行数据、Prometheus 指标、OpenTelemetry 追踪、日志流和外部密钥。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 AWS 上配置企业功能 <a id="configure-enterprise-features-on-aws"></a>

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 模块提供 Terraform 输入，为 AWS 部署接入多项 n8n 企业功能。本页介绍每项功能在该模块中的专属设置。有关功能的用途和使用方法，请参阅链接中的 n8n 功能页面。

## S3 中的执行数据 <a id="execution-data-in-s3"></a>

{% hint style="info" %}
**功能可用范围**

将执行数据存储到 S3，需要 n8n 2.27.0 或更高版本，以及具有 `feat:executionDataS3` 授权权益的 Enterprise 许可证。
{% endhint %}

模块始终将 n8n 的二进制数据保存在 S3 中。从 n8n 2.27.0 开始，还可以将执行数据卸载到同一存储桶，而不是 PostgreSQL，以减轻大规模运行时的数据库写入压力：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_execution_data_storage_mode = "s3" # default: "database"
  n8n_image_tag                   = "2.27.4"
}
```

只有新执行会写入 S3，不会回填旧数据。切换回原模式，也不会影响已按任一模式写入的数据。有关 n8n 如何使用外部存储，请参阅[使用外部存储](../../../configure-n8n/scaling/use-external-storage.md)。

{% hint style="warning" %}
**S3 执行数据不会自动备份**

与 PostgreSQL 不同，模块不会对 S3 存储桶启用版本控制或备份。如果需要保留执行历史，请自行向存储桶（`s3_bucket_name` 输出）添加 S3 版本控制或复制规则。
{% endhint %}

如果添加生命周期规则，请仅将范围限定为二进制数据对象。n8n 会根据执行数据清理设置，自行清理 S3 中的执行数据；不要为执行数据添加生命周期规则，否则可能删除 n8n 仍在引用的数据。

## Prometheus 指标 <a id="prometheus-metrics"></a>

设置 `n8n_metrics_enabled = true`，在 `/metrics` 路径暴露 n8n 内置 Prometheus 端点，端口为 `5678`，也是 Chart 用于界面和 API 的端口。暴露内容请参阅[启用 Prometheus 指标](../../../configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics.md)。模块不会配置采集：请向 `n8n-main` Service 添加采集注解；如果运行 Prometheus Operator，则可创建 `ServiceMonitor`。

在多主实例拓扑中，n8n 自身的 `/metrics` 端点不能报告可用的 Bull 队列深度。设置 `redis_exporter_enabled = true`，在 Release 旁部署 [redis_exporter](https://github.com/oliver006/redis_exporter)，将队列深度作为 `redis_key_size{key="<prefix>:jobs:wait"}` 和 `redis_key_size{key="<prefix>:jobs:active"}` 暴露在 `9121` 端口上。这与 KEDA 扩缩容工作进程所使用的队列深度相同。

## OpenTelemetry 追踪 <a id="opentelemetry-tracing"></a>

{% hint style="info" %}
**预览状态**

n8n 中的 OpenTelemetry 追踪可能更改，不建议在生产环境中使用。
{% endhint %}

设置 `n8n_otel_enabled = true`，在每个 n8n 容器上开启工作流和节点追踪。将 `n8n_otel_exporter_otlp_endpoint` 指向 OpenTelemetry Collector 的基础 URL（n8n 会自行追加 `/v1/traces`）：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_otel_enabled                = true
  n8n_otel_exporter_otlp_endpoint = "http://otel-collector.observability.svc.cluster.local:4318"
}
```

模块不会部署 Collector。请单独部署，例如使用上游 `open-telemetry/opentelemetry-collector` Helm Chart。可用调整变量和 n8n 追踪内容，请参阅[使用 OpenTelemetry 追踪执行](../../../keep-n8n-running/trace-executions-with-opentelemetry.md)。

## 日志流 <a id="log-streaming"></a>

{% hint style="info" %}
**功能可用范围**

日志流需要 n8n 2.19.0 或更高版本，以及 Enterprise 许可证。
{% endhint %}

设置 `n8n_log_streaming_managed_by_env = true`，通过 Terraform 而不是界面配置[日志流](../../../../../administer/observe-and-log/stream-logs-to-external-systems.md)目标：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_log_streaming_managed_by_env = true
  n8n_log_streaming_destinations = [
    {
      type             = "webhook"
      label            = "Audit events"
      enabled          = true
      subscribedEvents = ["n8n.audit", "n8n.workflow"]
      url              = "https://hooks.example.com/n8n"
      method           = "POST"
    },
  ]
}
```

n8n 会在每次启动时重新应用这些目标，界面中的日志流设置将变为只读。将 `n8n_log_streaming_managed_by_env` 改回 `false`，会保留最后应用的目标，同时恢复界面编辑权限。

## 外部密钥 <a id="external-secrets"></a>

n8n 的[外部密钥](../../../../../administer/manage-credentials/use-external-secret-stores.md)功能在运行时从外部保管库解析工作流凭据值。它需要具有 `feat:externalSecrets` 授权权益的 Enterprise 许可证，且默认开启（`n8n_external_secrets_enabled = true`）；设置为 `false` 后，即使许可证包含此功能，也会将其禁用。

无论哪种情况，都需要在 n8n 界面（**Settings（设置）** > **External Secrets（外部密钥）**）中手动连接保管库提供方。Terraform 无法创建此连接。模块能做的是，向 n8n Pod 的 Pod Identity 角色授予特定 AWS Secrets Manager 密钥的读取权限，让你在界面中选择自动检测凭据，而不必粘贴静态 IAM 用户密钥：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_external_secrets_aws_enabled      = true
  n8n_external_secrets_aws_secret_names = ["prod/n8n/stripe", "prod/n8n/hubspot"]
}
```

`n8n_external_secrets_aws_secret_names` 是必填项，不接受通配符：请显式列出每个密钥名称，因为 n8n 的 AWS Secrets Manager 集成没有其他方式限制可读取的密钥。

## 凭据覆盖 <a id="credential-overwrites"></a>

[凭据覆盖](../../../../../administer/manage-credentials/credential-overwrites.md)允许预配置共享凭据字段，并向用户隐藏它们。通过自行管理的 Kubernetes Secret 提供 JSON 内容，并使用 `n8n_credentials_overwrite_secret_ref` 引用：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_credentials_overwrite_secret_ref = {
    name = kubernetes_secret_v1.credentials_overwrite.metadata[0].name
  }
}
```

n8n 只在启动时读取一次此文件。轮换 Secret 内容后，请重启主、工作进程和 Webhook 处理器 Deployment，以加载变更。

## 相关资源 <a id="related-resources"></a>

* [使用 Terraform 部署到 AWS](./)
* [在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)
* [在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)
* [自定义 AWS 基础设施](customize-the-infrastructure.md)
* [维护和拆除 AWS 部署](maintain-and-tear-down.md)
* [使用外部存储](../../../configure-n8n/scaling/use-external-storage.md)
