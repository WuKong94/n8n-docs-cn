---
title: Insights 环境变量
description: 通过环境变量配置自托管 n8n 实例的 Insights 指标收集。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 洞察
originalFilePath: hosting/configuration/environment-variables/insights.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/insights
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Insights 环境变量 <a href="#insights-environment-variables" id="insights-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

Insights 让实例所有者和管理员了解工作流表现随时间的变化。详情请参阅[洞察](../../../../../administer/observe-and-log/track-usage-with-insights.md)。

{% hint style="warning" %}
**存储与聚合压缩阈值**

`N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` 和 `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` 指定每次聚合压缩前，高分辨率 Insights 数据的保留天数。数据最初按小时存储，再从小时聚合为天，最后从天聚合为周。保留天数可在实例中配置。

增大这些值会推迟聚合压缩，增加 `insights_by_period` 中的记录行数及数据库占用。它与保留期限的关系请参阅[洞察](../../../../../administer/observe-and-log/track-usage-with-insights.md#disable-or-configure-insights-metrics-collection)。
{% endhint %}

如果聚合压缩造成数据库负载问题，可以调整运行频率和单次工作量：

- 减小 `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES`，提高运行频率，减少两次运行之间积累的数据。
- 增大 `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS`，延长批次之间的等待时间。
- 减小 `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN`，减少每次运行处理的批次数。
- 减小 `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS`，让每次运行更早停止。

这些设置只控制聚合压缩的工作量和调度，不改变保留期限，也不改变各聚合步骤的数据年龄阈值。



| 变量 | 类型 | 默认值 | 说明 |
 |:---------------------------------------------------------|:-------|:--------|:----------------------------------------------------------------------------------------|
| `N8N_DISABLED_MODULES` | String | - | 设为 `insights`，禁用实例的此功能及指标收集。 |
| `N8N_INSIGHTS_COMPACTION_BATCH_SIZE` | Number | 500 | 单个批次聚合压缩的原始 Insights 数据条数。 |
| `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS` | Number | 100 | 完整聚合压缩批次之间的延迟，单位为毫秒。增大可延长批次间等待，设为 `0` 可跳过延迟。 |
| `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | Number | 180 | 按天存储的 Insights 记录经过多少天后聚合为周。 |
| `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | Number | 90 | 按小时存储的 Insights 记录经过多少天后聚合为天。 |
| `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES` | Number | 60 | 运行聚合压缩的间隔，单位为分钟。减小可提高频率，减少运行间积累的数据。 |
| `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN` | Number | 1000 | 单次运行最多处理的聚合压缩批次数。减小可减少每次运行的批次数，设为 `0` 可禁用限制。 |
| `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS` | Number | 300 | 单次聚合压缩的最长运行时长，单位为秒。减小可更早停止，设为 `0` 可禁用限制。 |
| `N8N_INSIGHTS_FLUSH_BATCH_SIZE` | Number | 1000 | 刷新缓冲区前，最多保留的 Insights 数据条数。 |
| `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS` | Number | 30 | 将 Insights 数据写入数据库的间隔，单位为秒。 |
| `N8N_INSIGHTS_MAX_AGE_DAYS` | Number | 365 | 聚合后的 Insights 数据保留多少天后清理。最大为 730 天，即两年。 |
| `N8N_INSIGHTS_PRUNE_CHECK_INTERVAL_HOURS` | Number | 24 | 实例检查并删除超过有效最长保留时长的 Insights 数据的频率，单位为小时。 |



## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
