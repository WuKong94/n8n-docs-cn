---
title: Loop Over Items (Split in Batches)（逐项循环）
description: 工作流自动化平台 n8n 中的 Loop Over Items (Split in Batches)（逐项循环） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: Loop Over Items (Split in Batches)（逐项循环）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Loop Over Items（逐项循环） <a href="#loop-over-items" id="loop-over-items"></a>

Loop Over Items 节点用于在需要时循环处理数据。

节点保存原始输入数据，每次迭代通过 **loop**（循环）输出返回预设数量的数据。

节点执行完成后，会合并所有已处理的数据，并通过 **done**（完成）输出返回。

## 何时使用 Loop Over Items 节点 <a href="#when-to-use-the-loop-over-items-node" id="when-to-use-the-loop-over-items-node"></a>

默认情况下，n8n 节点设计为处理输入数据项列表，部分例外见下文。根据目标的不同，工作流通常无需 Loop Over Items 节点。n8n 处理多个数据项的更多信息，请参阅 [n8n 中的循环](../../../build/flow-logic/loop.md)。

以下链接介绍 Loop Over Items 节点的一些适用情况：

* [循环直到处理完全部数据项](../../../build/flow-logic/loop.md#loop-until-all-items-are-processed)：介绍 Loop Over Items 节点与常规数据项处理的区别，以及何时适合使用此节点。
* [节点例外情况](../../../build/flow-logic/loop.md#node-exceptions)：列出可能需要使用 Loop Over Items 节点手动构建循环逻辑的特定场景和节点。
* [避免速率限制](../handle-rate-limits.md)：演示如何将 API 请求分批，避免其他服务的速率限制。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

### Batch Size（批次大小） <a href="#batch-size" id="batch-size"></a>

输入每次调用返回的数据项数量。

## 节点选项 <a href="#node-options" id="node-options"></a>

### Reset（重置） <a href="#reset" id="reset"></a>

开启后，节点每次循环都会以当前输入数据重新初始化并重置。当希望 Loop Over Items 节点将传入数据视为一组新数据，而非之前数据项的延续时，使用此项。

例如，无法预先知道分页服务的页数时，可将 Loop Over Items 节点的重置选项与 [If 节点](n8n-nodes-base.if.md)配合使用。循环每次查询一页，执行所需处理，再增加页码。循环重置确保每次迭代都被识别为一组新数据。If 节点判断退出条件，决定是否继续下一次迭代。

{% hint style="warning" %}
**设置有效的终止条件**

对于上述示例一类的工作流，为循环设置有效的终止条件至关重要。如果终止条件始终不满足，工作流执行会陷入无限循环。
{% endhint %}

启用后，可将参数表示方式从 **Fixed**（固定值）切换为 **Expression**（表达式），以调整重置条件。表达式的计算结果决定节点何时重置数据项处理。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Loop Over Items (Split in Batches)（逐项循环） 集成模板](https://n8n.io/integrations/split-in-batches)，或[搜索所有模板](https://n8n.io/workflows/)

### 从两个不同来源读取 RSS 订阅源 <a href="#read-rss-feed-from-two-different-sources" id="read-rss-feed-from-two-different-sources"></a>

此工作流使用 Loop Over Items 节点从两个不同来源读取 RSS 订阅源。由于 RSS Feed Read 节点只处理收到的第一个数据项，因此需要在工作流中使用 Loop Over Items 节点。也可在 n8n.io 找到此[工作流](https://n8n.io/workflows/687-read-rss-feed-from-two-different-sources/)。

本示例介绍工作流的构建过程，但假定你已熟悉 n8n。要构建第一个工作流并了解如何添加节点，请参阅[动手试用](../../../get-started/build-your-first-workflow.md)。

最终工作流如下所示：

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.manualTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%200%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22e6e1cfe6-eff1-48bd-b21c-6ba83d4244d9%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22jsCode%22%3A%20%22return%20%5B%5Cn%5Ct%7B%5Cn%5Ct%5Ctjson%3A%20%7B%5Cn%5Ct%5Ct%5Cturl%3A%20%27https%3A%2F%2Fmedium.com%2Ffeed%2Fn8n-io%27%2C%5Cn%5Ct%5Ct%7D%5Cn%5Ct%7D%2C%5Cn%5Ct%7B%5Cn%5Ct%5Ctjson%3A%20%7B%5Cn%5Ct%5Ct%5Cturl%3A%20%27https%3A%2F%2Fdev.to%2Ffeed%2Fn8n%27%2C%5Cn%5Ct%5Ct%7D%5Cn%5Ct%7D%5Cn%5D%3B%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.code%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20220%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22137f1128-45b6-4bc4-a9fb-8660baa652a9%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Code%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.splitInBatches%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20440%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%223449a953-49c2-4a36-ba3d-cbc0573f3f6c%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Loop%20Over%20Items%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22url%22%3A%20%22%3D%7B%7B%20%24json.url%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.rssFeedRead%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201.1%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20660%2C%0A%20%20%20%20%20%20%20%20100%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22cc2e59d7-0a9b-4640-8052-d8f7f8d8c9fe%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22RSS%20Read%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Code%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Code%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Loop%20Over%20Items%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Loop%20Over%20Items%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22RSS%20Read%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22RSS%20Read%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Loop%20Over%20Items%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%22cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7%22%0A%20%20%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/rss-feed-example.json" %}

复制上方工作流文件，粘贴到你的实例中，或按以下步骤手动构建：

1. 添加手动触发器。
2. 添加 Code 节点。
3. 将以下代码复制到 Code 节点：
	```js
	return [
		{
			json: {
				url: 'https://medium.com/feed/n8n-io',
			}
		},
		{
			json: {
				url: 'https://dev.to/feed/n8n',
			}
		}
	];
	```
4. 添加 Loop Over Items 节点。
5. 配置 Loop Over Items：在 **Batch Size**（批次大小）字段中将批次大小设为 `1`。
6. 添加 RSS Feed Read 节点。
7. 选择 **Execute Workflow**（执行工作流），运行工作流以将数据加载到 RSS Feed Read 节点。
8. 配置 RSS Feed Read：将输入中的 `url` 映射到 **URL** 字段。可从 **INPUT**（输入）面板拖放，也可使用表达式 `{{ $json.url }}`。
9. 选择 **Execute Workflow**（执行工作流），运行工作流并查看结果数据。

### 检查节点是否已处理全部数据项 <a href="#check-that-the-node-has-processed-all-items" id="check-that-the-node-has-processed-all-items"></a>

要检查节点是否仍有待处理的数据项，请使用表达式 `{{$("Loop Over Items").context["noItemsLeft"]}}`。此表达式返回布尔值：仍有待处理数据时返回 `false`，否则返回 `true`。

### 获取节点当前运行索引 <a href="#get-the-current-running-index-of-the-node" id="get-the-current-running-index-of-the-node"></a>

要获取节点当前运行索引，请使用表达式 `{{$("Loop Over Items").context["currentRunIndex"];}}`。

