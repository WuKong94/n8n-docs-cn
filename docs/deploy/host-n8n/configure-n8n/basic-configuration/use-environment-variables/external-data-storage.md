---
title: 外部数据存储环境变量
description: 配置自托管 n8n 实例外部数据存储的环境变量。
contentType: reference
tags:
- environment variables
- external storage
- storage
hide:
- toc
- tags
nodeTitle: 外部数据存储
originalFilePath: hosting/configuration/environment-variables/external-data-storage.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/external-data-storage
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部数据存储环境变量 <a href="#external-data-storage-environment-variables" id="external-data-storage-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

使用外部存储保存二进制数据和执行数据的更多说明，请参阅[外部存储](../../scaling/use-external-storage.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_STORAGE_S3_HOST` | String | - | 兼容 S3 的外部存储中，n8n 存储桶的主机，例如 `s3.us-east-1.amazonaws.com`。 |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME` | String | - | 兼容 S3 的外部存储中，n8n 存储桶的名称。 |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` | String | - | 兼容 S3 的外部存储中，n8n 存储桶所在的区域，例如 `us-east-1`。 |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY` | String | - | 兼容 S3 的外部存储访问密钥 ID。 |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET` | String | - | 兼容 S3 的外部存储访问密钥。 |
| `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` | Boolean | - | 通过自动检测凭据，为外部存储的 S3 调用验证身份。会忽略访问密钥 ID 和访问密钥，使用默认的[凭据提供商链](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain)。 |

## Azure Blob Storage <a href="#azure-blob-storage" id="azure-blob-storage"></a>

{% hint style="info" %}
**功能可用范围**

在 Azure Blob Storage 中存储执行数据或二进制数据的功能可用于：

- **自托管：**商业版、企业版。

n8n Cloud 不提供此功能。添加[许可证密钥](../../manage-your-license.md)即可解锁。
{% endhint %}

要在 Azure Blob Storage 中保存执行数据，将 `N8N_EXECUTION_DATA_STORAGE_MODE` 设为 `azure`；要保存二进制数据，将 `N8N_DEFAULT_BINARY_DATA_MODE` 设为 `azure`，参阅[外部存储](../../scaling/use-external-storage.md#storing-n8ns-binary-data-in-azure-blob-storage)。同一个容器可以保存两类数据。请配置下列变量，其中 `N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME` 始终必需。

身份验证可选择以下三种方式之一，n8n 按此顺序检查：

1. **连接字符串**：设置 `N8N_EXTERNAL_STORAGE_AZURE_CONNECTION_STRING`。优先于其他选项，设置后 n8n 会忽略账号名称、密钥和自动检测。这是最简单的方式，适合通过 Azurite 进行本地测试。
2. **自动检测**：设置 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME`，并将 `N8N_EXTERNAL_STORAGE_AZURE_AUTH_AUTO_DETECT` 设为 `true`。n8n 通过 Azure 的 `DefaultAzureCredential` 链验证身份，包括托管标识、环境或 Azure CLI，因此无需在 n8n 配置中保存密钥，适用于 Azure 生产环境。
3. **账号名称和密钥**：设置 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME` 和 `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_KEY`。

仅在使用 Azurite 或主权云等自定义端点时，才需要设置 `N8N_EXTERNAL_STORAGE_AZURE_ENDPOINT`。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_STORAGE_AZURE_CONNECTION_STRING` | String | - | Azure Blob Storage 的连接字符串。设置后，优先于账号名称和密钥。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME` | String | - | 存储账号名称，与账号密钥或托管标识配合使用。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_KEY` | String | - | 存储账号密钥，与账号名称配合使用。 |
| `N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME` | String | - | 保存执行数据和/或二进制数据的 Blob 容器名称。使用 Azure Blob Storage 时必需。 |
| `N8N_EXTERNAL_STORAGE_AZURE_ENDPOINT` | String | - | 自定义 Blob 端点，例如用于 Azurite 或主权云。 |
| `N8N_EXTERNAL_STORAGE_AZURE_AUTH_AUTO_DETECT` | Boolean | `false` | 通过 `DefaultAzureCredential`，即托管标识、环境或 Azure CLI 验证身份，不使用账号密钥。启用后忽略账号密钥。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
