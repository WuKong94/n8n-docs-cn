---
description: 使用晋级审核，在已晋级的变更进入环境分支前，直接在 n8n 中批准变更。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 晋级审核 <a id="promotion-reviews"></a>

晋级审核允许其他人在源实例上批准已晋级的变更，然后变更才会进入环境分支。从该环境应用变更的实例，只有在批准后才能获得这些变更。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## 晋级审核如何运作 <a id="how-promotion-reviews-work"></a>

在晋级目标环境中开启晋级审核后，每次晋级都会创建审核，而不是直接修改环境分支。审核显示在源实例左侧菜单的 **Reviews（审核）**中，你可以在此检查并批准变更。

某个项目的审核尚未完成时，无法再次晋级该项目，也无法向该审核追加变更。这样可以避免审核之间出现合并冲突。请先批准或关闭审核，再次晋级。

只有实例所有者和实例管理员可以查看和批准晋级审核。

## 支持的提供方 <a id="supported-providers"></a>

目前只有 GitLab 支持晋级审核。n8n 会创建合并请求并同步到 **Reviews（审核）**，在其中显示工作流变更的可视化差异，而不是原始文件。计划在未来支持更多 Git 提供方，以及不依赖 Git 托管服务的晋级审核。使用[通用 Git](git-based-promotion/generic-git.md)时，n8n 可以将每次晋级推送到功能分支，由其他人在 Git 托管服务上手动合并。

## 使用 GitLab 进行晋级审核 <a id="promotion-reviews-with-gitlab"></a>

### 开启晋级审核 <a id="turn-on-promotion-reviews"></a>

在执行晋级的实例上，编辑晋级目标环境，开启 **Open a merge request in GitLab（在 GitLab 中创建合并请求）**。

随后每次晋级都会推送功能分支，并创建合并到环境分支的合并请求。该合并请求会作为晋级审核显示在 **Reviews（审核）**中。Reviews 只列出 n8n 创建的合并请求。

### 审查并批准晋级 <a id="review-and-approve-a-promotion"></a>

1. 在晋级变更的实例上，选择左侧菜单中的 **Reviews（审核）**。晋级审核带有 **Promotion（晋级）**徽标。
2. 打开审核。**Changes（变更）**选项卡显示每个有变化的工作流和依赖资源。**Before（变更前）**对应环境分支，**After（变更后）**对应当前审核。
3. 选择 **Approve and merge（批准并合并）**。n8n 会在 GitLab 上批准合并请求、将其合并并删除对应分支。此操作无法撤销。

### 无法批准并合并时 <a id="when-you-cant-approve-and-merge"></a>

出现以下情况时，n8n 会禁用 **Approve and merge（批准并合并）**：

- 审核者在 GitLab 上要求修改。
- 合并请求存在冲突。
- 在加载审核后，有人推送了新提交。

GitLab 也可能拒绝合并，例如必需的流水线尚未通过。此时 n8n 会显示 GitLab 的消息。请在 GitLab 上解决原因，然后重新加载 **Reviews（审核）**。

### n8n 以令牌所属用户的身份操作 <a id="n8n-acts-as-the-tokens-user"></a>

n8n 以提供方访问令牌所属的 GitLab 用户身份创建、批准和合并请求，而不是以点击 **Approve and merge（批准并合并）**的 n8n 用户身份操作。n8n 会在合并请求中添加备注，记录批准该请求的 n8n 用户名称。

由于创建和批准合并请求的是同一个 GitLab 用户，如果批准规则禁止作者批准自己的合并请求，就会阻止 **Approve and merge（批准并合并）**。请调整批准规则，或在 GitLab 上合并。

### 审核状态 <a id="review-states"></a>

| 状态 | 含义 |
|---|---|
| **Open（待审核）** | 审核等待批准。 |
| **Changes requested（要求修改）** | 审核者在 GitLab 上要求修改。 |
| **Merged（已合并）** | 变更已进入环境分支。 |
| **Closed（已关闭）** | 有人关闭审核且未合并。 |

## 相关资源 <a id="related-resources"></a>

- [环境管理](./)
- [规划环境](plan-your-environments.md)
- [晋级变更](promote-changes.md)
- [应用变更](apply-changes.md)
- [基于 Git 的晋级](git-based-promotion/README.md)
- [已知限制](known-limitations.md)
- [从经典环境升级](upgrade-from-environments-classic.md)
- [GitLab](git-based-promotion/gitlab.md)
- [工作流审核](../../build/manage-workflows/workflow-reviews.md)
