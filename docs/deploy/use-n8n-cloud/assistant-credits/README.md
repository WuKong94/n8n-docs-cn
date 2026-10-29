---
description: 了解 Assistant 额度：n8n Cloud 套餐每月包含的额度、额外额度，以及 n8n Assistant 的使用计费方式。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Assistant 额度 <a id="assistant-credits"></a>

Assistant 额度用于支付 [n8n Assistant](../../../build/ways-of-building-workflows/n8n-assistant.md) 的使用费用。n8n Cloud 套餐每月包含一定 Assistant 额度，在每月第一天重置，因此无需另行购买就能使用 n8n Assistant。如果重置前已用完所含额度，可以购买额外额度，继续使用到下次重置。

Assistant 额度仅支付 n8n Assistant 的费用，不支付工作流或智能体运行时的 AI 模型调用费用，例如 AI Agent 节点背后的模型调用。这些调用使用 [Gateway 额度](../gateway-credits/README.md)或你自己的服务商凭据。

## 本节内容 <a id="in-this-section"></a>

* [充值 Assistant 额度](top-up-assistant-credits.md)：手动或自动购买额外额度。
* [跟踪 Assistant 额度支出](track-assistant-credit-spend.md)：监控余额、支出和充值记录。

{% hint style="info" %}
**功能可用范围**

以下套餐可以使用 Assistant 额度：

- **n8n Cloud：** Starter、Pro

n8n Cloud Enterprise 和自托管 n8n 不支持 Assistant 额度。免费试用包含一次性 Assistant 额度。
{% endhint %}

## Assistant 额度的工作方式 <a id="how-assistant-credits-work"></a>

n8n Assistant 根据底层 AI 模型处理每条消息所需的词元（token）消耗额度。较长的对话、较大的工作流和调试过程，比简短且目标明确的请求消耗更多额度。即使消息被你中途停止，或最终出错，n8n Assistant 在停止前完成的工作仍会消耗额度。

Assistant 额度余额包含两部分：

- **套餐内含额度**：套餐每月提供的额度，在每月第一天重置。
- **额外额度**：在套餐内含额度之外购买的额度，可以跨月结转。

n8n Assistant 始终优先使用套餐内含额度，用完后再以相同费率消耗额外额度，因此无论使用哪种额度，其工作方式都相同。如果未购买额外额度，n8n Assistant 会暂停，直到套餐内含额度重置。

这与仅有单一预付余额的 [Gateway 额度](../gateway-credits/README.md)不同：Gateway 额度以已购买的额度为限；Assistant 额度则由套餐每月补充，额外额度为可选购买项。

运行工作流不会消耗 Assistant 额度，即使工作流由 n8n Assistant 构建也是如此。只有与 n8n Assistant 的对话会消耗该额度。

## 每月内含额度 <a id="included-monthly-allowance"></a>

