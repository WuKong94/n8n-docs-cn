---
description: 在 n8n Cloud 控制台中，手动或通过自动充值购买额外 Assistant 额度，在每月额度用完后继续使用 n8n Assistant。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 充值 Assistant 额度 <a id="top-up-assistant-credits"></a>

n8n Cloud 套餐每月包含一定 [Assistant 额度](README.md)，在每月第一天重置。如果重置前已用完套餐内含额度，可以充值额外额度，继续使用 n8n Assistant。n8n Assistant 仅在套餐内含额度耗尽后，才以相同费率使用额外额度。

你可以按需手动购买额外额度，也可以启用自动充值，让 n8n 自动购买。

只有实例所有者可以充值，且必须持有有效的付费订阅。免费试用包含一次性 Assistant 额度，但不支持充值；如果试用额度用完，需要升级为付费套餐才能获得更多额度。

{% hint style="warning" %}
**Assistant 额度仅支付 n8n Assistant 的费用**

额外 Assistant 额度仅支付与 n8n Assistant 对话的费用，不支付工作流或智能体运行时的 AI 模型调用费用。对于这些调用，请改为[充值 Gateway 额度](../gateway-credits/top-up-gateway-credits.md)，或使用自有服务商凭据。充值后即为最终交易，因此付款前请确认正在充值哪一种余额。
{% endhint %}

## 手动充值 <a id="top-up-manually"></a>

1. 打开 [n8n Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Assistant credits（Assistant 额度）**。
1. 在 **Balance（余额）** 卡片上选择 **Top up（充值）**。
1. 选择额度包。
1. 阅读额度条款，并勾选复选框表示接受。
1. 选择 **Continue to checkout（继续结账）** 并完成付款。根据账单所属国家或地区，可能需要缴税。

付款完成后，页面会显示新增的额外额度。这些额度在购买 12 个月后到期。

## 设置自动充值 <a id="set-up-auto-top-up"></a>

当额外额度余额低于设定阈值时，自动充值会购买额外额度。如果你每天依赖 n8n Assistant，不希望它在套餐内含额度耗尽时暂停，可以启用此功能。自动充值始终使用订阅中保存的付款方式。

1. 打开 [Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Assistant credits（Assistant 额度）**。
1. 在 **Auto top-up extra credits（自动充值额外额度）** 卡片中启用自动充值。
1. 设置 **When extra credits drop to（当额外额度降至）**，即触发充值的额外额度阈值，以及 **Top up extra credits to（将额外额度充值至）**，即充值后的目标额外额度。Cloud 控制台会显示允许设置的最小值。
1. 如有需要，设置 **Monthly auto top-up limit（每月自动充值限额）**，限制每月自动充值的扣款金额。该限额默认启用。
1. 选择 **Save changes（保存修改）**，然后选择 **Turn on auto top-up（启用自动充值）** 进行确认。

{% hint style="info" %}
自动充值只关注额外额度。套餐内含额度不计入阈值，因此自动充值会预先保留额外额度，供套餐内含额度耗尽后使用。
{% endhint %}

自动充值的行为如下：

- 如果设置了每月限额，自动充值在当前自然月（UTC）累计扣款达到该金额后暂停，并在下个月恢复。
- Assistant 额度与 [Gateway 额度](../gateway-credits/top-up-gateway-credits.md)的自动充值设置相互独立。启用其中一个不会同时启用另一个。

## 退款 <a id="refunds"></a>

充值后即为最终交易。除法律要求的情况外，n8n 不退还未使用额度。如果认为收费有误，请[联系 n8n 支持](https://www.n8n.io/contact)。到期和失效规则请参阅[额度到期与失效](README.md#credit-expiry-and-forfeiture)。

## 相关资源 <a id="related-resources"></a>

- [Assistant 额度](README.md)
- [跟踪 Assistant 额度支出](track-assistant-credit-spend.md)
- [充值 Gateway 额度](../gateway-credits/top-up-gateway-credits.md)
