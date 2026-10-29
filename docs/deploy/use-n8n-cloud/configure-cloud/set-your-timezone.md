---
description: 如何在 n8n Cloud 上设置时区。
contentType: howto
nodeTitle: 设置时区
originalFilePath: manage-cloud/set-cloud-timezone.md
originalUrl: 'https://docs.n8n.io/manage-cloud/set-cloud-timezone'
url: 'https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/set-your-timezone'
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 Cloud 实例的时区 <a href="#set-the-cloud-instance-timezone" id="set-the-cloud-instance-timezone"></a>

你可以更改 n8n 实例的时区。这会影响 [Schedule Trigger（定时触发器）](../../../integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/README.md)和 [Date & Time（日期与时间）节点](../../../integrations/builtin/core-nodes/n8n-nodes-base.datetime.md)。用户可以在[工作流设置](../../../build/manage-workflows/configure-workflow-settings.md)中为单个工作流配置时区。

要更改实例时区：

1. 打开 [n8n Cloud 控制台](../use-the-cloud-console.md)，选择 **Instance settings（实例设置）**。
1. 在 **Runtime（运行时）** 部分，从 **Time zone（时区）** 下拉列表选择所需时区。你可以输入文字搜索列表。
1. 在页面底部的操作栏中选择 **Save and restart（保存并重启）**。实例会重启以应用修改，重启完成前会处于离线状态。

## 相关资源 <a id="related-resources"></a>

* [配置 Cloud](./)
* [查找 IP 地址](find-your-ip-addresses.md)
* [管理数据](manage-your-data.md)
* [更改实例所有者或用户名](change-instance-ownership-or-username.md)
