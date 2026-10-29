---
title: 时区设置
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

{% hint style="info" %}
**时区设置**

此节点依赖时区设置，n8n 按以下顺序选择：

1. 已设置工作流时区时，使用工作流时区。更多信息，请参阅[工作流设置](../../../../../../../build/manage-workflows/configure-workflow-settings.md)。
2. 未设置工作流时区时，使用 n8n 实例时区。自托管实例的默认值在原文中写作 `America/New York`；译注：该写法含空格，实际配置应使用 America/New_York。n8n Cloud 会在实例所有者注册时尝试检测其时区，检测失败则默认使用 GMT。自托管用户可通过[环境变量](../../../../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md)更改实例时区；n8n Cloud 实例所有者可在 Cloud 控制台[更改实例时区](../../../../../../../deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md)。
{% endhint %}
