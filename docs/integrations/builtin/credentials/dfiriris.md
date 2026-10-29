---
title: DFIR-IRIS 凭据
description: DFIR-IRIS 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 DFIR-IRIS 的身份验证。
contentType:
- integration
- reference
nodeTitle: DFIR-IRIS 凭据
originalFilePath: integrations/builtin/credentials/dfiriris.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/dfiriris
url: https://docs.n8n.io/integrations/builtin/credentials/dfiriris
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# DFIR-IRIS 凭据 <a href="#dfir-iris-credentials" id="dfir-iris-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

一个可访问的 [DFIR-IRIS](https://docs.dfir-iris.org/latest/getting_started/) 实例。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务身份验证的更多信息，请参阅 [DFIR-IRIS API 文档](https://docs.dfir-iris.org/operations/api/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/iris-dfir/)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：获取方法请参阅 [DFIR-IRIS API 文档](https://docs.dfir-iris.org/operations/api/)。
- DFIR-IRIS 实例的 **Base URL（基础 URL）**。
