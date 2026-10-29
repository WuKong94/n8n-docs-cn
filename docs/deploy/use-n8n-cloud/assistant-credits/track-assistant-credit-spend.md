---
description: 在 n8n Cloud 控制台和 n8n Assistant 面板中，监控 Assistant 额度余额、支出、高用量用户和充值记录。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 跟踪 Assistant 额度支出 <a id="track-assistant-credit-spend"></a>

n8n Cloud 控制台的 **Assistant credits（Assistant 额度）** 页面显示 [Assistant 额度](README.md)余额、各时段的支出、高用量用户和充值记录。打开 [Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Assistant credits** 即可进入。你也可以在 **Overview（概览）** 页面选择 Assistant 余额旁的 **Manage（管理）**。

你也可以在编辑器的 n8n Assistant 面板中查看余额。

## 余额 <a id="balance"></a>

余额卡片显示可用额度，分为两部分：

- **Included（内含额度）**：本月套餐内含额度的剩余数量，以及重置日期。
- **Extra credits（额外额度）**：已购买额外额度的剩余数量。额外额度可以跨月结转，直到到期。

免费试用期间，卡片会显示试用额度的剩余数量。

状态标签会显示 n8n Assistant 当前正在使用哪种额度：

- **Within included（使用内含额度）**：n8n Assistant 正在使用套餐内含额度。
- **Using extra credits（使用额外额度）**：套餐内含额度已用完，n8n Assistant 正在使用额外额度。
- **Paused — no extra credits（已暂停，无额外额度）**：两种额度均已用完；在充值或套餐内含额度重置之前，n8n Assistant 会保持暂停。

如果你是付费套餐的实例所有者，可以在这里充值。详情请参阅[充值 Assistant 额度](top-up-assistant-credits.md)。

## 支出 <a id="spend"></a>

支出图表显示实例在过去 24 小时、7 天或 30 天内使用的额度，并区分套餐内含额度和额外额度，便于查看超出每月额度的频率。

如果每个月都需要使用额外额度，可以比较充值费用与升级套餐所提供的额度。请参阅 [n8n 套餐与价格](https://n8n.io/pricing/)。

## 高用量用户 <a id="top-users"></a>

实例上的所有用户共享同一个 Assistant 额度余额。高用量用户卡片显示使用额度最多的用户，以及其用量占总用量的百分比；其余用户统一归入 **Other users（其他用户）**。

## 充值记录 <a id="top-up-history"></a>

充值记录列出通过手动和自动充值添加到余额的额外额度。每条记录显示数量、日期和额度到期时间。

## 在编辑器中查看余额 <a id="check-your-balance-in-the-editor"></a>

在编辑器中，打开 n8n Assistant 面板的额度菜单，可以查看：

- 实例的剩余额度总量，包括套餐内含额度和额外额度。
- 当前对话至今已消耗的额度。

余额降到 10% 或以下时，聊天输入框上方会出现余额不足提示横幅。你可以关闭横幅；下次余额再次跨过该阈值时，它会重新出现。

余额耗尽后，n8n Assistant 会显示 **You've run out of AI credits（AI 额度已用完）**，无法再发送新消息。如何获得更多额度，请参阅 [Assistant 额度耗尽后](README.md#when-your-assistant-credits-run-out)。

## 相关资源 <a id="related-resources"></a>

- [Assistant 额度](README.md)
- [充值 Assistant 额度](top-up-assistant-credits.md)
- [跟踪 Gateway 额度支出](../gateway-credits/track-gateway-credit-spend.md)
