---
title: Carbon Black 凭据
description: Carbon Black 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Carbon Black 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Carbon Black 凭据
originalFilePath: integrations/builtin/credentials/carbonblack.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/carbonblack
url: https://docs.n8n.io/integrations/builtin/credentials/carbonblack
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Carbon Black 凭据 <a href="#carbon-black-credentials" id="carbon-black-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 订阅 [Carbon Black](https://www.broadcom.com/products/carbon-black/threat-prevention/carbon-black-cloud)。
- 创建一个 [Carbon Black 开发者账号](https://developer.carbonblack.com/)。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Carbon Black 文档](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/carbon-black/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **URL**：取决于使用的环境或产品 URL，可以通过 Carbon Black Cloud 控制台的网页地址找到。更多信息请参阅 [Carbon Black URL 组成部分文档](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#the-url-parts)。
- 一个 **Access Token（访问令牌）**：按照 [Carbon Black 的创建 API 密钥文档](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#carbon-black-cloud-manages-identities-and-roles)创建密钥，再将 **API Secret Key（API 密钥机密值）** 填入 n8n 的 **Access Token** 字段。
