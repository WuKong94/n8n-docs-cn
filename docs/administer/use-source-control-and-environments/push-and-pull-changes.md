---
title: 推送和拉取
description: 将工作推送到 Git，并从 Git 拉取到实例。
contentType: howto
nodeTitle: 推送和拉取更改
originalFilePath: source-control-environments/using/push-pull.md
originalUrl: https://docs.n8n.io/source-control-environments/using/push-pull
url: https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 推送和拉取 <a href="#push-and-pull" id="push-and-pull"></a>

将 n8n 实例连接到 Git 仓库后，需要保持工作与 Git 同步。

本文假定你熟悉一些 Git 概念和术语。关于 n8n 如何使用 Git，请参阅 [Git 与 n8n](use-git-in-n8n.md)。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/one-direction.md" %}

## 获取他人的工作 <a href="#fetch-other-peoples-work" id="fetch-other-peoples-work"></a>

{% hint style="info" %}
**n8n 角色控制哪些用户可以拉取（获取）更改**

必须是实例所有者或实例管理员，才能从 Git 拉取更改。
{% endhint %}

要从 Git 拉取工作，请在主菜单中选择 **Pull**（拉取）<img src="../.gitbook/assets/pull-icon.png" alt="拉取图标" data-size="line">。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/push-pull-menu-state.md" %}

n8n 可能会警告该操作将覆盖本地更改。选择 **Pull and override**（拉取并覆盖），即可使用 Git 中的内容覆盖本地工作。

如果更改中包含新的变量或凭据存根，n8n 会提示你在使用这些项目之前补填相应的值。

{% hint style="info" %}
**如何处理已删除的资源**

当工作流、凭据、变量、标签和数据表从仓库中删除时，这些资源的本地版本不会自动删除。拉取仓库更改时，n8n 会提示哪些资源已过时，并询问是否删除。

译注：本段关于不自动删除资源的概述，与下文数据表的说明存在差异：下文指出，本地存在但 Git 中不存在的数据表会在拉取时删除，使用 force 的 API 或自动化拉取会跳过确认，并删除表中全部行数据。此处保留原文；不要将本段概述作为自动化拉取不会删除数据表的保证。
{% endhint %}

### 拉取可能更改工作流与凭据的所有者 <a href="#workflow-and-credential-owner-may-change-on-pull" id="workflow-and-credential-owner-may-change-on-pull"></a>

从 Git 拉取到 n8n 实例时，n8n 会尝试将工作流和凭据分配给匹配的用户或项目。

如果原所有者是用户：

如果两个实例中都有同一所有者（邮箱匹配），所有者保持不变。如果新实例中没有原所有者，n8n 会将执行拉取的用户设为工作流所有者。

如果原所有者是[项目](../manage-users-and-access/set-permissions-and-roles-rbac/README.md)：

n8n 会尝试按项目名称在新实例中匹配原项目。如果没有匹配项目，n8n 会创建同名项目，将当前用户分配为项目所有者，再将工作流和凭据导入该项目。

### 拉取时自动发布工作流 <a href="#auto-publish-workflows-on-pull" id="auto-publish-workflows-on-pull"></a>

拉取时，可通过拉取弹窗的 **Auto publish**（自动发布）下拉菜单，选择是否自动发布工作流。共有三种模式：

* **Off**（关闭，默认）：不尝试发布任何工作流。工作流保留当前在本地的发布状态。
* **If workflow already published**（工作流已发布时）：仅尝试发布本实例中已发布的工作流，新工作流不会发布。
* **On**（开启）：尝试发布所有拉取的工作流，包括新工作流。

无论自动发布设置如何，n8n 都不会自动发布已归档的工作流。

启用自动发布并完成拉取后，n8n 会显示结果弹窗，列出成功发布和发布失败的工作流。如果工作流存在验证错误或缺失凭据，发布可能失败。

也可通过 [API](../../connect/n8n-api/api-reference.md)，使用拉取端点的 `autoPublish` 参数自动发布，可选值为 `none`、`published` 或 `all`。

### 拉取可能造成短暂服务中断 <a href="#pulling-may-cause-brief-service-interruption" id="pulling-may-cause-brief-service-interruption"></a>

向已发布的工作流拉取更改时，n8n 会在拉取期间取消发布，再重新发布。这可能导致工作流中断几秒钟。

## 将工作发送到 Git <a href="#send-your-work-to-git" id="send-your-work-to-git"></a>

{% hint style="info" %}
**n8n 角色控制哪些用户可以推送更改**

