---
title: 通过架构定义结构
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


1. **Generate from JSON Example**（从 JSON 示例生成）：输入示例 JSON 对象，自动生成架构。节点使用对象属性的类型和名称，忽略实际值。根据 JSON 示例生成架构时，n8n 将每个字段都视为必填。
2. **Define using JSON Schema**（使用 JSON Schema 定义）：手动输入 JSON 架构。创建有效 JSON 架构的方法，请参阅 JSON Schema 的[指南和示例](https://json-schema.org/learn/miscellaneous-examples)。请注意，JSON 架构不支持通过 `$ref` 使用引用。
