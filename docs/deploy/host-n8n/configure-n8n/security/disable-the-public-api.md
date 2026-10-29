---
title: 禁用公共 REST API
description: 禁用 n8n 公共 REST API，防止其他人使用。
contentType: howto
nodeTitle: 禁用公共 API
originalFilePath: hosting/securing/disable-public-api.md
originalUrl: https://docs.n8n.io/hosting/securing/disable-public-api
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 禁用公共 REST API <a href="#disable-the-public-rest-api" id="disable-the-public-rest-api"></a>

[n8n 公共 REST API](../../../../connect/n8n-api/README.md)允许你通过程序完成许多与图形界面中相同的任务。

如果不打算使用此 API，n8n 建议禁用，以提高安装环境的安全性。

要禁用[公共 REST API](../../../../connect/n8n-api/README.md)，将 `N8N_PUBLIC_API_DISABLED` 环境变量设为 `true`，例如：

```bash
export N8N_PUBLIC_API_DISABLED=true
```

## 禁用 API 调试界面 <a href="#disable-the-api-playground" id="disable-the-api-playground"></a>

要禁用 [API 调试界面](../../../../connect/n8n-api/use-an-api-playground.md)，将 `N8N_PUBLIC_API_SWAGGERUI_DISABLED` 环境变量设为 `true`，例如：

```bash
export N8N_PUBLIC_API_SWAGGERUI_DISABLED=true
```

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [部署环境变量](../basic-configuration/use-environment-variables/deployment.md)：这些环境变量的更多信息。
* [配置](../basic-configuration.md)：如何设置环境变量。
