---
title: Think Tool（思考工具） 节点文档
description: 了解如何在 n8n 中使用 Think Tool 节点，并按照技术文档将思考工具集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Think Tool（思考工具） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Think Tool（思考工具） 节点 <a href="#think-tool-node" id="think-tool-node"></a>

Think Tool 节点是一种工具[^1]，让智能体[^2]在回答前先思考。它允许智能体先通过自我对话思考问题，再给出答案，特别适合需要仔细考虑的复杂查询。


{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Think Tool（思考工具） 集成模板](https://n8n.io/integrations/think-tool)，或[搜索所有模板](https://n8n.io/workflows/)

### 提示词示例 <a href="#prompting-example" id="prompting-example"></a>

例如，向智能体提出以下问题：


> *Jack 正看着 Anne，Anne 正看着 George。Jack 已婚，George 未婚，不知道 Anne 是否已婚。是否有已婚者正在看着未婚者？*

	
智能体会使用工具进行思考：


> *已知信息：1. Jack 正看着 Anne。2. Anne 正看着 George。3. Jack 已婚。4. George 未婚。5. 不知道 Anne 是否已婚。*

> *需要判断是否有已婚者正在看着未婚者。考虑 Anne 的两种情况：*

> *情况 1：Anne 已婚。*

> - *如果 Anne 已婚，那么她（已婚）正看着 George（未婚）。此时，已婚者 Anne 正看着未婚者 George。*

> *情况 2：Anne 未婚。*

> - *如果 Anne 未婚，那么 Jack（已婚）正看着 Anne（未婚）。此时，已婚者 Jack 正看着未婚者 Anne。*

> *两种情况下，都有已婚者正看着未婚者。因此，答案是肯定的。*

	
随后给出答案：


> *是的，有已婚者正在看着未婚者。无论 Anne 的婚姻状况是哪一种，都会有已婚者（Jack 或 Anne）正看着未婚者（George 或 Anne）。*


## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/tools-link.md" %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
[^2]: AI 智能体是能够响应请求、作出决策并为用户执行现实任务的人工智能系统。它们使用大型语言模型（LLM）理解用户输入，并根据可用的信息和资源，决定如何最好地处理请求。
