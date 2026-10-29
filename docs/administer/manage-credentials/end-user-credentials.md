---
description: 让每个用户将自己的账号连接到凭据，使工作流使用触发者的凭据运行。
layout:
  description:
    visible: false
status: preview
tags:
- tag: preview
  primary: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 最终用户凭据 <a id="end-user-credentials"></a>

最终用户凭据使工作流使用触发者的凭据运行，而非固定凭据。项目管理员创建一个凭据模板，每个用户连接自己的账号。n8n 使用各用户已连接的账号，并保护其数据隐私。

固定凭据意味着所有运行工作流的人都使用同一账号，可能将某个人的访问权限和数据暴露给其他人。最终用户凭据为每个用户提供独立连接，并隔离执行数据。

{% hint style="info" %}
**功能可用范围**

最终用户凭据可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。
{% endhint %}

{% hint style="info" %}
**预览状态**

最终用户凭据处于预览阶段，未来版本可能更改。请勿在生产工作流中依赖此功能。
{% endhint %}

## 什么是最终用户凭据 <a id="what-are-end-user-credentials"></a>

创建或编辑凭据时，可以选择 **Credential type**（凭据类型）：

* **Fixed credential**（固定凭据）：无论谁运行工作流，都使用同一凭据，这是默认方式。
* **End-user credential**（最终用户凭据）：运行时使用各用户的凭据，仅该用户能查看和使用自己的凭据。

最终用户凭据是一个模板，创建者只需配置一次连接，例如 Gmail 的 OAuth 应用详情。每个有访问权限的用户通过此模板连接自己的账号。每个连接属于建立它的用户，只有该用户能使用，也只有该用户能看到连接返回的数据。

### 示例 <a id="example"></a>

构建一个手动触发的工作流，从 Gmail 读取消息，再向 Slack 发送摘要。为 Gmail 创建最终用户凭据模板。用户 A 运行时，n8n 读取 A 的收件箱；用户 B 运行时，读取 B 的收件箱。每个用户仅看到自己的数据。

## 工作原理 <a id="how-it-works"></a>

与往常一样，通过节点的凭据下拉菜单选择凭据，无需额外节点设置。节点行为取决于凭据类型：

* 使用固定凭据时，节点行为与之前相同。
* 使用最终用户凭据时，节点显示使用触发者账号；尚未连接的用户会收到连接提示。

运行时，n8n 将凭据解析为触发工作流用户已连接的账号。每个有工作流访问权限的用户，都在自身身份上下文中查看节点。已连接账号时使用该连接运行，未连接时必须先连接才能触发工作流。

同一工作流的不同节点可以混用固定凭据和最终用户凭据。例如，用最终用户凭据读取各用户个人 Google Calendar，再通过使用固定凭据的团队共享 Slack 账号发送结果。

## 要求与限制 <a id="requirements-and-limitations"></a>

* **仅限 Enterprise**：最终用户凭据需要 Enterprise 套餐。
* **受控创建**：默认仅[项目管理员](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md)可创建最终用户凭据，可通过[自定义角色](../manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md)授予其他用户权限。限制创建者有助于集中管理凭据：管理员只需配置一次模板，再共享到所需项目，而非让大量用户各自配置。
* **仅限团队项目**：只能在团队项目创建最终用户凭据，不能在个人项目创建，以便由管理员集中配置凭据模板，避免个人用户在个人项目中各自创建。
* **仅限 OAuth 凭据**：最终用户凭据仅支持基于 OAuth 的凭据类型。
* **每个用户一个连接**：对于每个最终用户凭据模板，每个用户只能连接一个账号。
* **支持的触发器**：最终用户凭据解析适用于手动触发器、[Chat Hub](../../build/ways-of-building-workflows/chat-hub.md)、MCP Server Trigger、[Webhook 触发器](../../integrations/builtin/core-nodes/n8n-nodes-base.webhook/README.md)、[n8n Form Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md) 和 [Chat Trigger](../../integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/README.md)。Chat Trigger 仅支持 **Hosted Chat**（托管聊天），不支持 Embedded Chat/webhook 模式。Webhook、Form Trigger 和 Chat Trigger 使用 **n8n User Auth** 身份验证时，会解析最终用户凭据，让每个用户以自己的已连接账号运行工作流。Webhook 节点中，此选项名为 **n8n User Auth (OAuth2)**。

