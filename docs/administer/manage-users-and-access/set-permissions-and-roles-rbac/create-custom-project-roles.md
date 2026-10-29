---
title: 自定义项目角色
description: 在 n8n 中创建和管理具有细粒度权限的自定义项目角色。
contentType: howto
nodeTitle: 创建自定义角色
originalFilePath: user-management/rbac/custom-roles.md
originalUrl: https://docs.n8n.io/user-management/rbac/custom-roles
url: https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-project-roles
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自定义项目角色 <a href="#custom-project-roles" id="custom-project-roles"></a>

{% hint style="info" %}
**功能可用范围**

自定义项目角色可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 1.122.0 起提供。
{% endhint %}

{% hint style="info" %}
**实例角色与项目角色**

n8n 有两类自定义角色：

**自定义实例角色**：与用户在实例级别所需的管理能力相关的角色。参阅[创建自定义实例角色](create-custom-instance-roles.md)。

**自定义项目角色**：适用于特定项目内的角色。
{% endhint %}

自定义项目角色允许按团队需求创建具有特定权限的角色。不同于 Admin、Editor、Viewer 等内置项目角色，自定义角色可以为工作流、凭据和其他项目资源定义细粒度访问权限。

## 创建自定义角色 <a href="#create-a-custom-role" id="create-a-custom-role"></a>

实例所有者和实例管理员可以创建自定义角色。

要创建自定义角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Project roles**（项目角色）。
2. 选择 **Create role**（创建角色）。
3. 输入角色名称，以及可选描述。
4. 为此角色选择权限范围：
	* **工作流权限**：查看、执行、编辑、创建、发布、转移、删除工作流，或管理工作流数据脱敏。
	* **凭据权限**：查看、编辑、创建、共享、取消共享、转移或删除凭据。
	* **项目权限**：查看、编辑或删除项目。
	* **文件夹权限**：查看、编辑、创建、转移或删除文件夹。
	* **执行权限**：查看脱敏前的原始执行数据。
	* **密钥保管库权限**：查看、创建、编辑、删除或同步项目密钥保管库。
	* **密钥权限**：在凭据中使用密钥。
	* **数据表权限**：查看表、查看行、编辑表、编辑行、创建或删除表。
	* **项目变量权限**：查看、编辑、创建或删除项目变量。
	* **源代码管理**：推送到源代码管理。
5. 选择 **Create role**（创建角色）。

## 将自定义角色分配给用户 <a href="#assign-a-custom-role-to-users" id="assign-a-custom-role-to-users"></a>

项目管理员可以为项目成员分配自定义角色。角色仅适用于所分配的特定项目，同一用户可在不同项目中拥有不同角色。

要分配自定义角色：

1. 选择项目。
2. 选择 **Project settings**（项目设置）。
3. 在 **Project members**（项目成员）下浏览或搜索用户。
4. 选择用户，并从下拉菜单选择自定义角色。
5. 选择 **Save**（保存）。

{% hint style="info" %}
**项目级权限**

自定义角色权限仅在使用该角色的项目中生效。要在多个项目授予相同权限，请在每个项目分别分配此自定义角色。
{% endhint %}

## 编辑自定义角色 <a href="#edit-a-custom-role" id="edit-a-custom-role"></a>

要更新现有自定义角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Project roles**（项目角色）。
2. 找到要编辑的自定义角色。
3. 选择**三点菜单** > **Edit**（编辑）。
4. 更新角色名称、描述或权限。
5. 选择 **Save changes**（保存更改）。

{% hint style="warning" %}
**编辑会影响所有已分配此角色的用户**

更改自定义角色，会对任意项目中所有具有此角色的用户生效。如果多个项目使用此角色，权限更改会应用到所有分配位置。
{% endhint %}

## 复制自定义角色 <a href="#duplicate-a-custom-role" id="duplicate-a-custom-role"></a>

要基于现有角色创建新角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Project roles**（项目角色）。
2. 找到要复制的角色。
3. 选择**三点菜单** > **Duplicate**（复制）。
4. 按需更新角色名称和权限。
5. 选择 **Create role**（创建角色）。

## 删除自定义角色 <a href="#delete-a-custom-role" id="delete-a-custom-role"></a>

要删除自定义角色：

1. 前往 **Settings**（设置）> **Roles**（角色）> **Project roles**（项目角色）。
2. 找到要删除的角色。
3. 选择**三点菜单** > **Delete**（删除）。
4. 确认删除。

{% hint style="info" %}
**删除前请重新分配用户角色**

如果有用户被分配此角色，必须先为其重新分配其他角色，才能删除。
{% endhint %}

## 权限范围参考 <a href="#permission-scopes-reference" id="permission-scopes-reference"></a>

自定义角色通过权限范围定义用户在项目内能执行的操作。下列每个范围都对应 **Project roles**（项目角色）编辑器中的复选框。章节标题与编辑器分区名称对应，范围代码会出现在 API 响应和审计日志中。

{% hint style="info" %}
**自动授予的范围**

n8n 会将部分范围配对授予，因此不会显示为独立复选框：

* 授予 `<resource>:read` 时，也会授予该资源对应的列表范围，例如 `workflow:read` 同时授予 `workflow:list`。
* 授予 `workflow:publish` 时，也会授予 `workflow:unpublish`。
{% endhint %}

