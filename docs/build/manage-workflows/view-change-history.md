---
title: 工作流历史
contentType: howto
nodeTitle: 查看更改历史
originalFilePath: workflows/history.md
originalUrl: https://docs.n8n.io/workflows/history
url: https://docs.n8n.io/build/manage-workflows/view-change-history
description: 查看和恢复工作流的旧版本。
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


# 查看更改历史 <a id="view-change-history"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐提供完整的工作流历史：

- **n8n Cloud：** Enterprise
- **自托管：** Enterprise
{% endhint %}

所有用户都可以访问最近 24 小时内的版本。n8n Cloud Pro 可以访问最近五天内的版本。

使用工作流历史，可以查看和恢复工作流的旧版本。

## 理解工作流历史 <a href="#understand-workflow-history" id="understand-workflow-history"></a>

以下操作会让 n8n 创建新版本：

* 保存工作流。
* 恢复旧版本。恢复前，n8n 会先保存最新版本。
* 使用[源代码管理](../../administer/use-source-control-and-environments/README.md)从 Git 仓库拉取。注意，n8n 将版本保存在实例数据库中，而不是 Git 中。

更改工作流设置不会创建新版本。

{% hint style="info" %}
**工作流历史与执行历史**

不要将工作流历史与[工作流级别的执行列表](../understand-workflows/understand-executions/view-executions-for-a-single-workflow.md)混淆。

执行是指工作流的运行。通过执行列表，可以查看当前版本工作流之前的运行记录。可以将以往执行复制到编辑器，在当前工作流中[调试并重新运行](../understand-workflows/understand-executions/debug-executions.md)。

工作流历史保存的是工作流的旧版本，例如使用不同节点或不同参数设置的版本。
{% endhint %}

## 查看工作流历史 <a href="#view-workflow-history" id="view-workflow-history"></a>

查看工作流历史的步骤如下：

1. 打开工作流。
2. 选择 **Workflow history（工作流历史）** <img src="../.gitbook/assets/workflow-history.png" alt="工作流历史图标" data-size="line">。n8n 会打开显示已保存版本的菜单，并在画布中预览所选版本。

## 恢复或复制旧版本 <a href="#restore-or-copy-previous-versions" id="restore-or-copy-previous-versions"></a>

可以恢复工作流的旧版本，也可以创建其副本：

1. 在要恢复或复制的版本上，选择 **Options（选项）** <img src="../.gitbook/assets/three-dot-options-menu (1).png" alt="选项图标" data-size="line">。
2. 选择所需操作：
   * **Restore version（恢复版本）**：用所选版本替换当前工作流。
   * **Clone to new workflow（克隆为新工作流）**：基于所选版本创建新工作流。
   * **Open version in new tab（在新标签页中打开版本）**：在另一个标签页中显示所选版本，便于比较。
   * **Download（下载）**：将该版本下载为 JSON。
   * **Name version（为版本命名）**：为版本设置名称和说明。n8n 不会自动清理命名版本。详情请参阅[为版本命名](../understand-workflows/save-and-publish-workflows.md#naming-versions)。n8n Cloud Pro 和 Enterprise，以及自托管 Business 和 Enterprise 支持命名版本。

## 相关资源 <a id="related-resources"></a>

* [管理工作流](./)
* [配置工作流设置](configure-workflow-settings.md)
* [为工作流添加标签](tag-workflows.md)
* [收藏项目](favorite-items.md)
* [审核工作流](workflow-reviews.md)
* [导出和导入](export-and-import.md)
* [n8n 软件包](n8n-packages/README.md)
* [与他人共享](share-with-others.md)
