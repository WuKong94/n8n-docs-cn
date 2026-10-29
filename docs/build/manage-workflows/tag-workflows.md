---
title: 工作流标签
description: 使用标签标记工作流，便于浏览。
contentType: howto
nodeTitle: 为工作流添加标签
originalFilePath: workflows/tags.md
originalUrl: https://docs.n8n.io/workflows/tags
url: https://docs.n8n.io/build/manage-workflows/tag-workflows
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 标签 <a href="#tags" id="tags"></a>

工作流标签可以为工作流添加标记，之后即可按标签筛选。

标签是全局的。创建标签后，n8n 实例上的所有用户都可以使用。

## 为工作流添加标签 <a href="#add-a-tag-to-a-workflow" id="add-a-tag-to-a-workflow"></a>

为工作流添加标签的步骤如下：

1. 在工作流中选择 **+ Add tag（添加标签）**。
2. 选择已有标签，或输入新标签名称。
3. 选中标签并点击标签弹窗外部后，n8n 会在工作流名称旁显示该标签。

可以添加多个标签。

## 按标签筛选 <a href="#filter-by-tag" id="filter-by-tag"></a>

浏览实例中的工作流时，可以按标签筛选。

1. 在 **Workflows（工作流）** 页面中，选择 **Filters（筛选）**。
2. 选择 **Tags（标签）**。
3. 选择用于筛选的一个或多个标签。n8n 会列出带有对应标签的工作流。

## 管理标签 <a href="#manage-tags" id="manage-tags"></a>

可以编辑已有标签。实例所有者可以删除标签。

1. 选择 **Manage tags（管理标签）**。可以从 **Workflows（工作流）** 页面的 **Filters（筛选）** > **Tags（标签）** 进入，也可以从工作流中的 **+ Add tag（添加标签）** 弹窗进入。
2. 将鼠标悬停在要修改的标签上。
3. 选择 **Edit（编辑）** <img src="../.gitbook/assets/edit.png" alt="操作图标" data-size="line"> 来重命名，或选择 **Delete（删除）** <img src="../.gitbook/assets/delete.png" alt="操作图标" data-size="line"> 来删除。

{% hint style="warning" %}
**全局标签**

标签是全局的。编辑或删除标签会影响 n8n 实例上的所有用户。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [管理工作流](./)
* [配置工作流设置](configure-workflow-settings.md)
* [收藏项目](favorite-items.md)：固定工作流、文件夹、项目和数据表，方便快速访问。
* [查看更改历史](view-change-history.md)
* [审核工作流](workflow-reviews.md)
* [导出和导入](export-and-import.md)
* [n8n 软件包](n8n-packages/README.md)
* [与他人共享](share-with-others.md)
