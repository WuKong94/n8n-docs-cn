---
description: 了解环境管理在预览阶段尚未支持的内容，以及各项限制的替代处理方式。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 已知限制 <a id="known-limitations"></a>

环境管理处于预览阶段，n8n 正在持续改进和扩展。以下许多限制是暂时的；存在替代处理方式时，各条目会给出说明。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## 企业级就绪程度 <a id="enterprise-readiness"></a>

环境管理的**企业级就绪程度有限**，尚未支持以下企业功能：

- **多主实例：**环境管理不支持[多主实例配置](../../deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md#multi-main-setup)，计划在未来支持。
- **日志流：**晋级、应用和审核事件不会发送到[日志流](../observe-and-log/stream-logs-to-external-systems.md)目标，计划在未来支持。
- **公共 API：**公共 API 尚未覆盖晋级审核，计划在未来支持。
- **外部密钥：**提供方的访问令牌不能来自[外部密钥保管库](../manage-credentials/use-external-secret-stores.md)，计划在未来支持。

## 跨项目依赖 <a id="cross-project-dependencies"></a>

工作流可以使用项目外的资源：其他团队项目中的子工作流，以及其他项目拥有并共享的凭据。数据表和项目变量始终只属于一个项目。

- **其他项目中的子工作流：**项目级晋级只引用这些子工作流，因此它们必须已存在于目标实例上。
- **其他项目拥有的凭据：**项目级晋级会包含这些凭据，但项目级应用只有在目标实例上已存在相同 ID 的凭据（例如此前已应用其所属项目），且凭据已共享给当前项目时，才能使用。如果缺失，应用操作会被阻止，并且无法从 **Blockers（阻碍问题）**中创建。

**替代处理方式：**先晋级并应用共享资源所属的项目，或使用包含所有团队项目的实例级晋级和实例级应用。实例级应用会覆盖目标实例上的每个团队项目，请先阅读[实例级应用](apply-changes.md#instance-apply)。个人项目拥有的凭据绝不会传递。晋级前，请先在源实例上将其移至团队项目。

## 在项目之间移动工作流和文件夹 <a id="moving-workflows-and-folders-between-projects"></a>

项目级晋级和项目级应用无法将工作流或文件夹从一个项目移至另一个项目，支持项目内移动。计划在未来支持项目级晋级和应用中的跨项目移动。

**替代处理方式：**使用实例级晋级和实例级应用。它们会将目标实例上已有的工作流和文件夹移至分支中对应的项目，因此工作流会在目标实例上保留 ID、版本历史和执行记录。实例级应用会覆盖目标实例上的每个团队项目，请先阅读[实例级应用](apply-changes.md#instance-apply)。

## 项目专属环境 <a id="project-specific-environments"></a>

环境目前覆盖整个实例，计划在未来支持单个项目的环境。

## 可以使用环境管理的角色 <a id="roles-that-can-use-environments"></a>

目前只有实例所有者和实例管理员可以设置环境、晋级、应用和审核晋级。计划在未来支持项目角色。

## 支持的 Git 提供方 <a id="supported-git-providers"></a>

环境管理目前有两种提供方类型：通用 Git 和 GitLab。计划在未来提供专用的 GitHub 和 Bitbucket 提供方。

**替代处理方式：**通过[通用 Git](git-based-promotion/generic-git.md)连接 GitHub、Bitbucket 及其他 Git 托管服务。这些服务暂不支持晋级审核。

## 智能体支持 <a id="agent-support"></a>

晋级和应用尚不包含智能体，相关支持正在开发中。

## 个人项目 <a id="personal-projects"></a>

晋级和应用只覆盖团队项目。

**替代处理方式：**将需要晋级的工作流移至团队项目。

## 工作流描述 <a id="workflow-descriptions"></a>

晋级不包含工作流的描述。

**替代处理方式：**在目标实例上更新描述。

## 晋级不含工作流的项目 <a id="promoting-projects-without-workflows"></a>

项目级晋级要求至少包含一个工作流，因此无法单独晋级空项目。

**替代处理方式：**使用包含所有团队项目的实例级晋级，然后在目标实例上[从环境添加缺失的项目](apply-changes.md#add-missing-projects)。

## 选择依赖资源 <a id="selecting-dependencies"></a>

n8n 会包含选定工作流使用的每个凭据、变量、数据表和标签，个人项目拥有的凭据除外。无法自行选择依赖资源，也无法单独晋级凭据、变量、数据表或标签。计划在未来支持选择依赖资源。

**替代处理方式：**晋级使用这些资源的工作流。

## 凭据设置 <a id="credential-settings"></a>

晋级不包含凭据是否与所有用户和项目共享，以及是否由每位用户连接自己的账号这两项设置。

**替代处理方式：**在目标实例上编辑凭据，重新设置这些选项。

## 更新尚未完成的晋级审核 <a id="updating-an-open-promotion-review"></a>

n8n 无法将变更推送到尚未完成的晋级审核。例如审核者在 GitLab 上要求修改时，新的晋级无法将修改追加到该审核。计划在未来支持从 n8n 向尚未完成的晋级审核推送变更。

**替代处理方式：**在 GitLab 上关闭合并请求，打开 **Reviews（审核）**以便 n8n 获取已关闭状态，然后再次晋级，创建新的审核。n8n 目前还无法自行关闭审核。

## 功能分支名称 <a id="feature-branch-names"></a>

n8n 将功能分支命名为 `n8n-promotion/<timestamp>`，目前无法自行选择名称。计划在未来支持自定义分支名称。

## 晋级审核状态 <a id="promotion-review-status"></a>

打开 **Reviews（审核）**时，n8n 才会从 Git 托管服务更新晋级审核状态。在此之前，Git 托管服务上的变化不会显示在 n8n 中。

## GitLab 批准规则 <a id="gitlab-approval-rules"></a>

n8n 使用同一个 GitLab 令牌创建和批准合并请求。如果 GitLab 批准规则禁止作者批准自己的合并请求，就会阻止 **Approve and merge（批准并合并）**。

**替代处理方式：**调整批准规则，或在 GitLab 上合并。请参阅[晋级审核](promotion-reviews.md#n8n-acts-as-the-tokens-user)。

## 相关资源 <a id="related-resources"></a>

- [环境管理](./)
- [规划环境](plan-your-environments.md)
- [首次晋级](first-promotion.md)
- [晋级变更](promote-changes.md)
- [应用变更](apply-changes.md)
- [晋级审核](promotion-reviews.md)
- [基于 Git 的晋级](git-based-promotion/README.md)
- [从经典环境升级](upgrade-from-environments-classic.md)
