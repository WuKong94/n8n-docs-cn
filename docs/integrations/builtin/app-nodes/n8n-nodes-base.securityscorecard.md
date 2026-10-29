---
title: SecurityScorecard 节点文档
description: 了解如何在 n8n 中使用 SecurityScorecard 节点，并按照技术文档将 SecurityScorecard 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: SecurityScorecard 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SecurityScorecard 节点 <a href="#securityscorecard-node" id="securityscorecard-node"></a>

使用 SecurityScorecard 节点自动处理 SecurityScorecard 中的工作，并将其与其他应用集成。n8n 内置支持多种 SecurityScorecard 功能，包括创建、更新、删除和获取公司组合，以及获取公司数据。

本页列出了 SecurityScorecard 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [SecurityScorecard 凭据](../credentials/securityscorecard.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Company（公司）
    * Get company factor scores and issue counts（获取公司的因素评分和问题数量）
    * Get company's historical factor scores（获取公司的历史因素评分）
    * Get company's historical scores（获取公司的历史评分）
    * Get company information and summary of their scorecard（获取公司信息及其评分卡摘要）
    * Get company's score improvement plan（获取公司的评分改进计划）
* Industry（行业）
    * Get Factor Scores（获取因素评分）
    * Get Historical Factor Scores（获取历史因素评分）
    * Get Score（获取评分）
* Invite（邀请）
    * Create an invite for a company/user（为公司或用户创建邀请）
* Portfolio（公司组合）
    * Create a portfolio（创建公司组合）
    * Delete a portfolio（删除公司组合）
    * Get all portfolios（获取所有公司组合）
    * Update a portfolio（更新公司组合）
* Portfolio Company（组合中的公司）
    * Add a company to portfolio（向组合添加公司）
    * Get all companies in a portfolio（获取组合中的所有公司）
    * Remove a company from portfolio（从组合移除公司）
* Report（报告）
    * Download a generated report（下载已生成的报告）
    * Generate a report（生成报告）
    * Get list of recently generated report（获取最近生成的报告列表）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 SecurityScorecard 集成模板](https://n8n.io/integrations/securityscorecard)，或[搜索所有模板](https://n8n.io/workflows/)
