---
title: Metabase 凭据
description: Metabase 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Metabase 的身份验证。
contentType:
- integration
- reference
nodeTitle: Metabase 凭据
originalFilePath: integrations/builtin/credentials/metabase.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/metabase
url: https://docs.n8n.io/integrations/builtin/credentials/metabase
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Metabase 凭据 <a href="#metabase-credentials" id="metabase-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Metabase 节点](../app-nodes/n8n-nodes-base.metabase.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个可以访问 Metabase 实例的 [Metabase](https://www.metabase.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Metabase API 文档](https://www.metabase.com/docs/latest/api-documentation)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 一个 **URL**：输入 Metabase 实例的基础 URL。如果使用自定义域名，请输入该域名对应的 URL。
- 一个 **Username（用户名）**：输入 Metabase 用户名。
- 一个 **Password（密码）**：输入 Metabase 密码。
