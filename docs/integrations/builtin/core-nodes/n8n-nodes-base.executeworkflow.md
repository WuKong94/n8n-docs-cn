---
title: Execute Sub-workflow 节点
description: 了解 n8n 中 Execute Sub-workflow 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: high
nodeTitle: Execute Sub-workflow 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Execute Sub-workflow（执行子工作流） <a href="#execute-sub-workflow" id="execute-sub-workflow"></a>

使用 Execute Sub-workflow 节点，在运行 n8n 的主机上执行另一个工作流。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Source（来源） <a href="#source" id="source"></a>

选择节点从何处获取子工作流信息：

- **Database**（数据库）：通过 ID 从数据库加载工作流，还需选择以下方式之一：
    - **From list**（从列表选择）：从当前账户可用的工作流列表中选择。
    - **Workflow ID**（工作流 ID）：输入工作流 ID，即 URL 中 `/workflow/` 后面的部分。例如，工作流 URL 为 `https://my-n8n-acct.app.n8n.cloud/workflow/abCDE1f6gHiJKL7` 时，**Workflow ID** 为 `abCDE1f6gHiJKL7`。
- **Local File**（本地文件）：从本地保存的 JSON 文件加载工作流，还需填写：
    - **Workflow Path**（工作流路径）：输入要执行的本地 JSON 工作流文件路径。
- **Parameter**（参数）：从参数加载工作流，还需填写：
    - **Workflow JSON**（工作流 JSON）：输入要执行的 JSON 代码。
- **URL**：从 URL 加载工作流，还需填写：
    - **Workflow URL**（工作流 URL）：输入要从中加载工作流的 URL。

### Workflow Inputs（工作流输入） <a href="#workflow-inputs" id="workflow-inputs"></a>

使用 **database**（数据库）和 **From list**（从列表选择）选择子工作流后，会自动显示子工作流的输入项，供你填写或映射值。

可以移除请求的输入项，此时子工作流收到的对应值为 `null`。还可开启 **Attempt to convert types**（尝试转换类型），自动尝试将数据转换为子工作流输入项要求的类型。

如果子工作流的 Workflow Input Trigger 节点使用“Accept all data”（接受所有数据）输入模式，这些输入项不会显示。

### Mode（模式） <a href="#mode" id="mode"></a>

选择节点的执行模式：

- **Run once with all items**（所有数据项一起执行一次）：将所有输入数据项传入同一次节点执行。
- **Run once for each item**（每个数据项执行一次）：按顺序为每个输入数据项执行一次节点。

## 节点选项 <a href="#node-options" id="node-options"></a>

此节点有一个 **Wait for Sub-Workflow Completion**（等待子工作流完成）选项。开启时，主工作流等待子工作流完成后再继续下一步；关闭时，主工作流不等待，直接继续执行。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execute Sub-workflow 集成模板](https://n8n.io/integrations/execute-workflow)，或[搜索所有模板](https://n8n.io/workflows/)

## 设置和使用子工作流 <a href="#set-up-and-use-a-sub-workflow" id="set-up-and-use-a-sub-workflow"></a>

本节介绍如何设置父工作流和子工作流。

{% include "../../../reusable-content/.gitbook/includes/flow-logic/subworkflow-usage.md" %}


## 工作流之间如何传递数据 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "../../../reusable-content/.gitbook/includes/flow-logic/subworkflow-data-flow.md" %}
