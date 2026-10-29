---
title: Edit Fields (Set)（编辑字段）
contentType:
- integration
- reference
priority: critical
nodeTitle: Edit Fields (Set)（编辑字段）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.set.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set
description: 工作流自动化平台 n8n 中的 Edit Fields (Set)（编辑字段） 节点文档，包括使用说明和示例链接。
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


# Edit Fields (Set)（编辑字段） <a id="edit-fields-set"></a>

使用 Edit Fields 节点设置工作流数据，可设置新数据，也可覆盖已有数据。对于需要接收上游节点数据的工作流，例如向 Google Sheets 或数据库插入值，此节点十分关键。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

以下是 Edit Fields 节点可用的设置和选项。

### Mode（模式） <a href="#mode" id="mode"></a>

可使用 **Manual Mapping**（手动映射）在图形界面中编辑字段，或使用 **JSON Output**（JSON 输出）编写要添加到输入数据中的 JSON。

### Fields to Set（要设置的字段） <a href="#fields-to-set" id="fields-to-set"></a>

选择 **Mode**（模式）> **Manual Mapping**（手动映射）后，可从 **INPUT**（输入）拖放值来配置字段。

拖入值时的默认行为：

* n8n 将该值的名称设为字段名称。
* 字段值包含一个用于访问该值的表达式。

如果不想使用表达式：

1. 将鼠标悬停在字段上，n8n 会显示 **Fixed | Expressions**（固定值 | 表达式）切换控件。
2. 选择 **Fixed**（固定值）。

字段名称和值都可这样设置。

![将字段从 INPUT 拖到 Fields to Set，再将其 Value 从 Expression 切换为 Fixed](<../../.gitbook/assets/drag-drop-fixed-toggle (1).gif>)

### Keep Only Set Fields（仅保留设置的字段） <a href="#keep-only-set-fields" id="keep-only-set-fields"></a>

启用后，丢弃未在 **Fields to Set**（要设置的字段）中使用的所有输入数据。

### Include in Output（包含在输出中） <a href="#include-in-output" id="include-in-output"></a>

选择节点输出中应包含哪些输入数据。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项自定义节点行为。

### Include Binary Data（包含二进制数据） <a href="#include-binary-data" id="include-binary-data"></a>

如果输入数据包含二进制数据，选择是否在 Edit Fields 节点的输出中包含它们。

### Ignore Type Conversion Errors（忽略类型转换错误） <a href="#ignore-type-conversion-errors" id="ignore-type-conversion-errors"></a>

仅适用于 Manual Mapping（手动映射）。

启用后，n8n 在映射字段时会忽略部分数据类型错误。

### Support Dot Notation（支持点表示法） <a href="#support-dot-notation" id="support-dot-notation"></a>

默认情况下，n8n 支持点表示法。

例如，使用手动映射时，节点会按点表示法解析 **Name**（名称）字段。如果将 **Name** 字段设为 `number.one`，**Value**（值）字段设为 `20`，生成的 JSON 为：

```json
{ "number": { "one": 20} }
```

可选择 **Add Option**（添加选项）> **Support Dot Notation**（支持点表示法），将 **Dot Notion** 字段关闭，以禁用此行为。此时生成的 JSON 为：

```json
{ "number.one": 20 }
```

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Edit Fields (Set)（编辑字段） 集成模板](https://n8n.io/integrations/set)，或[搜索所有模板](https://n8n.io/workflows/)

## JSON Output 模式中的数组和表达式 <a href="#arrays-and-expressions-in-json-output-mode" id="arrays-and-expressions-in-json-output-mode"></a>

创建 JSON Output（JSON 输出）时，可使用数组和表达式。

例如，给定 Customer Datastore 节点生成的以下输入数据：

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10"
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05"
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09"
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12"
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16"
  }
]
```

在 **JSON Output**（JSON 输出）字段中添加以下 JSON，并将 **Include in Output**（包含在输出中）设为 **All Input Fields**（所有输入字段）：

```json
{
  "newKey": "new value",
  "array": [{{ $json.id }},"{{ $json.name }}"],
  "object": {
    "innerKey1": "new value",
    "innerKey2": "{{ $json.id }}",
    "innerKey3": "{{ $json.name }}",
 }
}
```

将得到以下输出：

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10",
    "newKey": "new value",
    "array": [
      23423532,
      "Jay Gatsby"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423532",
      "innerKey3": "Jay Gatsby"
    }
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05",
    "newKey": "new value",
    "array": [
      23423533,
      "José Arcadio Buendía"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423533",
      "innerKey3": "José Arcadio Buendía"
    }
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09",
    "newKey": "new value",
    "array": [
      23423534,
      "Max Sendak"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423534",
      "innerKey3": "Max Sendak"
    }
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12",
    "newKey": "new value",
    "array": [
      23423535,
      "Zaphod Beeblebrox"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423535",
      "innerKey3": "Zaphod Beeblebrox"
    }
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16",
    "newKey": "new value",
    "array": [
      23423536,
      "Edmund Pevensie"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423536",
      "innerKey3": "Edmund Pevensie"
    }
  }
]
```
