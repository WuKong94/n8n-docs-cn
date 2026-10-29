---
title: Trello 凭据
description: Trello 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Trello 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Trello 凭据
originalFilePath: integrations/builtin/credentials/trello.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/trello
url: https://docs.n8n.io/integrations/builtin/credentials/trello
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Trello 凭据 <a href="#trello-credentials" id="trello-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Trello](../app-nodes/n8n-nodes-base.trello.md)
- [Trello Trigger（触发器）](../trigger-nodes/n8n-nodes-base.trellotrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Trello API 文档](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Trello](https://trello.com/) 账号，以及：

- 一个 **API Key（API 密钥）**
- 一个 **API Token（API 令牌）**

如需同时生成 API Key 和 API Token，请创建 Trello Power-Up：

1. 打开 Trello 的 [Power-Up 管理门户](https://trello.com/power-ups/admin)。
2. 选择 **New**（新建）。
3. 输入 Power-Up 的 **Name**（名称），例如 `n8n integration`。
4. 选择 Power-Up 应有权访问的 **Workspace**（工作区）。
5. 将 **iframe connector URL**（iframe 连接器 URL）留空。
6. 输入适当的联系信息。
7. 选择 **Create**（创建）。
8. 此时应打开 Power-Up 的 **API Key**（API 密钥）页面。如果未打开，请手动打开。
9. 选择 **Generate a new API Key**（生成新的 API 密钥）。
10. 从 Trello 复制 **API key**（API 密钥），填入 n8n 凭据。
11. 在 Trello API 密钥页面，将 n8n 基础 URL 填入 **Allowed origin**（允许的来源）。
12. 在 **Capabilities**（功能）中，确保选中所需选项。
13. 选择 Trello **API Key**（API 密钥）旁的 **Token**（令牌）链接。
14. 出现提示时，选择 **Allow**（允许），授予请求的全部权限。
15. 复制 Trello 的 **Token**（令牌），填入 n8n 的 **API Token**（API 令牌）。

API 密钥和令牌的更多信息，请参阅 Trello 的 [API 简介](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#api-introduction)；创建 Power-Up 的更多信息，请参阅 Trello 的 [Power-Up 管理门户](https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-apps/)。
