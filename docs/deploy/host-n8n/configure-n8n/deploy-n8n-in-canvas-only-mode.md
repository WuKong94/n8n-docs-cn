---
title: 以仅画布模式部署 n8n
description: 了解 N8N_CANVAS_ONLY 环境变量如何隐藏 n8n 导航和工作流设置，仅显示工作流画布。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 以仅画布模式部署 n8n <a id="deploy-n8n-in-canvas-only-mode"></a>

在仅画布模式下，打开工作流时只会看到该工作流的画布。命令栏等可能引导用户离开画布的元素会隐藏。


{% hint style="info" %}
**功能可用范围**

自 n8n 2.15.0 起提供仅画布模式。
{% endhint %}

## 开启仅画布模式 <a id="turn-on-canvas-only-mode"></a>

将 `N8N_CANVAS_ONLY` 设为 `true`：

```bash
export N8N_CANVAS_ONLY=true
```

仅画布模式作用于整个实例，不能只对特定工作流或用户启用。

## 仅画布模式中的变化 <a id="what-changes-in-canvas-only-mode"></a>

在工作流详情路由中，仅画布模式会隐藏：

- **画布顶部区域**：不再显示工作流名称、面包屑导航、保存控件和标签。
- **左侧菜单**：不再显示 n8n 主导航。
- **浮层元素**：不再显示命令栏和“Ask AI assistant”按钮。
- **键盘快捷键**：仅画布模式会禁用以下快捷键：**Ctrl/Cmd** + **s**（保存）、**Ctrl/Cmd** + **Alt** + **n**（创建新工作流）、**Ctrl/Cmd** + **p**（发布）、**Ctrl/Cmd** + **u**（取消发布）、**Ctrl/Cmd** + **k**（命令栏）。

n8n 会保留以下元素：

- **工作流画布及其节点**：仍可平移、缩放和编辑工作流。
- **标签栏**：用于在编辑器、执行记录和评估之间切换，浮动在屏幕顶部附近，不再位于顶部区域内部。
- **日志面板**：显示各个节点的执行日志。
- **节点创建面板**：“Add a node（添加节点）”面板仍可从画布打开，但会移至屏幕顶部，而非顶部区域下方。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