### 工作流范围 <a href="#workflow-scopes" id="workflow-scopes"></a>
* `workflow:create` - 创建新工作流。
* `workflow:read` - 查看工作流详情。
* `workflow:update` - 编辑工作流。
* `workflow:execute` - 执行工作流。
* `workflow:publish` - 发布工作流，同时授予 `workflow:unpublish`。
* `workflow:delete` - 删除工作流。
* `workflow:move` - 在项目之间转移工作流。
* `workflow:enableRedaction` - 启用工作流数据脱敏，参阅[执行数据脱敏](../../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md)。
* `workflow:disableRedaction` - 关闭工作流数据脱敏，参阅[执行数据脱敏](../../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md)。

### 凭据范围 <a href="#credential-scopes" id="credential-scopes"></a>
* `credential:create` - 创建新凭据。
* `credential:read` - 查看凭据详情。
* `credential:update` - 编辑凭据。
* `credential:delete` - 删除凭据。
* `credential:move` - 在项目之间转移凭据。
* `credential:share` - 将凭据共享给其他用户。
* `credential:unshare` - 取消凭据共享。

### 项目范围 <a href="#project-scopes" id="project-scopes"></a>
* `project:read` - 查看项目详情。
* `project:update` - 编辑项目设置。
* `project:delete` - 删除项目。

### 文件夹范围 <a href="#folder-scopes" id="folder-scopes"></a>
* `folder:create` - 创建新文件夹。
* `folder:read` - 查看文件夹内容。
* `folder:update` - 重命名文件夹。
* `folder:delete` - 删除文件夹。
* `folder:move` - 转移文件夹。

### 执行范围 <a href="#execution-scopes" id="execution-scopes"></a>
* `execution:reveal` - 查看脱敏前的原始执行数据，参阅[执行数据脱敏](../../../deploy/host-n8n/configure-n8n/security/redact-execution-data.md)。

### 密钥保管库范围 <a href="#secret-vault-scopes" id="secret-vault-scopes"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.13.0 起提供密钥保管库范围。
{% endhint %}

范围代码使用 `externalSecretsProvider` 前缀，角色编辑器中的对应分区为 **Secrets vaults**（密钥保管库）。

* `externalSecretsProvider:create` - 在项目中创建新密钥保管库。
* `externalSecretsProvider:read` - 查看项目中的密钥保管库。
* `externalSecretsProvider:update` - 编辑密钥保管库配置。
* `externalSecretsProvider:delete` - 从项目删除密钥保管库。
* `externalSecretsProvider:sync` - 重新加载保管库密钥。

### 密钥范围 <a href="#secrets-scope" id="secrets-scope"></a>
范围代码使用 `externalSecret` 前缀，角色编辑器中的对应分区为 **Secrets**（密钥）。

* `externalSecret:list` - 在凭据中使用密钥。

### 数据表范围 <a href="#data-table-scopes" id="data-table-scopes"></a>
* `dataTable:create` - 创建新数据表。
* `dataTable:read` - 查看数据表结构。
* `dataTable:update` - 编辑数据表结构。
* `dataTable:delete` - 删除数据表。
* `dataTable:readRow` - 读取数据表中的行。
* `dataTable:writeRow` - 插入或更新数据表中的行。

### 项目变量范围 <a href="#project-variable-scopes" id="project-variable-scopes"></a>
* `projectVariable:create` - 创建新变量。
* `projectVariable:read` - 查看变量值。
* `projectVariable:update` - 编辑变量值。
* `projectVariable:delete` - 删除变量。

### 源代码管理范围 <a href="#source-control-scopes" id="source-control-scopes"></a>
* `sourceControl:push` - 将更改推送到源代码管理。

## 常见自定义角色示例 <a href="#common-custom-role-examples" id="common-custom-role-examples"></a>

以下是针对常见场景可创建的自定义项目角色示例。它们适用于单个项目，而非整个 n8n 实例。

### 工作流开发者 <a href="#workflow-developer" id="workflow-developer"></a>
适合只处理工作流的用户：
* `workflow:create`, `workflow:read`, `workflow:update`, `workflow:execute`, `workflow:delete`
* `credential:read`，查看凭据，但不能编辑。
* `project:read`

### 凭据管理员 <a href="#credential-manager" id="credential-manager"></a>
适合管理凭据的用户：
* `credential:create`, `credential:read`, `credential:update`, `credential:delete`, `credential:share`
* `workflow:read`，查看工作流，以了解凭据使用情况。
* `project:read`

### 密钥使用者 <a href="#secrets-user" id="secrets-user"></a>
适合在凭据中使用外部密钥，但不管理保管库的用户：
* `externalSecret:list`，在凭据表达式中使用密钥。
* `credential:create`、`credential:read`、`credential:update`，管理包含密钥的凭据。
* `workflow:read`
* `project:read`

### 工作流发布者 <a href="#workflow-publisher" id="workflow-publisher"></a>
适合能够发布工作流，但不具有完整编辑权限的用户：
* `workflow:read`, `workflow:publish`
* `credential:read`
* `project:read`

{% hint style="info" %}
**组合权限范围**

可以组合任意权限范围，创建符合需求的角色。应遵循最小权限原则，仅授予用户完成任务所需的权限。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [自定义角色](create-custom-roles.md)
* [创建自定义实例角色](create-custom-instance-roles.md)
