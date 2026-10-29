---
title: Elasticsearch 凭据
description: Elasticsearch 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Elasticsearch 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Elasticsearch 凭据
originalFilePath: integrations/builtin/credentials/elasticsearch.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/elasticsearch
url: https://docs.n8n.io/integrations/builtin/credentials/elasticsearch
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Elasticsearch 凭据 <a href="#elasticsearch-credentials" id="elasticsearch-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Elasticsearch](../app-nodes/n8n-nodes-base.elasticsearch.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Elasticsearch 文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要一个具有[部署](https://www.elastic.co/guide/en/cloud/current/ec-create-deployment.html)的 [Elasticsearch](https://www.elastic.co/) 账户，以及：

- 一个 **Username（用户名）**
- 一个 **Password（密码）**
- Elasticsearch 应用的 **Base URL**（基础 URL），也称为 Elasticsearch 应用端点。

设置凭据的步骤如下：

1. 输入 Elasticsearch 的 **Username**（用户名）。
2. 输入 Elasticsearch 的 **Password**（密码）。
3. 在 Elasticsearch 中进入 **Deployments**（部署）。
4. 选择你的部署。
5. 选择 **Manage this deployment**（管理此部署）。
6. 在 **Applications**（应用）部分，复制 **Elasticsearch** 应用的端点。
7. 将其填入 n8n 的 **Base URL**（基础 URL）。
8. 默认情况下，n8n 仅在 SSL 证书验证成功时连接。如果希望在 SSL 证书验证失败时仍连接，请开启 **Ignore SSL Issues**（忽略 SSL 问题）。

{% hint style="info" %}
**自定义端点别名**

如果为部署添加了[自定义端点别名](https://www.elastic.co/guide/en/cloud/current/ec-regional-deployment-aliases.html)，请将 n8n 凭据的 **Base URL**（基础 URL）更新为新端点。
{% endhint %}
