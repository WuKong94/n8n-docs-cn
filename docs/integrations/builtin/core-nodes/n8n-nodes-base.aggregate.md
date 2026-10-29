---
title: Aggregate（聚合）
description: 工作流自动化平台 n8n 中的 Aggregate（聚合） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Aggregate（聚合）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Aggregate（聚合） <a href="#aggregate" id="aggregate"></a>

使用 Aggregate 节点，将分散的数据项或其部分内容分组，聚合成单个数据项。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

首先选择要使用的 **Aggregate**（聚合）方式：

* [**Individual Fields（单独字段）**](#individual-fields)：分别聚合各个字段。
* [**All Item Data（所有数据项数据）**](#all-item-data)：将所有数据项的数据聚合成一个列表。

### Individual Fields（单独字段） <a href="#individual-fields" id="individual-fields"></a>

* **Input Field Name**（输入字段名称）：输入要聚合的输入数据字段名称。
* **Rename Field**（重命名字段）：此开关控制是否为聚合后的输出字段设置不同名称。开启后可指定不同的字段名称。聚合多个字段时，必须提供新的输出字段名称，不能将多个字段都留为未定义。
    * **Output Field Name**（输出字段名称）：开启 **Rename Field**（重命名字段）后显示，用于输入聚合输出数据的字段名称。

更多配置选项请参阅[节点选项](#node-options)。

### All Item Data（所有数据项数据） <a href="#all-item-data" id="all-item-data"></a>

* **Put Output in Field**（输出存入字段）：输入用于输出数据的字段名称。
* **Include**（包含）：选择输出中包含哪些字段，可选：
    * **All fields**（全部字段）：输出包含所有字段的数据，无需其他参数。
    * **Specified Fields**（指定字段）：选择后，在 **Fields To Include**（要包含的字段）参数中输入以逗号分隔的字段列表，输出仅包含列表中的字段。
    * **All Fields Except**（排除指定字段）：选择后，在 **Fields To Exclude**（要排除的字段）参数中输入以逗号分隔的字段列表，输出包含所有不在该列表中的字段。

更多配置选项请参阅[节点选项](#node-options)。

## 节点选项 <a href="#node-options" id="node-options"></a>

可使用以下 **Options**（选项）进一步配置节点：

* **Disable Dot Notation**（禁用点表示法）：**Aggregate**（聚合）方式为 **Individual Fields**（单独字段）时显示。开启后，不允许在字段名称中使用 `parent.child` 引用子字段；关闭时允许，默认为关闭。
* **Merge Lists**（合并列表）：**Aggregate**（聚合）方式为 **Individual Fields**（单独字段）时显示。如果要聚合的字段是列表，并希望输出单个扁平列表而不是列表的列表，请开启此项。
* **Include Binaries**（包含二进制数据）：两种聚合方式均显示此项。要在新输出中包含输入的二进制数据，请开启。
* **Keep Missing And Null Values**（保留缺失值和空值）：**Aggregate**（聚合）方式为 **Individual Fields**（单独字段）时显示。开启后，输入值为 null 或缺失时，会在输出列表中添加一个 null（空）条目；关闭时，输出会忽略 null 或空值。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Aggregate（聚合） 集成模板](https://n8n.io/integrations/aggregate)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
