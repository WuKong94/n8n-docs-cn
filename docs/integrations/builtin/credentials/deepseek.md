---
title: DeepSeek 凭据
description: DeepSeek 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 DeepSeek 的身份验证。
contentType:
- integration
- reference
priority: critical
nodeTitle: DeepSeek 凭据
originalFilePath: integrations/builtin/credentials/deepseek.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/deepseek
url: https://docs.n8n.io/integrations/builtin/credentials/deepseek
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# DeepSeek 凭据 <a href="#deepseek-credentials" id="deepseek-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Chat DeepSeek](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [DeepSeek](https://platform.deepseek.com/sign_up) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DeepSeek API 文档](https://api-docs.deepseek.com/api/deepseek-api)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

生成 API 密钥：

1. 登录 DeepSeek 账户，或[创建](https://platform.deepseek.com/sign_up)账户。
2. 打开 [API 密钥](https://platform.deepseek.com/api_keys)页面。
3. 选择 **Create new secret key**（创建新密钥），创建 API 密钥，也可以为密钥命名。
4. 复制密钥，填入 n8n 的 **API Key** 字段。

更多信息，请参阅[首次 API 调用](https://api-docs.deepseek.com/)页面。
