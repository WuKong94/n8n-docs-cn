---
title: OpenWeatherMap 凭据
description: OpenWeatherMap 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 OpenWeatherMap 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: OpenWeatherMap 凭据
originalFilePath: integrations/builtin/credentials/openweathermap.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/openweathermap
url: https://docs.n8n.io/integrations/builtin/credentials/openweathermap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenWeatherMap 凭据 <a href="#openweathermap-credentials" id="openweathermap-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [OpenWeatherMap](../app-nodes/n8n-nodes-base.openweathermap.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [OpenWeatherMap API 文档](https://openweathermap.org/api)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [OpenWeatherMap](https://openweathermap.org/) 账号，以及：

- 一个 **Access Token（访问令牌）**

获取 **Access Token**（访问令牌）：

1. 验证邮箱地址后，OpenWeatherMap 会在欢迎邮件中提供 **API Key**（API 密钥）。
2. 复制该密钥，填入 n8n 凭据。

如果希望创建新密钥：

1. 进入 **Account >** [**API Keys**](https://home.openweathermap.org/api_keys)（账户 > API 密钥）创建新密钥。
2. 在 **Create Key**（创建密钥）部分输入 **API Key Name**（API 密钥名称），例如 `n8n integration`。
3. 选择 **Generate**（生成）。
4. 复制生成的密钥，填入 n8n 凭据。
