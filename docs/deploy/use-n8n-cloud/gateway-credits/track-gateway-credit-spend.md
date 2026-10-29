---
description: 在 n8n Cloud 控制台中，监控 Gateway 额度余额、按模型或工作流分类的支出，以及充值记录。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 跟踪 Gateway 额度支出 <a id="track-gateway-credit-spend"></a>

n8n Cloud 控制台的 **Gateway credits（Gateway 额度）** 页面显示余额、各时段的支出和充值记录。打开 [Cloud 控制台](../use-the-cloud-console.md)，在侧边栏选择 **Gateway credits** 即可进入。你也可以在 **Overview（概览）** 页面选择 Gateway 余额旁的 **Manage（管理）**。

你也可以在编辑器中支持此功能的节点上，在 Gateway 额度选项旁查看当前余额。

## 余额 <a id="balance"></a>

余额卡片会显示剩余额度，包括注册时赠送的免费额度还剩多少。付费套餐用户可以在这里充值。详情请参阅[充值 Gateway 额度](top-up-gateway-credits.md)。

## 支出 <a id="spend"></a>

支出图表显示不同时间段的额度使用明细。你可以：

- 调整时间范围，查看近期或较长时间的使用情况。
- 按模型或服务分组，查看哪些服务商的费用最高。
- 按工作流分组，查看哪些工作流消耗的额度最多。

按工作流分组有助于找到超出预期支出的工作流，例如按高频时间计划调用模型的工作流。

## 充值记录 <a id="top-up-history"></a>

充值记录列出添加到余额的每一笔额度，包括注册赠送额度、手动充值和自动充值。每条记录都显示金额、日期和额度到期时间。已经退款的充值仍会保留在列表中，并标记为已退款。

如果 n8n 为了让已发出的请求完成而使余额低于零，超额部分会在下次充值中扣除，并在这里显示。详情请参阅[超额使用](top-up-gateway-credits.md#overspend)。

## 通知 <a id="notifications"></a>

余额发生以下变化时，n8n 会通过邮件通知实例所有者：

- 余额不足时，提醒你在工作流停止之前充值。
- 余额耗尽时。
- 自动充值成功添加额度、无法从付款方式扣款，或达到每月限额而暂停时。

## 余额耗尽后 <a id="when-your-balance-runs-out"></a>

余额归零后，使用 Gateway 额度的节点会失败，直到你添加额度。不使用 Gateway 额度的执行任务会照常运行。

- 付费套餐用户可以[充值余额](top-up-gateway-credits.md)，或设置自动充值以避免中断。
- 免费试用不支持充值，需要升级为付费套餐才能添加更多额度。
- 无论使用哪种套餐，都可以将受影响的节点切换为自有凭据。切换方法请参阅[使用 Gateway 额度](../../../build/understand-workflows/use-gateway-credits.md)。

## 相关资源 <a id="related-resources"></a>

- [Gateway 额度](README.md)：了解 Gateway 额度的工作方式。
- [充值 Gateway 额度](top-up-gateway-credits.md)：手动或自动添加额度。
- [服务价格页面](https://app.n8n.cloud/service-pricing)：所有受支持服务和模型的当前费率。
