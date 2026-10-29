---
title: 使用工作流差异视图比较更改
description: 使用工作流差异视图比较本地与远程更改。
contentType: howto
nodeTitle: 比较版本
originalFilePath: source-control-environments/using/compare-changes.md
originalUrl: https://docs.n8n.io/source-control-environments/using/compare-changes
url: https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用工作流差异视图比较更改 <a href="#compare-changes-with-workflow-diffs" id="compare-changes-with-workflow-diffs"></a>

工作流差异视图可直观比较实例中的工作流，与所连接 Git 仓库中最近保存的版本之间的更改，帮助你在决定跨环境推送或拉取前，了解具体变化。

{% hint style="info" %}
**功能可用范围**

工作流差异视图可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**Business、Enterprise。

仅当实例[启用环境功能](set-up-source-control.md)后，才可使用工作流差异视图。
{% endhint %}

## 打开工作流差异视图 <a href="#accessing-workflow-diffs" id="accessing-workflow-diffs"></a>

可以从两个位置打开工作流差异视图：

1. **推送更改时**：在提交弹窗中，点击待审核工作流旁的差异图标。
2. **拉取更改时**：在修改内容弹窗中，点击待审核工作流旁的差异图标。

## 理解工作流差异视图 <a href="#understanding-the-workflow-diff-view" id="understanding-the-workflow-diff-view"></a>

打开工作流差异视图后，n8n 会上下显示两个工作流：

### 推送时 <a href="#when-pushing" id="when-pushing"></a>

* **上方面板**（远程分支）：Git 仓库中的最新版本。
* **下方面板**（本地）：当前在本地保存的工作流版本。

### 拉取时 <a href="#when-pulling" id="when-pulling"></a>

* **上方面板**（本地）：n8n 实例中的当前版本。
* **下方面板**（远程分支）：要从 Git 仓库拉取的版本。

在这两种情况下，上方面板始终显示将被更改更新的工作流。

差异视图会突出显示三类更改：

* **新增节点和连接线**：新增节点或连接线以绿色显示，并带有“N”图标。
* **修改节点和连接线**：对现有节点或连接线的修改以橙色显示，并带有“M”图标。
* **删除节点和连接线**：删除的节点或连接线以红色显示，并带有“D”图标。

## 审核节点更改 <a href="#reviewing-node-changes" id="reviewing-node-changes"></a>

对于已修改的节点，还可以比较具体更改。点击节点即可显示 JSON 差异，查看其更改前后的准确配置。

## 查看更改汇总 <a href="#viewing-the-summary-of-changes" id="viewing-the-summary-of-changes"></a>

右上角的 **changes**（更改）按钮显示更改数量，即节点、节点连接线及工作流常规设置更新的总数。

## 逐项浏览更改 <a href="#navigating-through-each-change" id="navigating-through-each-change"></a>

使用右上角的**下一项**和**上一项**箭头，按逻辑顺序浏览更改。使用左上角的**返回**按钮，回到提交或拉取弹窗，选择其他工作流审核。

## 哪些用户可以使用工作流差异视图 <a href="#who-can-use-workflow-diffs" id="who-can-use-workflow-diffs"></a>

只有能为实例推送或拉取提交的用户，才能访问工作流差异视图：

* 实例所有者。
* 实例管理员。
* 项目管理员。

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)
