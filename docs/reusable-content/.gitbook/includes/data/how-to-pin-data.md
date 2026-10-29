---
title: 如何固定数据
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

在节点中固定数据的步骤如下：

1. 运行节点，加载数据。
2. 在 **OUTPUT（输出）** 视图中选择 **Pin data（固定数据）** <img src="../../assets/data-pinning-button.png" alt="固定数据图标" data-size="line">。固定生效后，按钮会被禁用，输出视图显示“This data is pinned（数据已固定）”横幅。

{% hint style="info" %}
**输出二进制数据的节点**

输出中包含二进制数据时，不能固定数据。
{% endhint %}
