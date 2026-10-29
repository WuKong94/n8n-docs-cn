---
title: Embeddings AWS Bedrock（AWS Bedrock 嵌入模型） 节点文档
description: 了解如何在 n8n 中使用 Embeddings AWS Bedrock（AWS Bedrock 嵌入模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Embeddings AWS Bedrock（AWS Bedrock 嵌入模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Embeddings AWS Bedrock（AWS Bedrock 嵌入模型） 节点 <a href="#embeddings-aws-bedrock-node" id="embeddings-aws-bedrock-node"></a>

使用 Embeddings AWS Bedrock 节点，为指定文本生成嵌入向量[^1]。

本页列出了 Embeddings AWS Bedrock 节点的参数，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [AWS 凭据文档](../../credentials/aws.md)。

如果通过未启用私有 DNS 的 [VPC 接口端点（PrivateLink）](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)访问 Bedrock，请在凭据中设置 **Bedrock Endpoint**（Bedrock 端点）和 **Bedrock Runtime Endpoint**（Bedrock 运行时端点）自定义端点。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**（身份验证）：选择身份验证方式：
    * **AWS (IAM)**：使用 IAM 访问密钥，选择 **AWS** 凭据。
    * **AWS (Assume Role)**：临时扮演 IAM 角色，选择 **AWS (Assume Role)** 凭据。
* **Model**（模型）：选择生成嵌入向量的模型或[推理配置文件](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)。下拉菜单同时列出按需嵌入模型和嵌入推理配置文件。如果列表为空或不完整，IAM 角色可能缺少 `bedrock:ListFoundationModels` 或 `bedrock:ListInferenceProfiles` 权限。可将字段切换为 **Expression**（表达式）模式，直接输入模型或推理配置文件 ID。

可用模型的更多信息，请参阅 [Amazon Bedrock 文档](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)。

## 节点选项 <a id="node-options"></a>

* **Additional Model Request Fields**（附加模型请求字段）：以 JSON 输入模型专用的请求字段，例如 Titan 的 `dimensions` 和 `normalize`，或 Cohere 的 `input_type` 和 `truncate`。各模型系列支持的字段，请参阅 [AWS 模型参数文档](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Timeout**（超时）：输入等待请求完成的最长时间，单位为毫秒。设为 `0` 可禁用超时。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Embeddings AWS Bedrock（AWS Bedrock 嵌入模型） 集成模板](https://n8n.io/integrations/embeddings-aws-bedrock)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

AWS Bedrock 的更多信息，请参阅 [AWS Bedrock 文档](https://docs.aws.amazon.com/bedrock/)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

[^1]: 嵌入是使用向量对数据进行数值化表示。AI 通过将值映射到多个维度，利用嵌入理解复杂数据及其关系。向量数据库或向量存储是专门用于存储和访问嵌入的数据库。
