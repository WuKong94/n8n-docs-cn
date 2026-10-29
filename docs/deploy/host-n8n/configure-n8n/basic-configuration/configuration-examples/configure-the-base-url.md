---
title: 配置 n8n 前端访问所用的 Base URL
description: 通过配置 Base URL 环境变量，定义 n8n 前端访问后端 REST API 的路径。
contentType: howto
nodeTitle: 配置 Base URL
originalFilePath: hosting/configuration/configuration-examples/base-url.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/base-url
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 配置 n8n 前端访问所用的 Base URL <a href="#configure-the-base-url-for-n8ns-front-end-access" id="configure-the-base-url-for-n8ns-front-end-access"></a>

{% hint style="warning" %}
**需要手动构建界面**

此场景需要配置 `VUE_APP_URL_BASE_API` 环境变量，并手动构建 `n8n-editor-ui` 包。默认 n8n Docker 镜像不支持这样使用，该镜像中此变量的默认值为 `/`，表示使用根域名。
{% endhint %}

可以配置前端连接后端 REST API 所用的 Base URL。在希望分别托管 n8n 前端和后端时，此设置会有帮助。

```bash
export VUE_APP_URL_BASE_API=https://n8n.example.com/
```
此变量的更多信息请参阅[环境变量参考](../use-environment-variables/deployment.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
