---
title: 时区与本地化环境变量
description: 设置自托管 n8n 实例的时区和默认语言区域。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 时区与本地化
originalFilePath: hosting/configuration/environment-variables/timezone-localization.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/timezone-localization
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 时区与本地化环境变量 <a href="#timezone-and-localization-environment-variables" id="timezone-and-localization-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `GENERIC_TIMEZONE` | * | `America/New_York` | n8n 实例的时区，对 Cron 等定时节点很重要。 |
| `N8N_DEFAULT_LOCALE` | String | `en` | 与 [Accept-Language 请求头](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)兼容的区域标识符。n8n 不支持 `de-AT` 这样的地区级标识符。使用非默认语言时，界面字符串按所选语言显示，未翻译的字符串回退到 `en`。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
