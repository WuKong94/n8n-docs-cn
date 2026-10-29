---
description: 收藏工作流、文件夹、项目和数据表，将其固定到左侧菜单以便快速访问。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 收藏项目 <a id="favorite-items"></a>

{% hint style="info" %}
**从 n8n 2.18.0 起可用**
{% endhint %}

可以收藏工作流、文件夹、项目和数据表，将它们固定起来以便快速访问。收藏后，该项会出现在左侧菜单的 **Favorites（收藏）** 部分，无需再搜索或浏览常用内容。

收藏属于每个用户的个人设置。收藏某项不会改变其查看或编辑权限，也不会影响其他用户的收藏。

## 收藏项目 <a id="favorite-an-item"></a>

要收藏某项，选择其**三点菜单**，再选择 **Favorite（收藏）**。要取消收藏，在同一**三点菜单**中选择 **Unfavorite（取消收藏）**。

各类内容的**三点菜单**位于以下位置：

* **工作流**：在 **Workflows（工作流）** 列表的工作流旁，或打开工作流后的顶部栏中。
* **文件夹**：在 **Workflows（工作流）** 列表的文件夹旁。
* **数据表**：在 **Data tables（数据表）** 列表的数据表旁。
* **项目**：在 **Workflows（工作流）** 列表的项目旁。团队项目的顶部栏还提供星标图标，也可以点击它来收藏。

{% hint style="info" %}
**星标图标仅在团队项目中显示**

只有打开团队项目时，项目顶部栏才显示星标图标。要收藏个人项目，请使用其**三点菜单**。
{% endhint %}

## 查看收藏 <a id="view-your-favorites"></a>

n8n 在左侧菜单的 **Favorites（收藏）** 部分列出收藏内容，按类型依次分为项目、文件夹、工作流和数据表。选择某项即可打开；选择旁边的 **x** 可以直接取消收藏，无需打开。

{% hint style="info" %}
**入口限制**

至少收藏一项后，左侧菜单才会显示 **Favorites（收藏）** 部分。目前没有独立的收藏页面，也无法在收藏列表中搜索、排序或筛选。
{% endhint %}

## 限制 <a id="limits"></a>

最多可以收藏 200 项。达到上限后，需要先移除已有收藏，才能添加新收藏。

对应内容被删除后，n8n 会自动移除收藏。如果失去某项收藏内容的访问权限，例如有人将你移出所属项目，该项会暂时从收藏列表中消失，直到你重新获得权限。

## 相关资源 <a id="related-resources"></a>

* [管理工作流](./)
* [配置工作流设置](configure-workflow-settings.md)
* [为工作流添加标签](tag-workflows.md)
* [查看更改历史](view-change-history.md)
* [审核工作流](workflow-reviews.md)
* [导出和导入](export-and-import.md)
* [n8n 软件包](n8n-packages/README.md)
* [与他人共享](share-with-others.md)
* [数据表](../work-with-data/data-tables.md)
* [在项目中组织工作](../../administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)
