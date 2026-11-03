---
description: 为 terraform-aws-n8n 模块使用自己的 VPC、数据库、缓存或集群，分离入口流量，或使用自定义 n8n 镜像。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义 AWS 基础设施 <a id="customize-the-aws-infrastructure"></a>

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 模块可以创建部署的每一层，也可以连接已有基础设施。本页介绍主要自定义方式：连接现有基础设施、分离入口流量，以及使用自定义 n8n 镜像。

## 客户管理的基础设施 <a id="customer-managed-infrastructure"></a>

模块可以创建的每一层，都可以改为连接已有基础设施。各层遵循相同模式：一个 `create_<x>` 布尔值（默认为 `true`），用于停止模块创建该层，以及仅当其设为 `false` 时必需的一个或多个引用输入。

| 层 | 开关 | 引用输入 |
|---|---|---|
| RDS PostgreSQL | `create_database` | `db_host`、`db_password`（或 `db_password_secret_ref`） |
| EKS 集群和节点组 | `create_eks` | `existing_eks_cluster_name`、`existing_eks_cluster_prerequisites_confirmed` |
| ElastiCache Redis | `create_elasticache` | `redis_host`、`redis_port`、`redis_auth_token`（或 `redis_auth_token_secret_ref`）、`redis_transit_encryption_enabled` |
| S3 存储桶 | `create_s3_bucket` | `existing_s3_bucket_name` |
| RDS KMS 密钥 | `create_db_kms_key` | `db_kms_key_arn` |
| S3 KMS 密钥 | `create_s3_kms_key` | `s3_kms_key_arn` |
| 集群控制器（负载均衡器控制器、Cluster Autoscaler、metrics-server、KEDA） | `install_lbc` / `install_cluster_autoscaler` / `install_metrics_server` / `install_keda` | 无；假定现有集群中已经运行对应组件 |

例如，要让模块使用已经管理的 Redis 实例：

```hcl
module "n8n" {
  # ...
  create_elasticache = false
  redis_host         = aws_elasticache_replication_group.shared.primary_endpoint_address
  redis_port         = 6379
  redis_auth_token   = var.shared_redis_auth_token
}
```

{% hint style="warning" %}
**同时设置开关和对应引用输入**

只设置 `redis_host` 等引用输入，而未将对应的 `create_<x>` 布尔值设为 `false`，不会报错：模块仍会创建自己的托管资源并让 n8n 使用它，而你提供的基础设施不会被使用。务必同时设置两者。
{% endhint %}

如果两个 n8n 部署使用同一 Redis 主机，请为每个部署设置唯一的 `redis_key_prefix`。否则两个部署会共享队列和领导者选举通道，在一个实例上激活工作流时，可能导致另一个实例出现 `webhook not registered` 错误。

各类客户管理基础设施的可运行参考配置，位于模块的 [examples](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples) 文件夹（`customer-managed-redis`、`customer-managed-s3`、`customer-managed-cluster` 和 `customer-managed-everything`）。

{% hint style="info" %}
**模块始终不负责创建 VPC**

模块始终要求提供现有 VPC（`vpc_id`、`private_subnets`、`public_subnets`），绝不会创建 VPC。
{% endhint %}

## 客户管理的入口 <a id="customer-managed-ingress"></a>

默认情况下，模块创建一个面向互联网的应用程序负载均衡器，将 `/webhook` 路由到 Webhook 处理器，将 `/` 路由到主 Pod。设置 `create_ingress = false` 后，可以自行管理入口，例如将公开 Webhook 流量与仅内部可访问的编辑器和 API 分离。

将流量路由到模块通过输出暴露的 Service：

| 输出 | 提供的服务 |
|---|---|
| `n8n_service_name` | 编辑器界面、REST API |
| `n8n_webhook_service_name` | Webhook、表单、等待恢复、MCP |
| `n8n_webhook_path_prefixes` | 必须由 Webhook 处理器接收的路径前缀 |
| `n8n_service_port` | 两者（`5678`） |

