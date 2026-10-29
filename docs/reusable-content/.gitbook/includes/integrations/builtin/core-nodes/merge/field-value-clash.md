---
title: 字段值冲突
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

同一索引位置的多个数据项具有同名字段时，就会发生冲突。例如，Input 1 和 Input 2 中的所有数据项都具有名为 `language` 的字段，这些字段便会冲突。默认情况下，n8n 优先使用 Input 2，即 Input 2 的 `language` 有值时，合并数据项会使用该值。

可通过 **Options**（选项）> **Clash Handling**（冲突处理）更改此行为：

- **When Field Values Clash**（字段值冲突时）：选择优先使用哪个输入，或选择 **Always Add Input Number to Field Names**（始终在字段名称后添加输入编号），保留全部字段和值，并在字段名称后附加输入编号，标明来源。
- **Merging Nested Fields**（合并嵌套字段）
    - **Deep Merge**（深度合并）：合并数据项各层级的属性，包括嵌套对象。适合处理复杂的嵌套数据结构，需要确保各层嵌套属性都被合并的情况。
    - **Shallow Merge**（浅合并）：仅合并数据项顶层的属性，不合并嵌套对象。适合扁平数据结构，或仅需合并顶层属性、不关注嵌套属性的情况。
