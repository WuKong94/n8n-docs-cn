---
title: Kitemaker 节点文档
description: 了解如何在 n8n 中使用 Kitemaker 节点，并按照技术文档将 Kitemaker 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Kitemaker 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.kitemaker.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kitemaker
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kitemaker
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Kitemaker 节点 <a href="#kitemaker-node" id="kitemaker-node"></a>

使用 Kitemaker 节点自动处理 Kitemaker 中的工作，并将其与其他应用集成。n8n 内置支持多种 Kitemaker 功能，包括获取组织、空间和用户的数据，以及创建、获取和更新工作项。

本页列出了 Kitemaker 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Kitemaker 凭据](../credentials/kitemaker.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Organization（组织）
    * Retrieve data on the logged-in user's organization.（获取当前登录用户所属组织的数据）
* Space（空间）
    * Retrieve data on all the spaces in the logged-in user's organization.（获取当前登录用户所属组织中全部空间的数据）
* User（用户）
    * Retrieve data on all the users in the logged-in user's organization.（获取当前登录用户所属组织中全部用户的数据）
* Work Item（工作项）
    * Create（创建）
    * Get（获取）
    * Get All（获取全部）
    * Update（更新）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Kitemaker 集成模板](https://n8n.io/integrations/kitemaker)，或[搜索所有模板](https://n8n.io/workflows/)
