---
description: 将项目或整个 n8n 实例中的变更晋级到该实例配置的目标环境。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 晋级变更 <a id="promote-changes"></a>

晋级操作将工作流及其依赖资源从当前实例发送到晋级目标环境。你可以晋级某个项目中选定的工作流，也可以晋级实例上的所有项目。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

开始前，添加此实例要晋级变更到的环境。请参阅[规划环境](plan-your-environments.md)。

## 项目级晋级 <a id="project-promote"></a>

项目级晋级发送一个团队项目中选定的变更。

1. 打开一个团队项目。项目名称旁带向上箭头的徽标会显示待晋级变更的数量。
2. 选择该徽标，打开 **Changes to promote（待晋级变更）**页面。
3. 选择要晋级的工作流。n8n 会包含凭据、变量、数据表和标签等依赖资源。
4. 检查变更。每项资源会显示发生的变化，例如 **New（新增）**、**Modified（修改）**、**Renamed（重命名）**、**Moved（移动）**、**Archived（归档）**或 **Deleted（删除）**。要以可视化方式比较工作流，请选择 **Show diff（显示差异）**。差异查看器显示画布的 **Before（变更前）**与 **After（变更后）**，其中 Before 是环境分支，After 是当前实例。
5. 选择 **Promote N changes（晋级 N 项变更）**。
6. 可选：输入 **Commit message（提交说明）**。如果留空，n8n 会自动生成。
7. 选择 **Promote（晋级）**。

如果在页面打开期间编辑了工作流，请在晋级前选择 **Refresh（刷新）**，以显示最新变更。

其他项目中的子工作流只会被引用，不会包含在晋级内容中，因此必须已存在于目标实例上。请参阅[跨项目依赖](known-limitations.md#cross-project-dependencies)。

n8n 绝不会将凭据密钥、数据表行或执行记录写入仓库。凭据以 ID、名称、类型及使用表达式的字段形式传递。变量会携带其值。变量只有名称和值，因此不像凭据那样具有可由 n8n 省略的密钥部分。请将密钥保存在凭据中，而不是变量中。

晋级标记为 **Deleted（删除）**的工作流会将其从分支中移除，应用操作会在目标实例上将其删除。已归档的工作流保持归档状态。

## 实例级晋级 <a id="instance-promote"></a>

实例级晋级发送所有团队项目，并覆盖分支上的项目内容，使其与当前实例一致。不包含个人项目。

1. 前往 **Settings**（设置）> **Environments**（环境）。
2. 在 **Promote changes to（晋级变更目标）**下的环境中，选择 **Promote（晋级）**。
3. 可选：输入 **Commit message（提交说明）**。如果留空，n8n 会自动生成。
4. 选择 **Promote（晋级）**。

## 变更的去向 <a id="where-the-changes-go"></a>

环境设置决定 n8n 如何处理变更：

- **直接提交：**n8n 提交到环境分支。
- **功能分支：**n8n 以环境分支为基础，推送名为 `n8n-promotion/<timestamp>` 的功能分支，再由其他人在 Git 托管服务上合并。
- **带晋级审核的功能分支：**n8n 还会创建晋级审核。使用 GitLab 时，审核对应一个合并请求。请参阅[晋级审核](promotion-reviews.md)。

n8n 将提交作者设为你的 n8n 名称和邮箱。Git 托管服务则将推送和合并请求记录在提供方的账号或令牌名下。

## 哪些问题会阻止晋级 <a id="what-blocks-a-promote"></a>

### 工作流或文件夹已移至其他项目 <a id="workflows-or-folders-moved-to-another-project"></a>

项目级晋级无法跨项目移动工作流或文件夹。n8n 会指出该内容及两个项目的名称。请改用实例级晋级。支持项目内移动，但不支持移入个人项目。请参阅[在项目之间移动工作流和文件夹](known-limitations.md#moving-workflows-and-folders-between-projects)。

### 个人项目中的工作流 <a id="workflows-in-personal-projects"></a>

如果工作流引用了个人项目中的工作流（例如子工作流或错误工作流），实例级晋级会失败。n8n 会显示 **workflow dependencies not included in the package. Export aborted.（包中未包含工作流依赖，导出已中止。）**。请将被引用的工作流移至团队项目，或删除该引用，然后再次晋级。请参阅[个人项目](known-limitations.md#personal-projects)。

## 相关资源 <a id="related-resources"></a>

- [环境管理](./)
- [规划环境](plan-your-environments.md)
- [首次晋级](first-promotion.md)
- [应用变更](apply-changes.md)
- [晋级审核](promotion-reviews.md)
- [基于 Git 的晋级](git-based-promotion/README.md)
- [已知限制](known-limitations.md)
- [从经典环境升级](upgrade-from-environments-classic.md)
