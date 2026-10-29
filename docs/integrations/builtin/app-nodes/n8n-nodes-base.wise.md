---
title: Wise 节点文档
description: 了解如何在 n8n 中使用 Wise 节点，并按照技术文档将 Wise 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Wise 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.wise.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wise
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wise
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wise 节点 <a href="#wise-node" id="wise-node"></a>

使用 Wise 节点自动处理 Wise 中的工作，并将其与其他应用集成。n8n 内置支持多种 Wise 功能，包括获取个人资料、汇率和收款人。

本页列出了 Wise 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Wise 凭据](../credentials/wise.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Account（账户）
    * 获取此用户账户中所有币种的余额。
    * 获取此用户无国界账户中的币种。
    * 获取此用户无国界账户的对账单。
* Exchange Rate（汇率）
    * Get（获取）
* Profile（个人资料）
    * Get（获取）
    * Get All（获取全部）
* Recipient（收款人）
    * Get All（获取全部）
* Quote（报价）
    * Create（创建）
    * Get（获取）
* Transfer（汇款）
    * Create（创建）
    * Delete（删除）
    * Execute（执行）
    * Get（获取）
    * Get All（获取全部）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Wise 集成模板](https://n8n.io/integrations/wise)，或[搜索所有模板](https://n8n.io/workflows/)