## 创建最终用户凭据 <a id="create-an-end-user-credential"></a>

1. 创建凭据，或打开现有凭据。
2. 在 **Credential type**（凭据类型）下，选择 **End-user credential**（最终用户凭据）。
3. 配置连接。对于 OAuth 凭据，填写 **Client ID**（客户端 ID）、**Client Secret**（客户端密钥）和用于向服务注册的 **OAuth Redirect URL**（OAuth 重定向 URL）。
4. 选择 **Save**（保存）。

现在用户可将自己的账号连接到此凭据。用户运行使用该凭据的工作流时，若尚未连接，n8n 会提示连接。有项目访问权限的用户，也可提前在界面中，通过打开画布节点或项目 **Credentials**（凭据）列表完成连接。

{% hint style="info" %}
MCP Server Trigger、Webhook、Chat Trigger 和 Form Trigger 等部分触发器节点，允许要求触发者具有执行触发器的权限。启用后，只有具有允许执行工作流的项目角色的用户才能触发。没有该角色的用户无法连接账号。
{% endhint %}

## 连接账号 <a id="connect-your-account"></a>

在工作流中使用最终用户凭据前，需要将账号连接到模板。可通过以下位置操作：

* **节点**：打开使用最终用户凭据的节点时，会显示账号是否已连接。尚未连接时，选择 **Connect**（连接）。
* **凭据**：打开最终用户凭据，在凭据弹窗中连接账号。
* **凭据列表**：项目 **Credentials**（凭据）列表中的最终用户凭据卡片提供 **Connect**（连接）选项。

为账号完成 OAuth 流程。连接后，节点显示账号，例如 **Connected as you@example.com**（已连接为 you@example.com）。

连接是私有的。其他用户向同一模板连接自己的账号，绝不会使用你的账号。

## 执行数据与隐私 <a id="execution-data-and-privacy"></a>

工作流执行使用最终用户凭据时，有权访问该工作流执行的任何人，仍可查看执行元数据，包括状态、运行时间和使用了最终用户凭据这一事实。变化在于谁能查看内部数据。

只有使用自己已连接账号触发工作流的用户，才能查看相关节点的输入和输出数据，包括连接服务返回的数据。对其他所有人，包括实例管理员，这些节点均显示脱敏后的输出。

### 管理员可见范围 <a id="admin-visibility"></a>

管理员可以看到最终用户凭据模板存在，且有连接附加其上。例如，删除最终用户凭据时，管理员会看到附加的用户连接数量，仅此而已，不能：

* 查看任何单个连接的信息。
* 查看连接中的密钥。
* 在自己的工作流中使用任何其他人的已连接账号。
* 查看通过其他用户连接运行的执行的脱敏前输出。

共享方式与普通凭据相同，但仅共享模板，不共享已连接账号。管理员可将模板共享给其他项目或用户，各接收者自行连接账号。

{% hint style="warning" %}
**删除最终用户凭据会移除全部连接**

删除凭据模板会删除整个凭据，包括每个用户的连接，而非仅删除你自己的。依赖它的工作流将无法为这些用户解析凭据，直到重新配置凭据并重新连接。删除已有连接附加的最终用户凭据之前，n8n 会发出警告。
{% endhint %}

## 跨项目共享最终用户凭据 <a id="share-end-user-credentials-across-projects"></a>

使用标准[凭据共享](share-credentials-securely.md)机制，将最终用户凭据共享到其他项目。共享的是模板，而非连接。其他项目的用户会看到连接自己账号的选项，不会获得原所有者的连接。

每个用户对同一模板仅需连接一次，该连接会在模板共享到的所有项目中为其解析，无需逐项目重新连接。

一种良好做法是在单个项目集中创建最终用户凭据，例如 Gmail、Linear、Jira 和 Google Sheets，再共享到其他所需项目。每个项目获得同一模板，各用户的单个连接可跨所有项目使用。

## 相关资源 <a id="related-resources"></a>

* [管理凭据](./)
* [安全共享凭据](share-credentials-securely.md)
* [凭据覆盖](credential-overwrites.md)
* [使用外部密钥存储](use-external-secret-stores.md)
* [创建和编辑凭据](../../build/understand-workflows/create-and-edit-credentials.md)
* [RBAC 角色类型](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md)
