---
title: 表达式引擎环境变量
description: 选择 n8n 后端和编辑器的表达式引擎，并配置自托管实例的沙箱池。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 表达式引擎
originalFilePath: hosting/configuration/environment-variables/expression-engine.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/expression-engine
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 表达式引擎环境变量 <a href="#expression-engine-environment-variables" id="expression-engine-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

[表达式](../../../../../build/work-with-data/expressions-versus-data-nodes.md)是 n8n 在运行时求值的 JavaScript 片段，用于动态设置节点参数。表达式引擎负责求值。本页列出用于配置该引擎的环境变量。

{% hint style="warning" %}
**避免使用 `legacy` 表达式引擎**

`legacy` 引擎在没有隔离的情况下运行表达式，因此对恶意表达式的防护弱于沙箱引擎。n8n 计划在未来版本中弃用 `legacy`。要获得最强的安全防护：

* 保持 `N8N_EXPRESSION_ENGINE` 为后端默认值 `vm`。
* 将 `N8N_EXPRESSION_ENGINE_FRONTEND` 设为 `quickjs`。编辑器当前仍默认使用 `legacy`。
{% endhint %}

## 选择表达式引擎 <a id="choose-the-expression-engine"></a>

n8n 会在两个位置求值表达式，每处都有独立的引擎设置：

* **后端**：工作流运行时，由 n8n 服务器求值表达式，通过 `N8N_EXPRESSION_ENGINE` 选择引擎。
* **编辑器**：构建工作流时，浏览器会求值表达式，例如预览结果，通过 `N8N_EXPRESSION_ENGINE_FRONTEND` 选择引擎。

这两项设置相互独立。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_EXPRESSION_ENGINE` | 枚举字符串： `vm`, `quickjs`, `legacy` | `vm` | 后端使用的表达式引擎。`vm` 在沙箱隔离的 V8 环境中运行表达式；`quickjs` 在编译为 WebAssembly 的 QuickJS 沙箱中运行；`legacy` 不提供隔离，n8n 计划将其弃用。自 n8n 2.35.0 起，默认值为 `vm`；更早版本默认使用 `legacy`。 |
| `N8N_EXPRESSION_ENGINE_FRONTEND` | 枚举字符串： `legacy`, `quickjs` | `legacy` | 浏览器中的编辑器所用的表达式引擎。`quickjs` 在编译为 WebAssembly 的 QuickJS 沙箱中运行表达式，与页面其他部分隔离；`legacy` 不提供隔离。n8n 强烈建议使用 `quickjs`。自 n8n 2.41.0 起提供。 |

## 配置后端沙箱引擎 <a id="configure-the-sandboxed-backend-engines"></a>

以下变量配置后端的 `vm` 和 `quickjs` 引擎。当 `N8N_EXPRESSION_ENGINE` 为 `legacy` 时不生效，也不影响编辑器引擎。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_EXPRESSION_ENGINE_POOL_SIZE` | Number | `1` | 池中保持预热状态的沙箱数量。 |
| `N8N_EXPRESSION_ENGINE_MAX_CODE_CACHE_SIZE` | Number | `1024` | 缓存的已编译表达式数量上限。 |
| `N8N_EXPRESSION_ENGINE_TIMEOUT` | Number | `5000` | 每次表达式求值的执行超时，单位为毫秒。 |
| `N8N_EXPRESSION_ENGINE_MEMORY_LIMIT` | Number | `128` | 每个沙箱的内存上限，单位为 MiB。 |
| `N8N_EXPRESSION_ENGINE_IDLE_TIMEOUT` | Number | - | 设置后，无活动达到指定秒数时，池中的预热沙箱数量会缩减为零。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
