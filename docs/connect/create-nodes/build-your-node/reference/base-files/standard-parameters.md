---
title: 标准参数
description: 列出节点基础文件标准参数的参考文档。
contentType: reference
nodeTitle: 标准参数
originalFilePath: integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-base-files/standard-parameters
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 标准参数 <a href="#standard-parameters" id="standard-parameters"></a>

以下是[节点基础文件](README.md)的标准参数，适用于所有节点类型。

## `displayName` <a href="#displayname" id="displayname"></a>

_字符串_ | _必填_

用户在 n8n 图形界面中看到的名称。

## `name` <a href="#name" id="name"></a>

_字符串_ | _必填_

对象的内部名称，用于在节点的其他位置引用该对象。

## `icon` <a href="#icon" id="icon"></a>

_字符串_ 或 _对象_ | _必填_

指定节点的图标。n8n 建议上传自己的图片文件。

可以用字符串提供图标文件名，也可以用对象分别指定浅色和深色模式的图标。
如果同一个图标适用于浅色和深色模式，请使用以 `file:` 开头的字符串指定图标文件路径。例如：

```
icon: 'file:exampleNodeIcon.svg'
```
要为浅色和深色模式提供不同图标，请使用包含 `light` 和 `dark` 属性的对象。例如：
```
icon: { 
  light: 'file:exampleNodeIcon.svg', 
  dark: 'file:exampleNodeIcon.dark.svg' 
}
```

{% include "../../../../../reusable-content/.gitbook/includes/integrations/creating-nodes/node-icons.md" %}

## `group` <a href="#group" id="group"></a>

_字符串数组_ | _必填_

告诉 n8n 节点在工作流运行时如何行动。可选值：

* `trigger`：节点等待触发。
* `schedule`：节点等待计时结束。
* `input`、`output`、`transform`：目前没有作用。
* 空数组 `[]`：如果不需要 `trigger` 或 `schedule`，请将其用作默认选项。

## `description` <a href="#description" id="description"></a>

_字符串_ | _必填_

节点的简短描述，供 n8n 在图形界面中使用。

## `defaults` <a href="#defaults" id="defaults"></a>

_对象_ | _必填_

包含基本的品牌和名称设置。

此对象可包含：

* `name`：字符串。如果 `displayName` 太长，则将此值用作画布上的节点名称。
* `color`：字符串。自 n8n 1.52.0 起弃用，并在 n8n 3.0 中移除。此字段仅用于为 Font Awesome 图标着色。请改用文件形式的[图标](#icon)。

## `forceInputNodeExecution` <a href="#forceinputnodeexecution" id="forceinputnodeexecution"></a>

_布尔值_ | _可选_

构建多输入节点时，可以选择在该节点运行前，强制执行所有分支上的全部上游节点。默认值为 `false`，即只要求其中一个输入分支运行。

## `inputs` <a href="#inputs" id="inputs"></a>

_字符串数组_ | _必填_

为输入连接器命名，并控制节点输入侧的连接器数量。如果只需要一个连接器，请使用 `inputs: [NodeConnectionTypes.Main]`。


## `outputs` <a href="#outputs" id="outputs"></a>

_字符串数组_ | _必填_

为输出连接器命名，并控制节点输出侧的连接器数量。如果只需要一个连接器，请使用 `outputs: [NodeConnectionTypes.Main]`。

## `requiredInputs` <a href="#requiredinputs" id="requiredinputs"></a>

_整数_ 或 _数组_ | _可选_

用于多输入节点。按编号指定哪些输入必须有数据（对应分支必须运行），节点才能执行。

## `credentials` <a href="#credentials" id="credentials"></a>

_对象数组_ | _必填_

此参数指定 n8n 的凭据选项，每个对象定义一种身份验证类型。

此对象必须包含：


* `name`：凭据名称，必须与凭据文件中的 `name` 属性匹配。例如，`name: 'asanaApi'`（位于 [`Asana.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Asana/Asana.node.ts)）对应 `name = 'asanaApi'`（位于 [`AsanaApi.credential.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/credentials/AsanaApi.credentials.ts)）。
* `required`：布尔值，指定使用此节点是否需要身份验证。


## `requestDefaults` <a href="#requestdefaults" id="requestdefaults"></a>

_对象_ | _必填_

设置节点调用 API 时的基本信息。

此对象必须包含：

* `baseURL`：API 的基础 URL。

还可以添加：

* `headers`：描述 API 调用请求头的对象，例如内容类型。
* `url`：字符串，附加在 `baseURL` 之后。通常可以省略，更常见的做法是在 `operations` 中提供此值。

## `properties` <a href="#properties" id="properties"></a>

_对象数组_ | _必填_

包含定义节点行为的资源对象和操作对象，以及用于配置必填和可选用户输入字段的对象。

### 资源对象 <a href="#resource-objects" id="resource-objects"></a>

资源对象包含以下参数：

* `displayName`：字符串，必须始终为 `Resource`。
* `name`：字符串，必须始终为 `resource`。
* `type`：字符串，告诉 n8n 使用哪种界面元素，以及预期的输入类型。例如，`options` 会添加一个供用户单选的下拉菜单。更多信息请参阅[节点界面元素](../node-ui-elements.md)。
* `noDataExpression`：布尔值，禁止对此参数使用表达式。此值必须始终为 `true`（适用于 `resource`）。

### 操作对象 <a href="#operations-objects" id="operations-objects"></a>

操作对象定义可对资源执行的操作。

> 译注：本节原文将操作字段的显示名称写为 Options、内部名称写为 option，并以 dateTime 举例；同一版本“代码标准”和节点构建教程的操作选择字段示例使用 Operation、operation 和 options。此处保留原文并提示差异，请对照完整节点示例理解，不将这两行作为操作字段命名的唯一依据。

* `displayName`：字符串，必须始终为 `Options`。
* `name`：字符串，必须始终为 `option`。
* `type`：字符串，告诉 n8n 使用哪种界面元素，以及预期的输入类型。例如，`dateTime` 会添加日期选择器。更多信息请参阅[节点界面元素](../node-ui-elements.md)。
* `noDataExpression`：布尔值，禁止对此参数使用表达式。此值必须始终为 `true`（适用于 `operation`）。
* `options`：对象数组。每个对象描述某项操作的行为，例如路由和所用的 REST 动词。`options` 对象包含：
	* `name`：字符串。
	* `value`：字符串。
	* `action`：字符串，将资源和操作组合在一起。应始终包含此参数，因为 n8n 会在后续版本中使用它。例如，资源名为 `"Card"`、操作为 `"Get all"` 时，action 应为 `"Get all cards"`。
	* `description`：字符串。
	* `routing`：包含请求详细信息的对象。

### 附加字段对象 <a href="#additional-fields-objects" id="additional-fields-objects"></a>

这些对象定义可选参数。n8n 会将它们放在图形界面的 **Additional Fields**（附加字段）中，供用户选择需要设置的参数。

这些对象必须包含：

```js
displayName: 'Additional Fields',
name: 'additionalFields',
// The UI element type
type: ''
placeholder: 'Add Field',
default: {},
displayOptions: {
  // Set which resources and operations this field is available for
  show: {
    resource: [
      // Resource names
    ],
    operation: [
      // Operation names
    ]
  },
}
```

界面元素类型的更多信息，请参阅[界面元素](../node-ui-elements.md)。

## 相关资源 <a id="related-resources"></a>

* [基础文件](./)
* [结构](structure.md)
* [声明式参数](declarative-style-parameters.md)
* [编程式参数](programmatic-style-parameters.md)
* [编程式 execute 方法](programmatic-style-execute-method.md)
