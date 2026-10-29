---
title: Vercel AI Gateway 凭据
description: Vercel AI Gateway 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Vercel AI Gateway 的身份验证。
contentType:
- integration
- reference
priority: critical
nodeTitle: Vercel AI Gateway 凭据
originalFilePath: integrations/builtin/credentials/vercel.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/vercel
url: https://docs.n8n.io/integrations/builtin/credentials/vercel
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Vercel AI Gateway 凭据 <a href="#vercel-ai-gateway-credentials" id="vercel-ai-gateway-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Chat Vercel AI Gateway](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Vercel](https://vercel.com/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）
- OIDC token（OIDC 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Vercel AI Gateway 文档](https://vercel.com/docs/ai-gateway)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**

生成 API 密钥：

1. [登录 Vercel](https://vercel.com/login) 或[创建账户](https://vercel.com/signup)。
2. 进入 Vercel 控制台，选择 **AI Gateway** 标签页。
3. 在左侧边栏选择 **API keys**（API 密钥）。
4. 选择 **Add key**（添加密钥），再在对话框中选择 **Create key**（创建密钥）。
4. 复制密钥，填入 n8n 的 **API Key** 字段。

## 使用 OIDC 令牌 <a href="#using-oidc-token" id="using-oidc-token"></a>

配置此凭据需要：

- 一个 **OIDC token**（OIDC 令牌）

生成 OIDC 令牌的步骤如下：

1. 本地开发时，使用 `vc link` 命令将应用关联到 Vercel 项目。
2. 运行 `vercel env pull` 命令，从 Vercel 拉取环境变量。
3. 复制令牌，将其添加到 n8n 的 **OIDC TOKEN** 字段。
