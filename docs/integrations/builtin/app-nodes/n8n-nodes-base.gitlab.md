---
title: GitLab 节点文档
description: 了解如何在 n8n 中使用 GitLab 节点，并按照技术文档将 GitLab 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitLab 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitLab 节点 <a href="#gitlab-node" id="gitlab-node"></a>

使用 GitLab 节点自动处理 GitLab 中的工作，并将其与其他应用集成。n8n 内置支持多种 GitLab 功能，包括创建、更新、删除和编辑议题、仓库、发布版本及用户。

本页列出了 GitLab 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [GitLab 凭据](../credentials/gitlab.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* File（文件）
    * Create（创建）
    * Delete（删除）
    * Edit（编辑）
    * Get（获取）
    * List（列出）
* Issue（议题）
    * Create a new issue（创建新议题）
    * Create a new comment on an issue（在议题中创建新评论）
    * Edit an issue（编辑议题）
    * Get the data of a single issue（获取单个议题的数据）
    * Lock an issue（锁定议题）
* Release（发布版本）
    * Create a new release（创建新发布版本）
    * Delete a new release（删除新发布版本）
    * Get a new release（获取新发布版本）
    * Get all releases（获取全部发布版本）
    * Update a new release（更新新发布版本）
* Repository（仓库）
    * Get the data of a single repository（获取单个仓库的数据）
    * Returns issues of a repository（返回仓库的议题）
* User（用户）
    * Returns the repositories of a user（返回用户的仓库）

## 使用子群组和嵌套仓库 <a id="working-with-subgroups-and-nested-repositories"></a>

如果仓库位于嵌套的 GitLab 群组或子群组中，例如 `https://gitlab.com/org/subgroup1/subgroup2/my-repo`，GitLab API 要求对命名空间路径进行 URL 编码。

为嵌套子群组配置节点：

1. **Project Owner**（项目所有者）：输入仓库上方完整的子群组层级，将所有正斜杠（`/`）替换为 `%2F`。例如：`org%2Fsubgroup1%2Fsubgroup2`
2. **Project Name**（项目名称）：输入项目的仓库 slug。例如：`my-repo`


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 GitLab 集成模板](https://n8n.io/integrations/gitlab)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GitLab 文档](https://docs.gitlab.com/ee/api/rest/)。

n8n 为 GitLab 提供触发器节点。更多信息请参阅 [GitLab Trigger 节点文档](../trigger-nodes/n8n-nodes-base.gitlabtrigger.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

