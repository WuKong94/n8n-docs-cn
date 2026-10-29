---
title: Rundeck 节点文档
description: 了解如何在 n8n 中使用 Rundeck 节点，并按照技术文档将 Rundeck 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Rundeck 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.rundeck.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Rundeck 节点 <a href="#rundeck-node" id="rundeck-node"></a>

使用 Rundeck 节点自动处理 Rundeck 中的工作，并将其与其他应用集成。n8n 内置支持执行任务和获取元数据。

本页列出了 Rundeck 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Rundeck 凭据](../credentials/rundeck.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

- **Job**（任务）
    - Execute a job（执行任务）
    - Get metadata of a job（获取任务元数据）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Rundeck 集成模板](https://n8n.io/integrations/rundeck)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

## 查找任务 ID <a href="#find-the-job-id" id="find-the-job-id"></a>

1. 打开 Rundeck 控制台。
2. 打开包含所需任务的项目，该任务将供 n8n 使用。
3. 在侧边栏中选择 **JOBS**（任务）。
4. 在 **All Jobs**（全部任务）下，选择要与 n8n 配合使用的任务名称。
5. 在左上角找到任务名称，复制其下方以较小字号显示的字符串，这就是任务 ID。
6. 将任务 ID 粘贴到 n8n 的 **Job Id** 字段。

