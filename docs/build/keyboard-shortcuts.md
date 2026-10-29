---
tags:
- Keyboard
- Move canvas
- Move nodes
- Drag and drop
description: n8n 中可用的键盘快捷键。
hide:
- tags
contentType: reference
nodeTitle: 键盘快捷键
originalFilePath: keyboard-shortcuts.md
originalUrl: https://docs.n8n.io/keyboard-shortcuts
url: https://docs.n8n.io/build/keyboard-shortcuts
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 键盘快捷键与操作 <a href="#keyboard-shortcuts-and-controls" id="keyboard-shortcuts-and-controls"></a>

n8n 为部分操作提供了键盘快捷键。

## 工作流操作 <a href="#workflow-controls" id="workflow-controls"></a>
 
 - **Ctrl/Cmd** + **Alt** + **n**：创建新工作流。
 - **Ctrl/Cmd** + **o**：打开工作流。
 - **Ctrl/Cmd** + **s**：保存当前工作流。
 - **Ctrl/Cmd** + **z**：撤销。
 - **Ctrl/Cmd** + **shift** + **z**：重做。
 - **Ctrl/Cmd** + **Enter**：执行工作流。

## 画布 <a href="#canvas" id="canvas"></a>

### 移动画布 <a href="#move-the-canvas" id="move-the-canvas"></a>

 - **Ctrl/Cmd** + **鼠标左键** + 拖动：移动节点视图。
 - **Ctrl/Cmd** + **鼠标中键** + 拖动：移动节点视图。
 - **Space（空格）** + 拖动：移动节点视图。
 - **鼠标中键** + 拖动：移动节点视图。
 - 在触摸屏上使用双指：移动节点视图。

### 缩放画布 <a href="#canvas-zoom" id="canvas-zoom"></a>

- **+** 或 **=**：放大。
- **-** 或 **_**：缩小。
- **0**：重置缩放级别。
- **1**：缩放至完整显示工作流。
- **Ctrl/Cmd** + **鼠标滚轮**：放大或缩小。

### 画布上的节点 <a href="#nodes-on-the-canvas" id="nodes-on-the-canvas"></a>

- **双击**节点：打开节点详情。
- **Ctrl/Cmd** + **双击**子工作流节点：在新标签页中打开子工作流。
- **Alt** + **g**：展开所有分组。
- **Shift** + **Alt** + **g**：折叠所有分组。
- **Ctrl/Cmd** + **a**：选择所有节点。
- **Ctrl/Cmd** + **v**：粘贴节点。
- **Shift** + **s**：添加便签。

### 在画布上选中一个或多个节点时 <a href="#with-one-or-more-nodes-selected-in-canvas" id="with-one-or-more-nodes-selected-in-canvas"></a>

 - **Alt** + **g**：展开选中的分组，选中组内节点时同样有效。
 - **Shift** + **Alt** + **g**：折叠选中的分组，选中组内节点时同样有效。
 - **ArrowDown（↓）**：选择当前节点下方的同级节点。
 - **ArrowLeft（←）**：选择当前节点左侧的节点。
 - **ArrowRight（→）**：选择当前节点右侧的节点。
 - **ArrowUp（↑）**：选择当前节点上方的同级节点。
 - **Ctrl/Cmd** + **c**：复制。
 - **Ctrl/Cmd** + **g**：将选中节点分组。
 - **Ctrl/Cmd** + **shift** + **g**：取消选中节点的分组。
 - **Ctrl/Cmd** + **x**：剪切。
 - **D**：停用。
 - **Delete**：删除。
 - **Enter**：打开。
 - **F2**：重命名。
 - **P**：固定节点中的数据。更多信息请参阅[数据固定](work-with-data/pin-and-mock-data.md)。
 - **Shift** + **ArrowLeft（←）**：选择当前节点左侧的所有节点。
 - **Shift** + **ArrowRight（→）**：选择当前节点右侧的所有节点。
 - **Space（空格）**：重命名选中的分组。
 - 在子工作流节点上按 **Ctrl/Cmd** + **Shift** + **o**：在新标签页中打开子工作流。

## 节点面板 <a href="#node-panel" id="node-panel"></a>

 - **N**：打开节点面板。
 - **Enter**：将选中节点插入工作流。
 - **Escape**：关闭节点面板。

### 节点面板中的分类 <a href="#node-panel-categories" id="node-panel-categories"></a>

- **Enter**：将节点插入工作流、折叠或展开分类、打开子分类。
- **ArrowRight（→）**：展开分类、打开子分类。
- **ArrowLeft（←）**：折叠分类、关闭子分类视图。

## 节点内部 <a href="#within-nodes" id="within-nodes"></a>

- **=**：在空的参数输入框中，切换到表达式[^1]模式。

## 命令栏 <a href="#command-bar" id="command-bar"></a>

命令栏可以快速执行操作并在 n8n 中导航。按 **Ctrl/Cmd + K**，或点击画布上的放大镜图标打开。可用命令会根据当前视图和权限调整。

* **工作流操作**：添加节点、保存、测试、整理、发布或取消发布、复制、导入或导出、归档、删除。
* **资源导航**：创建和打开工作流、凭据、数据表和项目；访问最近使用的资源。
* **执行操作**：调试、复制、重试、停止或删除执行记录。
* **常规导航**：访问模板、变量、洞察、设置、帮助资源和文档。

## 相关资源 <a id="related-resources"></a>

* [构建](./)
* [理解工作流](understand-workflows/README.md)
* [构建和管理智能体](build-and-manage-agents/README.md)
* [构建工作流的方式](ways-of-building-workflows/README.md)
* [管理工作流](manage-workflows/README.md)
* [流程逻辑](flow-logic/README.md)
* [处理数据](work-with-data/README.md)
* [在 n8n 中编写代码](code-in-n8n/README.md)
* [集成 AI](integrate-ai/README.md)

[^1]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填写节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义参数值，而不必提供静态值。
