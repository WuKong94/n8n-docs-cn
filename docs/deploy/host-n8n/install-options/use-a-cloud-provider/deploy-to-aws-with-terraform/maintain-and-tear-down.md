---
description: 在 terraform-aws-n8n 模块中管理加密密钥、验证数据库 TLS 并配置删除保护。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 维护和拆除 AWS 部署 <a id="maintain-and-tear-down-the-aws-deployment"></a>

[terraform-aws-n8n](https://github.com/n8n-io/terraform-aws-n8n) 模块管理加密密钥和数据库保护设置，它们在升级、事故恢复和停用部署时尤其重要。本页介绍这些设置。有关逐步升级和销毁排错，请参阅 GitHub 上模块的[升级指南](https://github.com/n8n-io/terraform-aws-n8n/blob/main/docs/upgrading-n8n.md)和[销毁检查清单](https://github.com/n8n-io/terraform-aws-n8n/blob/main/docs/destroy-cleanup.md)。

## 使用自己的 KMS 密钥 <a id="bring-your-own-kms-key"></a>

默认情况下，模块会创建并管理自己的 KMS 密钥，用于加密 RDS 实例和 S3 存储桶。如果要使用已有密钥（例如由中央安全团队控制的密钥）：

```hcl
create_db_kms_key = false
db_kms_key_arn    = "arn:aws:kms:eu-west-1:123456789012:key/1a2b3c4d-..."

create_s3_kms_key = false
s3_kms_key_arn    = "arn:aws:kms:eu-west-1:123456789012:key/1a2b3c4d-..."
```

同时设置布尔值和 ARN：仅设置布尔值会阻止模块创建自己的密钥，仅设置 ARN 则会被忽略。

{% hint style="info" %}
**CloudWatch Logs 日志组需要独立的密钥策略声明**

RDS 可以通过授权使用你的密钥，但如果密钥策略未明确指定区域 Logs 服务主体，CloudWatch Logs 会拒绝使用。缺少此声明时，模块的 `postgresql` 日志组会回退到 CloudWatch 自己管理的密钥。请添加声明，将 `kms:Encrypt`、`kms:Decrypt`、`kms:ReEncrypt*`、`kms:GenerateDataKey*` 和 `kms:DescribeKey` 权限授予 `logs.<region>.amazonaws.com` 主体，然后将 `db_logs_kms_key_enabled = true` 和 `db_logs_kms_key_arn` 设为同一个密钥。
{% endhint %}

## 验证 PostgreSQL TLS 证书 <a id="verify-the-postgresql-tls-certificate"></a>

默认情况下，n8n 与模块 RDS 实例之间的连接已加密，但不验证证书（`DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false`），因为 RDS 服务器证书的证书链指向 Amazon 自己的证书颁发机构，而 Node.js 默认不信任它。要在加密连接的同时验证服务器身份：

```hcl
db_postgresdb_ssl_reject_unauthorized = true
db_postgresdb_ssl_ca_pem              = file("${path.module}/global-bundle.pem")
```

从 AWS 信任库 `https://truststore.pki.rds.amazonaws.com` 下载合并的 CA 证书包。模块会以只读方式将其挂载到每个 n8n Pod，并让 `DB_POSTGRESDB_SSL_CA_FILE` 指向它。

## terraform destroy 后的 KMS 密钥 <a id="kms-keys-after-terraform-destroy"></a>

执行 `terraform destroy` 后，模块会安排在七天后删除其托管 KMS 密钥，而不是立即删除。密钥一旦进入计划删除状态就无法使用，尽管只有七天窗口结束后才会永久丢失。要在销毁完成后重用密钥，请先取消删除、启用密钥并将其重新导入 Terraform 状态，然后再次应用：

```bash
aws kms cancel-key-deletion --key-id <key-id>
aws kms enable-key --key-id <key-id>
```

{% hint style="warning" %}
**即使保留了快照或 S3 对象，待删除密钥也会阻止恢复**

一旦密钥进入 `PendingDeletion` 状态，使用模块自身 KMS 密钥加密的 RDS 快照和 S3 对象就无法解密。如果加密备份需要在 `terraform destroy` 后继续保留，请在模块之外管理一个长期保留的 KMS 密钥。对于已有部署，请在销毁前使用该密钥复制 RDS 快照，并重新加密或复制 S3 对象；更改配置中的密钥不会重新加密已有数据。
{% endhint %}

## 删除保护与拆除 <a id="deletion-protection-and-teardown"></a>

模块默认采用便于拆除的设置，以确保示例部署能够顺利销毁：

| 设置 | 默认值 | 生产值 |
|---|---|---|
| `db_deletion_protection` | `false` | `true` |
| `db_skip_final_snapshot` | `true` | `false`（同时设置 `db_final_snapshot_identifier`） |
| `db_delete_automated_backups` | `true` | `false` |
| `s3_force_destroy` | `true` | `false` |

这四项均可在已有部署上原位修改，不会强制替换资源。运行 `terraform destroy` 前，请先应用这些设置。Terraform 使用状态中保存的值，而不是尚未应用的配置。因此，编辑 `.tfvars` 文件后立即运行销毁，仍会使用旧值。

## 相关资源 <a id="related-resources"></a>

* [使用 Terraform 部署到 AWS](./)
* [在 AWS 上部署首个 n8n 实例](deploy-your-first-instance.md)
* [在 AWS 上扩缩容并实现高可用](scale-and-run-at-high-availability.md)
* [在 AWS 上配置企业功能](use-enterprise-features-on-aws.md)
* [自定义 AWS 基础设施](customize-the-infrastructure.md)
