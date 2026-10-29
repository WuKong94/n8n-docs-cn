---
title: 节点环境变量
description: 配置自托管 n8n 的节点管理和节点专用限制的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 节点
originalFilePath: hosting/configuration/environment-variables/nodes.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/nodes
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点环境变量 <a href="#nodes-environment-variables" id="nodes-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

本页列出 n8n 节点[^1]管理的环境变量，包括指定加载或排除的节点、在 Code 节点中导入内置或外部模块、启用社区节点，以及配置节点专用限制。

## 节点和社区节点设置 <a href="#nodes-and-community-node-settings" id="nodes-and-community-node-settings"></a>

| 变量 | 类型 | 默认值 | 说明 |
|:-----------------------------------------|:-----------------|:------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `N8N_COMMUNITY_PACKAGES_AUTH_TOKEN` | String | - | 私有 npm 注册表的身份验证令牌。与 `N8N_COMMUNITY_PACKAGES_REGISTRY` 配合，为从私有注册表安装社区节点时的请求验证身份。 |
| `N8N_COMMUNITY_PACKAGES_ENABLED` | Boolean | `true` | 是否允许安装和加载社区节点，true 表示启用，false 表示禁用。设为 false 时，不论各自设置如何，经过验证和未经验证的社区节点包都不可用。 |
| `N8N_COMMUNITY_PACKAGES_PREVENT_LOADING` | Boolean | `false` | 是否阻止实例启动时加载已安装的社区节点，true 表示阻止，false 表示允许。故障节点导致实例无法启动时，可使用此设置。 |
| `N8N_COMMUNITY_PACKAGES_REGISTRY` | String | `https://registry.npmjs.org` | 用于获取社区节点包的 npm 注册表 URL，需要许可证。 |
| `N8N_CUSTOM_EXTENSIONS` | String | - | 指定包含自定义节点的目录路径。 |
| `N8N_PYTHON_ENABLED` | Boolean | `true` | 是否在 Code 节点中启用 Python 执行。 |
| `N8N_UNVERIFIED_PACKAGES_ENABLED` | Boolean | `true` | 当 `N8N_COMMUNITY_PACKAGES_ENABLED` 为 true 时，控制是否允许安装和使用 npm 注册表中未经验证的社区节点，true 表示允许，false 表示不允许。 |
| `N8N_VERIFIED_PACKAGES_ENABLED` | Boolean | `true` | 当 `N8N_COMMUNITY_PACKAGES_ENABLED` 为 true 时，控制是否在节点面板中显示经过验证的社区节点以供安装和使用，true 表示显示，false 表示隐藏。 |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | 允许用户在 Code 节点中导入指定的内置模块。使用 * 可允许全部模块。n8n 默认禁止导入模块。 |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | 允许用户在 Code 节点中导入指定的外部模块，模块来源为 `n8n/node_modules`。n8n 默认禁止导入模块。 |
| `NODES_ERROR_TRIGGER_TYPE` | String | `n8n-nodes-base.errorTrigger` | 指定用作 Error Trigger 的节点类型。 |
| `NODES_EXCLUDE` | 字符串数组 | `[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.localFileTrigger\"]` | 指定不加载的节点。例如，用户不可信时，可阻止具有安全风险的节点：`NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"@n8n/n8n-nodes-langchain.lmChatDeepSeek\"]"`。要启用所有节点，指定 `NODES_EXCLUDE: "[]"`。 |
| `NODES_INCLUDE` | 字符串数组 | - | 指定要加载的节点。 |
| `NODES_MERGE_SQL_SANDBOX_MEMORY_LIMIT_MB` | Number | `64` | Merge 节点 SQL 沙箱的内存上限，单位为 MB。Combine by SQL 处理大数据集失败，且实例有足够内存时，可以提高此值。 |

## Compression 节点设置 <a href="#compression-node-settings" id="compression-node-settings"></a>

| 变量 | 类型 | 默认值 | 说明 |
|:-----------------------------------------------------|:-------|:---------------|:-------------------------------------------------------------------------------------|
| `N8N_COMPRESSION_NODE_MAX_DECOMPRESSED_SIZE_BYTES` | Number | `268435456` | 解压后输出的总大小上限，单位为字节。默认为 256 MiB。 |
| `N8N_COMPRESSION_NODE_MAX_ZIP_ENTRIES` | Number | `1000` | ZIP 压缩包允许的最大条目数量。 |

## 管理已安装的社区节点包 <a href="#manage-installed-community-packages" id="manage-installed-community-packages"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.21.0 起，支持通过环境变量管理已安装的社区节点包。
{% endhint %}

通过环境变量预配置已安装的[社区节点包](../../../../../integrations/community-nodes/installation-and-management/README.md)。有关 `*_MANAGED_BY_ENV` 机制，请参阅[通过环境变量管理实例设置](../../manage-settings-using-environment-variables.md)。

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/community-packages.md" %}

[^1]: 在 n8n 中，节点是组成工作流的独立组件。节点定义工作流何时运行，获取、发送和处理数据，控制流程逻辑，并连接外部服务。

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
