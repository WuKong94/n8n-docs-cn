---
description: Insights 使用分析。
contentType: explanation
nodeTitle: 使用 Insights 跟踪使用情况
originalFilePath: insights.md
originalUrl: https://docs.n8n.io/insights
url: https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Insights <a href="#insights" id="insights"></a>

Insights 让实例所有者和管理员了解工作流随时间变化的运行表现。此功能包含三部分：

- [**Insights 汇总横幅**](#insights-summary-banner)：在 **Overview**（概览）空间顶部，显示实例最近 7 天的关键指标。
- [**Insights 仪表盘**](#insights-dashboard)：通过更详细的图表，展示各工作流的指标及历史对比。
- [**节省时间（工作流投资回报率）**](#setting-the-time-saved-by-a-workflow)：可为每个工作流设置固定的节省时间，也可根据某次执行实际经过的工作流路径动态计算。

{% hint style="info" %}
**功能可用范围**

显示最近 7 天活动的 Insights 汇总横幅可用于：

- **n8n Cloud：**所有方案。
- **自托管：**所有版本。

Insights 仪表盘可用于：

- **n8n Cloud：**Pro、Enterprise。
- **自托管：**Business、Enterprise。
{% endhint %}

## Insights 汇总横幅 <a href="#insights-summary-banner" id="insights-summary-banner"></a>

n8n 为 Insights 汇总横幅和仪表盘收集多项指标，包括：

- 生产执行总次数（不包含子工作流执行和手动执行）。
- 失败的生产执行总次数。
- 生产执行失败率。
- 节省时间（至少在一个活跃工作流上设置后）。
- 平均运行时间（包括所有 Wait 节点的等待时间）。

## Insights 仪表盘 <a href="#insights-dashboard" id="insights-dashboard"></a>

从侧边导航进入 **Insights**。也可点击汇总横幅中的各项指标，跳转到对应图表。

Insights 仪表盘还有一个表格，按工作流显示分析结果，包括生产执行总次数、失败的生产执行次数、失败率、节省时间和平均运行时间。

## Insights 时间范围 <a href="#insights-time-periods" id="insights-time-periods"></a>

默认情况下，Insights 汇总横幅和仪表盘显示滚动的 7 天窗口，并与上一时段对比，以查看各项指标的增减。在仪表盘中，付费方案还可显示其他日期范围的数据：

- **n8n Cloud Pro：**7 天和 14 天。
- **自托管 Business：**24 小时、7 天、14 天和 30 天。
- **n8n Cloud Enterprise、自托管 Enterprise：**24 小时、7 天、14 天、30 天、90 天、6 个月和 1 年。

## 设置工作流节省的时间 <a href="#setting-the-time-saved-by-a-workflow" id="setting-the-time-saved-by-a-workflow"></a>

可以为每个工作流跟踪节省的时间。此设置有助于比较自动化流程与手动完成同一任务或流程的耗时，计算长期节省的时间。

配置后，n8n 根据生产执行次数计算工作流节省的时间，并显示在汇总横幅和 Insights 仪表盘上。

可选择两种节省时间计算方法：

### 固定节省时间 <a href="#fixed-time-saved" id="fixed-time-saved"></a>

使用固定节省时间时，设置一个时间值，应用于工作流的每次生产执行，不受实际执行路径影响。

配置固定节省时间：

1. 进入工作流。
2. 打开右上角的三点菜单，选择 **Settings**（设置）。
3. 在 **Estimated time saved**（预计节省时间）下拉菜单中，选择 **Fixed**（固定）。
4. 输入每次执行节省的工作分钟数。
5. 保存设置。

### 动态节省时间 <a href="#dynamic-time-saved" id="dynamic-time-saved"></a>

动态节省时间根据实际执行路径计算，适用于不同执行路径节省时间不同的工作流。

配置动态节省时间：

1. 进入工作流。
2. 打开右上角的三点菜单，选择 **Settings**（设置）。
3. 在 **Estimated time saved**（预计节省时间）下拉菜单中，选择 **Dynamic**（动态）。
4. 保存设置。
5. 在工作流中节省时间的位置添加 **Time Saved**（节省时间）节点。
6. 为每个 Time Saved 节点配置：
   - **Time saved**（节省时间）：节省的时间量，以分钟计。
   - **Calculation mode**（计算模式）：选择每次执行对全部数据项只计算一次，或按数据项计算；后者会将节省的分钟数乘以输入数据项总数。

使用动态节省时间时，n8n 会累加一次工作流运行中所有实际执行的 Time Saved 节点的时间，计算此次执行节省的总时间。

{% hint style="info" %}
**子工作流和错误工作流支持**

目前仅支持在父工作流中跟踪节省时间，暂不支持子工作流，计划在未来版本支持。错误工作流执行不会计入节省时间，但会计入其他 Insights 指标。
{% endhint %}

## 禁用或配置 Insights 指标收集 <a href="#disable-or-configure-insights-metrics-collection" id="disable-or-configure-insights-metrics-collection"></a>

如果自托管 n8n，可以通过[环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md)禁用或配置 Insights 及指标收集。

默认情况下，n8n 将压缩汇总后的 Insights 数据保留 365 天（`N8N_INSIGHTS_MAX_AGE_DAYS`）。保留时间上限为 730 天（两年），可设置较小的值以缩短窗口。要完全关闭 Insights 收集，请设置 `N8N_DISABLED_MODULES=insights`（参阅[环境变量页面](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md)）。

{% hint style="info" %}
**自托管升级**

旧版本的清理可能遵循许可证决定的默认值（通常为 180 天）。现在由 `N8N_INSIGHTS_MAX_AGE_DAYS` 控制清理（默认 365 天）。如果希望沿用类似以前默认值的保留窗口，请设置 `N8N_INSIGHTS_MAX_AGE_DAYS=180`。
{% endhint %}

n8n 以一小时粒度存储近期 Insights 数据，再将较旧的数据压缩汇总为按天和按周的摘要。使用 [Insights 环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md)控制压缩汇总的时间、批次限制、运行时长和延迟。

将这些阈值提高到默认值以上，会保留更久的细粒度数据。这会为 `insights_by_period` 增加更多数据行，占用比仅延长 `N8N_INSIGHTS_MAX_AGE_DAYS` 更多的数据库空间。如果只需要更长的保留窗口，请先增加 `N8N_INSIGHTS_MAX_AGE_DAYS`。

## Insights 常见问题 <a href="#insights-faqs" id="insights-faqs"></a>


### n8n 使用哪些执行来计算 Insights 横幅和仪表盘的值？ <a href="#which-executions-do-n8n-use-to-calculate-the-values-in-the-insights-banner-and-dashboard" id="which-executions-do-n8n-use-to-calculate-the-values-in-the-insights-banner-and-dashboard"></a>

Insights 从生产执行收集数据，例如由定时计划或 Webhook 触发的已发布工作流执行，也包括错误工作流执行。不包括手动（测试）执行和子工作流执行。

n8n 将错误工作流执行自身的结果和运行时间记在错误工作流上，而非原先失败的工作流上。这会影响执行总次数、失败指标和平均运行时间。在 n8n 2.23.0 及更高版本中，错误工作流执行不会计入节省时间。

### 升级到包含 Insights 的版本时，n8n 会使用历史执行数据吗？ <a href="#does-n8n-use-historic-execution-data-when-upgrading-to-a-version-with-insights" id="does-n8n-use-historic-execution-data-when-upgrading-to-a-version-with-insights"></a>

只有更新到首个支持 Insights 的 n8n 1.89.0 后，n8n 才开始收集分析数据。因此，Insights 仅报告此后的执行，不会显示更早时期的执行数据。

## 相关资源 <a id="related-resources"></a>

* [观测与日志](./)
* [向外部系统发送日志流](stream-logs-to-external-systems.md)
