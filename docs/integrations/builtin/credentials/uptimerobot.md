---
title: UptimeRobot 凭据
description: UptimeRobot 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 UptimeRobot 的身份验证。
contentType:
- integration
- reference
nodeTitle: UptimeRobot 凭据
originalFilePath: integrations/builtin/credentials/uptimerobot.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/uptimerobot
url: https://docs.n8n.io/integrations/builtin/credentials/uptimerobot
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# UptimeRobot 凭据 <a href="#uptimerobot-credentials" id="uptimerobot-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [UptimeRobot](../app-nodes/n8n-nodes-base.uptimerobot.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [UptimeRobot](https://uptimerobot.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [UptimeRobot API 文档](https://uptimerobot.com/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 **My Settings > API Settings**（我的设置 > API 设置）中获取。创建一个 **Main API Key**（主 API 密钥），填入 n8n 凭据。

### API 密钥类型 <a href="#api-key-types" id="api-key-types"></a>

UptimeRobot 支持三种 API 密钥类型：

- **Account-specific**（账户专用，也称 **main**）：获取多个监控项的数据。
- **Monitor-specific**（监控项专用）：获取单个监控项的数据。
- **Read-only**（只读）：仅执行 `GET` API 调用。

要执行 UptimeRobot 节点的全部操作，请使用 **Main** 或 **Account-specific** API 密钥。更多信息请参阅 [API 身份验证](https://uptimerobot.com/api/#auth)。
