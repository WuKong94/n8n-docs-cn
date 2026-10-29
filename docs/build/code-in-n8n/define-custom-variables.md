---
title: 自定义变量
description: 通过自定义变量，在 n8n 工作流中存储和复用值。
contentType: howto
nodeTitle: 定义自定义变量
originalFilePath: code/variables.md
originalUrl: https://docs.n8n.io/code/variables
url: https://docs.n8n.io/build/code-in-n8n/define-custom-variables
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义变量 <a href="#custom-variables" id="custom-variables"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐提供自定义变量：

- **n8n Cloud：** Pro、Enterprise
- **自托管：** Business、Enterprise

只有实例所有者和管理员可以创建变量。
{% endhint %}

自定义变量是只读变量，可用于在 n8n 工作流中存储和复用值。

{% hint style="warning" %}
**变量的作用范围和可用性**

* **全局变量**适用于 n8n 实例中的所有用户和项目。
* **项目变量**仅适用于创建它的特定项目。
* 项目变量从 n8n 1.118.0 起可用。更早版本只支持从左侧菜单访问的全局变量。
{% endhint %}

## 创建变量 <a href="#create-variables" id="create-variables"></a>

可以从概览页面或某个项目进入 **Variables（变量）** 标签页。

创建变量的步骤如下：

1. 在 **Variables（变量）** 标签页选择 **Add Variable（添加变量）**。
2. 输入 **Key（键）** 和 **Value（值）**。键最长 50 个字符，值最长 1000 个字符。n8n 将键和值可用的字符限制为大小写字母、数字和下划线（`A-Z`、`a-z`、`0-9`、`_`）。
3. 选择 **Scope（作用范围）**（仅从概览页面创建时可用）：
    * **Global（全局）**：变量适用于实例中的所有项目。
    * **Project（项目）**：变量仅适用于某个指定项目，可以自行选择项目。
    * 从项目页面创建时，作用范围会自动设为该项目。
4. 选择 **Save（保存）**。变量即可在作用范围内的工作流中使用。

## 编辑和删除变量 <a href="#edit-and-delete-variables" id="edit-and-delete-variables"></a>

编辑或删除变量的步骤如下：

1. 在 **Variables（变量）** 标签页，将鼠标悬停在要修改的变量上。
2. 选择 **Edit（编辑）** 或 **Delete（删除）**。

## 在工作流中使用变量 <a href="#use-variables-in-workflows" id="use-variables-in-workflows"></a>

可以在 Code 节点和表达式[^1]中访问变量：

```javascript
// Access a variable
$vars.<variable-name>
```

所有变量都是字符串。

工作流执行时，n8n 会用变量值替换变量。如果变量没有值，n8n 将其视为 `undefined`，这种情况下工作流不会自动失败。

{% hint style="info" %}
**变量优先级**

项目变量与全局变量具有相同键时，项目变量优先，在该项目的工作流中覆盖全局变量值。
{% endhint %}

变量是只读的，必须通过界面更改值。如果需要在工作流中设置并访问自定义数据，请使用[工作流静态数据](cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。

[^1]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义值，而不是提供静态值。

## 相关资源 <a id="related-resources"></a>

* [在 n8n 中编写代码](./)
* [使用 Code 节点](using-the-code-node.md)
* [获取 AI 编程帮助](get-coding-help-from-ai.md)
* [使用内置快捷方法](use-built-in-shortcuts.md)
* [实用示例](cookbook/README.md)
