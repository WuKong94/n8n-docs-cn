---
title: SecurityScorecard 凭据
description: SecurityScorecard 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SecurityScorecard 的身份验证。
contentType:
- integration
- reference
nodeTitle: SecurityScorecard 凭据
originalFilePath: integrations/builtin/credentials/securityscorecard.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/securityscorecard
url: https://docs.n8n.io/integrations/builtin/credentials/securityscorecard
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SecurityScorecard 凭据 <a href="#securityscorecard-credentials" id="securityscorecard-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SecurityScorecard](../app-nodes/n8n-nodes-base.securityscorecard.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SecurityScorecard](https://securityscorecard.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [SecurityScorecard 开发者文档](https://securityscorecard.readme.io/docs/integrate-ratings-platform-services)和 [API 文档](https://securityscorecard.readme.io/reference/introduction)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：可通过以下任一方式生成：
    * 以普通用户身份，在 [**My Settings > API**](https://platform.securityscorecard.io/#/my-settings/api)（我的设置 > API）中生成。更多信息请参阅[获取 API 密钥](https://securityscorecard.readme.io/docs/getting-started#step-1-get-an-api-key)。
    * 以机器人用户身份，查看该机器人用户并选择 **create token**（创建令牌）。更多信息请参阅[使用机器人用户进行身份验证](https://securityscorecard.readme.io/docs/authentication#)。