将 `n8n_webhook_path_prefixes` 中的每个前缀都路由到 Webhook 处理器，而不只是 `/webhook`：模块在主 Pod 上禁用了生产 Webhook 处理，因此 `/webhook-waiting`（等待节点恢复）、`/form` 和 `/form-waiting`（Form Trigger 节点）以及 `/mcp`（MCP 服务器触发器）如果被路由到主 Pod，都会返回 404。请在兜底的 `/` 规则之前声明这些前缀。

自行管理的入口还需要：

- 对 `n8n_service_name` **启用会话粘性**，让每个浏览器始终连接同一个主 Pod。否则同一浏览器的编辑器请求和 WebSocket 连接会分散到不同主 Pod，导致编辑器断开连接。
- **设置 `n8n_proxy_hops`**，其值为客户端与 n8n 之间会添加 `X-Forwarded-For` 请求头的代理数量。模块默认设为 `1`；如果模块或你自己的负载均衡器是唯一代理，该值就是正确的。对于路径中的每个额外 HTTP 代理（例如 CloudFront），都要加一。

包含证书和两条 DNS 记录的完整可运行分离入口示例，见 [`examples/split-ingress`](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/split-ingress)。

## 自定义 n8n 镜像 <a id="custom-n8n-images"></a>

设置 `n8n_image_repository`，让 Helm Release 使用自行构建的镜像，替代默认 n8n 镜像。常见原因包括使用内部基础镜像，或将社区节点预装到镜像中：

```hcl
module "n8n" {
  # ...other inputs...

  n8n_image_repository = "123456789012.dkr.ecr.eu-west-1.amazonaws.com/n8n"
  n8n_image_tag        = "2.27.4-mypackages"

  # Pin to the n8n version the custom image is built from.
  n8n_task_runner_image_tag = "2.27.4"

  # Not needed when packages are already in the image.
  n8n_reinstall_missing_packages = false
}
```

{% hint style="warning" %}
**通过界面安装的社区包不会直接从自定义镜像中加载**

n8n 只会从 `N8N_CUSTOM_EXTENSIONS` 指定的目录加载社区节点，而不会仅因执行 `npm install`、将包安装到镜像的 `node_modules` 中就加载。请将 `n8n_custom_extensions_path` 设为镜像中实际安装包的目录，并在 Dockerfile 中将包安装到该目录。以这种方式加载的节点还会被重命名为 `CUSTOM.*` 类型，因此使用通过界面安装的同一包创建的已有工作流，需要更新节点类型才能解析。
{% endhint %}

如果每次修改包都重建镜像不切实际，可以通过 `n8n_extra_volumes` 和 `n8n_extra_volume_mounts`，从 ConfigMap、Secret 或持久卷声明挂载同一目录，而不是将其打包进镜像。

## 大规模 Pod 的 DNS <a id="pod-dns-at-scale"></a>

`n8n_dns_config` 用于设置 n8n Pod 的 DNS 选项。Pod 数量较大时，Kubernetes 默认的 DNS 搜索路径行为（`ndots:5`）会在按原名查询前，让每次集群内部或 AWS 服务主机名查询（例如 S3 或 ElastiCache）多产生最多四次无用的搜索域查询。如果部署使用完全限定域名访问所有依赖（模块默认就是如此），请将 `n8n_dns_config` 设为 `ndots:1`：

```hcl
n8n_dns_config = {
  options = [{ name = "ndots", value = "1" }]
}
```

这会在大规模部署中显著减少 DNS 查询量，消除因 CoreDNS 饱和导致的请求失败，但不会让单次请求更快。

## 相关资源 <a id="related-resources"></a>

* [使用 Terraform 部署到 AWS](./)
* [在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)
* [在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)
* [在 AWS 上配置企业功能](use-enterprise-features-on-aws.md)
* [维护和拆除 AWS 部署](maintain-and-tear-down.md)
