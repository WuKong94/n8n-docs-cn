---
description: 发布前提交工作流版本供审核，使用可视化差异比较更改，在活动评论中讨论，并批准或要求修改。
contentType: howto
nodeTitle: 工作流审核
url: https://docs.n8n.io/build/manage-workflows/workflow-reviews
status: preview
layout:
  description:
    visible: false
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流审核 <a id="workflow-reviews"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐支持工作流审核：

- **n8n Cloud：** Enterprise
- **自托管：** Enterprise

工作流审核从 n8n 2.37.0 起可用。实例管理员必须在 **Settings（设置）** > **Security & policies（安全与策略）** 中启用此功能。
{% endhint %}

{% hint style="info" %}
**预览状态**

工作流审核处于预览阶段，正式推出前可能发生变化。请避免在生产工作流中依赖此功能。
{% endhint %}

工作流审核让团队在发布前批准某个特定[工作流版本](view-change-history.md)。在 **Publish（发布）** 菜单中选择 **Submit for review（提交审核）**，而不是直接发布，再指定审核人。批准后，n8n 会自动发布该版本。

启用此功能后，审核仍是可选流程。只要工作流当前没有尚未结束的审核，就仍可直接发布。

指定审核人或审核人要求修改时，n8n 不会发送电子邮件或其他外部通知。请在左侧菜单的 **Reviews（审核）** 中查看需要处理的请求。

## 审核机制 <a id="how-reviews-work"></a>

审核与某个已保存的工作流版本关联，该版本称为*固定版本*。审核进行期间可以继续编辑。新保存会创建更新的版本，但只有将这些更改提交到审核后，才会改变固定版本。

### 审核涵盖的内容 <a id="what-a-review-covers"></a>

审核涵盖单个工作流中固定保存版本所包含的内容，即节点和连接。可视化差异和批准仅适用于这些内容。

审核不涵盖工作流依赖的资源。以下资源不属于差异比较内容，不受批准流程约束；即使审核仍在进行，修改后也会立即影响已发布的工作流：

* **工作流设置**，例如时区、错误工作流和执行顺序。
* 工作流使用的**凭据**。
* **变量**。
* **数据表**。
* 工作流调用的**子工作流**。每个子工作流都是独立工作流，可以有自己的审核。

### 审核状态 <a id="review-statuses"></a>

* **Waiting for review（等待审核）**：固定版本等待审核决定。n8n 会禁止发布。
* **Changes requested（要求修改）**：审核人要求更新。n8n 会继续禁止发布，直到有人提交更新版本（审核返回 **Waiting for review（等待审核）** 状态），并有人批准该版本。
* **Approved（已批准）**：审核人或管理员已批准。审核关闭，发布限制解除。n8n 会以**请求者**（提交工作流供审核的用户）的身份发布固定版本，因此发布历史和审计记录会将此次发布归属于请求者，而不是批准的审核人。少数情况下，n8n 无法自动发布该版本，但审核仍保持已批准且已关闭状态。此时，请自行使用编辑器中的 **Publish（发布）** 按钮发布该版本。
* **Closed（已关闭，未批准）**：当没有内容需要继续审核时，例如工作流被删除、归档或移出项目，n8n 也可以不经批准关闭审核。此类审核显示在 **Reviews（审核）** > **Closed（已关闭）** 中，**Activity（活动）** 会说明关闭原因。

### 审核进行期间的发布 <a id="publishing-while-a-review-is-open"></a>

审核尚未结束时（`Waiting for review` 或 `Changes requested`），n8n 会禁止从编辑器、公共 API 和 n8n MCP 服务器发布该工作流。仍然可以取消发布，但这不会关闭审核，也不会解除发布新版本的限制。

