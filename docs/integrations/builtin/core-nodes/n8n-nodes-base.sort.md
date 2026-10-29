---
title: Sort（排序）
description: 工作流自动化平台 n8n 中的 Sort（排序） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: medium
nodeTitle: Sort（排序）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.sort.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Sort（排序） <a href="#sort" id="sort"></a>

使用 Sort 节点按所需顺序排列数据项列表，或生成随机选择结果。

{% hint style="info" %}
**数组排序行为**

Sort 操作使用 JavaScript 的默认排序方式：先将待排序元素转换为字符串，再比较它们的值。更多信息请参阅 [Mozilla 的数组排序指南](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用 **Type**（类型）参数配置节点。

从下拉菜单中选择以下一种排序输入方式。

### Simple（简单） <a href="#simple" id="simple"></a>

使用所选字段进行升序或降序排序。

选择此 **Type**（类型）后：

* 使用 **Add Field To Sort By**（添加排序字段）按钮输入 **Field Name**（字段名称）。
* 选择 **Ascending**（升序）或 **Descending**（降序）。

#### Simple（简单）选项 <a href="#simple-options" id="simple-options"></a>

**Type**（类型）为 **Simple**（简单）时，可选择 **Disable Dot Notation**（禁用点表示法）。默认情况下，n8n 启用点表示法，以 `parent.child` 格式引用子字段。开启此选项可禁用点表示法，关闭则继续使用。

### Random（随机） <a href="#random" id="random"></a>

将列表排列为随机顺序。

### Code（代码） <a href="#code" id="code"></a>

输入自定义 JavaScript 代码来执行排序。如果简单排序无法满足需求，可使用此选项。

在 **Code**（代码）输入框中填写自定义 JavaScript 代码。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Sort（排序） 集成模板](https://n8n.io/integrations/sort)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
