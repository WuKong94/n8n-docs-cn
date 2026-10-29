---
title: 在 Code 节点中使用 AI
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

{% hint style="info" %}
**功能可用范围**

Code 节点的 AI 辅助功能适用于 Cloud 用户，自托管 n8n 不提供。
{% endhint %}

{% hint style="info" %}
**AI 生成的代码会覆盖现有代码**

如果已在 **Code（代码）** 标签页编写代码，AI 生成的代码会将其替换。n8n 建议先用 AI 生成初始代码，再按需要编辑。
{% endhint %}

使用 ChatGPT 在 Code 节点中生成代码的步骤如下：

1. 在 Code 节点中，将 **Language（语言）** 设为 **JavaScript**。
1. 选择 **Ask AI（询问 AI）** 标签页。
1. 编写请求。
1. 选择 **Generate Code（生成代码）**。n8n 会将请求发送给 ChatGPT，再在 **Code（代码）** 标签页显示结果。
