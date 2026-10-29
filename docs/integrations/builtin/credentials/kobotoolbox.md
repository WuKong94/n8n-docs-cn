---
title: KoboToolbox 凭据
description: KoboToolbox 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 KoboToolbox 的身份验证。
contentType:
- integration
- reference
nodeTitle: KoboToolbox 凭据
originalFilePath: integrations/builtin/credentials/kobotoolbox.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox
url: https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# KoboToolbox 凭据 <a href="#kobotoolbox-credentials" id="kobotoolbox-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [KoboToolbox 触发器](../trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md)
* [KoboToolbox](../app-nodes/n8n-nodes-base.kobotoolbox.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [KoboToolbox](https://www.kobotoolbox.org/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [KoboToolbox API 文档](https://support.kobotoolbox.org/api.html)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **API Root URL（API 根 URL）**：输入创建账号所在的 KoboToolbox 服务器 URL。对于全球 KoboToolbox 服务器，使用 `https://kf.kobotoolbox.org`；对于欧盟 KoboToolbox 服务器，使用 `https://eu.kobotoolbox.org`。
- 一个 **API Token（API 令牌）**：在 **Account Settings（账号设置）** 中显示。更多信息请参阅[获取 API 令牌](https://support.kobotoolbox.org/api.html#getting-your-api-token)。
