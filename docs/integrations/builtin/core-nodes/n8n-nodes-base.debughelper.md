---
title: Debug Helper 节点
description: 了解 n8n 中 Debug Helper 节点的用法，并查看相关示例。
contentType:
- integration
- reference
priority: medium
nodeTitle: Debug Helper 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.debughelper.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.debughelper
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.debughelper
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Debug Helper（调试辅助） <a href="#debug-helper" id="debug-helper"></a>

使用 Debug Helper 节点触发不同类型的错误，或生成随机数据集，帮助测试 n8n 工作流。

## 操作 <a href="#operations" id="operations"></a>

通过选择 **Category**（类别）定义操作：

* **Do Nothing**（不执行操作）：不做任何处理。
* [**Throw Error**](#throw-error)（抛出错误）：抛出指定类型及消息的错误。
* [**Out Of Memory**](#out-of-memory)（内存不足）：生成指定内存量，以模拟内存不足。
* [**Generate Random Data**](#generate-random-data)（生成随机数据）：按选定格式生成随机数据。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

节点参数取决于所选的 **Category**（类别）。**Do Nothing**（不执行操作）类别没有其他参数。

### Throw Error（抛出错误） <a href="#throw-error" id="throw-error"></a>

* **Error Type**（错误类型）：选择要抛出的错误类型，可选：
    * **NodeApiError**
    * **NodeOperationError**
    * **Error**
* **Error Message**（错误消息）：输入要抛出的错误消息。

### Out Of Memory（内存不足） <a href="#out-of-memory" id="out-of-memory"></a>

Out Of Memory 类别增加一个 **Memory Size to Generate**（生成的内存量）参数，输入大致要生成的内存量。

### Generate Random Data（生成随机数据） <a href="#generate-random-data" id="generate-random-data"></a>

* **Data Type**（数据类型）：选择要生成的随机数据类型，可选：
    * **Address**（地址）
    * **Coordinates**（坐标）
    * **Credit Card**（信用卡）
    * **Email**（电子邮箱）
    * **IPv4**
    * **IPv6**
    * **MAC**
    * **Nanoids**：选择此类型后，还需输入：
        * **Nanoid Alphabet**（Nanoid 字符集）：生成器创建 nanoid 时使用的字符集。
        * **Nanoid Length**（Nanoid 长度）：每个 nanoid 的长度。
    * **URL**
    * **User Data**（用户数据）
    * **UUID**
    * **Version**（版本）
* **Seed**（种子）：如需使用特定种子生成数据，在此输入，以确保生成结果可重复。希望随机生成时，留空此字段。
* **Number of Items to Generate**（生成数据项数量）：输入要生成的随机数据项数量。
* **Output as Single Array**（输出为单个数组）：开启时生成单个数组，关闭时生成多个数据项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Debug Helper 集成模板](https://n8n.io/integrations/debughelper)，或[搜索所有模板](https://n8n.io/workflows/)
