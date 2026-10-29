---
description: 使用节点类型策略，控制用户在实例或项目中可以添加、发布和运行的节点。
status: preview
tags:
- tag: preview
  primary: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 通过节点类型策略控制节点可用性 <a id="control-node-availability-with-node-type-policies"></a>

节点类型策略是一组规则，用于决定整个实例或某个项目中的用户可以使用哪些节点。

{% hint style="info" %}
**预览状态**

节点类型策略处于预览阶段，未来版本可能更改，请避免在生产环境中依赖此功能。
{% endhint %}

{% hint style="info" %}
**功能可用范围**

节点类型策略可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 2.45.0 起提供节点类型策略。
{% endhint %}

实例所有者或管理员设置实例策略，项目管理员可以进一步限制自己的项目。通过 [n8n 公共 API](../../connect/n8n-api/node-type-policy.md)管理策略。

## 节点类型策略的工作原理 <a id="how-node-type-policies-work"></a>

一个策略包含规则列表和默认动作。

每条规则包含：

- `id`：规则名称，在策略内唯一。规则阻止节点时，n8n 会报告此 ID。
- `action`：`allow`、`deny` 或 `delegate`。只有实例策略接受 `delegate`。
- `selector`：此规则匹配的节点。

选择器通过以下两种方式之一匹配节点：

| 选择器 | 匹配内容 | 示例 |
|----------|---------|---------|
| `{ "kind": "name", "value": "<node-type>" }` | 按精确名称匹配一种节点类型。 | `n8n-nodes-base.executeCommand` |
| `{ "kind": "package", "value": "<package-name>" }` | 某个包中的全部节点。 | `n8n-nodes-base`、`@n8n/n8n-nodes-langchain` |

n8n 按顺序检查规则，使用首条匹配的规则。没有匹配时，使用策略的 `defaultAction`。

要查找节点类型名称，请在画布上选中节点并复制，粘贴到文本编辑器，查看 `type` 字段。

`name` 规则也匹配该节点的工具版本。例如，针对 `n8n-nodes-base.gmail` 的规则也会阻止 AI 智能体使用的 **Gmail Tool**。

### 实例与项目策略如何组合 <a id="how-instance-and-project-policies-combine"></a>

n8n 先评估实例策略，再评估项目策略：

| 实例判定 | 结果 |
|------------------|--------|
| `deny` | 节点被阻止，项目无法再次允许。 |
| `allow` | 由项目策略决定，项目只能进一步限制。 |
| `delegate` | 节点被阻止，除非项目有针对它的显式 `allow` 规则。项目的 `defaultAction` 不算。 |

如果希望某节点默认被阻止，但允许项目管理员为自己的项目启用，请使用 `delegate`。只有实例策略接受 `delegate`。

未配置任何策略时，所有节点都可用。

使用策略可以在项目级别阻止节点，同时保留安装。在自托管实例上，使用 [`NODES_EXCLUDE`](../../deploy/host-n8n/configure-n8n/security/block-specific-nodes.md) 可从整个实例中移除节点。

## 通过 API 设置策略 <a id="set-a-policy-with-the-api"></a>

### 身份验证与权限 <a id="authentication-and-permissions"></a>

