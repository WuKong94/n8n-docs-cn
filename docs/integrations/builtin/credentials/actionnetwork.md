---
title: Action Network 凭据
description: Action Network 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Action Network 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Action Network 凭据
originalFilePath: integrations/builtin/credentials/actionnetwork.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/actionnetwork
url: https://docs.n8n.io/integrations/builtin/credentials/actionnetwork
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Action Network 凭据 <a href="#action-network-credentials" id="action-network-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Action Network](../app-nodes/n8n-nodes-base.actionnetwork.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何使用该服务的更多信息，请参阅 [Action Network API 文档](https://actionnetwork.org/docs/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个[已启用 API 密钥访问](#request-api-access)的 [Action Network](https://actionnetwork.org/) 账户，以及：

- 一个 **API Key（API 密钥）**

获取 API 密钥：

1. 登录你的 Action Network 账户。
2. 从 **Start Organizing**（开始组织活动）菜单选择 **Details >** [**API & Sync**](https://actionnetwork.org/apis)（详情 > API 与同步）。
3. 选择要为其生成 API 密钥的列表。
4. 为该列表生成 API 密钥。
5. 复制 **API Key**（API 密钥），填入 n8n 凭据。

更多信息请参阅 [Action Network API 身份验证说明](https://actionnetwork.org/docs/v2/#auth)。

## 申请 API 访问权限 <a href="#request-api-access" id="request-api-access"></a>

Action Network 中的每个用户账户和群组都有独立的 API 密钥，用于访问该用户或群组的数据。

必须明确向 Action Network 申请 API 访问权限，可通过以下两种方式之一：

1. 如果已经是付费客户，请[联系他们](https://actionnetwork.org/contact)申请合作伙伴访问权限。合作伙伴访问包含 API 密钥访问。
2. 如果是开发者，请[申请开发者账户](https://actionnetwork.org/developers)。账户申请获批后，即可获得 API 密钥访问权限。
