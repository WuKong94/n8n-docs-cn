---
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# 处理数据 <a href="#work-with-data" id="work-with-data"></a>

在 n8n 中，数据沿着工作流从一个节点传递到下一个节点。每个节点接收并处理数据，再将结果传给后续节点。理解数据如何流转和转换，是构建有效工作流的基础。

## n8n 中的数据如何工作 <a href="#how-data-works-in-n8n" id="how-data-works-in-n8n"></a>

**数据流经节点**：连接节点后，数据会自动依次传递。每个节点处理传入数据，并根据配置输出结果。

**查看每个阶段的数据**：可以在工作流任意位置检查数据：

- **节点详情视图**：双击节点，查看输入和输出数据。可以选择 **Schema（结构）**、**Table（表格）** 或 **JSON** 视图。Schema 只显示第一个数据项的简化结构，Table 和 JSON 则显示完整数据集。
- **执行日志**：查看以往工作流运行，了解流经各节点的数据。

**引用之前的数据**：使用[数据映射](reference-data/README.md)引用工作流前面节点的数据。可以：

- 通过界面选择前面节点的值
- 编写[表达式](expressions-versus-data-nodes.md)，动态访问和组合数据
- 按名称引用特定节点，获取其输出

**转换数据**：n8n 提供多种修改数据的方式：

- 使用专用转换节点，例如 Aggregate、Split Out、Sort 等
- 直接在节点参数中编写[表达式](transform-data/expressions-for-data-transformation.md)
- 使用 [Code 节点](expressions-versus-data-nodes.md#code-node)编写自定义 JavaScript 或 Python 逻辑
- 使用 [AI Transform 节点](expressions-versus-data-nodes.md#ai-transform-node)进行 AI 辅助转换

**理解数据结构**：所有节点采用[一致的数据结构](understand-n8ns-data-structure.md)，便于预测数据在工作流中的流转和转换方式。

## 本节内容 <a id="in-this-section"></a>

* [理解 n8n 的数据结构](understand-n8ns-data-structure.md)：n8n 如何组织数据，以及如何在节点之间传递数据。
* [表达式与数据节点](expressions-versus-data-nodes.md)：比较表达式、Code 节点、AI Transform 节点和数据转换节点。
* [引用数据](reference-data/README.md)：引用工作流前面节点的数据。
* [转换数据](transform-data/README.md)：修改、重组或丰富工作流中的数据。
* [过滤不需要的数据](filter-out-unwanted-data.md)：通过界面或在执行过程中筛选数据。
* [固定和模拟数据](pin-and-mock-data.md)：开发期间固定和模拟工作流数据。
* [处理特殊数据类型](handle-special-data-types/README.md)：处理二进制文件、日期时间和嵌套 JSON。
* [数据表](data-tables.md)：在项目范围内存储和管理结构化表格数据。

## 相关资源 <a id="related-resources"></a>

* [构建](../)
* [理解工作流](../understand-workflows/README.md)
* [构建和管理智能体](../build-and-manage-agents/README.md)
* [构建工作流的方式](../ways-of-building-workflows/README.md)
* [管理工作流](../manage-workflows/README.md)
* [流程逻辑](../flow-logic/README.md)
* [在 n8n 中编写代码](../code-in-n8n/README.md)
* [集成 AI](../integrate-ai/README.md)
* [键盘快捷键](../keyboard-shortcuts.md)
