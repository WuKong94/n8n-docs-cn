---
title: 许可证环境变量
contentType: reference
hide:
- toc
- tags
nodeTitle: 许可证
originalFilePath: hosting/configuration/environment-variables/licenses.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/licenses
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license
description: 配置 n8n 许可证设置的环境变量，包括隐藏使用情况页面、激活和自动续订，以及指定许可证服务器 URL。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
tags:
- environment variables
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 许可证 <a id="license"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

要启用某些需要许可的功能，必须先激活许可证。可以通过界面或环境变量完成。更多信息请参阅[许可证密钥](../../manage-your-license.md)。

| 变量 | 类型 | 默认值 | 说明 |
| ----------------------------------------- | ------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `N8N_HIDE_USAGE_PAGE` | boolean | `false` | 隐藏应用中的使用情况与套餐页面。 |
| `N8N_LICENSE_ACTIVATION_KEY` | String | `''` | 用于初始化许可证的激活密钥。实例已激活时不适用。 |
| `N8N_LICENSE_AUTO_RENEW_ENABLED` | Boolean | `true` | <p>是否自动续订许可证，true 表示启用，false 表示禁用。<br>禁用后，需要每十天手动续订一次：进入 <strong>Settings（设置）</strong> > <strong>Usage and plan（使用情况与套餐）</strong>，按 <code>F5</code>。未续订会禁用所有需要许可的功能。</p> |
| `N8N_LICENSE_CERT` | String | `''` | n8n 提供的 base64 编码许可证证书。在隔离网络等特殊场景中，替代 `N8N_LICENSE_ACTIVATION_KEY` 使用。 |
| `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN` | Boolean | `true` | <p>控制实例关闭时是否将<a href="../../../../../get-started/key-concept-glossary.md#entitlement-n8n">浮动授权额度</a>释放回资源池。设为 <code>true</code>，允许其他实例复用授权；设为 <code>false</code> 则保留。<br>对于必须始终保留许可功能的生产实例，请设为 <code>false</code>。<br>多主节点模式下会忽略此设置：所有主实例共享一个席位，关闭的主实例不会释放该席位。</p> |
| `N8N_LICENSE_SERVER_URL` | String | `https://license.n8n.io/v1` | 用于获取许可证的服务器 URL。 |
| `N8N_LICENSE_TENANT_ID` | Number | `1` | 与许可证关联的租户 ID。仅在 n8n 明确要求时设置此变量。 |
| `https_proxy_license_server` | String | `https://user:pass@proxy:port` | 获取许可证时，HTTPS 请求所用的代理服务器 URL。此变量名必须为小写。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
