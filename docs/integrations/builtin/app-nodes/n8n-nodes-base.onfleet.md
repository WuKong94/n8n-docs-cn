---
title: Onfleet 节点文档
description: 了解如何在 n8n 中使用 Onfleet 节点，并按照技术文档将 Onfleet 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Onfleet 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.onfleet.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Onfleet 节点 <a href="#onfleet-node" id="onfleet-node"></a>

使用 Onfleet 节点自动处理 Onfleet 中的工作，并将其与其他应用集成。n8n 内置支持多种 Onfleet 功能，包括在 Onfleet 中创建和删除任务，以及获取组织详情。

本页列出了 Onfleet 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Onfleet 凭据](../credentials/onfleet.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Admin（管理员）
    * Create a new Onfleet admin（创建新的 Onfleet 管理员）
    * Delete an Onfleet admin（删除 Onfleet 管理员）
    * Get all Onfleet admins（获取所有 Onfleet 管理员）
    * Update an Onfleet admin（更新 Onfleet 管理员）
* Container（容器）
    * Add task at index (or append)（在指定索引位置添加任务，或追加到末尾）
    * Get container information（获取容器信息）
    * Fully replace a container's tasks（完全替换容器中的任务）
* Destination（目的地）
    * Create a new destination（创建新目的地）
    * Get a specific destination（获取指定目的地）
* Hub（配送站）
    * Create a new Onfleet hub（创建新的 Onfleet 配送站）
    * Get all Onfleet hubs（获取所有 Onfleet 配送站）
    * Update an Onfleet hub（更新 Onfleet 配送站）
* Organization（组织）
    * Retrieve your own organization's details（获取自身组织的详情）
    * Retrieve the details of an organization with which you are connected（获取与你建立连接的组织详情）
* Recipient（收件人）
    * Create a new Onfleet recipient（创建新的 Onfleet 收件人）
    * Get a specific Onfleet recipient（获取指定 Onfleet 收件人）
    * Update an Onfleet recipient（更新 Onfleet 收件人）
* Task（任务）
    * Create a new Onfleet task（创建新的 Onfleet 任务）
    * Clone an Onfleet task（克隆 Onfleet 任务）
    * Force-complete a started Onfleet task（强制完成已开始的 Onfleet 任务）
    * Delete an Onfleet task（删除 Onfleet 任务）
    * Get all Onfleet tasks（获取所有 Onfleet 任务）
    * Get a specific Onfleet task（获取指定 Onfleet 任务）
    * Update an Onfleet task（更新 Onfleet 任务）
* Team（团队）
    * Automatically dispatch tasks assigned to a team to on-duty drivers（将分配给团队的任务自动派发给在岗配送员）
    * Create a new Onfleet team（创建新的 Onfleet 团队）
    * Delete an Onfleet team（删除 Onfleet 团队）
    * Get a specific Onfleet team（获取指定 Onfleet 团队）
    * Get all Onfleet teams（获取所有 Onfleet 团队）
    * Get estimated times for upcoming tasks for a team, returns a selected driver（获取团队即将执行任务的预计时间，并返回所选配送员）
    * Update an Onfleet team（更新 Onfleet 团队）
* Worker（配送员）
    * Create a new Onfleet worker（创建新的 Onfleet 配送员）
    * Delete an Onfleet worker（删除 Onfleet 配送员）
    * Get a specific Onfleet worker（获取指定 Onfleet 配送员）
    * Get all Onfleet workers（获取所有 Onfleet 配送员）
    * Get a specific Onfleet worker schedule（获取指定 Onfleet 配送员的排班）
    * Update an Onfleet worker（更新 Onfleet 配送员）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Onfleet 集成模板](https://n8n.io/integrations/onfleet)，或[搜索所有模板](https://n8n.io/workflows/)