必须是实例所有者、实例管理员或项目管理员，才能向 Git 推送更改。
{% endhint %}

{% include "../../reusable-content/.gitbook/includes/source-control-environments/push.md" %}

## 提交的内容 <a href="#what-gets-committed" id="what-gets-committed"></a>

n8n 会将以下内容提交到 Git：

* 工作流，包括其标签和工作流所有者的邮箱地址。可以选择要推送的工作流。
* 凭据存根，即 ID、名称和类型。只有字段内容为[表达式](../../build/work-with-data/expressions-versus-data-nodes.md)时，才会包含其他字段。可以选择要推送的凭据。
* 变量存根（ID 和名称）。
* 数据表结构（表名和列定义，不含行数据）。可以选择要推送的数据表。
* 项目。
* 文件夹。

## 合并行为与冲突 <a href="#merge-behaviors-and-conflicts" id="merge-behaviors-and-conflicts"></a>

n8n 的源代码管理实现采用了特定的处理规则：自动解决凭据和变量的合并冲突，但无法检测工作流冲突。

### 工作流 <a href="#workflows" id="workflows"></a>

推送或拉取时，需要明确告诉 n8n 如何处理工作流。Git 仓库充当权威来源。

拉取时，n8n 可能警告本地工作流副本与 Git 中不同。如果接受拉取，本地副本将被覆盖。拉取时请注意保留重要更改。

推送时，本地工作流会覆盖 Git 中的版本，因此应确保本地版本最新，否则可能覆盖最近的更改。

为避免上述问题，完成工作流修改后应立即推送更改，再进行拉取会更安全。

为避免丢失数据：

* 设计源代码管理流程，使工作流单向流动。例如，在开发实例编辑，推送到 Git，再拉取到生产环境。不要在生产实例修改后再推送。
* 不要推送所有工作流，只选择需要的工作流。
* 手动编辑 Git 仓库中的文件时要谨慎。

### 凭据、变量和工作流标签 <a href="#credentials-variables-and-workflow-tags" id="credentials-variables-and-workflow-tags"></a>

n8n 会决定保留哪个版本，因此凭据和变量不会产生需要手动处理的合并问题。

拉取时：

* 如果标签、变量或凭据不存在，n8n 会创建它。
* 如果标签、变量或凭据已存在，n8n 不会更新它，以下情况除外：
	* 通过 API 或外部方式设置变量值，新值会覆盖现有值。
	* 凭据名称已更改，n8n 会使用 Git 中的版本。
	* 标签名称已更改，n8n 会更新标签名。标签名必须唯一，因此重命名时要谨慎，以免在拉取过程中产生数据库唯一性问题。

推送时：

* n8n 会覆盖整个变量文件和标签文件。
* 如果凭据已存在，n8n 会使用更改覆盖它，但拉取时不会将这些更改应用到已有凭据。

### 数据表 <a href="#data-tables" id="data-tables"></a>

n8n 会在环境间同步数据表结构（表结构和列定义），不会同步行数据。

推送时：

* 可以选择包含哪些数据表。
* n8n 会导出表名、列名、列类型和列顺序。

拉取时：

* n8n 会创建本地不存在的数据表。
* n8n 会更新现有数据表，使其与 Git 中的结构一致：新增列，并删除远程版本中已不存在的列。其余列的数据会保留。
* n8n 按项目内的表名匹配数据表。如果在源环境中删除数据表后以相同名称重建，或在两个环境中手动创建同名表，n8n 会将其视为同一张表：把本地表的 ID 调整为传入表的 ID，像其他更改一样更新结构，并保留本地行数据。
* 如果数据表在本地存在、但在 Git 中不存在，拉取会将其删除，包括全部行数据。交互式拉取会在执行操作前，在确认对话框中将该表列为 **Deleted**（已删除）。使用强制选项的拉取（例如通过 API 或自动化配置）会直接删除表，不再询问。要保留此表，请在拉取前先推送。

{% hint style="warning" %}
**移除列会造成数据丢失**

如果拉取的数据表比本地版本少了一些列，n8n 会删除这些列及其中的数据，且无法撤销。发生这种情况时，n8n 会在拉取弹窗中显示警告。
{% endhint %}

{% hint style="info" %}
**使用外部密钥库管理凭据**

如果不同 n8n 环境需要使用不同凭据，请使用[外部密钥](../manage-credentials/use-external-secret-stores.md)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [比较版本](compare-versions.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)
