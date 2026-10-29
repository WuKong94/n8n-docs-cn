---
title: 外部密钥环境变量
description: 配置自托管 n8n 实例外部密钥的更新间隔、连接超时和刷新超时。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 外部密钥
originalFilePath: hosting/configuration/environment-variables/external-secrets.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/external-secrets
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部密钥环境变量 <a href="#external-secrets-environment-variables" id="external-secrets-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

可以使用外部密钥存储管理 n8n 凭据。详情请参阅[外部密钥](../../../../../administer/manage-credentials/use-external-secret-stores.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL` | Number | `300`（5 分钟） | 检查密钥更新的频率，单位为秒。 |
| `N8N_EXTERNAL_SECRETS_CONNECT_TIMEOUT` | Number | `20` | n8n 等待密钥库连接的最长时长，单位为秒。未及时响应时，n8n 会将其标记为错误，以逐渐增加的间隔在后台重试连接，启动流程则继续，但暂时无法使用该密钥库的密钥。自 n8n 2.41.0 起提供。 |
| `N8N_EXTERNAL_SECRETS_REFRESH_TIMEOUT` | Number | `20` | 启动及每次更新时，n8n 等待密钥库返回密钥的最长时长，单位为秒。获取耗时过长时，n8n 停止等待，获取操作继续在后台运行，成功后会保存密钥。启动时，使用该密钥库密钥的工作流会失败，直到首次获取完成；定期更新时，之前获取的密钥仍可使用。密钥很多时，可增加此值。对于 HashiCorp Vault 和 Infisical，每个单独 HTTP 请求也会在两个超时值中较大的时长后取消。自 n8n 2.41.0 起提供。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
