---
title: Code 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Code 节点常见问题
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues
description: 了解 n8n 工作流自动化平台中 Code 节点的常见问题，包括问题详情和建议的解决方法。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 常见问题 <a id="common-issues"></a>

本页介绍 [Code 节点](./README.md)的一些常见错误和问题，以及解决或排查步骤。

## 代码未正确返回数据项 <a href="#code-doesnt-return-items-properly" id="code-doesnt-return-items-properly"></a>

当 Code 节点中的代码未按预期格式返回数据时，会出现此错误。

在 n8n 中，节点之间传递的数据都是对象数组。每个对象都通过 `json` 键包装另一个对象：

```javascript
[
  {
    "json": {
	  // your data goes here
	}
  }
]
```

要排查此错误，请检查以下内容：

* 阅读[数据结构](../../../../build/work-with-data/understand-n8ns-data-structure.md)，了解 Code 节点接收的数据，以及节点输出数据须满足的要求。
* 了解数据项的工作方式，以及如何通过[数据项关联](../../../../build/work-with-data/reference-data/link-data-items/README.md)连接前序节点的数据项。

## A 'json' property isn't an object（json 属性不是对象） <a href="#a-json-property-isnt-an-object" id="a-json-property-isnt-an-object"></a>

当 Code 节点返回的数据中，`json` 键未指向对象时，会出现此错误。

如果将 `json` 设为数组等其他数据结构，就可能出现此问题：

```javascript
[
  {
    "json": [
	  // Setting `json` to an array like this will produce an error
	]
  }
]
```

要解决此问题，请确保返回数据中的 `json` 键引用一个对象：

```javascript
[
  {
    "json": {
	  // Setting `json` to an object as expected
	}
  }
]
```

## 代码未返回对象 <a href="#code-doesnt-return-an-object" id="code-doesnt-return-an-object"></a>

如果 Code 节点未返回任何内容，或返回了非预期结果，可能会出现此错误。

要解决此问题，请确保 Code 节点返回[预期的数据结构](../../../../build/work-with-data/understand-n8ns-data-structure.md)：

```javascript
[
  {
    "json": {
	  // your data goes here
	}
  }
]
```

如果代码返回 `'undefined'`，而不是预期结果，也可能出现此错误。请确保 Code 节点引用的数据在每次执行时都存在，且结构符合代码预期。

## import 和 export 只能出现在顶层 <a href="#import-and-export-may-only-appear-at-the-top-level" id="import-and-export-may-only-appear-at-the-top-level"></a>

在 Code 节点中尝试使用 `import` 或 `export` 时，会出现此错误。n8n 的 JavaScript 沙盒不支持这两种语法，请改用 `require` 函数加载模块。

要解决此问题，可尝试将 `import` 语句改为使用 `require`：

```javascript
// Original code:
// import express from "express";
// New code:
const express = require("express");
```

## Cannot find module '\<module>'（找不到模块） <a href="#cannot-find-module-andltmoduleandgt" id="cannot-find-module-andltmoduleandgt"></a>

在 Code 节点中使用 `require`，但 n8n 找不到模块时，会出现此错误。

{% hint style="warning" %}
**仅适用于自托管环境**

n8n 的 [Cloud](../../../../deploy/use-n8n-cloud/README.md) 版本不支持导入模块。
{% endhint %}

如果你[自行托管](../../../../deploy/host-n8n/README.md) n8n，请按以下步骤操作：

* 将模块安装到 n8n 所在环境。
  * 如果通过 [npm](../../../../deploy/host-n8n/install-options/install-with-npm.md) 运行 n8n，请将模块安装到与 n8n 相同的环境中。
  * 如果通过 [Docker](../../../../deploy/host-n8n/install-options/install-with-docker.md) 运行 n8n，需要基于官方 n8n 镜像构建包含所需模块的[自定义镜像](https://docs.docker.com/build/building/base-images/)。
* 设置 `NODE_FUNCTION_ALLOW_BUILTIN` 和 `NODE_FUNCTION_ALLOW_EXTERNAL` [环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node.md)，允许导入模块。

## 使用全局变量 <a href="#using-global-variables" id="using-global-variables"></a>

有时需要在单次执行内或跨多次执行，设置和读取与工作流有关的简单全局数据。例如，编写项目更新列表报告时，可能希望包含上一份报告的日期。

要直接为工作流设置、更新和读取数据，请在代码中使用[静态数据](../../../../build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)函数。可以在工作流全局范围内管理数据，也可以将其关联到特定节点。

{% hint style="info" %}
**尽可能使用 Remove Duplicates**

如果想通过变量避免重复处理相同的数据项，可以考虑使用 [Remove Duplicates 节点](../n8n-nodes-base.removeduplicates/README.md)。它能跨多次执行保存信息，避免重复处理相同数据项。
{% endhint %}

## 无法在 Code 节点中访问凭据 <a href="#cant-access-credentials-in-a-code-node" id="cant-access-credentials-in-a-code-node"></a>

Code 节点在设计上无法访问凭据，也不能访问 n8n 内部的凭据管理系统，以防敏感身份验证数据泄露。

尝试在 Code 节点中通过表达式或 `this.getCredentials()`、`$getCredentials()` 等方法引用凭据，会导致 `this.getCredentials is not a function`、`$getCredentials is not defined` 等错误。

需要发起带身份验证的 API 调用时，请使用支持凭据的 [HTTP Request 节点](../n8n-nodes-base.httprequest/README.md)。

需要动态使用凭据时，请在 Code 节点之外处理凭据选择逻辑：

* 使用 [Switch](../n8n-nodes-base.switch.md) 节点，将流程路由到使用不同凭据的不同节点。
* 直接在凭据字段中使用表达式，根据前序节点的数据动态选择凭据。
* 在 HTTP Request 节点中使用 Custom Auth，通过表达式动态设置请求头、查询参数或请求体的值。
