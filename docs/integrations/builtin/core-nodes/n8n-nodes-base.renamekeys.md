---
title: Rename Keys（重命名键）
description: 工作流自动化平台 n8n 中的 Rename Keys（重命名键） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: Rename Keys（重命名键）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Rename Keys（重命名键） <a href="#rename-keys" id="rename-keys"></a>

使用 Rename Keys 节点重命名 n8n 中键值对的键。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

Rename Keys 节点可重命名一个或多个键。选择 **Add new key**（添加新键）按钮以重命名键。

为每个键输入以下内容：

- **Current Key Name**（当前键名）：要重命名的键的当前名称。
- **New Key Name**（新键名）：希望赋予该键的新名称。

## 节点选项 <a href="#node-options" id="node-options"></a>

选择是否使用 **Regex**（正则表达式）识别要重命名的键。使用此选项时，还必须输入：

* 要使用的 **Regular Expression**（正则表达式）。
* **Replace With**（替换为）：为匹配 **Regular Expression**（正则表达式）的键输入新名称。
* 还可选择以下正则表达式专用选项：
    * **Case Insensitive**（不区分大小写）：关闭时，正则表达式区分大小写；开启时不区分。
    * **Max Depth**（最大深度）：输入替换键的最大深度，`-1` 表示不限制，`0` 表示仅顶层。

{% hint style="warning" %}
**正则表达式的影响**

正则表达式可能影响所有匹配的键，包括已经重命名的键。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Rename Keys（重命名键） 集成模板](https://n8n.io/integrations/rename-keys)，或[搜索所有模板](https://n8n.io/workflows/)
