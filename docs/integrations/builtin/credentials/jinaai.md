---
title: Jina AI 凭据
description: Jina AI 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Jina AI 的身份验证。
contentType:
- integration
- reference
nodeTitle: Jina AI 凭据
originalFilePath: integrations/builtin/credentials/jinaai.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jinaai
url: https://docs.n8n.io/integrations/builtin/credentials/jinaai
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jina AI 凭据 <a href="#jina-ai-credentials" id="jina-ai-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Jina AI](../app-nodes/n8n-nodes-base.jinaai.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Jina AI Reader API 文档](https://r.jina.ai/docs)和 [Jina AI Search API 文档](https://s.jina.ai/docs)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

* **API key**（API 密钥）：Jina AI API 密钥。无需创建账户即可按以下步骤获取免费 API 密钥：
	1. 访问 [Jina AI 网站](https://jina.ai/)。
	2. 在页面中选择 **API**。
	3. 在 API 应用组件中选择 **API KEY & BILLING**（API 密钥与账单）。
	4. 复制标有“This is your unique key. Store it securely!”（这是你的专属密钥，请安全保存）的密钥。

Jina AI API 密钥初始包含 1,000 万个可用于非商业用途的免费 token。要充值密钥或用于商业用途，在 **API** 组件的 **API KEY & BILLING** 标签页中向下滚动，选择适合需求的充值选项。

