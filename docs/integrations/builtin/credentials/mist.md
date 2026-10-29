---
title: Mist 凭据
description: Mist 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mist 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mist 凭据
originalFilePath: integrations/builtin/credentials/mist.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mist
url: https://docs.n8n.io/integrations/builtin/credentials/mist
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mist 凭据 <a href="#mist-credentials" id="mist-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Mist](https://www.mist.com/) 账户和组织。详细步骤请参阅[创建 Mist 账户和组织](https://www.mist.com/documentation/create-mist-org/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Mist 文档](https://www.mist.com/documentation/mist-api-introduction/)。登录 Mist 账户后，可以访问 [https://api.mist.com/api/v1/docs/Home](https://api.mist.com/api/v1/docs/Home) 查看完整 API 文档。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/mist/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- **API Token**（API 令牌）：可以使用 User API token（用户 API 令牌）或 Org API token（组织 API 令牌）。用户令牌的生成步骤，请参阅[如何生成用户 API 令牌](https://www.mist.com/documentation/using-postman/)；组织令牌的生成步骤，请参阅[组织 API 令牌](https://www.mist.com/documentation/org-api-token/)。
- 选择所在的 **Region**（地区），选项包括：
    - **Europe**（欧洲）：云环境位于任一 EMEA 地区时选择此项。
    - **Global**（全球）：云环境位于任一 global 地区时选择此项。
