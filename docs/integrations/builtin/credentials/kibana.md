---
title: Kibana 凭据
description: Kibana 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Kibana 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Kibana 凭据
originalFilePath: integrations/builtin/credentials/kibana.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/kibana
url: https://docs.n8n.io/integrations/builtin/credentials/kibana
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Kibana 凭据 <a href="#kibana-credentials" id="kibana-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Elasticsearch](https://www.elastic.co/) 账户。
- 如果创建新账户用于测试，请向 Kibana 加载一些示例数据。更多信息请参阅 [Kibana 快速入门](https://www.elastic.co/guide/en/kibana/current/get-started.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Kibana API 文档](https://www.elastic.co/guide/en/kibana/current/api.html)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/kibana/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 访问 Kibana 所用的 **URL**，例如 `http://localhost:5601`。
- **Username**（用户名）：使用登录 Elastic 时的用户名。
- **Password**（密码）：使用登录 Elastic 时的密码。
