---
title: OpenAI Chat Model 节点常见问题
description: 工作流自动化平台 n8n 中 OpenAI Chat Model 节点的常见错误和问题，包括问题详情及建议的解决办法。
contentType:
- integration
- reference
priority: high
nodeTitle: OpenAI Chat Model 节点常见问题
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OpenAI Chat Model 节点常见问题 <a href="#openai-chat-model-node-common-issues" id="openai-chat-model-node-common-issues"></a>

以下列出 [OpenAI Chat Model 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 参数处理 <a href="#processing-parameters" id="processing-parameters"></a>

OpenAI Chat Model 是子节点[^1]。使用表达式处理多个数据项时，子节点的行为与其他节点不同。

多数节点，包括[根节点](#user-content-fn-2)[^2]，可以接收任意数量的输入数据项，处理后输出结果。你可以用表达式引用输入数据项，节点会依次对每个数据项解析表达式。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 会依次解析为每个名称。

在子节点中，表达式始终解析为第一个数据项。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 始终解析为第一个名称。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/openai-api-issues.md" %}

[^1]: n8n 集群节点由连接到根节点的一个或多个子节点组成。子节点通过访问特定服务或资源，或提供特定类型的专用处理（例如计算器功能），扩展根节点的功能。
<a id="user-content-fn-2"></a>
[^2]: 每个 n8n 集群节点都包含一个根节点，用于定义集群的主要功能。一个或多个子节点连接到根节点，以扩展其功能。
