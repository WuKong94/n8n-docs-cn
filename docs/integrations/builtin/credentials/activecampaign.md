---
title: ActiveCampaign 凭据
description: ActiveCampaign 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 ActiveCampaign 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: ActiveCampaign 凭据
originalFilePath: integrations/builtin/credentials/activecampaign.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/activecampaign
url: https://docs.n8n.io/integrations/builtin/credentials/activecampaign
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# ActiveCampaign 凭据 <a href="#activecampaign-credentials" id="activecampaign-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [ActiveCampaign](../app-nodes/n8n-nodes-base.activecampaign.md)
- [Active Campaign Trigger（触发器）](../trigger-nodes/n8n-nodes-base.activecampaigntrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何使用该服务的更多信息，请参阅 [ActiveCampaign API 文档](https://help.activecampaign.com/hc/en-us/sections/360005740979-ActiveCampaign-API-Resources)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [ActiveCampaign](https://www.activecampaign.com/) 账号，以及：

- **API URL**
- 一个 **API Key（API 密钥）**

获取这两个值并设置凭据：

1. 在 ActiveCampaign 左侧菜单中选择 **Settings**（设置，齿轮图标）。
2. 选择 **Developer**（开发者）。
3. 复制 **API URL**，填入 n8n 凭据。
4. 复制 **API Key**（API 密钥），填入 n8n 凭据。

更多信息或重置 API 密钥的步骤，请参阅[如何获取 ActiveCampaign API URL 和密钥](https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#h_01HJ6REM2YQW19KYPB189726ST)。
