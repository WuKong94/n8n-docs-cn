---
description: 使用 Gateway 额度，在 n8n 工作流中调用 AI 模型和第三方服务，无需服务商账号或 API 密钥。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Gateway 额度 <a id="gateway-credits"></a>

Gateway 额度让你无需创建服务商账号或管理 API 密钥，就能在工作流中使用受支持的 AI 模型和第三方服务。你只需在支持的节点上选择 Gateway 额度，无需配置凭据；n8n 会从预付额度余额中扣除使用费用。

Gateway 额度仅支付工作流中节点的使用费用，不支付 n8n Assistant 的费用。后者使用独立的 [Assistant 额度](../assistant-credits/README.md)，套餐每月包含一定额度。充值 Gateway 额度不会增加 n8n Assistant 的额度。

## 本节内容 <a id="in-this-section"></a>

* [充值 Gateway 额度](top-up-gateway-credits.md)：手动或自动添加额度。
* [跟踪 Gateway 额度支出](track-gateway-credit-spend.md)：监控余额、支出和充值记录。

{% hint style="info" %}
**功能可用范围**

以下套餐可以使用 Gateway 额度：

- **n8n Cloud：** Starter、Pro

n8n Cloud Enterprise 和自托管 n8n 不支持 Gateway 额度。此功能从 n8n 2.36.0 开始提供。免费试用包含 Gateway 额度，但只有升级为付费套餐后才能充值。
{% endhint %}

## Gateway 额度的工作方式 <a id="how-gateway-credits-work"></a>

在支持的节点上选择 **Use Gateway credits（使用 Gateway 额度）** 后，n8n 会通过自己管理的网关，将节点请求转发给服务商。网关使用 n8n 的身份向服务商进行认证，因此你无需服务商账号。n8n 会从额度余额中扣除每个请求的费用。

n8n 根据[服务价格页面](https://app.n8n.cloud/service-pricing)列出的费率，按请求计费。不同模型和服务的费率不同，并会随服务商调价而变化，因此当前费率始终以服务价格页面为准。

如何在节点上选择 Gateway 额度，以及在编辑器中查找支持的节点，请参阅[使用 Gateway 额度](../../../build/understand-workflows/use-gateway-credits.md)。

## 支持的服务 <a id="supported-services"></a>

Gateway 额度支持两类服务：

- **AI 模型**：例如 OpenAI、Anthropic 和 Google Gemini 等大语言模型服务商。
- **工具服务**：例如 Brave Search 和 Firecrawl 等提供网络搜索、网页抓取、浏览器自动化和文档解析能力的服务。

支持目录会持续扩展。最新的服务和模型列表，请查看[服务价格页面](https://app.n8n.cloud/service-pricing)。编辑器节点面板中的 **Included in n8n（n8n 内含）** 部分会显示支持 Gateway 额度的节点。

未列入目录的服务仍可按常规方式在 n8n 中使用：使用自己的 API 密钥创建凭据。详情请参阅[创建和编辑凭据](../../../build/understand-workflows/create-and-edit-credentials.md)。

## 额度余额 <a id="your-credit-balance"></a>

每个 Cloud 实例都有一个额度余额，由该实例上所有使用 Gateway 额度的用户共享。你可以在编辑器节点的 Gateway 额度选项旁，或 [n8n Cloud 控制台](../use-the-cloud-console.md)的 **Gateway credits（Gateway 额度）** 页面查看余额。该页面还会显示各时段的支出。详情请参阅[跟踪 Gateway 额度支出](track-gateway-credit-spend.md)。

Cloud 新用户注册时会获得少量免费额度，可以在购买额度之前体验支持的服务。免费试用也包含 Gateway 额度，从第一个工作流开始就能使用。

余额归零后，使用 Gateway 额度的节点会停止工作，直到你添加额度。使用自有凭据的节点不受影响。如果执行过程中余额耗尽，n8n 会让已经发出的请求完成，不会中途停止，并在下次充值时扣除超出余额的费用。付费套餐可以手动或自动[充值余额](top-up-gateway-credits.md)。免费试用期间无法充值；如果试用时耗尽免费额度，需要升级为付费套餐才能添加额度。

### 额度到期与失效 <a id="credit-expiry-and-forfeiture"></a>

- n8n 优先使用免费额度，再使用充值额度，并优先消耗最早到期的额度。
- 充值额度在购买 12 个月后到期。
- 额度不是现金，不能转移到其他账号。
- 充值后即为最终交易。除法律要求的情况外，n8n 不退还未使用额度。
- 关闭 n8n 账号后，剩余额度将失效。只要账号仍然存在，取消订阅不会导致额度失效。

## Gateway 额度与其他额度类型 <a id="gateway-credits-and-other-credit-types"></a>

n8n 提供多种额度，它们的余额相互独立，用于支付不同费用：

| 额度类型 | 支付内容 | 查看位置 |
|---|---|---|
| Gateway 额度 | 工作流节点使用的 AI 模型和工具服务 | 支持此功能的节点，以及 Cloud 控制台的 **Gateway credits（Gateway 额度）** 页面 |
| [Assistant 额度](../assistant-credits/README.md) | [n8n Assistant](../../../build/ways-of-building-workflows/n8n-assistant.md) 的使用费用，套餐每月包含一定额度 | 编辑器中的 n8n Assistant 面板，以及 Cloud 控制台的 **Assistant credits（Assistant 额度）** 页面 |
| 免费 OpenAI API 额度 | 旧有机制为 Cloud 新用户提供的一次性 OpenAI 额度 | 仅适用于尚未启用 Gateway 额度的实例 |

充值 Gateway 额度不会增加 Assistant 额度；使用 n8n Assistant 也不会消耗 Gateway 额度余额。

## 数据处理 <a id="data-handling"></a>

节点使用 Gateway 额度运行时，n8n 会通过网关，使用自己的服务商账号将请求发送给服务商。服务商会收到请求内容，例如发送给模型的提示词或发送给解析器的文本，但不会收到你的身份或 n8n 账号信息。有关 n8n 如何处理数据的更多信息，请参阅[隐私](../../../privacy-and-security/README.md)文档和 n8n 服务条款。

## 相关资源 <a id="related-resources"></a>

- [使用 n8n Cloud](../)
- [免费试用并选择套餐](../start-your-free-trial.md)
- [使用 Cloud 控制台](../use-the-cloud-console.md)
- [更新版本](../update-your-version.md)
- [配置 Cloud](../configure-cloud/README.md)
- [Assistant 额度](../assistant-credits/README.md)
- [理解并发](../understand-concurrency.md)
- [下载工作流](../download-workflows.md)
- [使用 Gateway 额度](../../../build/understand-workflows/use-gateway-credits.md)：在节点上选择 Gateway 额度并查找支持的节点。
- [服务价格页面](https://app.n8n.cloud/service-pricing)：所有受支持服务和模型的当前费率。
