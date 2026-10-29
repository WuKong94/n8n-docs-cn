---
title: 安全环境变量
description: 配置自托管 n8n 实例的身份验证和环境变量访问。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 安全
originalFilePath: hosting/configuration/environment-variables/security.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/security
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安全环境变量 <a href="#security-environment-variables" id="security-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | Boolean | `false` | 是否允许用户在表达式和 Code 节点中访问环境变量，false 表示允许，true 表示不允许。 |
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | Boolean | `true` | 设为 `true`，禁止访问 `.n8n` 目录中的所有文件及用户自定义配置文件。 |
| `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS` | Boolean | `false` | 设为 `true`，尝试将设置文件权限设为 0600，仅允许所有者读写。 |
| `N8N_RESTRICT_FILE_ACCESS_TO` | String |  | 将文件访问限制在这些目录中。多个文件以分号分隔，即“`;`”。 |
| `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` | Number | 90 | 工作流未执行多少天后被视为闲置。 |
| `N8N_CONTENT_SECURITY_POLICY` | String | `script-src <nonce> 'strict-dynamic' 'unsafe-eval'; object-src 'none'; base-uri 'none'` | n8n 在自身页面提供的 [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)。接受策略字符串，例如 `frame-ancestors http://localhost:3000`，或 [helmet.js](https://helmetjs.github.io/#content-security-policy) 指令对象。使用 `<nonce>` 标记 n8n 插入每请求 nonce 的位置。设为 `default` 使用 n8n 策略，设为 `{}` 则不发送该响应头。 |
| `N8N_CONTENT_SECURITY_POLICY_REPORT_ONLY` | String |  | n8n 通过 `Content-Security-Policy-Report-Only` 提供的策略，格式与 `N8N_CONTENT_SECURITY_POLICY` 相同。浏览器会报告违规但不阻止，可先试用策略，再强制实施。 |
| `N8N_SECURE_COOKIE` | Boolean | `true` | 确保 Cookie 仅通过 HTTPS 发送，以提高安全性。 |
| `N8N_SAMESITE_COOKIE` | 枚举字符串： `strict`, `lax`, `none` | `lax` | 控制跨站 Cookie 行为（[了解更多](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)）：<ul><li>`strict`：仅对第一方请求发送。</li><li>`lax`，默认值：随顶层导航请求发送。</li><li>`none`：在所有上下文中发送，需要 HTTPS。</li></ul> |
| `N8N_GIT_NODE_DISABLE_BARE_REPOS` | Boolean | `false` | 设为 `true`，禁止 [Git 节点](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.git.md)操作裸仓库，以提高安全性。 |
| `N8N_GIT_NODE_ENABLE_HOOKS` | Boolean | `false` | 设为 `true`，允许 [Git 节点](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.git.md)执行 Git 钩子。 |
| `N8N_POSTMESSAGE_ALLOWED_ORIGINS` | String |  | 将编辑器嵌入其他页面时，允许与其交换 `postMessage` 命令的源。仅在能够嵌入编辑器时适用，例如以 `N8N_PREVIEW_MODE=true` 运行。多个源以逗号分隔，例如 `https://n8n.io,https://app.example.com`。默认留空时，编辑器接受任意源的消息。 |

## 通过环境变量管理安全策略 <a href="#security-policy-using-environment-variables" id="security-policy-using-environment-variables"></a>

将 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 设为 `true`，通过环境变量管理安全策略。启用机制请参阅[通过环境变量管理实例设置](../../manage-settings-using-environment-variables.md)。

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/security-policy.md" %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
