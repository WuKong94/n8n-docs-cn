---
title: GitLab 触发器节点文档
description: 了解如何在 n8n 中使用 GitLab 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitLab 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitLab 触发器节点 <a href="#gitlab-trigger-node" id="gitlab-trigger-node"></a>

[GitLab](https://gitlab.com/) 是基于网页的 DevOps 生命周期工具，提供 Git 仓库管理、Wiki、问题跟踪，以及持续集成与安装流水线等功能。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [GitLab 凭据文档](../credentials/gitlab.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [GitLab Trigger 集成](https://n8n.io/integrations/gitlab-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Comment（评论）
* Confidential issues（机密问题）
* Confidential comments（机密评论）
* Deployments（部署）
* Issue（问题）
* Job（任务）
* Merge request（合并请求）
* Pipeline（流水线）
* Push（推送）
* Release（发布版本）
* Tag（标签）
* Wiki page（Wiki 页面）

## 使用子群组和嵌套仓库 <a id="working-with-subgroups-and-nested-repositories"></a>

如果仓库位于嵌套的 GitLab 群组或子群组中，例如 `https://gitlab.com/org/subgroup1/subgroup2/my-repo`，GitLab API 要求对命名空间路径进行 URL 编码。

为嵌套子群组配置节点：

1. **Repository Owner**（仓库所有者）：输入仓库上方完整的子群组层级，将所有正斜杠（`/`）替换为 `%2F`。例如：`org%2Fsubgroup1%2Fsubgroup2`
2. **Repository Name**（仓库名称）：输入项目的仓库 slug。例如：`my-repo`

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 GitLab 提供应用节点。更多信息请参阅 [GitLab 节点文档](../app-nodes/n8n-nodes-base.gitlab.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/gitlab-trigger/)。

API 的详细信息，请参阅 [GitLab 文档](https://docs.gitlab.com/api/rest/)。
