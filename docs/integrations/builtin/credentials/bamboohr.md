---
title: BambooHR 凭据
description: BambooHR 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 BambooHR 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: BambooHR 凭据
originalFilePath: integrations/builtin/credentials/bamboohr.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/bamboohr
url: https://docs.n8n.io/integrations/builtin/credentials/bamboohr
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# BambooHR 凭据 <a href="#bamboohr-credentials" id="bamboohr-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [BambooHR](../app-nodes/n8n-nodes-base.bamboohr.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [BambooHR](https://www.bamboohr.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [BambooHR API 文档](https://documentation.bamboohr.com/docs/getting-started)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 你的 BambooHR **Subdomain（子域名）**：即 `https://` 与 `.bamboohr.com` 之间的部分。
- 一个 BambooHR **API Key（API 密钥）**：生成方法请参阅 [BambooHR API 入门文档的身份验证部分](https://documentation.bamboohr.com/docs/getting-started#authentication)。

