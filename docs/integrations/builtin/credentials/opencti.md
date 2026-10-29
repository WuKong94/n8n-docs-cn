---
title: OpenCTI 凭据
description: OpenCTI 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 OpenCTI 的身份验证。
contentType:
- integration
- reference
nodeTitle: OpenCTI 凭据
originalFilePath: integrations/builtin/credentials/opencti.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/opencti
url: https://docs.n8n.io/integrations/builtin/credentials/opencti
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenCTI 凭据 <a href="#opencti-credentials" id="opencti-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [OpenCTI](https://filigran.io/solutions/open-cti/) 开发者账号。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [OpenCTI 文档](https://docs.opencti.io/latest/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/opencti/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**：进入 **Profile > API access（个人资料 > API 访问）** 获取密钥。更多信息请参阅 OpenCTI 的[集成身份验证文档](https://docs.opencti.io/latest/deployment/integrations/#authentication)。
