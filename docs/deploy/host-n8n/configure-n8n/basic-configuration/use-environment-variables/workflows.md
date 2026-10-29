---
title: 工作流环境变量
description: 配置 n8n 工作流的环境变量，包括默认名称、入门提示、标签管理和调用方策略。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 工作流
originalFilePath: hosting/configuration/environment-variables/workflows.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/workflows
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流环境变量 <a href="#workflows-environment-variables" id="workflows-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_ONBOARDING_FLOW_DISABLED` | Boolean | `false` | 是否禁用创建新工作流时的入门提示，true 表示禁用，false 表示不禁用。 |
| `N8N_WORKFLOW_ACTIVATION_BATCH_SIZE` | Number | `1` | 启动时同时发布的工作流数量。 |
| `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION` | String | `workflowsFromSameOwner` | 哪些工作流可以调用某个工作流。可选值为 `any`、`none`、`workflowsFromAList`、`workflowsFromSameOwner`。此功能需要[工作流共享](../../../../../build/manage-workflows/share-with-others.md)。 |
| `N8N_WORKFLOW_TAGS_DISABLED` | Boolean | `false` | 是否禁用工作流标签，true 表示禁用，false 表示启用。 |
| `WORKFLOWS_DEFAULT_NAME` | String | `My workflow` | 新建工作流使用的默认名称。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
