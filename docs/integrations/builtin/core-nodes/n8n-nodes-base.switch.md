---
title: Switch（多路分支）
description: 工作流自动化平台 n8n 中的 Switch（多路分支） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: critical
nodeTitle: Switch（多路分支）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.switch.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Switch（多路分支） <a href="#switch" id="switch"></a>

使用 Switch 节点，根据比较操作按条件路由工作流。它类似于 [IF](n8n-nodes-base.if.md) 节点，但支持多个输出分支。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

选择节点使用的 **Mode**（模式）：

* **Rules**（规则）：为每个输出构建匹配规则。
* **Expression**（表达式）：编写表达式，以编程方式返回输出索引。

节点配置取决于所选 **Mode**（模式）。

### Rules（规则） <a href="#rules" id="rules"></a>

使用以下参数配置此操作：

* 创建 **Routing Rules**（路由规则）来定义比较条件。
    * 使用数据类型下拉菜单，选择条件的数据类型和比较操作类型。例如，要创建针对某个日期之后的日期的规则，请选择 **Date & Time > is after**（日期和时间 > 晚于）。
    * 条件中需要输入的字段和值，取决于所选的数据类型和比较方式。按数据类型列出的完整比较列表，请参阅[可用的数据类型比较](#available-data-type-comparisons)。
* **Rename Output**（重命名输出）：开启此项，重命名用于存放匹配数据的输出字段，并输入所需的 **Output Name**（输出名称）。

选择 **Add Routing Rule**（添加路由规则）添加更多规则。

#### 规则选项 <a href="#rule-options" id="rule-options"></a>

执行此操作时，可使用以下 **Options**（选项）进一步配置节点：

- **Fallback Output**（后备输出）：选择数据项不匹配任何规则或条件时如何路由工作流。
    - **None**（无）：忽略该数据项，这是默认行为。
    - **Extra Output**（额外输出）：将数据项发送到额外的独立输出。
    - **Output 0**（输出 0）：将数据项发送到与匹配第一条规则的数据项相同的输出。
- **Ignore Case**（忽略大小写）：开启时，判断条件忽略字母大小写；关闭时区分大小写。
- **Less Strict Type Validation**（较宽松的类型验证）：选择是否让 n8n 根据所选操作符尝试转换值类型，开启时尝试，关闭时不尝试。
- **Send data to all matching outputs**（将数据发送到所有匹配输出）：开启时，将数据发送到所有满足条件的输出；关闭时，仅发送到第一个匹配条件的输出。

### Expression（表达式） <a href="#expression" id="expression"></a>

使用以下参数配置此操作：

- **Number of Outputs**（输出数量）：设置节点应有多少个输出。
- **Output Index**（输出索引）：创建表达式，计算每个输入数据项应路由到哪个输出。表达式必须返回数字。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Switch（多路分支） 集成模板](https://n8n.io/integrations/switch)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

使用条件在 n8n 中创建复杂逻辑的更多信息，请参阅[使用条件分支](../../../build/flow-logic/split-with-conditionals.md)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-types.md" %}

