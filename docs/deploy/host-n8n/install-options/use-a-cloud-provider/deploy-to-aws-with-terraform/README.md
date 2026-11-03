---
description: 使用官方 Terraform 模块，在 AWS 上部署适用于生产环境的高可用 n8n 实例。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Terraform 部署到 AWS <a id="deploy-to-aws-with-terraform"></a>

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 是一个 Terraform 模块，可在 AWS 上部署适用于生产环境的多主实例 n8n。它会创建运行 n8n Helm Chart 的 Amazon EKS 集群，并配置托管 PostgreSQL（RDS）、Redis（ElastiCache）及用于共享文件存储的 S3。

这与 n8n 在其他章节介绍的手动 [Kubernetes 配置](../deploy-to-aws.md)不同：该指南通过手写清单部署单个 n8n 实例；此模块则自动部署支持高可用和自动扩缩容的架构，由 n8n Solutions 团队独立维护。

{% hint style="warning" %}
**预发布模块**

`terraform-aws-n8n` 处于预发布阶段。在模块达到首个稳定版本（1.0）之前，可能发生不兼容变更。
{% endhint %}

{% hint style="info" %}
**功能可用范围**

该模块默认部署的多主实例拓扑适用于：

- **自托管：**Enterprise。

设置 `n8n_main_hpa_min_replicas = 1` 后，将改为运行一个主 Pod，此模式只需要 Business 套餐许可证。在该模式下，主 Pod 的扩缩容上限固定为一个，升级使用 `Recreate` 策略。升级和维护期间，编辑器、REST API 和定时触发器会发生停机。
{% endhint %}

## 架构 <a id="architecture"></a>

用户和传入 Webhook 通过应用程序负载均衡器访问 EKS 集群。集群内，n8n Helm Chart 运行三个独立的 Deployment：

- **主 Pod：**处理领导者选举、编辑器界面和 REST API。
- **Webhook 处理器 Pod：**处理传入触发事件。
- **工作进程 Pod：**执行工作流，并通过 [KEDA](https://keda.sh/)根据 Redis 队列深度扩缩容。

状态保存在集群外的托管服务中：RDS PostgreSQL 保存工作流数据，ElastiCache Redis 用于领导者选举和工作队列，S3 保存二进制数据。AWS Certificate Manager（ACM）为负载均衡器签发 TLS 证书。

AWS 通过 EKS Pod Identity 为 Pod 授权，包括 Load Balancer Controller、Cluster Autoscaler、EBS CSI 驱动以及 n8n 自身的 S3 访问权限。

## 前置条件 <a id="prerequisites"></a>

- **n8n 许可证密钥：**默认多主实例拓扑需要 Enterprise 许可证；设置 `n8n_main_hpa_min_replicas = 1` 时，可以使用 Business 许可证。
- **已存在的 VPC：**包含已为 EKS 和 ALB 用途设置标签的公有和私有子网。模块不会创建 VPC。请参阅[自定义 AWS 基础设施](customize-the-infrastructure.md)。
- **Terraform CLI 1.11 或更高版本**，并配置 `aws`、`kubernetes` 和 `helm` 提供程序。
- DNS 方案：使用 Route 53 托管区域（`route53_zone_id`），让模块签发 ACM 证书并管理 DNS 记录；或使用其他提供方已验证的证书（`certificate_arn`）。

## 用法 <a id="usage"></a>

有关从空文件夹到运行实例的分步流程，请参阅[在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)。以下配置包含最少必需输入：

```hcl
module "n8n" {
  source  = "n8n-io/n8n/aws"
  version = "~> 0.5.0"

  aws_region      = "us-east-1"
  cluster_name    = "n8n-cluster"
  n8n_domain      = "n8n.example.com"
  n8n_license_key = var.n8n_license_key

  # Bring your own VPC.
  vpc_id          = module.vpc.vpc_id
  private_subnets = module.vpc.private_subnets
  public_subnets  = module.vpc.public_subnets
  vpc_cidr_block  = module.vpc.vpc_cidr_block

  # EKS node group autoscaling bounds. You pay for node_min nodes at all times.
  node_min = 3
  node_max = 6

  # Set exactly one of these for DNS and TLS.
  route53_zone_id = "Z0123456789ABCDEFGHIJ"
  # certificate_arn = aws_acm_certificate_validation.n8n.certificate_arn
}
```

通过密钥管理器传入 `n8n_license_key` 等敏感值，并将 Terraform 状态保存在加密且受访问控制的后端，因为模块会将密钥写入 Helm Release。绝不要将密钥硬编码到提交至版本控制的 `.tfvars` 文件中。

## 选择初始规模 <a id="choose-a-starting-size"></a>

模块提供三种规模示例。选择一种作为起点，再调整节点类型、数量和数据库规格。

| | [small](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/small)（默认） | [medium](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/medium) | [large](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/large) |
|---|---|---|---|
| 目标规模 | 开发或小型团队 | 约 5-15M 次执行/天 | 约 50-60M+ 次执行/天 |
| 节点类型 | t3.xlarge | m6i.2xlarge | m7i.4xlarge |
| 节点数（最小/最大） | 3/6 | 5/15 | 10/50 |
| 数据库 | RDS db.t3.small | RDS db.m6g.2xlarge | Aurora PostgreSQL I/O-Optimized |
| Redis | cache.t3.medium | cache.r6g.large | cache.r6g.large |
| 预计每月费用（按需） | 约 $440 | 约 $2,000 | 约 $21,000+ |

还提供两个拓扑变体示例：[split-ingress](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/split-ingress)（请参阅[自定义 AWS 基础设施](customize-the-infrastructure.md#customer-managed-ingress)）和 [worker-pools](https://github.com/n8n-io/terraform-aws-n8n/tree/main/examples/worker-pools)。后者使用 n8n 的 Alpha 功能运行带有不同标签的独立工作进程池。

## 支持 <a id="support"></a>

此模块开放源代码，由 n8n Solutions 团队独立于 n8n Enterprise 支持服务进行维护。请通过 [GitHub Issues](https://github.com/n8n-io/terraform-aws-n8n/issues)报告问题或请求功能，维护者会尽力处理，但不提供 SLA。对于与模块无关的一般 n8n 问题，请使用 [n8n 社区论坛](https://community.n8n.io/)。

## 本节内容 <a id="in-this-section"></a>

- [在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)：从空文件夹到运行实例的分步指南。
- [在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)：配置多主实例、工作进程自动扩缩容和 Redis 高可用。
- [在 AWS 上配置企业功能](use-enterprise-features-on-aws.md)：接入 S3 执行数据、Prometheus 指标、OpenTelemetry 追踪、日志流和外部密钥。
- [自定义 AWS 基础设施](customize-the-infrastructure.md)：使用自己的 VPC、数据库、缓存或集群，分离入口流量，或使用自定义 n8n 镜像。
- [维护和拆除 AWS 部署](maintain-and-tear-down.md)：管理加密密钥、验证数据库 TLS，以及配置删除保护。

## 相关资源 <a id="related-resources"></a>

* [使用云服务商](../)
* [部署到 AWS](../deploy-to-aws.md)
* [DigitalOcean](../deploy-to-digital-ocean.md)
* [Heroku](../deploy-to-heroku.md)
* [Hetzner Cloud](../deploy-to-hetzner.md)
* [Azure](../deploy-to-azure.md)
* [Google Cloud Run](../deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](../deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](../deploy-to-openshift-local-crc.md)
* [使用 Docker Compose](../use-docker-compose.md)
* [启用队列模式](../../../configure-n8n/scaling/enable-queue-mode.md)