一个工作流同一时间只能有一个尚未结束的审核。此期间再次选择 **Publish（发布）** 或 **Submit for review（提交审核）**，不会启动新的审核。应将更新的已保存版本提交到现有审核中（请参阅[向进行中的审核提交后续更改](#submit-later-changes-to-an-open-review)）。

## 启用工作流审核 <a id="enable-workflow-reviews"></a>

实例管理员可以在 **Settings（设置）** > **Security & policies（安全与策略）** 的 **Workflow reviews（工作流审核）** 下，为整个实例启用此功能。

实例安全策略的更多信息，请参阅[管理安全策略](../../deploy/host-n8n/configure-n8n/security/manage-security-policies.md)。

## 提交或更新审核 <a id="submit-or-update-a-review"></a>

*版本*是待审核和发布的工作流快照；*审核*则是围绕该版本的请求与讨论。两者分别命名，因此提交流程会要求填写两个名称。

1. 打开工作流，选择 **Publish（发布）**（或按 `Shift`+`P`）。
2. 选择 **Submit for review（提交审核）**，而不是直接发布。
3. 第一步，输入快照的 **Version name（版本名称）**（必填）。也可以按需描述版本更改。
4. 下一步，输入 **Review title（审核标题）**，并指定 **Reviewer（审核人）**（两者均必填）。也可以按需添加 **Review description（审核说明）**。
5. 选择 **Submit（提交）**。

审核人需要对此工作流具有 `workflow:read` 权限，无需 `workflow:publish` 权限。

n8n 会针对当前已保存版本创建审核。可以从左侧菜单的 **Reviews（审核）** 中打开。

### 向进行中的审核提交后续更改 <a id="submit-later-changes-to-an-open-review"></a>

1. 打开工作流。
2. 在编辑器顶部的审核状态处，选择 **Submit changes（提交更改）**。
3. 为更新版本输入 **Version name（版本名称）**（必填）。也可以按需描述版本更改。
4. 按需更新 **Review description（审核说明）**，再选择 **Submit（提交）**。

n8n 会将进行中的审核更新为较新的版本。如果之前处于 **Changes requested（要求修改）** 状态，会返回 **Waiting for review（等待审核）**。

### 必须审核的偏好设置 <a id="review-required-preference"></a>

在 **Publish（发布）** 菜单中，可以为当前工作流开启 **Review required（需要审核）**。开启后，选择 **Publish** 会打开提交审核弹窗，而不是直接发布。

此工作流的偏好设置保存在浏览器中，不保存在工作流本身，因此不会影响其他用户。只要仍有进行中的审核，所有用户的发布操作都会被禁止，直到审核关闭。

## 审核提交内容 <a id="review-a-submission"></a>

审核详情包含两个标签页：

* **Activity（活动）**：说明、活动记录和评论。审核关闭后，评论仍然可见。当前版本不支持将评论关联到特定节点。
* **Changes（更改）**：当前 **Published（已发布）** 版本与 **In review（审核中）** 版本之间的可视化工作流差异。其工作方式与[源代码管理中的工作流差异](../../administer/use-source-control-and-environments/compare-versions.md)相同。

有权打开审核的人，可以在 **Activity（活动）** 中发表评论，而不作出决定。要作出决定，指定的审核人、项目管理员或实例管理员可以选择：

* **Approve（批准）**：关闭审核，并以请求者身份发布固定版本。
* **Request changes（要求修改）**：保持审核进行中，供编辑者更新工作流并重新提交。

## 权限 <a id="permissions"></a>

| 操作 | 有权执行的用户 |
| --- | --- |
| 为实例启用或禁用工作流审核 | 有权访问 **Settings（设置）** > **Security & policies（安全与策略）** 的实例管理员 |
| 提交工作流供审核 | 对该工作流具有 `workflow:publish` 权限的用户 |
| 使用更新版本更新进行中的审核 | 对该工作流具有 `workflow:publish` 权限的用户 |
| 查看是否有正在进行的审核 | 可以打开工作流的用户，包括查看者和编辑者。只有属于下方所列人员时，才能打开审核详情。 |
| 打开审核详情，并在 **Reviews（审核）** 中显示 | 请求者、审核中的作者、指定的审核人，以及项目或实例管理员。管理员可以看到所有审核。 |
| 成为可选审核人 | 对该工作流至少具有 `workflow:read` 权限的用户 |
| 批准或要求修改 | 指定的审核人、项目管理员或实例管理员。作者只有同时具备这些角色之一时，才能作出决定。 |

**请求者**是提交工作流供审核的用户。**作者**包括请求者，以及之后向同一进行中审核提交过更新版本的任何人。

{% hint style="info" %}
**取消审核**

目前无法取消或撤回进行中的审核。n8n 计划在未来版本中添加此功能。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [管理工作流](./)
* [配置工作流设置](configure-workflow-settings.md)
* [为工作流添加标签](tag-workflows.md)
* [收藏项目](favorite-items.md)
* [查看更改历史](view-change-history.md)
* [导出和导入](export-and-import.md)
* [n8n 软件包](n8n-packages/README.md)
* [与他人共享](share-with-others.md)
* [保存和发布工作流](../understand-workflows/save-and-publish-workflows.md)
* [通过工作流差异比较更改](../../administer/use-source-control-and-environments/compare-versions.md)
* [管理安全策略](../../deploy/host-n8n/configure-n8n/security/manage-security-policies.md)
* [查看可用角色](../../administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md)
