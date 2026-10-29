---
title: npm 凭据
description: npm 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 npm 的身份验证。
contentType:
- integration
- reference
nodeTitle: npm 凭据
originalFilePath: integrations/builtin/credentials/npm.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/npm
url: https://docs.n8n.io/integrations/builtin/credentials/npm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# npm 凭据 <a href="#npm-credentials" id="npm-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [npm](../app-nodes/n8n-nodes-base.npm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [npm](https://www.npmjs.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [npm 外部集成文档](https://docs.npmjs.com/integrations/integrating-npm-with-external-services)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- 一个 **Access Token（访问令牌）**：从个人资料菜单中选择 **Access Tokens（访问令牌）**，创建令牌。详细说明请参阅 [npm 的创建和查看访问令牌文档](https://docs.npmjs.com/creating-and-viewing-access-tokens)。
- 一个 **Registry URL（包注册表 URL）**：如果使用自定义 npm 注册表，请将 **Registry URL** 更新为该注册表的地址；否则保留公共注册表地址。

