---
title: 创建和调用子工作流
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

### 创建子工作流 <a href="#create-the-sub-workflow" id="create-the-sub-workflow"></a>


1. 创建一个新工作流。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>从现有工作流创建子工作流</strong></p><p>也可以使用 <a href="../../../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md">Execute Sub-workflow</a> 节点，直接从现有父工作流创建子工作流。在节点中选择 <strong>Database（数据库）</strong> 和 <strong>From list（从列表选择）</strong> 选项，再在列表中选择 <strong>Create a sub-workflow（创建子工作流）</strong>。</p><p>还可以通过上下文菜单中的 <a href="../../../../build/flow-logic/convert-to-sub-workflows.md">Sub-workflow conversion（子工作流转换）</a>，直接提取选中的节点。</p></div>

1. **可选**：配置哪些工作流可以调用此子工作流：
	1. 选择 **Options（选项）** <img src="../../assets/three-dot-options-menu.png" alt="Options menu" data-size="line"> 菜单 > **Settings（设置）**。n8n 会打开 **Workflow settings（工作流设置）** 弹窗。
	1. 更改 **This workflow can be called by（允许调用此工作流的工作流）** 设置。有关配置工作流的更多信息，请参阅[工作流设置](../../../../build/manage-workflows/configure-workflow-settings.md)。
1. 添加 **Execute Sub-workflow** 触发器节点（在触发器节点中搜索时，也称为 **When Executed by Another Workflow**）。
1. 设置 **Input data mode（输入数据模式）**，选择如何定义子工作流的输入数据：
	* **Define using fields below（使用下方字段定义）**：选择此模式，逐项定义调用方工作流需要提供的输入名称和数据类型。调用方工作流中的 [Execute Sub-workflow 节点](../../../../integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md)或 [Call n8n Workflow Tool 节点](../../../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)会自动获取此处定义的字段。
	* **Define using JSON example（使用 JSON 示例定义）**：选择此模式，提供一个 JSON 对象示例，展示预期的输入数据项及其类型。
	* **Accept all data（接受所有数据）**：选择此模式，无条件接受所有数据。子工作流不会定义任何必需输入项，必须自行处理输入不一致或值缺失的情况。
1. 根据需要添加其他节点，实现子工作流功能。
1. 保存子工作流。

{% hint style="info" %}
**子工作流不得包含错误**

如果子工作流存在错误，父工作流将无法触发它。
{% endhint %}
{% hint style="info" %}
**构建前先向子工作流加载数据**

此操作需要[加载以往执行数据](../../../../build/understand-workflows/understand-executions/debug-executions.md)的功能，n8n Cloud 和已注册的 Community 套餐支持此功能。

如果希望向子工作流加载数据，在构建时使用：

1. 创建子工作流并添加 **Execute Sub-workflow Trigger**。
1. 将节点的 **Input data mode（输入数据模式）** 设为 **Accept all data（接受所有数据）**；如果输入项已确定，也可以通过字段或 JSON 定义。
1. 在子工作流[设置](../../../../build/manage-workflows/configure-workflow-settings.md)中，将 **Save successful production executions（保存成功的生产执行）** 设为 **Save（保存）**。
1. 先跳至设置父工作流的步骤，并运行父工作流。
1. 按照步骤[加载以往执行的数据](../../../../build/understand-workflows/understand-executions/debug-executions.md)。
1. 如有需要，调整 **Input data mode（输入数据模式）**，使其与父工作流发送的输入一致。

现在可以在触发器节点中固定示例数据，以便在配置工作流其余部分时使用真实数据。
{% endhint %}


### 调用子工作流 <a href="#call-the-sub-workflow" id="call-the-sub-workflow"></a>

1. 打开要从中调用子工作流的工作流。
1. 添加 **Execute Sub-workflow** 节点。
1. 在 **Execute Sub-workflow** 节点中设置要调用的子工作流。可以按 ID 调用、从本地文件加载工作流、将工作流 JSON 作为节点参数添加，或通过 URL 指定工作流。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>查找工作流 ID</strong></p><p>子工作流的 ID 是其 URL 末尾由字母和数字组成的字符串。</p></div>

1. 填写子工作流定义的必需输入项。
1. 保存工作流。

工作流执行时，会将数据发送给子工作流，并运行子工作流。

要从父工作流跟踪到子工作流的执行流程，可以打开 Execute Sub-workflow 节点，选择 **View sub-execution（查看子执行）** 链接。同样，子工作流的执行记录中也包含返回父工作流执行记录的链接，方便反向查看。
