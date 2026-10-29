---
description: 在 n8n Cloud 控制台中，手动或通过自动充值增加 Gateway 额度余额。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 充值 Gateway 额度 <a id="top-up-gateway-credits"></a>

当 [Gateway 额度](README.md)余额不足时，可以在 n8n Cloud 控制台充值。你可以按需手动添加额度，也可以启用自动充值，让 n8n 自动补充余额。

只有实例所有者可以充值，且必须持有有效的付费订阅。免费试用包含 Gateway 额度，但不支持充值；如果试用期间用完免费额度，需要升级为付费套餐才能添加更多额度。

{% hint style="warning" %}
**Gateway 额度不支付 n8n Assistant 的费用**

Gateway 额度仅支付工作流节点使用的 AI 模型和服务费用。如果需要增加 n8n Assistant 的额度，请改为[充值 Assistant 额度](../assistant-credits/top-up-assistant-credits.md)。充值后即为最终交易，因此付款前请确认正在充值哪一种余额。
{% endhint %}

## 手动充值 <a id="top-up-manually"></a>

1. 打开 [Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Gateway credits（Gateway 额度）**。
1. 在 **Balance（余额）** 卡片上选择 **Top up（充值）**。
1. 选择充值金额。
1. 阅读额度条款，并勾选复选框表示接受。
1. 选择 **Continue to checkout（继续结账）** 并完成付款。你可以使用订阅中保存的付款方式，也可以使用其他付款方式。根据账单所属国家或地区，可能需要缴税。n8n 会通过邮件发送发票。

付款完成后，页面会显示新余额。

## 设置自动充值 <a id="set-up-auto-top-up"></a>

余额低于设定阈值时，自动充值会补充余额，使其保持在零以上，让依赖 Gateway 额度的工作流持续运行。与手动充值不同，自动充值始终使用订阅中保存的付款方式。

1. 打开 [Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Gateway credits（Gateway 额度）**。
1. 在 **Auto top-up（自动充值）** 卡片上启用自动充值。
1. 设置 **When balance drops to（当余额降至）**，即触发充值的余额阈值，以及 **Top up to（充值至）**，即充值后的目标余额。
1. 如有需要，启用 **Monthly auto top-up limit（每月自动充值限额）**，限制每月自动添加额度的金额。
1. 选择 **Save changes（保存修改）**，然后选择 **Turn on auto top-up（启用自动充值）** 进行确认。

{% hint style="info" %}
如果保存时余额已经低于阈值，n8n 会立即触发一次充值，使余额达到目标值。保存前，页面会显示预计费用。
{% endhint %}

自动充值的行为如下：

- 每次自动充值添加额度后，n8n 都会通过邮件发送发票。
- 如果设置了每月限额，自动充值在当月累计添加到该金额后暂停，并在下个月恢复。
- 付款失败后，n8n 会重试。如果重试仍失败，n8n 会关闭自动充值并发送邮件通知。由于自动充值始终使用订阅中保存的付款方式，请先修正该付款方式，再重新启用。

## 超额使用 <a id="overspend"></a>

执行过程中，余额可能耗尽。此时 n8n 会让已经发出的 Gateway 请求完成，不会中途停止，因此余额可能略微低于零。超额部分会在下次充值中扣除，并显示在[充值记录](track-gateway-credit-spend.md#top-up-history)中。

## 退款 <a id="refunds"></a>

充值后即为最终交易。除法律要求的情况外，n8n 不退还未使用额度。如果认为收费有误，请[联系 n8n 支持](https://www.n8n.io/contact)。到期和失效规则请参阅[额度到期与失效](README.md#credit-expiry-and-forfeiture)。

## 相关资源 <a id="related-resources"></a>

- [Gateway 额度](README.md)：了解 Gateway 额度的工作方式。
- [跟踪 Gateway 额度支出](track-gateway-credit-spend.md)：监控余额、支出和充值记录。
- [服务价格页面](https://app.n8n.cloud/service-pricing)：所有受支持服务和模型的当前费率。
