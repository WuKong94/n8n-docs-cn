---
description: 将 n8n 实例的二进制数据和执行数据存储到外部。
contentType: howto
tags:
- external storage
- storage
hide:
- tags
search:
  boost: 1.5
nodeTitle: 使用外部存储
originalFilePath: hosting/scaling/external-storage.md
originalUrl: https://docs.n8n.io/hosting/scaling/external-storage
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部存储 <a href="#external-storage" id="external-storage"></a>

{% hint style="info" %}
**功能可用范围**

外部存储可用于：

- **自托管：**商业版、企业版。

n8n Cloud 不提供此功能。

{% endhint %}

n8n 可以将工作流执行产生的二进制数据和执行数据存储到外部，避免依赖数据库或文件系统存储大量数据。

## 将 n8n 的二进制数据存储到 S3 <a href="#storing-n8ns-binary-data-in-s3" id="storing-n8ns-binary-data-in-s3"></a>

n8n 支持使用 [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) 作为工作流执行产生的二进制数据的外部存储。也可以使用 Cloudflare R2、Backblaze B2 等其他兼容 S3 的服务，但 n8n 不提供官方支持。

{% hint style="info" %}
**功能可用范围**

S3 二进制数据存储可用于：

- **自托管：**商业版、企业版。

n8n Cloud 不提供此功能。

启用外部存储前，请激活[许可证密钥](../manage-your-license.md)。没有有效许可证时，n8n 无法以 `s3` 二进制数据模式启动；请将 `N8N_DEFAULT_BINARY_DATA_MODE` 设为其他模式，或升级套餐。
{% endhint %}

### 设置 <a href="#setup" id="setup"></a>

按照 [AWS 文档](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)创建并配置存储桶。可以使用以下策略，将 `<bucket-name>` 替换为所创建存储桶的名称：

```json
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "VisualEditor0",
   "Effect": "Allow",
   "Action": ["s3:*"],
   "Resource": ["arn:aws:s3:::<bucket-name>", "arn:aws:s3:::<bucket-name>/*"]
  }
 ]
}
```

设置存储桶级生命周期配置，让 S3 自动删除旧二进制数据。n8n 将二进制数据清理交由 S3 处理，因此除非希望永久保留二进制数据，否则必须设置生命周期配置。

创建存储桶后，你会获得主机地址、存储桶名称、区域，以及访问密钥 ID 和秘密访问密钥。需要在 n8n 的环境中设置：

```sh
export N8N_EXTERNAL_STORAGE_S3_HOST=... # example: s3.us-east-1.amazonaws.com
export N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME=...
export N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET=...
```

{% hint style="info" %}
**无区域**

如果提供商不要求区域，可以将 `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` 设为 `'auto'`。
{% endhint %}

## 验证并更新 S3 存储桶区域格式，自 n8n 2.6.4 起 <a href="#validate-and-update-your-s3-bucket-region-format-v264-onward" id="validate-and-update-your-s3-bucket-region-format-v264-onward"></a>

自 n8n 2.6.4 起，环境变量 `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` 的值必须满足以下条件：

- 仅包含字母数字字符（`a-z`、`A-Z`、`0-9`）和连字符（`-`）。
- 不包含下划线（`_`）或其他特殊字符。

不满足这些条件时，即使存储端点可访问，且在旧版本中正常工作，n8n 也会因连接错误启动失败。

如果升级到 n8n 2.6.4 后 S3 连接失败，请确认区域值符合这些条件，然后重新部署 n8n。

指示 n8n 将二进制数据存储到 S3：

```sh
export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3
export N8N_DEFAULT_BINARY_DATA_MODE=s3
```


{% hint style="info" %}
**自动检测身份验证信息**

要自动检测 S3 调用所需的凭据，将 `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` 设为 `true`，即可使用默认的[凭据提供程序链](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain)。
{% endhint %}

重启服务器以加载新配置。

### 使用 <a href="#usage" id="usage"></a>

启用 S3 后，n8n 会将所有新的二进制数据写入 S3 存储桶，并从中读取。写入存储桶时使用以下格式：

```
workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}
```

只要 `filesystem` 仍列为 `N8N_AVAILABLE_BINARY_DATA_MODES` 中的选项，n8n 就会继续从文件系统读取此前存储在其中的旧二进制数据。

如果将二进制数据存入 S3 后又切换为文件系统模式，只要 `s3` 仍列在 `N8N_AVAILABLE_BINARY_DATA_MODES` 中，且 S3 凭据仍有效，实例就会继续读取 S3 中的数据。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/scaling/binary-data-pruning.md" %}

### S3 存储升级最佳实践 <a href="#upgrade-best-practices-for-s3-storage" id="upgrade-best-practices-for-s3-storage"></a>

使用 S3 或兼容 S3 的存储时：

1. 同时将所有 n8n 组件，包括主实例、工作进程和任务运行器，升级到同一版本，以避免协议不兼容。
2. 对于通过 HTTP 访问的本地部署或兼容 S3 的存储，设置 `N8N_EXTERNAL_STORAGE_S3_PROTOCOL=http`，并在主机配置中包含协议。
3. 仅使用受支持的环境变量名：访问密钥使用 `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY`。

