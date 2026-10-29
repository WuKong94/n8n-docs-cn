---
title: SyncroMSP 节点文档
description: 了解如何在 n8n 中使用 SyncroMSP 节点，并按照技术文档将 SyncroMSP 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: SyncroMSP 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.syncromsp.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SyncroMSP 节点 <a href="#syncromsp-node" id="syncromsp-node"></a>

使用 SyncroMSP 节点自动处理 SyncroMSP 中的工作，并将其与其他应用集成。n8n 内置支持多种 SyncroMSP 功能，包括创建和删除客户、工单及联系人。

本页列出了 SyncroMSP 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [SyncroMSP 凭据](../credentials/syncromsp.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Contact（联系人）
    * Create new contact（创建新联系人）
    * Delete contact（删除联系人）
    * Retrieve contact（获取联系人）
    * Retrieve all contacts（获取全部联系人）
    * Update contact（更新联系人）
* Customer（客户）
    * Create new customer（创建新客户）
    * Delete customer（删除客户）
    * Retrieve customer（获取客户）
    * Retrieve all customers（获取全部客户）
    * Update customer（更新客户）
* RMM（远程监控与管理）
    * Create new RMM Alert（创建 RMM 告警）
    * Delete RMM Alert（删除 RMM 告警）
    * Retrieve RMM Alert（获取 RMM 告警）
    * Retrieve all RMM Alerts（获取全部 RMM 告警）
    * Mute RMM Alert（静默 RMM 告警）
* Ticket（工单）
    * Create new ticket（创建新工单）
    * Delete ticket（删除工单）
    * Retrieve ticket（获取工单）
    * Retrieve all tickets（获取全部工单）
    * Update ticket（更新工单）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 SyncroMSP 集成模板](https://n8n.io/integrations/syncromsp)，或[搜索所有模板](https://n8n.io/workflows/)
