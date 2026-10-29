---
title: Code 节点
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


使用 Code 节点编写自定义 JavaScript 或 Python，并将其作为工作流中的一个步骤运行。

{% hint style="info" %}
**在 n8n 中编写代码**

本页介绍 Code 节点的使用方法。更多编程指导请参阅[代码](../../../../../../build/code-in-n8n/README.md)章节，其中包括：

* [内置方法和变量](../../../../../../build/code-in-n8n/use-built-in-shortcuts.md)参考文档
* [日期处理](../../../../../../build/work-with-data/handle-special-data-types/work-with-dates-and-times.md)和 [JSON 查询](../../../../../../build/work-with-data/handle-special-data-types/query-json-data.md)指南
* [实用示例](../../../../../../build/code-in-n8n/cookbook/code-node/README.md)中不断增加的示例集合
{% endhint %}

{% hint style="info" %}
**示例和模板**

入门示例和模板，请参阅 n8n 的 [Code 集成](https://n8n.io/integrations/code/)页面。
{% endhint %}

{% hint style="info" %}
**Function 和 Function Item 节点**

从 n8n 0.198.0 起，Code 节点替代 Function 和 Function Item 节点。使用更早版本时，仍可查看 [Function 节点文档](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.function.md)和 [Function Item 节点文档](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.functionItem.md)。
{% endhint %}

## 使用方式 <a href="#usage" id="usage"></a>

如何使用 Code 节点。

### 选择模式 <a href="#choose-a-mode" id="choose-a-mode"></a>

有两种模式：

* **Run Once for All Items（为所有数据项运行一次）**：默认模式。工作流运行时，无论输入多少个数据项，Code 节点中的代码都只执行一次。
* **Run Once for Each Item（为每个数据项运行一次）**：希望代码针对每个输入数据项分别运行时，选择此模式。

## JavaScript <a href="#javascript" id="javascript"></a>

Code 节点支持 Node.js。

### 支持的 JavaScript 功能 <a href="#supported-javascript-features" id="supported-javascript-features"></a>

Code 节点支持：

* Promise。可以返回会解析为相应结果的 Promise，而不是直接返回数据项。
* 使用 `console.log` 向浏览器控制台写入信息，便于调试和排查工作流。

### 外部库 <a href="#external-libraries" id="external-libraries"></a>

自托管 n8n 时，可以在 Code 节点中导入并使用内置和外部 npm 模块。启用外部模块的方法，请参阅[在 Code 节点中启用模块](../../../../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node.md)。

使用 n8n Cloud 时，不能导入外部 npm 模块。n8n 提供两个可用模块：

* [crypto Node.js 模块](https://nodejs.org/docs/latest-v18.x/api/crypto.html)
* [moment npm 包](https://www.npmjs.com/package/moment)

### 内置方法和变量 <a href="#built-in-methods-and-variables" id="built-in-methods-and-variables"></a>

n8n 提供内置方法和变量，用于处理数据和访问 n8n 数据。更多信息请参阅[内置方法和变量](../../../../../../build/code-in-n8n/use-built-in-shortcuts.md)。

使用内置方法和变量的语法是 `$variableName` 或 `$methodName()`。在 Code 节点或表达式编辑器中输入 `$`，即可查看建议方法和变量列表。

### 键盘快捷键 <a href="#keyboard-shortcuts" id="keyboard-shortcuts"></a>

Code 节点编辑环境提供多种实用快捷键，可用于自动补全、代码折叠、多光标等操作。完整列表见[键盘快捷键](../../../../../../integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md)。

## Python（Pyodide，旧版） <a href="#python-pyodide-legacy" id="python-pyodide-legacy"></a>

{% hint style="warning" %}
**功能可用范围**

Pyodide 已从 n8n 2.0 中移除，n8n 不再支持此功能。
{% endhint %}

n8n 在 1.0 中加入 Python 支持，但不包含 Python 可执行程序，而是通过 [Pyodide](https://pyodide.org/en/stable/)（CPython 的 WebAssembly 移植版）提供支持。因此，可用包仅限 [Pyodide 包含的包](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide)。首次使用时，n8n 会自动下载对应包。

{% hint style="info" %}
**比 JavaScript 慢**

由于需要额外编译步骤，Code 节点处理 Python 比处理 JavaScript 耗时更长。
{% endhint %}

### 内置方法和变量 <a href="#built-in-methods-and-variables" id="built-in-methods-and-variables"></a>

n8n 提供内置方法和变量，用于处理数据和访问 n8n 数据。更多信息请参阅[内置方法和变量](../../../../../../build/code-in-n8n/use-built-in-shortcuts.md)。

使用内置方法和变量的语法是 `_variableName` 或 `_methodName()`。在 Code 节点中输入 `_`，即可查看建议方法和变量列表。

### 键盘快捷键 <a href="#keyboard-shortcuts" id="keyboard-shortcuts"></a>

Code 节点编辑环境提供多种实用快捷键，可用于自动补全、代码折叠、多光标等操作。完整列表见[键盘快捷键](../../../../../../integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md)。

## 文件系统与 HTTP 请求 <a href="#file-system-and-http-requests" id="file-system-and-http-requests"></a>

不能访问文件系统或发出 HTTP 请求，请改用以下节点：

* [Read/Write File From Disk（读写磁盘文件）](../../../../../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)
* [HTTP Request](../../../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md)

## Python（原生） <a href="#python-native" id="python-native"></a>

{% hint style="info" %}
**功能可用范围**

使用任务运行器的原生 Python 支持从 n8n 1.111.0 起可用，在 n8n 2 中已稳定。
{% endhint %}

与 Pyodide 的主要区别：

* 原生 Python 在处理所有数据项的模式下仅支持 `_items`，逐项模式下仅支持 `_item`，不支持其他 n8n 内置方法和变量。
* 自托管环境中，如果 `n8nio/runners` 镜像包含相应模块，且已显式加入允许列表，原生 Python 可以导入标准库和第三方原生模块。详情请参阅[为任务运行器添加额外依赖](../../../../../../deploy/host-n8n/configure-n8n/set-up-task-runners.md#adding-extra-dependencies)。
* 原生 Python 默认禁止不安全的内置功能。详情请参阅[任务运行器环境变量](../../../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md)。
* Pyodide 接受点访问语法，例如 `item.json.myNewField`；原生 Python 则只接受方括号访问语法，例如 `item["json"]["my_new_field"]`。还可能有其他细微差异：Pyodide 接受的某些写法，在原生 Python 中并不合法。
* 在 n8n Cloud 上，Code 节点的 Python 选项不允许导入任何 Python 库，包括标准库和第三方包。自托管环境如何包含外部库，请参阅[为任务运行器添加额外依赖](../../../../../../deploy/host-n8n/configure-n8n/set-up-task-runners.md#adding-extra-dependencies)。长期而言，n8n 团队致力于通过任务运行器，让用户安全执行使用任意标准库和第三方库的 Python 代码。

升级为原生 Python 属于破坏性变更，可能需要调整脚本，才能使用原生 Python 运行器。

## 在 n8n 中编写代码 <a href="#coding-in-n8n" id="coding-in-n8n"></a>

n8n 中有两处可以使用代码：Code 节点和表达式编辑器。使用任一方式时，都需要了解一些关键概念；也有内置方法和变量可以辅助完成常见任务。

### 关键概念 <a href="#key-concepts" id="key-concepts"></a>

使用 Code 节点时，需要了解以下概念：

* [数据结构](../../../../../../build/work-with-data/understand-n8ns-data-structure.md)：了解 Code 节点收到的数据，以及输出数据必须满足的要求。
* [数据项关联](../../../../../../build/work-with-data/reference-data/link-data-items/README.md)：了解数据项如何工作，以及如何关联到前面节点的数据项。输入和输出数据项数量不同时，需要在代码中处理数据项关联。

### 内置方法和变量 <a href="#built-in-methods-and-variables" id="built-in-methods-and-variables"></a>

n8n 内置方法和变量可以帮助你：

* 访问特定数据项的数据
* 访问工作流、执行和 n8n 环境的信息
* 使用辅助变量处理数据和时间

更多信息请参阅[内置方法和变量](../../../../../../build/code-in-n8n/use-built-in-shortcuts.md)。

## 在 Code 节点中使用 AI <a href="#use-ai-in-the-code-node" id="use-ai-in-the-code-node"></a>
