---
title: 源代码控制环境变量
description: 设置源代码控制默认 SSH 密钥类型的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 源代码控制
originalFilePath: hosting/configuration/environment-variables/source-control.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/source-control
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 源代码控制环境变量 <a href="#source-control-environment-variables" id="source-control-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

n8n 通过基于 Git 的源代码控制支持多环境。有关连接 Git 仓库到实例及配置源代码控制的说明，请参阅[源代码控制与环境](../../../../../administer/use-source-control-and-environments/set-up-source-control.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE` | String | `ed25519` | 设为 `rsa`，将[源代码控制设置](../../../../../administer/use-source-control-and-environments/set-up-source-control.md)中的默认 SSH 密钥类型设为 RSA。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
