---
title: TheHive 凭据
description: TheHive 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 TheHive 的身份验证。
contentType:
- integration
- reference
nodeTitle: TheHive 凭据
originalFilePath: integrations/builtin/credentials/thehive.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/thehive
url: https://docs.n8n.io/integrations/builtin/credentials/thehive
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TheHive 凭据 <a href="#thehive-credentials" id="thehive-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [TheHive](../app-nodes/n8n-nodes-base.thehive.md)

{% hint style="info" %}
**TheHive 与 TheHive 5**

n8n 为 TheHive 提供两个节点。将此凭据用于支持 TheHive 3 或 TheHive 4 的 TheHive 节点。如果使用 TheHive5 节点，请改用 [TheHive 5 凭据](thehive5.md)。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在服务器上安装 [TheHive](https://docs.strangebee.com/thehive/installation/installation-methods/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

这些服务的更多信息，请参阅 [TheHive 3 API 文档](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)和 [TheHive 4 API 文档](https://docs.thehive-project.org/thehive/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key**（API 密钥）：在 **Organization > Create API Key**（组织 > 创建 API 密钥）中创建 API 密钥。更多信息请参阅 [API 身份验证](https://docs.thehive-project.org/thehive/legacy/thehive3/api/authentication/)。
- 你的 **URL**：TheHive 服务器的 URL。
- 一个 **API Version**（API 版本），可选择：
    - **TheHive 3 (api v0)**（TheHive 3，API v0）
    - **TheHive 4 (api v1)**（TheHive 4，API v1）
    - 对于 TheHive 5，请改用 [TheHive 5 凭据](thehive5.md)。
- **Ignore SSL Issues**（忽略 SSL 问题）：开启后，即使 SSL 证书验证失败，n8n 仍会连接。

