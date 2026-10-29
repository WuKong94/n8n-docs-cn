---
title: AWS Bedrock Chat Model（AWS Bedrock 聊天模型） 节点文档
description: 了解如何在 n8n 中使用 AWS Bedrock Chat Model（AWS Bedrock 聊天模型） 节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: AWS Bedrock Chat Model（AWS Bedrock 聊天模型） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS Bedrock Chat Model（AWS Bedrock 聊天模型） 节点 <a href="#aws-bedrock-chat-model-node" id="aws-bedrock-chat-model-node"></a>

AWS Bedrock Chat Model 节点支持通过 AWS Bedrock 平台使用大型语言模型。

本页列出了 AWS Bedrock Chat Model 节点的参数，并提供更多资源的链接。

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
* **Model**（模型）：选择生成补全的模型或[推理配置文件](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)。下拉菜单同时列出按需基础模型和跨区域推理配置文件。最新模型（例如 Claude Sonnet 4.x）仅通过推理配置文件提供。列表不完整时，IAM 角色可能缺少 `bedrock:ListFoundationModels` 或 `bedrock:ListInferenceProfiles` 权限。也可切换为 **Expression**（表达式）模式，直接输入模型 ID、推理配置文件 ID 或 ARN。

{% hint style="info" %}
节点版本 1.1 的下拉菜单每次仅显示一个列表，通过 **Model Source**（模型来源）参数在按需基础模型和推理配置文件之间切换。节点版本 1 仅支持按需基础模型。
{% endhint %}

可用模型的更多信息，请参阅 [Amazon Bedrock 模型文档](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**（最大 token 数）：输入使用的 token 数量上限，以设置补全长度。
* **Sampling Temperature**（采样温度）：控制采样过程的随机性。温度越高，采样结果越多样，但产生幻觉的风险也越高。
* **Top P**：设置 token 选择的概率阈值。较低值将候选集限制为更高概率的 token，较高值允许更多样的选项。
* **Max Retries**（最大重试次数）：输入请求的最大重试次数。
* **Timeout**（超时）：输入等待请求完成的最长时间，单位为毫秒。生成耗时较长时，可提高此值。设为 `0` 可禁用超时。
* **Additional Model Request Fields**（附加模型请求字段）：以 JSON 输入模型系列专用的推理参数，例如 Claude 的 `top_k` 或 Nova 的 `inferenceConfig`。各模型系列支持的参数，请参阅 [AWS 模型参数文档](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)。
* **Latency Optimization**（延迟优化）：选择请求使用 **Standard**（标准）还是 **Optimized**（优化）延迟模式。对于支持的模型和区域，优化模式可缩短响应时间。可用性请参阅 [AWS 延迟优化推理文档](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)。
* **Guardrail**（护栏）：为请求应用 [Amazon Bedrock 护栏](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)。详情请参阅[使用 AWS 护栏](#using-aws-guardrails)。

### 使用 AWS 护栏 <a href="#using-aws-guardrails" id="using-aws-guardrails"></a>

护栏让组织能够对模型调用实施内容和安全策略。护栏必须与模型位于同一个 AWS 区域。**Guardrail**（护栏）选项包含以下字段：

* **Guardrail Identifier**（护栏标识符）：要应用的护栏 ID 或完整 ARN。
* **Guardrail Version**（护栏版本）：使用的护栏版本，可为数字版本字符串（例如 `1`），或使用 `DRAFT` 指定工作草稿。默认为 `DRAFT`。
* **Trace**（追踪）：选择 AWS 是否在响应中包含护栏评估的诊断追踪信息，可选 **Disabled**（禁用，默认）、**Enabled**（启用）或 **Enabled (Full)**（完全启用）。注意，启用追踪会使 AWS 在响应中包含护栏评估详情，其中可能回显匹配到的输入内容，例如个人身份信息的检测结果；n8n 目前不会在 AI 日志中显示这些详情。

护栏介入时，节点以护栏配置的阻止消息替代模型输出，作为正常响应返回，而不是报错。n8n 不暴露底层停止原因；要在下游检测护栏介入，请匹配护栏的阻止消息文本。护栏标识符或版本无效时，节点会以 AWS 验证错误失败。护栏同时适用于流式和非流式请求。

{% hint style="info" %}
**IAM 权限**

除调用权限外，凭据还需要对护栏资源拥有 `bedrock:ApplyGuardrail` 权限。否则，设置护栏后请求会以 `AccessDeniedException` 失败。如果组织要求每次调用都使用护栏，请在 IAM 调用权限中强制执行 `bedrock:GuardrailIdentifier` 条件键，而不是仅依赖此可选节点字段。
{% endhint %}

## 代理限制 <a href="#proxy-limitations" id="proxy-limitations"></a>

此节点不支持 [`NO_PROXY` 环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS Bedrock Chat Model（AWS Bedrock 聊天模型） 集成模板](https://n8n.io/integrations/aws-bedrock-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [LangChain 的 AWS Bedrock Chat Model 文档](https://docs.langchain.com/oss/javascript/integrations/chat/bedrock_converse)。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

