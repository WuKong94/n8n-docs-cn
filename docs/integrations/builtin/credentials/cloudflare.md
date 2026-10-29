---
title: Cloudflare 凭据
description: Cloudflare 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cloudflare 的身份验证。
contentType:
- integration
- reference
nodeTitle: Cloudflare 凭据
originalFilePath: integrations/builtin/credentials/cloudflare.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cloudflare
url: https://docs.n8n.io/integrations/builtin/credentials/cloudflare
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cloudflare 凭据 <a href="#cloudflare-credentials" id="cloudflare-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Cloudflare 节点](../app-nodes/n8n-nodes-base.cloudflare.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cloudflare 账号](https://developers.cloudflare.com/fundamentals/setup/account/)。
- [添加域名](https://developers.cloudflare.com/fundamentals/setup/manage-domains/add-site/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cloudflare API 文档](https://developers.cloudflare.com/fundamentals/api/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **API token（API 令牌）**：按照 [Cloudflare 文档创建 API 令牌](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)。