新版 n8n 的验证和协议处理更严格，升级后可能需要更新旧配置。

## 将 n8n 的二进制数据存储到 Azure Blob Storage <a id="storing-n8ns-binary-data-in-azure-blob-storage"></a>

n8n 支持使用 [Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) 作为工作流执行产生的二进制数据的外部存储。它使用与[外部执行数据存储](../basic-configuration/use-environment-variables/external-data-storage.md#azure-blob-storage)相同的 Azure Blob 配置，因此单个容器可同时存放二进制数据和执行数据。

{% hint style="info" %}
**功能可用范围**

Azure Blob Storage 二进制数据存储可用于：

- **自托管：**商业版、企业版。

n8n Cloud 不提供此功能。

启用外部存储前，请激活[许可证密钥](../manage-your-license.md)。没有有效许可证时，n8n 无法以 `azure` 二进制数据模式启动；请将 `N8N_DEFAULT_BINARY_DATA_MODE` 设为其他模式，或升级套餐。
{% endhint %}

### Azure 设置 <a id="azure-setup"></a>

按照 [Azure 文档](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal)在 Azure 存储账号中创建 Blob 容器。

在 n8n 环境中设置容器名称。`N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME` 始终为必填项：

```sh
export N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME=...
```

身份验证方面，n8n 支持连接字符串、账号名称和密钥，或托管标识（`DefaultAzureCredential`）。完整的身份验证变量列表及 n8n 检查这些变量的顺序，请参阅[外部数据存储环境变量 | Azure Blob Storage](../basic-configuration/use-environment-variables/external-data-storage.md#azure-blob-storage)。

n8n 将二进制数据清理交由 Azure 处理，因此请为容器设置[生命周期管理策略](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)，自动删除旧二进制数据。除非希望永久保留二进制数据，否则必须设置生命周期策略。

指示 n8n 将二进制数据存储到 Azure Blob Storage：

```sh
export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,azure
export N8N_DEFAULT_BINARY_DATA_MODE=azure
```

重启服务器以加载新配置。

### Azure 使用 <a id="azure-usage"></a>

启用 Azure Blob Storage 后，n8n 会将所有新的二进制数据写入容器，并从中读取。写入容器时使用以下格式：

```
workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}
```

只要 `filesystem` 仍列为 `N8N_AVAILABLE_BINARY_DATA_MODES` 中的选项，n8n 就会继续从文件系统读取此前存储在其中的旧二进制数据。

如果将二进制数据存入 Azure Blob Storage 后又切换为文件系统模式，只要 `azure` 仍列在 `N8N_AVAILABLE_BINARY_DATA_MODES` 中，且 Azure 凭据仍有效，实例就会继续读取 Azure 中的数据。

## 将 n8n 的执行数据存储到 S3 <a id="storing-n8ns-execution-data-in-s3"></a>

n8n 也可以将执行数据存储到 S3。

按照二进制数据[设置](#setup)一节配置 S3 存储桶和凭据，然后指示 n8n 将执行数据存储到 S3：

```sh
export N8N_EXECUTION_DATA_STORAGE_MODE=s3
```

在[队列模式](enable-queue-mode.md)下，需要在包括工作进程在内的所有实例上设置 `N8N_EXECUTION_DATA_STORAGE_MODE` 和 `N8N_EXTERNAL_STORAGE_S3_*` 变量。

{% hint style="warning" %}
**启动需要许可证**

S3 执行数据存储需要 Business 或 Enterprise 套餐，以及已激活的[许可证密钥](../manage-your-license.md)。没有有效许可证时，如果设置了 `N8N_EXECUTION_DATA_STORAGE_MODE=s3`，n8n 将无法启动。要重新启动，请将模式改回 `database` 或 `filesystem`，或恢复有效许可证。
{% endhint %}

启用 S3 执行数据存储后，n8n 会将所有新执行的数据按以下格式写入 S3 存储桶：

```
workflows/{workflowId}/executions/{executionId}/execution_data/bundle.json
```

n8n 会记录每次执行的数据存储位置，因此切换模式不会破坏数据。旧执行仍可从数据库或文件系统读取；以后切回其他模式时，只要存储桶仍配置有效，S3 中的执行也保持可读。

n8n 会使用标准[执行清理](manage-execution-data.md#enable-executions-pruning)设置，即 `EXECUTIONS_DATA_*` 变量，自行清理 S3 中的执行数据。与二进制数据不同，执行数据不依赖 S3 生命周期规则。不要为执行数据添加生命周期规则，否则可能删除 n8n 仍在引用的数据。

## 相关资源 <a id="related-resources"></a>

* [扩展](../scaling.md)
* [衡量性能](measure-performance.md)
* [启用队列模式](enable-queue-mode.md)
* [控制并发](control-concurrency.md)
* [管理执行数据](manage-execution-data.md)
* [处理二进制数据](handle-binary-data.md)
* [解决内存问题](fix-memory-issues.md)
