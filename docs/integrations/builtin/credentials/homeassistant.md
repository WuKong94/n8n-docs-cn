---
title: Home Assistant 凭据
description: Home Assistant 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Home Assistant 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Home Assistant 凭据
originalFilePath: integrations/builtin/credentials/homeassistant.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/homeassistant
url: https://docs.n8n.io/integrations/builtin/credentials/homeassistant
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Home Assistant 凭据 <a href="#home-assistant-credentials" id="home-assistant-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Home Assistant](../app-nodes/n8n-nodes-base.homeassistant.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Home Assistant API 文档](https://developers.home-assistant.io/docs/api/rest)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要先[安装](https://www.home-assistant.io/installation/) Home Assistant，创建 [Home Assistant](https://www.home-assistant.io/getting-started/onboarding) 账户，并准备：

- **Host**（主机）
- **Port**（端口）
- 长期有效的 **Access Token**（访问令牌）

生成访问令牌并设置凭据的步骤如下：

1. 如需生成 **Access Token**（访问令牌），请登录 Home Assistant 并打开[用户资料](https://my.home-assistant.io/redirect/profile)。
2. 在 **Long-Lived Access Tokens**（长期访问令牌）部分，生成新令牌。
3. 复制此令牌，在 n8n 中填入 **Access Token**（访问令牌）。
4. 输入 Home Assistant **Host**（主机）的 URL 或 IP 地址，不包含 `http://` 或 `https://` 协议，例如 `your.awesome.home`。
5. 在 **Port**（端口）中输入适当端口：
    - 未更改端口且通过 `http://` 访问 Home Assistant 时，保留默认值 `8123`。
    - 未更改端口且通过 `https://` 访问 Home Assistant 时，输入 `443`。
    - 如果已将 Home Assistant 配置为使用特定端口，请输入该端口。
6. 如果在 Home Assistant 的 [config.yml 映射键](https://developers.home-assistant.io/docs/add-ons/configuration/?_highlight=ssl#add-on-configuration)中启用了 SSL，请在 n8n 中开启 **SSL** 开关。如果不确定，通过 `https://` 而非 `http://` 访问 Home Assistant 界面时，最好开启此设置。

