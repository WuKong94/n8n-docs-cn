---
title: Datadog 凭据
description: Datadog 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Datadog 的身份验证。
contentType:
- integration
- reference
nodeTitle: Datadog 凭据
originalFilePath: integrations/builtin/credentials/datadog.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/datadog
url: https://docs.n8n.io/integrations/builtin/credentials/datadog
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Datadog 凭据 <a href="#datadog-credentials" id="datadog-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Datadog](https://app.datadoghq.eu/signup) 账号。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [Datadog API 文档](https://docs.datadoghq.com/api/latest/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/datadog/)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- Datadog 实例的 **Host（主机）**
- 一个 **API Key（API 密钥）**
- 一个 **App Key（应用密钥）**
	
更多信息请参阅 Datadog 网站上的[身份验证](https://docs.datadoghq.com/api/latest/authentication/)说明。
