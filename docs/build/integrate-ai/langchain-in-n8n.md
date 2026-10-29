---
description: 了解 n8n 如何实现 LangChain 概念，以及如何将自托管 n8n 实例连接到 LangSmith 进行追踪。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 中的 LangChain <a id="langchain-in-n8n"></a>

n8n 的 AI 节点使用 [LangChain](https://docs.langchain.com/oss/javascript/langchain/overview) 的 JavaScript 框架。每个节点都可以配置，你可以自行选择智能体、LLM、记忆和其他组件。其他 n8n 节点可以像平常一样连接到 LangChain 节点，因此能将 LangChain 逻辑与 n8n 支持的任意数据源或服务组合使用。

本页面向已经了解 LangChain、希望知道其概念如何映射到 n8n 的读者。如果刚开始了解 AI 概念，请先阅读[理解 AI 组件](understand-ai-components/README.md)。

## LangChain 概念如何映射到 n8n 节点 <a id="how-langchain-concepts-map-to-n8n-nodes"></a>

n8n 将大多数 LangChain 概念表示为[集群节点](../../integrations/builtin/cluster-nodes/README.md)：由一个定义主要功能的[根节点](../../get-started/key-concept-glossary.md#root-node-n8n)，以及一个或多个用于扩展功能的[子节点](../../get-started/key-concept-glossary.md#sub-node-n8n)组成。

| LangChain 概念 | 节点类别 | 示例节点 | 了解更多 |
| --- | --- | --- | --- |
| 链 | 根节点 | [Basic LLM Chain](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md)、[Question and Answer Chain](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/README.md)、[Summarization Chain](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md) | [什么是 AI 链？](understand-ai-components/what-chains-do.md) |
| 智能体 | 根节点 | [AI Agent](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md) | [什么是 AI 智能体？](understand-ai-components/what-agents-do.md) |
| 语言模型 | 子节点 | [Anthropic Chat Model](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)、[OpenAI Chat Model](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md)、[Ollama Chat Model](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/README.md) | [子节点](../../integrations/builtin/cluster-nodes/sub-nodes/README.md) |
| 向量存储 | 根节点 | [Pinecone Vector Store](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)、[Qdrant Vector Store](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)、[Simple Vector Store](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md) | [使用向量存储和搜索数据](understand-ai-components/store-and-search-data-with-vectors.md) |
| 记忆 | 子节点 | [Postgres Chat Memory](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md)、[Redis Chat Memory](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)、[Simple Memory](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/README.md) | [记忆的工作原理](understand-ai-components/how-memory-works.md) |
| 工具 | 子节点 | [Call n8n Workflow Tool](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)、[Custom Code Tool](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md)、[Wikipedia](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md) | [AI 中的工具是什么？](understand-ai-components/how-tools-work.md) |
| 检索器 | 子节点 | [Vector Store Retriever](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md)、[Workflow Retriever](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md) | [检索相关上下文](understand-ai-components/retrieve-relevant-context.md) |
| 嵌入模型 | 子节点 | [Embeddings OpenAI](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)、[Embeddings Cohere](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md) | [检索相关上下文](understand-ai-components/retrieve-relevant-context.md) |
| 文档加载器 | 子节点 | [Default Data Loader](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)、[GitHub Document Loader](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md) | [子节点](../../integrations/builtin/cluster-nodes/sub-nodes/README.md) |
| 输出解析器 | 子节点 | [Structured Output Parser](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/README.md)、[Auto-fixing Output Parser](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md) | [子节点](../../integrations/builtin/cluster-nodes/sub-nodes/README.md) |
| 文本分割器 | 子节点 | [Recursive Character Text Splitter](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)、[Token Splitter](../../integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md) | [子节点](../../integrations/builtin/cluster-nodes/sub-nodes/README.md) |

记忆子节点只能连接到 [AI Agent](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/README.md) 根节点。与 LangChain 不同，n8n 的所有链节点均不支持记忆，因此无法引用对话中的早期消息。如果工作流需要此能力，请使用智能体而非链。

上述示例并不完整。各类别完整且最新的节点列表，请浏览[根节点](../../integrations/builtin/cluster-nodes/root-nodes/README.md)和[子节点](../../integrations/builtin/cluster-nodes/sub-nodes/README.md)库。n8n 还提供 [Chat Trigger](../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/README.md) 节点，可通过聊天消息启动工作流；以及 [LangChain Code](../../integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md) 节点，可直接编写 LangChain JavaScript 代码，实现尚无专用 n8n 节点的功能。

## 将自托管 n8n 实例连接到 LangSmith <a id="use-langsmith-with-a-self-hosted-n8n-instance"></a>

[LangSmith](https://www.langchain.com/langsmith) 是 LangChain 团队提供的开发者平台。将自托管 n8n 实例连接到 LangSmith 后，可以像追踪 LangChain 应用一样记录和监控 n8n 执行。

{% hint style="info" %}
**功能可用范围**

LangSmith 追踪可用于：

- **自托管：**所有版本。

n8n Cloud 不提供此功能。
{% endhint %}

将 n8n 连接到 LangSmith：

1. [登录 LangSmith](https://smith.langchain.com/settings)，获取 API 密钥。
2. 在托管 n8n 的环境中设置以下[环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)：

   | 变量 | 值 |
   | --- | --- |
   | `LANGCHAIN_ENDPOINT` | `https://api.smith.langchain.com` |
   | `LANGCHAIN_TRACING_V2` | `true` |
   | `LANGCHAIN_API_KEY` | LangSmith API 密钥 |
   | `LANGCHAIN_PROJECT` | 可选的项目名称，默认为 `default` |
   | `LANGCHAIN_CALLBACKS_BACKGROUND` | 设置为 `true` 可异步上传追踪记录 |

3. 重启 n8n。

n8n 发送第一条追踪记录后，LangSmith 会创建名为 **default** 的项目，除非你通过 `LANGCHAIN_PROJECT` 指定其他名称；指定后，所有追踪记录都会发送到该项目。由于 `LANGCHAIN_CALLBACKS_BACKGROUND` 默认异步上传，追踪记录可能略有延迟。调试时，可以将其设为 `false` 以同步上传。

LangSmith 本身的使用方法请参阅 [LangSmith 文档](https://docs.smith.langchain.com/)。

## 进一步了解 LangChain <a id="learn-more-about-langchain"></a>

使用 n8n 不需要先了解 LangChain，但如果想深入学习，可以参考以下资源：

* [LangChain 文档](https://docs.langchain.com/)介绍了核心概念和使用场景。可以选择 [LangChain | Python](https://docs.langchain.com/oss/python/langchain/overview) 或 [LangChain | JavaScript](https://docs.langchain.com/oss/javascript/langchain/overview)，查阅快速入门、代码示例和 API 文档。LangChain 也提供 Python 和 JavaScript 的[代码模板](https://github.com/langchain-ai/cookbooks)，展示常见模式和使用场景。
* [什么是 LangChain？](https://www.ibm.com/think/topics/langchain)面向普通读者，用通俗语言解释 LangChain 术语。
* [Greg Kamradt 的 YouTube 系列](https://youtu.be/_v_fgW2SkkQ?si=8Z2tfAoXnN3lXU9s)通过代码示例讲解 LangChain 文档。
* 加入 n8n [Discord](https://discord.gg/bAt54txhHg)，与 n8n 社区讨论 LangChain 并分享项目。

## 相关资源 <a id="related-resources"></a>

* [集成 AI](./)
* [MCP 服务器](mcp-servers.md)
* [理解 AI 组件](understand-ai-components/README.md)
* [测试和改进 AI 工作流](test-and-improve-ai-workflows/README.md)
* [AI 示例](ai-examples.md)