每月额度的数量取决于套餐。各套餐当前包含的额度，请参阅 [n8n 套餐与价格](https://n8n.io/pricing/)。

额度规则如下：

- 套餐内含额度在每个自然月第一天的 UTC 零点重置，与账单日期无关。
- 未使用的套餐内含额度不能结转。每次重置都会以新额度替换剩余额度。
- 如果在月中开始订阅付费套餐，仍可获得当月完整额度，不会按剩余天数折算。
- 升级套餐后，当月套餐内含额度会立即变更为新套餐的完整额度。
- 降级套餐后，较高额度会保留到下次重置；之后才适用较低额度。
- 取消订阅后，套餐内含额度会在取消生效时停止提供。

### 免费试用期间的 Assistant 额度 <a id="assistant-credits-during-a-free-trial"></a>

免费试用提供一次性 Assistant 额度，而非每月额度。试用额度不会重置，试用期间也无法充值。如果试用额度耗尽，需要升级为付费套餐才能继续使用 n8n Assistant。详情请参阅[免费试用并选择套餐](../start-your-free-trial.md)。

## 额外额度 <a id="extra-credits"></a>

当月套餐内含额度用完后，额外额度让你可以继续使用 n8n Assistant。这是可选项：如果不购买，n8n Assistant 会在套餐内含额度耗尽时暂停，并在下次重置时恢复。

- n8n Assistant 仅在套餐内含额度用完后，才会消耗额外额度。
- 每条消息消耗额外额度的数量与套餐内含额度相同，n8n Assistant 的工作方式不会改变。
- 额外额度可以跨月结转，在购买 12 个月后到期。
- 只有实例所有者可以购买额外额度，且必须持有有效的付费订阅。

你可以手动购买额外额度，也可以设置自动充值，由 n8n 自动购买。详情请参阅[充值 Assistant 额度](top-up-assistant-credits.md)。

## Assistant 额度余额 <a id="your-assistant-credit-balance"></a>

每个 Cloud 实例都有一个 Assistant 额度余额，由该实例上所有使用 n8n Assistant 的用户共享。套餐内含额度和额外额度都来自这个共享余额。

你可以在编辑器的 n8n Assistant 面板额度菜单中，或 [n8n Cloud 控制台](../use-the-cloud-console.md)的 **Assistant credits（Assistant 额度）** 页面查看余额。该页面还会显示各时段的支出，以及使用额度最多的用户。详情请参阅[跟踪 Assistant 额度支出](track-assistant-credit-spend.md)。

## Assistant 额度耗尽后 <a id="when-your-assistant-credits-run-out"></a>

套餐内含额度和额外额度都用完后，实例上所有用户的 n8n Assistant 都会暂停：

- 编辑器中的 n8n Assistant 会显示 **You've run out of AI credits（AI 额度已用完）**，无法再发送新消息。
- Cloud 控制台的 **Assistant credits（Assistant 额度）** 页面会显示 **The Assistant is paused for your instance（此实例的 Assistant 已暂停）** 横幅。

如果在一条消息处理过程中额度耗尽，n8n 会让该消息处理完成，不会中途停止。因此，实际用量可能略微超出余额。

要恢复使用 n8n Assistant：

- 付费套餐的实例所有者可以[购买额外额度](top-up-assistant-credits.md)，也可以等待下个月第一天重置套餐内含额度。
- 免费试用用户需要升级为付费套餐。

工作流不受影响。Assistant 额度耗尽后，工作流仍会继续运行，因为运行工作流不消耗 Assistant 额度。

## 额度到期与失效 <a id="credit-expiry-and-forfeiture"></a>

Assistant 额度与 Gateway 额度采用相同的到期和失效规则：

- n8n 优先使用套餐内含额度，再使用额外额度。额外额度中优先消耗最早到期的额度。
- 套餐内含额度在下个月第一天重置时到期。
- 额外额度在购买 12 个月后到期。
- 额度不是现金，不能转移到其他账号。
- 充值后即为最终交易。除法律要求的情况外，n8n 不退还未使用额度。
- 关闭 n8n 账号后，剩余额度将失效。只要账号仍然存在，取消订阅不会导致额外额度失效。

## Assistant 额度与 Gateway 额度 <a id="assistant-credits-and-gateway-credits"></a>

Assistant 额度和 Gateway 额度的余额相互独立，用于支付不同费用：

| | Assistant 额度 | Gateway 额度 |
|---|---|---|
| 支付内容 | 与 n8n Assistant 的对话，包括让它构建工作流或智能体 | 工作流节点使用的 AI 模型和工具服务 |
| 不支付的内容 | 工作流或智能体运行时发起的 AI 模型调用 | n8n Assistant |
| 套餐包含内容 | 每月第一天重置的月度额度 | 注册时提供的少量一次性免费额度 |
| 购买更多额度 | 额外额度，仅在套餐内含额度用完后使用 | 充值后直接增加余额 |
| 管理位置 | Cloud 控制台的 **Assistant credits（Assistant 额度）** 页面 | Cloud 控制台的 **Gateway credits（Gateway 额度）** 页面 |

充值一种额度不会增加另一种。如果 n8n Assistant 构建的工作流中有节点使用 Gateway 额度，运行该节点消耗的是 Gateway 额度，不是 Assistant 额度。

## 自托管 n8n 中的 n8n Assistant <a id="n8n-assistant-on-self-hosted-n8n"></a>

自托管 n8n 不使用 Assistant 额度。自托管实例上的 n8n Assistant 使用你自己的服务商账号提供的 AI 模型，由服务商直接计费。详情请参阅[设置 n8n Assistant](../../host-n8n/configure-n8n/set-up-n8n-assistant.md)。

## 相关资源 <a id="related-resources"></a>

- [使用 n8n Cloud](../)
- [免费试用并选择套餐](../start-your-free-trial.md)
- [使用 Cloud 控制台](../use-the-cloud-console.md)
- [更新版本](../update-your-version.md)
- [配置 Cloud](../configure-cloud/README.md)
- [Gateway 额度](../gateway-credits/README.md)
- [理解并发](../understand-concurrency.md)
- [下载工作流](../download-workflows.md)
- [使用 n8n Assistant](../../../build/ways-of-building-workflows/n8n-assistant.md)
- [n8n 套餐与价格](https://n8n.io/pricing/)
