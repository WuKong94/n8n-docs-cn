---
title: 外部钩子环境变量
description: 用于在自托管 n8n 实例中集成外部钩子的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 外部钩子
originalFilePath: hosting/configuration/environment-variables/external-hooks.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/external-hooks
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部钩子环境变量 <a href="#external-hooks-environment-variables" id="external-hooks-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

可以定义外部钩子，让 n8n 在特定操作运行时执行。完整参考，包括可用钩子和文件格式，请参阅[外部钩子](../../external-hooks.md)。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------ | :---------- |
| `EXTERNAL_HOOK_FILES` | String | - | 包含后端外部钩子的文件。提供多个文件时，使用 `EXTERNAL_HOOK_FILES_SEPARATOR` 定义的字符分隔。 |
| `EXTERNAL_HOOK_FILES_SEPARATOR` | String | `:` | `EXTERNAL_HOOK_FILES` 使用的分隔符。在 Windows 上使用 `;`，以避免与 `C:\` 这样的盘符路径冲突。 |
| `EXTERNAL_FRONTEND_HOOKS_URLS` | String | - | 包含前端外部钩子的文件 URL。多个 URL 以冒号分隔，即“`:`”。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
