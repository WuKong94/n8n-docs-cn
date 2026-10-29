---
title: 工作流历史环境变量
description: 配置 n8n 工作流历史的环境变量。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 工作流历史
originalFilePath: hosting/configuration/environment-variables/workflow-history.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/workflow-history
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流历史环境变量 <a href="#workflow-history-environment-variables" id="workflow-history-environment-variables"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `N8N_WORKFLOW_HISTORY_PRUNE_TIME` | Number | `-1` | 自动删除工作流历史版本前的保留时长，单位为小时。设为 `-1` 可永久保留所有版本。 |

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
