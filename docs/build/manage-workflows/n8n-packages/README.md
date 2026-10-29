---
description: 将工作流及其所需结构打包为可移植的 .n8np 文件，在 n8n 实例之间迁移。
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 软件包 <a id="n8n-packages"></a>

{% hint style="info" %}
**功能可用范围**

n8n 软件包从 n8n 2.27.0 起可用，此后大多数版本都增加了选项。如果本文中的某个选项无法识别，请检查所用版本。
{% endhint %}

{% hint style="info" %}
**预览状态**

n8n 软件包处于预览阶段。软件包格式和 API 在未来版本中可能发生变化，因此在没有更新计划的情况下，请避免让关键自动化任务依赖此功能。
{% endhint %}

n8n 软件包是一个文件，包含 n8n 实例中的一部分内容：若干工作流，以及这些工作流运行所需的结构和引用。可以从一个实例导出软件包，移动文件，再导入另一个实例。可以将其理解为 n8n 实例部分内容的 `npm` 软件包。

软件包是扩展名为 `.n8np` 的 gzip 压缩 tar 归档。内部每个实体都是一个小型 JSON 文件，`manifest.json` 列出包内内容以及目标实例必须提供的资源。完整布局请参阅[软件包格式](package-format.md)。

软件包是 API 功能。可以通过 [n8n API](../../../connect/n8n-api/README.md) 导出和导入，也可以使用封装了相同两个端点的 [n8n CLI](../../../connect/n8n-cli.md)。n8n 编辑器不提供软件包导出或导入功能。

## 三种软件包结构 <a id="three-package-shapes"></a>

导出的内容决定软件包的结构，而结构决定导入时内容存放的位置：

* **工作流软件包**：包含一个或多个工作流。导入时，工作流存放到指定的项目和文件夹。
* **文件夹软件包**：包含一个或多个文件夹，始终包含其中的所有嵌套内容。导入时，文件夹树存放到指定项目中。
* **项目软件包**：包含一个或多个完整项目。软件包自带项目，因此由自身结构决定内容的存放位置，传入的目标项目会被忽略。

一次导出可以同时包含工作流和文件夹，但不能将这两者中的任意一种与项目混合导出。

## 软件包包含的内容 <a id="what-travels-in-a-package"></a>

| 随包迁移 | 不随包迁移 |
|---------|----------------|
| 工作流：节点、连接、设置、发布状态和归档状态 | 凭据机密值和配置 |
| 文件夹及其嵌套关系 | 数据表中的行 |
| 项目：名称、说明和图标 | 执行记录和执行历史 |
| 凭据引用：仅 ID、名称和类型 | 用户、项目成员、角色和共享关系 |
| 数据表结构：列 ID、名称和类型 | 固定数据和工作流静态数据 |
| 变量：名称、类型及变量值（除非选择排除值） | 工作流版本历史 |
| 标签 | 工作流是否被收藏 |

**凭据机密值绝不会随包迁移。** 软件包中的凭据文件只有三个字段：ID、名称和类型。主机、基础 URL、区域等非机密配置与机密值保存在同一加密存储中，因此也不会随包迁移。导入时，n8n 会将每个引用匹配到目标实例上已有的凭据，或创建空占位凭据，供你补充信息。

**数据表中的行绝不会随包迁移。** 只迁移表结构。导入的数据表最初为空。

## 何时使用软件包 <a id="when-to-use-packages"></a>

需要以可重复、可自动化的方式在实例间迁移工作时，可以使用软件包：

* **在环境之间推进部署。** 作为流水线的一部分，将工作流从开发环境推到预发布环境，再推到生产环境。重复导入会就地更新，而不是创建副本，因此首次及后续迁移都可以使用同一条命令。
* **迁移到新实例。** 用一个文件迁移项目、其文件夹及工作流。
* **共享成果而不共享机密信息。** 将工作流交给其他团队，同时确保文件不含凭据数据。
* **备份结构。** 保存重建时所需的工作流和结构副本。不过软件包不是完整备份，不包含执行数据。

## 快速入门 <a id="quick-start"></a>

将 CLI 指向源实例，再导出一个工作流：

```bash
n8n-cli config set-url https://source.example.com
n8n-cli config set-api-key <your-api-key>

n8n-cli package export --workflow-id=<workflow-id> --output=triage.n8np
```

将 CLI 指向目标实例，再导入文件：

```bash
n8n-cli config set-url https://target.example.com
n8n-cli config set-api-key <your-api-key>

n8n-cli package import --file=triage.n8np --project-id=<target-project-id>
```

n8n 会在写入任何内容前检查整个软件包。如果存在阻止导入的问题，例如工作流使用了目标实例没有的节点类型，命令会以非零状态退出，并一次性列出发现的所有问题。

## 本节内容 <a id="in-this-section"></a>

* [软件包格式](package-format.md)：`.n8np` 文件的内容、三种软件包结构和清单。
* [导出软件包](export-a-package.md)：将工作流、文件夹或完整项目导出为软件包。
* [导入软件包](import-a-package.md)：导入软件包，并控制内容的存放位置。
* [导入机制](how-import-works.md)：n8n 如何在写入前检查软件包并解析依赖。
* [限制和权限](limits-and-permissions.md)：大小限制、许可证功能和 API 密钥权限范围。

有关复制粘贴以及编辑器下载、导入选项等其他迁移方式，请参阅[导出和导入](../export-and-import.md)。

## 相关资源 <a id="related-resources"></a>

* [管理工作流](../)
* [配置工作流设置](../configure-workflow-settings.md)
* [为工作流添加标签](../tag-workflows.md)
* [收藏项目](../favorite-items.md)
* [查看更改历史](../view-change-history.md)
* [审核工作流](../workflow-reviews.md)
* [导出和导入](../export-and-import.md)
* [与他人共享](../share-with-others.md)
