---
title: TheHive 5 凭据
description: TheHive 5 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 TheHive 的身份验证。
contentType:
- integration
- reference
nodeTitle: TheHive 5 凭据
originalFilePath: integrations/builtin/credentials/thehive5.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/thehive5
url: https://docs.n8n.io/integrations/builtin/credentials/thehive5
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TheHive 5 凭据 <a href="#thehive-5-credentials" id="thehive-5-credentials"></a>

这些凭据可用于以下节点与 TheHive 5 之间的身份验证。

- [TheHive 5](../app-nodes/n8n-nodes-base.thehive5.md)

{% hint style="info" %}
**TheHive 和 TheHive 5**

n8n 为 TheHive 提供两个节点。请将这些凭据用于 TheHive 5 节点。如果使用的是面向 TheHive 3 或 TheHive 4 的 TheHive 节点，请使用 [TheHive 凭据](thehive.md)。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在服务器上安装 [TheHive 5](https://docs.strangebee.com/thehive/download/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [TheHive API 文档](https://docs.strangebee.com/thehive/api-docs/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：使用 `orgAdmin` 和 `superAdmin` 账户的用户可生成 API 密钥：
    - `orgAdmin` 账户：进入目标用户的 **Organization > Create API Key**（组织 > 创建 API 密钥）。
    - `superAdmin` 账户：进入目标用户的 **Users > Create API Key**（用户 > 创建 API 密钥）。
    - 更多信息，请参阅 [API 身份验证](https://docs.strangebee.com/cortex/api/api-guide/?h=api+key#authentication)。
- **URL**：TheHive 服务器的 URL。
- **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，n8n 仍会连接。


