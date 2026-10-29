---
title: CrowdStrike 凭据
description: CrowdStrike 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 CrowdStrike 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: CrowdStrike 凭据
originalFilePath: integrations/builtin/credentials/crowdstrike.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/crowdstrike
url: https://docs.n8n.io/integrations/builtin/credentials/crowdstrike
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# CrowdStrike 凭据 <a href="#crowdstrike-credentials" id="crowdstrike-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [CrowdStrike](https://www.crowdstrike.com/en-us/) 账号。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 CrowdStrike 文档。文档需要登录，必须先在其网站登录账户才能访问 API 文档。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/crowdstrike/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- CrowdStrike 实例的 **URL**。
- **Client ID**（客户端 ID）：在 Crowdstrike 的 **Support > API Clients and Keys**（支持 > API 客户端和密钥）中创建新的 API 客户端时生成。
- **Client Secret**（客户端密钥）：在 Crowdstrike 的 **Support > API Clients and Keys**（支持 > API 客户端和密钥）中创建新的 API 客户端时生成。

设置 API 客户端时，为其授予 `usermgmt:read` 作用域。n8n 依靠此作用域测试凭据是否有效。

大致步骤在 CrowdStrike 博客的 [Getting Access to the CrowdStrike API](https://www.crowdstrike.com/blog/tech-center/get-access-falcon-apis/) 中公开提供。CrowdStrike 完整文档需要登录账户后才能访问。


