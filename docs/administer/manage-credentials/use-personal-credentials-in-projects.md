---
description: 在团队项目中使用个人凭据，了解谁能查看、使用和编辑凭据，以及工作流运行代表谁操作。
hidden: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在项目中使用个人凭据 <a id="use-personal-credentials-in-projects"></a>

可以在所属的任意团队项目中使用个人凭据，无需共享。只有你和你共享的对象，才能使用这些凭据运行工作流。

本页说明凭据访问级别、个人凭据在团队项目中的行为、工作流使用他人凭据时队友看到的内容，以及运行代表谁操作。要向其他人或项目授予凭据访问权限，请参阅[安全共享凭据](share-credentials-securely.md)。

## 关键术语 <a id="key-terms"></a>

* **个人凭据**：位于个人空间中的凭据，或他人直接共享给你的凭据。
* **项目凭据**：团队项目持有的凭据，可以是在项目内创建的，也可以是他人共享给项目的。
* **实际操作用户**：工作流运行所代表的人。手动运行时，是选择 **Execute**（执行）的人；触发运行时，包括计划、webhook、应用事件等，是最后发布工作流的人。

## 凭据访问级别 <a id="levels-of-credential-access"></a>

凭据的 **Sharing**（共享）选项卡显示两个访问级别：

| 访问级别 | 可执行的操作 |
| ------------ | --------------- |
| **Can view**（可查看） | 查看凭据是否存在及使用位置，无法用它运行或发布任何内容。 |
| **Can use**（可使用） | 使用凭据运行和发布工作流，无法查看或更改凭据详情。 |

将凭据共享给某个人时，n8n 授予其 **Can use**（可使用）角色。要查看和更改详情，需要拥有凭据，或具有允许编辑全部凭据的[实例角色](../manage-users-and-access/understand-instance-roles.md)。对于团队项目持有的凭据，由[项目角色](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md)决定访问权限。

## 在团队项目中使用个人凭据 <a id="use-personal-credentials-in-team-projects"></a>

可以在所属任意团队项目的工作流中选择自己的个人凭据，无需先将凭据共享给项目。

打开节点的凭据选择器时，n8n 将可选凭据分组：

* **Available to you**（你可用的）：个人凭据。
* **Available in** _项目名称_（项目中可用的）：项目持有的凭据，以及实例中所有人可用的凭据。

个人空间中，第二组改为 **Available to everyone**（所有人可用的）。

只有你和你直接共享凭据的对象，才能在该项目中使用你的个人凭据运行工作流。其他项目成员能看到工作流使用了此凭据，但无法用它运行或发布工作流。要让整个项目使用，请[将凭据共享给项目](share-credentials-securely.md#share-a-credential)。

{% hint style="info" %}
**智能体仅使用项目凭据**

智能体，包括 AI 智能体和 Slack、Microsoft Teams 集成，目前不提供个人凭据选项，只能使用项目持有的凭据。
{% endhint %}

## 工作流使用你的凭据时，队友会看到什么 <a id="what-teammates-see-when-a-workflow-uses-your-credential"></a>

无法使用凭据的队友，会在节点上看到凭据名称和所有者，例如 **Jane's Slack account**（Jane 的 Slack 账号）。n8n 会为其禁用 **Execute**（执行）和 **Publish**（发布）。

要运行工作流，他们可以将节点改为使用自己的凭据，或请你共享凭据。

## 工作流运行代表谁操作 <a id="who-a-workflow-run-acts-as"></a>

每次运行都代表某个人，该用户必须能够使用工作流所需凭据。

* **手动运行**代表运行工作流的人。对于工作流项目未持有的每个凭据，该用户都必须具有使用权限。
* 已发布工作流的**触发运行**代表最后发布它的人。

项目持有的凭据可用于该项目中的每次运行。即使发布者自身的访问权限后来发生变化，计划运行仍能继续使用这些凭据。

不能发布使用了你无权使用凭据的工作流。发布检查会指出阻止发布的凭据。如果工作流失去发布者，例如发布者账号被删除，请重新发布，使其代表你运行。发布机制请参阅[保存和发布工作流](../../build/understand-workflows/save-and-publish-workflows.md)。

## 所有者和管理员的凭据访问权限 <a id="credential-access-for-owners-and-admins"></a>

实例所有者和管理员可以查看和共享实例上的全部凭据，但使用权限取决于工作流所在位置：

* **自己的个人空间中**：所有者和管理员可以使用任何凭据。凭据的 **Sharing**（共享）选项卡，会针对其个人空间显示 **Can use in personal space**（可在个人空间使用）。
* **团队项目中**：实例角色不允许他们使用未共享给项目的成员个人凭据。可以在节点上看到该凭据，但无法用它运行。

## 使用你无权使用凭据的执行数据 <a id="execution-data-from-credentials-you-cant-use"></a>

如果执行使用了你无权使用的凭据，n8n 会向你隐藏其数据，但执行状态和时间信息仍可见。即使父工作流本身未使用该凭据，从使用了该凭据的子工作流返回的数据也会隐藏。通过公共 API 或 n8n MCP 服务器读取的执行同样遵循这些规则。

## 相关资源 <a id="related-resources"></a>

* [管理凭据](./)
* [安全共享凭据](share-credentials-securely.md)
* [最终用户凭据](end-user-credentials.md)
* [凭据覆盖](credential-overwrites.md)
* [使用外部密钥存储](use-external-secret-stores.md)
* [使用项目组织工作](../manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)
