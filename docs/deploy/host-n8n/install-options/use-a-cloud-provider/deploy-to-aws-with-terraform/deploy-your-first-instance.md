---
description: 使用 terraform-aws-n8n 模块，从空文件夹到可运行的编辑器，逐步在 AWS 上部署 n8n 实例。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 AWS 上部署首个 n8n 实例 <a id="deploy-your-first-n8n-instance-on-aws"></a>

本指南使用 [terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 模块的 `small` 示例，通过六个步骤，从空文件夹开始，在 AWS 上部署可运行的 n8n 实例。只需编写一个 `main.tf` 文件，然后运行 `terraform init`、`terraform plan` 和 `terraform apply`。

无需克隆仓库。示例在 Terraform Registry 中以 [`n8n-io/n8n/aws`](https://registry.terraform.io/modules/n8n-io/n8n/aws/0.5.0) 提供，`terraform init` 会自动下载。该示例已包含 VPC 和提供程序配置，因此本页配置就是全部需要编写的 Terraform 内容。

从 `terraform apply` 到编辑器可访问，预计约需 30 分钟。

{% hint style="info" %}
**功能可用范围**

该模块默认部署的多主实例拓扑适用于：

- **自托管：**Enterprise。

如果设置 `n8n_main_hpa_min_replicas = 1` 以运行一个主 Pod，也可以使用 Business 许可证。有关此模式带来的变化，请参阅[在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)。
{% endhint %}

## 前置条件 <a id="prerequisites"></a>

开始前，请确认具备以下条件：

- 已安装 [Terraform CLI 1.11 或更高版本](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)。
- 已安装 [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)，并配置可以创建 EKS、RDS、ElastiCache、IAM、VPC、KMS、S3、ACM 和 Route 53 资源的凭据。
- 一个父区域托管在 AWS Route 53 的域名，需要其托管区域 ID。例如，在 `n8n.example.com` 上运行 n8n，需要 `example.com` 的托管区域。
- n8n Enterprise 许可证密钥；如果设置 `n8n_main_hpa_min_replicas = 1`，也可以使用 Business 许可证密钥。

## 步骤 1：创建项目文件夹 <a id="step-1-create-a-project-folder"></a>

Terraform 在运行命令所在的文件夹中工作，因此请从空文件夹开始：

```bash
mkdir n8n-aws
cd n8n-aws
```

## 第 2 步：选择部署规模 <a id="step-2-choose-a-deployment-size"></a>

terraform-aws-n8n 模块提供三种规模示例。本指南部署适合开发或小型团队实例的 `small`：

| | small（默认） | medium | large |
|---|---|---|---|
| 目标规模 | 开发或小型团队 | 约 5–15M 次执行/天 | 约 50–60M+ 次执行/天 |
| 节点类型 | t3.xlarge | m6i.2xlarge | m7i.4xlarge |
| 预计每月费用（按需） | 约 $440 | 约 $2,000 | 约 $21,000+ |

包含 Pod 数量、数据库规格和预留实例价格的完整比较，请参阅[使用 Terraform 部署到 AWS](./)中的规模表。如果不确定，请从 `small` 开始：从 `small` 升级到 `medium` 较为直接，而升级到 `large` 涉及基础设施变更。

要部署更大规模，请将模块的 `source`（位于 `main.tf` 中）指向对应示例的子路径。[`examples/medium`](https://registry.terraform.io/modules/n8n-io/n8n/aws/0.5.0/examples/medium) 使用与 `small` 相同的输入，[`examples/large`](https://registry.terraform.io/modules/n8n-io/n8n/aws/0.5.0/examples/large) 则额外需要 `certificate_arn` 和 `aurora_instance_class`。

## 步骤 3：创建 `main.tf` <a id="step-3-create-maintf"></a>

在项目文件夹中创建一个 `main.tf` 文件。它将 Registry 中的 [small 示例](https://registry.terraform.io/modules/n8n-io/n8n/aws/0.5.0/examples/small)作为模块引用，版本固定为 0.5.0：

{% code title="main.tf" %}
```hcl
variable "n8n_license_key" {
  type      = string
  sensitive = true
}

module "n8n" {
  source  = "n8n-io/n8n/aws//examples/small"
  version = "0.5.0"

  n8n_domain      = "n8n.example.com"
  route53_zone_id = "<hosted-zone-id>"
  n8n_license_key = var.n8n_license_key

  # Applied to every resource, for cost tracking and ownership.
  tags = {
    Environment = "development"
    Owner       = "platform-team"
  }

  # aws_region   = "eu-west-1"   # optional, defaults to us-east-1
  # cluster_name = "n8n-cluster" # optional, 14 characters or fewer
}

output "n8n_url" {
  description = "The URL to open once the load balancer finishes provisioning."
  value       = module.n8n.n8n_url
}

output "n8n_encryption_key" {
  description = "Back this up in a password manager. n8n emits it once."
  value       = module.n8n.n8n_encryption_key
  sensitive   = true
}
```
{% endcode %}

`cluster_name` 不得超过 14 个字符。模块由此派生出 `<cluster-name>-redis` 形式的 ElastiCache 集群 ID，而 AWS 将此类 ID 限制为 20 个字符。

## 第 4 步：设置值 <a id="step-4-set-your-values"></a>

在 `main.tf` 中替换：

- 将 `n8n_domain` 替换为运行 n8n 所需的域名。
- 将 `route53_zone_id` 替换为该域名父区域的托管区域 ID。
- 将 `tags` 替换为组织用于成本追踪和归属管理的信息。

然后通过环境变量提供许可证密钥，避免写入文件：

```bash
export TF_VAR_n8n_license_key="<your-license-key>"
```

## 第 5 步：初始化 Terraform <a id="step-5-initialize-terraform"></a>

```bash
terraform init
```

这会下载 n8n 模块、VPC 模块，以及 `aws`、`kubernetes` 和 `helm` 提供程序。

## 第 6 步：规划并应用 <a id="step-6-plan-and-apply"></a>

预览 Terraform 将创建的资源：

```bash
terraform plan
```

检查计划，然后应用：

```bash
terraform apply
```

按提示输入 `yes`，或添加 `-auto-approve` 跳过确认。资源创建大约需要 20 到 25 分钟，之后负载均衡器还需约五分钟才能访问。

完成后，打开 `n8n_url` 输出中的 URL：

```bash
terraform output -raw n8n_url
```

n8n 会显示设置页面。输入邮箱、名字、姓氏和密码，创建所有者账号。完成或跳过问卷，即可进入工作区。

{% hint style="danger" %}
**立即保存加密密钥**

n8n 只生成一次加密密钥。没有它，所有已存储的凭据都将无法读取，也无人能够为你恢复。继续之前，运行 `terraform output -raw n8n_encryption_key`，将该值保存在密码管理器中。
{% endhint %}

## 保护 Terraform 状态文件 <a id="protect-your-terraform-state-file"></a>

Terraform 在项目文件夹中写入 `terraform.tfstate` 文件。该文件记录基础设施，并以明文保存 n8n 加密密钥、数据库密码和许可证密钥。将输出标记为 `sensitive` 只会在终端中隐藏它，不会从状态文件中隐藏。

遵循两条规则：

- 绝不要将 `terraform.tfstate` 提交到版本控制。
- 除短暂试用外，均应将状态远程保存到 HCP Terraform，或配置了加密、版本控制、状态锁定和严格访问控制的 S3 存储桶中。

## 清理 <a id="clean-up"></a>

要拆除本示例创建的所有资源：

```bash
terraform destroy
```

按提示输入 `yes`，或添加 `-auto-approve`。

`small` 示例默认便于拆除，以确保 `terraform destroy` 可以顺利运行：RDS 实例跳过最终快照，S3 存储桶允许强制销毁。在将此配置用于生产前，请审查这些设置。生产值请参阅[维护和拆除 AWS 部署](maintain-and-tear-down.md)。另请注意，模块会在销毁后七天安排删除其 KMS 密钥，这将阻止从保留的快照恢复。

## 相关资源 <a id="related-resources"></a>

实例目前使用模块的默认配置。接下来可以：

- [在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)：调整多主实例、工作进程自动扩缩容和 Redis 高可用。
- [在 AWS 上配置企业功能](use-enterprise-features-on-aws.md)：接入 S3 执行数据、Prometheus 指标、OpenTelemetry 追踪、日志流和外部密钥。
- [自定义 AWS 基础设施](customize-the-infrastructure.md)：连接已有的 VPC、数据库、缓存或集群，分离入口流量，或使用自定义 n8n 镜像。
