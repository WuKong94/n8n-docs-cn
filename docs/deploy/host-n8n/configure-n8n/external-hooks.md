---
title: 外部钩子
description: 使用外部钩子，在 n8n 执行特定操作时运行自定义代码。
contentType: howto
nodeTitle: 外部钩子
originalFilePath: hosting/configuration/external-hooks.md
originalUrl: https://docs.n8n.io/hosting/configuration/external-hooks
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/external-hooks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部钩子 <a href="#external-hooks" id="external-hooks"></a>

外部钩子允许你在 n8n 执行特定操作时运行自定义代码。可用于记录数据、修改数据，或通过抛出错误禁止操作。

有两种类型：

- **后端钩子**：在服务器端运行，通过 `EXTERNAL_HOOK_FILES` 环境变量注册。
- **前端钩子**：在浏览器中运行，使用 script 标签加载。

注册钩子所用的环境变量，请参阅[外部钩子环境变量](basic-configuration/use-environment-variables/external-hooks.md)。

## 后端钩子 <a href="#backend-hooks" id="backend-hooks"></a>

### 可用钩子 <a href="#available-hooks" id="available-hooks"></a>

| 钩子 | 参数 | 说明 |
| :------- | :---------| :---------- |
| `credentials.create` | `[credentialData: ICredentialsDb]` | 创建新凭据前调用，可用于限制凭据数量。 |
| `credentials.delete` | `[id: credentialId]` | 删除凭据前调用。 |
| `credentials.update` | `[credentialData: ICredentialsDb]` | n8n 保存现有凭据前调用。 |
| `frontend.settings` | `[frontendSettings: IN8nUISettings]` | n8n 启动时调用，可用于覆盖前端数据，例如显示的 OAuth URL。 |
| `n8n.ready` | `[app: App]` | n8n 就绪后调用，例如可用于注册自定义 API 端点。 |
| `n8n.stop` |  | n8n 进程停止时调用，可用于保存部分进程数据。 |
| `oauth1.authenticate` | `[oAuthOptions: clientOAuth1.Options, oauthRequestData: {oauth_callback: string}]` | OAuth1 身份验证前调用，可用于覆盖 OAuth 回调 URL。 |
| `oauth2.callback` | `[oAuth2Parameters: {clientId: string, clientSecret: string \| undefined, accessTokenUri: string, authorizationUri: string, redirectUri: string, scopes: string[]}]` | OAuth2 回调中调用，可用于覆盖 OAuth 回调 URL。 |
| `workflow.activate` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 激活工作流前调用，可用于限制活动工作流数量。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.afterCreate` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 创建工作流后调用。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.afterDelete` | `[workflowId: string, actor?: WorkflowLifecycleHookActor]` | 删除工作流后调用。`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.afterUpdate` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 保存现有工作流后调用。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.create` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 创建工作流前调用，可用于限制已保存工作流数量。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.deactivate` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 停用工作流前调用，此时 `active` 仍为 `true`。抛出错误可中止停用，使工作流保持活动状态。自 n8n 2.33.1 起提供。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.delete` | `[workflowId: string, actor?: WorkflowLifecycleHookActor]` | 删除工作流前调用。`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.postExecute` | `[fullRunData: IRun \| undefined, workflowData: IWorkflowBase, executionId: string, workflowContext: WorkflowHookContextService]` | 执行工作流后调用。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)。 |
| `workflow.preExecute` | `[workflow: Workflow, mode: WorkflowExecuteMode, workflowContext: WorkflowHookContextService]` | 执行工作流前调用，可用于统计或限制工作流执行。如果钩子抛出错误，n8n 不会创建执行记录。在 n8n 3.0.0 之前，可以设置 `N8N_PRE_EXECUTE_ERROR_CREATES_EXECUTION=true`，使钩子抛错时仍创建失败执行。n8n 3.0.0 移除了此变量。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，自 n8n 2.23.0 起提供。 |
| `workflow.update` | `[workflowData: IWorkflowBase, workflowContext: WorkflowHookContextService, actor?: WorkflowLifecycleHookActor]` | 保存现有工作流前调用。`workflowContext` 参数请参阅[工作流钩子上下文](#workflow-hook-context)，`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.afterArchive` | `[workflowId: string, actor?: WorkflowLifecycleHookActor]` | 归档工作流后调用。`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |
| `workflow.afterUnarchive` | `[workflowId: string, actor?: WorkflowLifecycleHookActor]` | 从归档恢复工作流后调用。`actor` 参数请参阅[工作流生命周期钩子的操作者](#workflow-lifecycle-hook-actor)。 |

### 注册钩子 <a href="#registering-hooks" id="registering-hooks"></a>

通过注册包含钩子函数的钩子文件来设置钩子。要注册钩子，请设置环境变量 `EXTERNAL_HOOK_FILES`。

可以将变量设为单个文件：

`EXTERNAL_HOOK_FILES=/data/hook.js`

也可以指定多个文件，以冒号分隔：

`EXTERNAL_HOOK_FILES=/data/hook1.js:/data/hook2.js`

### 钩子文件 <a href="#hook-files" id="hook-files"></a>

钩子文件是采用以下格式的普通 JavaScript 文件：

```js
module.exports = {
    "frontend": {
        "settings": [
            async function (settings) {
                settings.oauthCallbackUrls.oauth1 = 'https://n8n.example.com/oauth1/callback';
                settings.oauthCallbackUrls.oauth2 = 'https://n8n.example.com/oauth2/callback';
            }
        ]
    },
    "workflow": {
        "activate": [
            async function (workflowData) {
                const activeWorkflows = await this.dbCollections.Workflow.count({ active: true });

                if (activeWorkflows > 1) {
                    throw new Error(
                        'Active workflow limit reached.'
                    );
                }
            }
        ]
    }
}
```

### 钩子示例 <a href="#hook-examples" id="hook-examples"></a>

#### 缺少必需标签时阻止工作流执行 <a href="#block-workflow-execution-if-a-required-tag-is-missing" id="block-workflow-execution-if-a-required-tag-is-missing"></a>

请注意：自 n8n 2.23.0 起，`workflowContext` 参数会传给 `workflow.preExecute` 钩子。哪些钩子从哪个版本开始接收此参数，完整列表请参阅[工作流钩子上下文](#workflow-hook-context)。

当工作流缺少必需标签时，使用 `workflow.preExecute` 中止执行：

```js
module.exports = {
	workflow: {
		preExecute: [
			async function (workflow, mode, workflowContext) {
				const requiredTag = 'exampleTag';
				const workflowTags = await workflowContext.getWorkflowTags(workflow.id);
				if (!workflowTags.includes(requiredTag)) {
					throw new Error(`Workflow is missing required tag "${requiredTag}", aborting`);
				}
			},
		],
	},
};
```

### 工作流钩子上下文 <a id="workflow-hook-context"></a>

部分工作流钩子接收 `workflowContext` 参数，它是 `WorkflowHookContextService` 的实例，提供可在钩子函数中调用的辅助方法。

{% hint style="info" %}
**自 n8n 2.23.0 起提供**

n8n 将 `workflowContext` 传给 `workflow.preExecute` 钩子。
{% endhint %}

{% hint style="info" %}
**自 n8n 2.33.1 起提供**

n8n 将 `workflowContext` 传给 `workflow.create`、`workflow.afterCreate`、`workflow.activate`、`workflow.deactivate`、`workflow.update`、`workflow.afterUpdate` 和 `workflow.postExecute` 钩子。
{% endhint %}

上下文提供以下方法：

| 方法 | 返回值 | 说明 |
| :----- | :------ | :---------- |
| `getWorkflowTags(workflowId: string)` | `Promise<string[]>` | 返回给定工作流上附加的标签名称。 |
| `resolveIsTriggerNodeType(type: string, typeVersion?: number)` | `boolean` | 给定节点类型为触发器时返回 `true`。`type` 是完全限定的节点类型名称，例如 `n8n-nodes-base.manualTrigger`。`typeVersion` 默认为最新注册版本。n8n 无法解析节点类型时，例如实例未注册该类型，返回 `false`。 |

此示例使用 `resolveIsTriggerNodeType`，阻止激活不包含触发器节点的工作流：

```js
module.exports = {
	workflow: {
		activate: [
			async function (workflowData, workflowContext) {
				const hasTrigger = workflowData.nodes.some((node) =>
					workflowContext.resolveIsTriggerNodeType(node.type, node.typeVersion),
				);
				if (!hasTrigger) {
					throw new Error('Workflow must contain a trigger node, aborting activation');
				}
			},
		],
	},
};
```

### 工作流生命周期钩子的操作者 <a id="workflow-lifecycle-hook-actor"></a>

部分工作流生命周期钩子接收 `actor` 参数，仅包含执行操作的用户的必要信息。可用它确定操作归属，例如根据用户身份或角色允许或拒绝操作。

{% hint style="info" %}
**自 n8n 2.33.1 起提供**

n8n 将 `actor` 传给 `workflow.create`、`workflow.afterCreate`、`workflow.activate`、`workflow.deactivate`、`workflow.update`、`workflow.afterUpdate`、`workflow.delete`、`workflow.afterDelete`、`workflow.afterArchive` 和 `workflow.afterUnarchive` 钩子。此参数可选，n8n 无法确定操作者时可能为 `undefined`。
{% endhint %}

`actor` 对象具有以下属性：

| 属性 | 类型 | 说明 |
| :------- | :--- | :---------- |
| `id` | `string` | 用户的唯一 ID。 |
| `email` | `string \| null` | 用户邮箱地址，可能为 `null`，例如已受邀但尚未完成设置的用户。 |
| `firstName` | `string \| null` | 用户名字，可能为 `null`，例如已受邀但尚未完成设置的用户。 |
| `lastName` | `string \| null` | 用户姓氏，可能为 `null`，例如已受邀但尚未完成设置的用户。 |
| `role` | `string` | 用户角色的 slug，例如 `global:admin`，可选。 |

此示例使用 `actor`，记录谁删除了工作流：

```js
module.exports = {
	workflow: {
		delete: [
			async function (workflowId, actor) {
				console.log(`Workflow ${workflowId} deleted by ${actor?.email} (${actor?.role})`);
			},
		],
	},
};
```

### 钩子函数 <a href="#hook-functions" id="hook-functions"></a>

一个钩子或钩子文件可以包含多个钩子函数，所有函数依次执行。

如果钩子函数的参数是对象，就可以更改参数数据，从而改变 n8n 的行为。

还可以在任意钩子函数中使用 `this.dbCollections` 访问数据库，参阅上文[钩子文件](#hook-files)中的代码示例。

## 前端外部钩子 <a href="#frontend-external-hooks" id="frontend-external-hooks"></a>

与后端外部钩子一样，也可以在前端代码中定义外部钩子，使 n8n 在用户执行特定操作时调用。例如，可以记录和修改数据。

### 可用钩子 <a href="#available-hooks" id="available-hooks"></a>

| 钩子 | 说明 |
| :------- | :---------- |
| `credentialsEdit.credentialTypeChanged` | 现有凭据类型更改时调用。 |
| `credentials.create` | 创建新凭据时调用。 |
| `credentialsList.dialogVisibleChanged` |  |
| `dataDisplay.nodeTypeChanged` |  |
| `dataDisplay.onDocumentationUrlClick` | 选择帮助文档链接时调用。 |
| `execution.open` | 打开现有执行时调用。 |
| `executionsList.openDialog` | 从现有工作流执行中选择某次执行时调用。 |
| `expressionEdit.itemSelected` |  |
| `expressionEdit.dialogVisibleChanged` |  |
| `nodeCreateList.filteredNodeTypesComputed` |  |
| `nodeCreateList.nodeFilterChanged` | 对节点面板筛选器作出任何更改时调用。 |
| `nodeCreateList.selectedTypeChanged` |  |
| `nodeCreateList.mounted` |  |
| `nodeCreateList.destroyed` |  |
| `nodeSettings.credentialSelected` |  |
| `nodeSettings.valueChanged` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.addNodeButton` |  |
| `nodeView.mount` |  |
| `pushConnection.executionFinished` |  |
| `showMessage.showError` |  |
| `runData.displayModeChanged` |  |
| `workflow.activeChange` |  |
| `workflow.activeChangeCurrent` |  |
| `workflow.afterUpdate` | 更新现有工作流时调用。 |
| `workflow.open` |  |
| `workflowRun.runError` |  |
| `workflowRun.runWorkflow` | 工作流执行时调用。 |
| `workflowSettings.dialogVisibleChanged` |  |
| `workflowSettings.saveSettings` | 保存工作流设置时调用。 |

### 注册前端钩子 <a href="#registering-frontend-hooks" id="registering-frontend-hooks"></a>

可以通过在页面中加载钩子脚本来设置钩子。一种方式是在项目中创建钩子文件，并在 `editor-ui/public/index.html` 文件中添加 script 标签：

```html
<script src="frontend-hooks.js"></script>
```

### 前端钩子文件 <a href="#frontend-hook-files" id="frontend-hook-files"></a>

前端外部钩子文件是采用以下格式的普通 JavaScript 文件：

```js
window.n8nExternalHooks = {
  nodeView: {
    mount: [
      function (store, meta) {
        // do something
      },
    ],
    createNodeActiveChanged: [
      function (store, meta) {
        // do something
      },
      function (store, meta) {
        // do something else
      },
    ],
    addNodeButton: [
      function (store, meta) {
        // do something
      },
    ],
  },
};
```

### 前端钩子函数 <a href="#frontend-hook-functions" id="frontend-hook-functions"></a>

每个钩子可以定义多个钩子函数。n8n 调用各函数时传入以下参数：

* `store`：Vuex store 对象，可用于修改或获取 store 中的数据。
* `metadata`：包含钩子提供的全部数据的对象。要查看传入内容，请在 `editor-ui` 包中搜索该钩子。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