在 `X-N8N-API-KEY` 标头中发送 API 密钥，该密钥需要 `nodeTypePolicy:manage` 权限范围。参阅[创建 API 密钥](../../connect/n8n-api/authentication.md#create-an-api-key)。

| 端点 | 可调用者 |
|----------|-----------------|
| `GET` 和 `PUT /api/v1/node-type-policies/instance` | 实例所有者和管理员。 |
| `GET` 和 `PUT /api/v1/node-type-policies/projects/<project-id>` | 实例所有者、实例管理员，以及该项目的管理员。 |

要查找项目 ID，请在 n8n 中打开项目。URL 中 `/projects/` 后的部分即为 ID。

### 读取、修改，再写入策略 <a id="read-change-then-write-the-policy"></a>

每个策略都有 `version`。`PUT` 必须发送最近读取的版本，避免两名管理员相互覆盖更改。

要更改策略：

1. 使用 `GET` 读取[实例](../../connect/n8n-api/node-type-policy.md#preview-retrieve-the-instance-node-type-policy)或[项目](../../connect/n8n-api/node-type-policy.md#preview-retrieve-a-projects-node-type-policy)的当前策略。
2. 修改 `rules` 或 `defaultAction`。
3. 使用 `PUT`，将完整策略写回[实例](../../connect/n8n-api/node-type-policy.md#preview-replace-the-instance-node-type-policy)或[项目](../../connect/n8n-api/node-type-policy.md#preview-replace-a-projects-node-type-policy)，携带相同的 `version`。

尚未设置过的策略返回 `version: 0`，因此首次 `PUT` 发送 `0`。读取后如果有人更改策略，n8n 返回 `409 Conflict`，请重新读取后重试。

如果某个作用域附加了多个策略，或其策略与其他作用域共享，`PUT` 也会返回 `409 Conflict`。此时应更新共享策略或作用域的附加关系。参阅[跨作用域共享同一策略](#share-one-policy-across-scopes)。

`PUT` 会替换策略中的全部规则。要添加一条规则，请发送现有规则加新规则。

### 示例：为整个实例阻止节点 <a id="example-block-nodes-for-the-whole-instance"></a>

此实例策略阻止 **Execute Command** 节点，并允许项目管理员为自己的项目启用 **SSH** 节点。使用 [`PUT /node-type-policies/instance`](../../connect/n8n-api/node-type-policy.md#preview-replace-the-instance-node-type-policy) 发送，并携带当前 `version`：

```json
{
	"version": 0,
	"defaultAction": "allow",
	"rules": [
		{
			"id": "block-execute-command",
			"action": "deny",
			"selector": { "kind": "name", "value": "n8n-nodes-base.executeCommand" }
		},
		{
			"id": "ssh-on-request",
			"action": "delegate",
			"selector": { "kind": "name", "value": "n8n-nodes-base.ssh" }
		}
	]
}
```

响应返回已保存策略及新的 `version`，也可能包含 `warnings`，列出已被前面规则覆盖的规则。n8n 永远不会执行到这些规则。更改大约在一秒内生效。

### 示例：在某个项目启用委托节点 <a id="example-turn-on-a-delegated-node-in-one-project"></a>

上方实例策略委托了 **SSH** 节点。以下项目策略为一个项目启用它。使用 [`PUT /node-type-policies/projects/<project-id>`](../../connect/n8n-api/node-type-policy.md#preview-replace-a-projects-node-type-policy) 发送，并携带当前 `version`：

```json
{
	"version": 0,
	"defaultAction": "allow",
	"rules": [
		{
			"id": "allow-ssh",
			"action": "allow",
			"selector": { "kind": "name", "value": "n8n-nodes-base.ssh" }
		}
	]
}
```

必须有 `allow` 规则。项目的 `defaultAction: allow` 不会启用被委托的节点。

### 跨作用域共享同一策略 <a id="share-one-policy-across-scopes"></a>

`/node-type-policies/policies` 和 `/node-type-policies/scopes/<scope-id>/attachments` 端点允许实例管理员在多个项目中复用同一组规则。大多数部署不需要。对附加关系端点执行 `GET`，会返回附加的策略，以及 `version`，供 `PUT` 使用。详情请参阅[端点参考](../../connect/n8n-api/node-type-policy.md)。

## 编辑器中节点被阻止时用户会看到什么 <a id="what-users-see-when-a-node-is-blocked-in-the-editor"></a>

项目中的节点被阻止时，该项目用户会看到：

- **节点面板**：浏览时不显示被阻止节点。搜索时仍会出现，位于列表末尾并带锁图标，用户无法添加。
- **画布**：工作流中已有的被阻止节点显示受限标签。
- **节点详情**：参数只读，用户可以联系实例管理员或替换节点。
- **发布和运行**：n8n 拒绝操作，显示列出全部被阻止节点的消息，并提供在工作流中定位节点的链接。如果保存操作添加了被阻止节点，n8n 也以相同方式拒绝保存。

## 智能体中节点被阻止时用户会看到什么 <a id="what-users-see-when-a-node-is-blocked-in-agents"></a>

- **工具选择器**：被阻止节点显示在列表末尾，带锁图标，无法添加。Chat Hub 工具也相同。
- **聊天**：n8n 拒绝调用被阻止工具，将步骤标为受限。智能体告知用户哪些操作无法完成。
- **保存和发布**：n8n 拒绝保存添加了被阻止工具的智能体，也拒绝发布使用此工具的智能体。
- **AI 构建器**：**Agent Builder** 可能建议被阻止节点，但 n8n 随后会拒绝保存。具有预览访问权限的 Enterprise 客户使用 n8n Assistant 时也相同。

## 已使用被阻止节点的工作流 <a id="workflows-that-already-use-a-blocked-node"></a>

新策略不修改现有工作流，但会限制用户能进行的操作：

| 操作 | 结果 |
|--------|--------|
| 打开和编辑 | 允许。 |
| 保存 | 允许，前提是未添加新的被阻止节点类型。 |
| 发布 | 拒绝。 |
| 运行，包括触发器触发或作为子工作流 | 拒绝，n8n 记录为失败执行。 |
| 移动到其他项目 | 根据目标项目策略检查。 |

已发布的工作流保持发布状态，但执行会失败，直到允许该节点或将其移出工作流。

已禁用节点仍计入检查。用户无法先以禁用状态添加被阻止节点，再于之后启用。

## 限制 <a id="limitations"></a>

- **尚无设置页面**：目前仅通过公共 API 管理策略，计划提供设置页面。
- **不支持通配符**：`name` 规则精确匹配一种节点类型。要匹配多个节点，请使用 `package` 规则。
- **`package` 规则要求包已安装**：n8n 拒绝针对未安装包的 `package` 规则。`name` 规则没有此限制，因此可以在任何人安装社区节点前，预先阻止它。
- **没有节点豁免**：策略默认拒绝时，也会阻止 **Manual Trigger** 和 **Sticky Note** 等节点。请为用户所需的每个节点添加 `allow` 规则。
- **不是数据边界**：阻止节点不代表阻止其背后的服务。用户仍可通过 **HTTP Request** 或 **Code** 节点访问相同 API。自托管实例要完全阻止 n8n 加载某个节点，请使用 [`NODES_EXCLUDE`](../../deploy/host-n8n/configure-n8n/security/block-specific-nodes.md)。
- **源代码管理拉取**：n8n 跳过使用被阻止节点的拉取工作流，并在拉取结果中报告。Git 与 n8n 中的工作流会保持不同，直到允许该节点或将其移除。
- **节点参数内的子工作流**：n8n 不检查在其他节点参数内定义的子工作流中的节点。

## 相关资源 <a id="related-resources"></a>

* [管理用户与访问](./)
* [设置 Cloud 用户管理](set-up-for-cloud.md)
* [添加和移除用户](add-and-remove-users.md)
* [理解实例角色](understand-instance-roles.md)
* [设置权限与角色（RBAC）](set-permissions-and-roles-rbac/README.md)
* [验证用户身份](verify-user-identity/README.md)
* [遵循最佳实践](follow-best-practices.md)
* [使用项目组织工作](set-permissions-and-roles-rbac/organize-work-in-projects.md)
* [阻止特定节点](../../deploy/host-n8n/configure-n8n/security/block-specific-nodes.md)
* [端点参考](../../connect/n8n-api/node-type-policy.md)
