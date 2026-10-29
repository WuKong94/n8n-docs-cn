---
title: Zulip 凭据
description: Zulip 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zulip 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zulip 凭据
originalFilePath: integrations/builtin/credentials/zulip.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zulip
url: https://docs.n8n.io/integrations/builtin/credentials/zulip
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zulip 凭据 <a href="#zulip-credentials" id="zulip-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Zulip](../app-nodes/n8n-nodes-base.zulip.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zulip](https://zulip.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zulip API 文档](https://zulip.com/api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **URL**：输入 Zulip 域名对应的 URL。
- 一个 **Email（电子邮件）** 地址：输入用于登录 Zulip 的邮箱地址。
- 一个 **API Key（API 密钥）**：进入 **Gear cog > Personal Settings > Account & privacy > API Key（齿轮图标 > 个人设置 > 账号与隐私 > API 密钥）** 获取密钥。更多信息请参阅 [API 密钥](https://zulip.com/api/api-keys)。

