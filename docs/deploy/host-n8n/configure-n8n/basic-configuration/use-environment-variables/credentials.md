---
title: 凭据环境变量
description: 通过环境变量管理和覆盖自托管 n8n 实例的默认凭据。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 凭据
originalFilePath: hosting/configuration/environment-variables/credentials.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/credentials
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 凭据环境变量 <a href="#credentials-environment-variables" id="credentials-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

使用以下环境变量启用凭据覆盖。详情请参阅[凭据覆盖](../../../../../administer/manage-credentials/credential-overwrites.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `CREDENTIALS_OVERWRITE_DATA`<br>/`_FILE` | * | - | 凭据覆盖配置。 |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | String | - | 用于获取凭据的 API 端点。 |
| `CREDENTIALS_OVERWRITE_PERSISTENCE` | Boolean | `false` | 启用凭据覆盖的数据库持久化。多实例或队列模式需要此设置，以通过发布/订阅机制将覆盖配置传播到工作进程。 |
| `N8N_MANAGED_OAUTH_SHOW_SCOPES` | String | - | 允许用户配置作用域字段的托管 OAuth 凭据类型列表，以逗号分隔。 |
| `CREDENTIALS_DEFAULT_NAME` | String | `My credentials` | 凭据的默认名称。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
