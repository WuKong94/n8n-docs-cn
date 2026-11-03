---
description: 首次将工作内容从源实例引入新的目标实例。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 首次晋级 <a id="your-first-promotion"></a>

首次将工作内容从开发等源实例引入生产等目标实例。

如果实例使用经典环境，请先阅读[从经典环境迁移](upgrade-from-environments-classic.md#migrate-from-environments-classic)。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## 晋级与应用 <a id="promote-and-apply"></a>

1. 在源实例上，添加要晋级到的环境。请参阅[规划环境](plan-your-environments.md)。
2. 在目标实例上，添加要从中应用变更的环境，使用与源实例环境相同的仓库和分支。
3. 一次性或逐项目引入工作内容：
   - **一次性引入：**在源实例上运行[实例级晋级](promote-changes.md#instance-promote)，发送所有团队项目。在目标实例上运行[实例级应用](apply-changes.md#instance-apply)，创建所有团队项目并处理跨项目依赖。
   - **逐项目引入：**在源实例上运行实例级晋级，或在每个项目中运行[项目级晋级](promote-changes.md#project-promote)。没有工作流的项目需要实例级晋级，请参阅[晋级不含工作流的项目](known-limitations.md#promoting-projects-without-workflows)。在目标实例上，[添加缺失的项目](apply-changes.md#add-missing-projects)，然后逐个运行[项目级应用](apply-changes.md#project-apply)。先处理其他项目依赖的项目，例如包含共享子工作流或凭据的项目。

   如果环境会推送功能分支或创建晋级审核，请先合并功能分支，或批准并合并审核，然后再应用。n8n 提示时，创建目标实例上尚不存在的凭据和变量。如果目标实例已有内容，请先阅读[应用到已有内容的实例](#apply-to-an-instance-that-already-has-content)。
4. 发布需要运行的工作流。应用操作创建的工作流处于未发布状态。
5. [保护目标实例](protect-a-production-instance.md)。

源实例和目标实例应使用相同的 n8n 版本。

个人项目不会晋级。开始之前，请将团队项目使用的工作流和凭据，从个人项目移至团队项目。

### 应用到已有内容的实例 <a id="apply-to-an-instance-that-already-has-content"></a>

应用操作按 ID 匹配项目、工作流、凭据和数据表。即使名称相同，在目标实例上手动创建的内容也具有与源实例不同的 ID，因此应用操作会在其旁边创建源实例的内容。

对于分支中不存在的内容，处理方式取决于应用级别：

- **项目级应用：**仅修改一个项目中选定的工作流及其依赖资源，绝不会删除项目。如果需要保留目标实例上的内容，请使用此方式。若目标实例尚无该项目，实例所有者或管理员应先在 **Settings（设置）** > **Environments（环境）**中，实例级 **Apply（应用）**旁[从环境添加该项目](apply-changes.md#add-missing-projects)，以保留源项目的 ID。手动创建的项目会获得不同 ID，应用操作不会将其匹配。先处理其他项目依赖的项目，例如包含共享子工作流或凭据的项目。请参阅[跨项目依赖](known-limitations.md#cross-project-dependencies)。
- **实例级应用：**使所有团队项目与分支一致。确认后，会删除分支中不存在的项目，例如手动创建的项目。

{% hint style="warning" %}
实例级应用无法撤销。它将环境分支作为团队项目的权威来源，会删除分支中不存在的项目及其中所有内容，包括凭据和数据表行；对于保留的项目，也会删除分支中不存在的工作流。请仅在源实例执行了实例级晋级后，或者备份目标实例后运行。对于新的目标实例，请在其他人开始使用之前执行实例级应用。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

- [环境管理](./)
- [规划环境](plan-your-environments.md)
- [晋级变更](promote-changes.md)
- [应用变更](apply-changes.md)
- [保护生产实例](protect-a-production-instance.md)
- [基于 Git 的晋级](git-based-promotion/README.md)
- [已知限制](known-limitations.md)
- [从经典环境升级](upgrade-from-environments-classic.md)
