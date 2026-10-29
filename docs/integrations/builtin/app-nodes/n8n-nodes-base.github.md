---
title: GitHub 节点文档
description: 了解如何在 n8n 中使用 GitHub 节点，并按照技术文档将 GitHub 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitHub 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.github.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitHub 节点 <a href="#github-node" id="github-node"></a>

使用 GitHub 节点自动处理 GitHub 中的工作，并将其与其他应用集成。n8n 内置支持多种 GitHub 功能，包括创建、更新、删除和编辑文件、仓库、议题、拉取请求、发布版本及用户。

本页列出了 GitHub 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [GitHub 凭据](../credentials/github.md)。
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
    * Create（创建）
    * Create Comment（创建评论）
    * Edit（编辑）
    * Get（获取）
    * Lock（锁定）
* Organization（组织）
    * Get Repositories（获取仓库）
* Pull Request（拉取请求）
    * Close（关闭）
    * Create（创建）
    * Create Comment（创建评论）
    * Edit Comment（编辑评论）
    * Get（获取）
    * Get Diff（获取差异）
    * Get Patch（获取补丁）
    * Merge（合并）
    * Reopen（重新打开）
    * Update（更新）
* Release（发布版本）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Update（更新）
* Repository（仓库）
    * Get（获取）
    * Get Issues（获取议题）
    * Get License（获取许可证）
    * Get Profile（获取个人资料）
    * Get Pull Requests（获取拉取请求）
    * List Popular Paths（列出热门路径）
    * List Referrers（列出引荐来源）
* Review（评价）
    * Create（创建）
    * Get（获取）
    * Get Many（获取多条）
    * Update（更新）
* User（用户）
    * Get Repositories（获取仓库）
    * Invite（邀请）
* Workflow（工作流）
    * Disable（禁用）
    * Dispatch（触发运行）
    * Enable（启用）
    * Get（获取）
    * Get Usage（获取用量）
    * List（列出）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 GitHub 集成模板](https://n8n.io/integrations/github)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

