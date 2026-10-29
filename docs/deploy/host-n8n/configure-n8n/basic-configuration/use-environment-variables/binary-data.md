---
title: 二进制数据环境变量
description: 通过环境变量自定义自托管 n8n 实例的二进制数据存储模式和路径。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 二进制数据
originalFilePath: hosting/configuration/environment-variables/binary-data.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/binary-data
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 二进制数据环境变量 <a href="#binary-data-environment-variables" id="binary-data-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

n8n 默认在内存中存储二进制数据。自托管商业版和企业版套餐也可以选择外部服务。更多二进制数据外部存储说明请参阅[外部存储](../../scaling/use-external-storage.md)。


| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_AVAILABLE_BINARY_DATA_MODES` | String | `filesystem` | 可用二进制数据模式的列表，以逗号分隔。 |
| `N8N_BINARY_DATA_DATABASE_MAX_FILE_SIZE` | Number | `512` | 当 `N8N_DEFAULT_BINARY_DATA_MODE` 为 `database` 时，n8n 存储的单个文件大小上限，单位为 MiB。不能超过数据库列的上限 `1024`，存储更大的文件会失败。 |
| `N8N_BINARY_DATA_STORAGE_PATH` | String | `N8N_USER_FOLDER/binaryData` | n8n 存储二进制数据的路径。 |
| `N8N_DEFAULT_BINARY_DATA_MODE` | String | `default` | 默认二进制数据模式。`default` 将数据保留在内存中；设为 `filesystem` 使用文件系统，`s3` 使用 AWS S3，`azure` 使用 Azure Blob Storage，`database` 使用数据库。二进制数据清理仅针对当前启用的存储模式。例如，实例原先在 S3 中存储数据，后来切换到文件系统模式，n8n 只会清理文件系统中的二进制数据。此行为未来可能变化。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
