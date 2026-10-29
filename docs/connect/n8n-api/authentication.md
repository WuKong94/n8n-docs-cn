---
description: n8n 公共 REST API 的身份验证。
contentType: howto
nodeTitle: 身份验证
originalFilePath: api/authentication.md
originalUrl: https://docs.n8n.io/api/authentication
url: https://docs.n8n.io/connect/n8n-api/authentication
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# API 身份验证 <a href="#api-authentication" id="api-authentication"></a>

n8n 使用 API 密钥验证 API 调用。

{% hint style="info" %}
**功能可用范围**

免费试用期间无法使用 n8n API，请升级后使用此功能。
{% endhint %}

## 创建 API 密钥 <a href="#create-an-api-key" id="create-an-api-key"></a>

1. 登录 n8n。
1. 前往 **Settings**（设置）> **n8n API**。
1. 选择 **Create an API key**（创建 API 密钥）。
1. 为密钥设置 **Label**（标签）和 **Expiration**（过期时间）。
1. 如果使用 Enterprise 方案，选择要授予密钥的 **Scopes**（作用域）。完整列表请参阅 [API 作用域](#api-scopes)。
1. 复制 **My API Key**（我的 API 密钥），用它验证调用。

## 使用密钥调用 API <a href="#call-the-api-using-your-key" id="call-the-api-using-your-key"></a>

在 API 调用中，通过名为 `X-N8N-API-KEY` 的请求头发送 API 密钥。

例如，要获取所有活跃工作流，curl 请求如下：

```shell
# For a self-hosted n8n instance <a href="#for-a-self-hosted-n8n-instance" id="for-a-self-hosted-n8n-instance"></a>
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# For n8n Cloud <a href="#for-n8n-cloud" id="for-n8n-cloud"></a>
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

## 节点配置 <a href="#node-configuration" id="node-configuration"></a>

要在工作流中调用 n8n API，请使用 [n8n 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)。创建凭据时，填写以下字段：

- **API Key**（API 密钥）：粘贴在[创建 API 密钥](#create-an-api-key)中生成的密钥。
- **Base URL**（基础 URL）：使用以下格式之一填写实例的 API 根地址：
	- Cloud：`https://<name>.app.n8n.cloud/api/v1`，其中 `<name>` 是 Cloud 子域名。
	- 自托管：`https://<your-instance-url>/api/v1`。

可用操作和参数请参阅 [n8n 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)文档。

## 删除 API 密钥 <a href="#delete-an-api-key" id="delete-an-api-key"></a>

1. 登录 n8n。
2. 前往 **Settings**（设置）> **n8n API**。
3. 选择待删除密钥旁的 **Delete**（删除）。
4. 选择 **Delete Forever**（永久删除）进行确认。

## API 作用域 <a href="#api-scopes" id="api-scopes"></a>

在 [Enterprise 实例](https://n8n.io/enterprise/)中，可以使用作用域限制 API 密钥可访问的资源和操作。请为密钥的预定用途选择所需的最小作用域。

非 Enterprise 方案的 API 密钥具有该账号全部资源和功能的完整访问权限。

{% hint style="info" %}
**API 密钥作用域与项目角色作用域**

API 密钥作用域控制 API 密钥在实例级别能执行的操作，不同于定义项目内自定义角色所用的**项目角色作用域**。项目角色作用域请参阅[自定义项目角色](../../administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md)。
{% endhint %}

以下表格按资源列出创建受限 API 密钥时可用的作用域。

### 社区软件包作用域 <a href="#community-package-scopes" id="community-package-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `communityPackage:install` | 在实例上安装社区节点软件包。 |
| `communityPackage:list` | 列出已安装的社区节点软件包。 |
| `communityPackage:uninstall` | 卸载社区节点软件包。 |
| `communityPackage:update` | 更新已安装的社区节点软件包。 |

### 凭据作用域 <a href="#credential-scopes" id="credential-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `credential:create` | 创建凭据。 |
| `credential:read` | 获取凭据及其数据结构。 |
| `credential:list` | 列出凭据。 |
| `credential:update` | 更新凭据。 |
| `credential:delete` | 删除凭据。 |
| `credential:move` | 将凭据转移到其他项目。 |

### 数据表作用域 <a href="#data-table-scopes" id="data-table-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `dataTable:create` | 创建数据表。 |
| `dataTable:read` | 获取数据表。 |
| `dataTable:list` | 列出数据表。 |
| `dataTable:update` | 更新数据表元数据。 |
| `dataTable:delete` | 删除数据表。 |

### 数据表列作用域 <a href="#data-table-column-scopes" id="data-table-column-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `dataTableColumn:create` | 向数据表添加列。 |
| `dataTableColumn:read` | 获取数据表列。 |
| `dataTableColumn:update` | 更新数据表列。 |
| `dataTableColumn:delete` | 删除数据表列。 |

### 数据表行作用域 <a href="#data-table-row-scopes" id="data-table-row-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `dataTableRow:create` | 向数据表插入行。 |
| `dataTableRow:read` | 从数据表读取行。 |
| `dataTableRow:update` | 更新数据表中的已有行。 |
| `dataTableRow:delete` | 删除数据表中的行。 |
| `dataTableRow:upsert` | 更新数据表中的已有行；如果没有行匹配筛选条件，则插入新行。 |

### 执行作用域 <a href="#execution-scopes" id="execution-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `execution:read` | 获取执行及其详细信息。 |
| `execution:list` | 列出执行。 |
| `execution:retry` | 重试失败的执行。 |
| `execution:stop` | 停止正在运行的执行。 |
| `execution:delete` | 删除执行。 |

### 执行标签作用域 <a href="#execution-tags-scopes" id="execution-tags-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `executionTags:list` | 读取分配给执行的注释标签。 |
| `executionTags:update` | 更新分配给执行的注释标签。 |

### 文件夹作用域 <a href="#folder-scopes" id="folder-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `folder:create` | 在项目中创建文件夹。 |
| `folder:read` | 获取文件夹。 |
| `folder:list` | 列出项目中的文件夹。 |
| `folder:update` | 更新文件夹。 |
| `folder:delete` | 删除文件夹。 |

### Insights 作用域 <a href="#insights-scopes" id="insights-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `insights:read` | 读取实例 Insights 数据，包括执行次数、失败率、节省时间和平均运行时间。 |

### 项目作用域 <a href="#project-scopes" id="project-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `project:create` | 创建项目。 |
| `project:list` | 列出项目。 |
| `project:update` | 更新项目。 |
| `project:delete` | 删除项目。 |

### 安全审计作用域 <a href="#security-audit-scopes" id="security-audit-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `securityAudit:generate` | 为实例生成安全审计报告。 |

### 源代码管理作用域 <a href="#source-control-scopes" id="source-control-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `sourceControl:pull` | 从已连接的源代码管理仓库向实例拉取更改。 |

译注：本表只列出 sourceControl:pull，但同一版本“通过公共 API 以编程方式使用环境”指南还使用 sourceControl:read 和 sourceControl:push。此处保留原表并提示其列表差异；请结合目标实例支持的端点和作用域核对，不将本表视为全部源代码管理作用域的完整清单。

### 标签作用域 <a href="#tag-scopes" id="tag-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `tag:create` | 在全局标签注册表中创建标签。 |
| `tag:read` | 获取标签。 |
| `tag:list` | 列出标签。 |
| `tag:update` | 更新标签。 |
| `tag:delete` | 删除标签。 |

### 用户作用域 <a href="#user-scopes" id="user-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `user:create` | 在实例中邀请或创建用户。 |
| `user:read` | 获取用户。 |
| `user:list` | 列出用户。 |
| `user:changeRole` | 更改用户的全局（实例级）角色。 |
| `user:enforceMfa` | 保留作用域。没有 `/api/v1/` 端点使用它，因此在公共 API 密钥上选择此作用域不会影响公开接口。 |
| `user:delete` | 从实例删除用户。 |

### 变量作用域 <a href="#variable-scopes" id="variable-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `variable:create` | 创建实例变量。 |
| `variable:list` | 列出实例变量。 |
| `variable:update` | 更新实例变量。 |
| `variable:delete` | 删除实例变量。 |

### 工作流作用域 <a href="#workflow-scopes" id="workflow-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `workflow:create` | 创建工作流。 |
| `workflow:read` | 获取工作流及其详细信息。 |
| `workflow:list` | 列出工作流。 |
| `workflow:update` | 更新工作流。 |
| `workflow:delete` | 删除、归档或取消归档工作流。 |
| `workflow:move` | 将工作流转移到其他项目。 |
| `workflow:activate` | 激活或停用工作流。在公共 API 中也称为“发布/取消发布”（`/workflows/{id}/activate` 和 `/workflows/{id}/deactivate`）。 |

### 工作流标签作用域 <a href="#workflow-tags-scopes" id="workflow-tags-scopes"></a>

| 作用域 | 说明 |
|-------|-------------|
| `workflowTags:list` | 读取分配给工作流的标签。 |
| `workflowTags:update` | 更新分配给工作流的标签。 |

## 相关资源 <a id="related-resources"></a>

* [n8n API](./)
* [分页](pagination.md)
* [幂等性](idempotency.md)
* [使用 API 测试台](use-an-api-playground.md)
* [端点参考](api-reference.md)

