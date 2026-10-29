---
title: n8n 节点
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.n8n.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n
description: 了解 n8n 中 n8n 管理节点的用法，并查看相关示例。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n <a id="n8n"></a>

此节点与 n8n 本身集成，可在工作流中调用 [n8n API](../../../connect/n8n-api/README.md)。

使用 n8n API 的更多信息，请参阅 [n8n REST API 文档](../../../connect/n8n-api/README.md)；要直接调用端点，请参阅 [API 端点参考](../../../connect/n8n-api/api-reference.md)。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [API 身份验证文档](../../../connect/n8n-api/authentication.md)。
{% endhint %}

{% hint style="warning" %}
**SSL**

译注：原文“不支持 SSL”的说法过于宽泛，同版本 API 认证文档为 n8n 节点提供了 HTTPS Base URL，不能据此认为该节点不能访问 HTTPS。需要为请求提供 SSL 证书时，可使用 [HTTP Request 节点](n8n-nodes-base.httprequest/README.md)调用 [n8n API](../../../connect/n8n-api/README.md)，并通过其选项[提供 SSL 证书](../credentials/httprequest.md#provide-an-ssl-certificate)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Audit（审计）
  * [**Generate**（生成）安全审计](n8n-nodes-base.n8n.md#generate-audit)
* Credential（凭据）
  * [**Create**（创建）凭据](n8n-nodes-base.n8n.md#create-credential)
  * [**Delete**（删除）凭据](n8n-nodes-base.n8n.md#delete-credential)
  * [**Get Schema**](n8n-nodes-base.n8n.md#get-credential-schema)（获取 schema）：获取指定凭据类型的数据 schema。
* Execution（执行）
  * [**Get**（获取）一次执行](n8n-nodes-base.n8n.md#get-execution)
  * [**Get Many**（获取多个）执行](n8n-nodes-base.n8n.md#get-many-executions)
  * [**Delete**（删除）一次执行](n8n-nodes-base.n8n.md#delete-execution)
* Workflow（工作流）
  * [**Publish**（发布）工作流](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Create**（创建）工作流](n8n-nodes-base.n8n.md#create-workflow)
  * [**Unpublish**（取消发布）工作流](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Delete**（删除）工作流](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Get**（获取）工作流](n8n-nodes-base.n8n.md#activate-deactivate-delete-and-get-workflow)
  * [**Get Many**（获取多个）工作流](n8n-nodes-base.n8n.md#get-many-workflows)
  * [**Update**（更新）工作流](n8n-nodes-base.n8n.md#update-workflow)

## 生成审计 <a href="#generate-audit" id="generate-audit"></a>

此操作没有参数，可配置以下选项：

* **Categories**（类别）：选择要纳入审计的风险类别：
  * **Credentials**（凭据）
  * **Database**（数据库）
  * **Filesystem**（文件系统）
  * **Instance**（实例）
  * **Nodes**（节点）
* **Days Abandoned Workflow**（工作流废弃判定天数）：设置连续多少天未执行后将工作流视为废弃，输入天数，默认为 `90`。

## 创建凭据 <a href="#create-credential" id="create-credential"></a>

使用以下参数配置此操作：

* **Name**（名称）：要创建的凭据名称。
* **Credential Type**（凭据类型）：可用类型取决于实例已安装的节点，内置类型包括 `githubApi`、`notionApi` 和 `slackApi`。
* **Data**（数据）：包含该 **Credential Type**（凭据类型）所需属性的有效 JSON 对象。使用 **Get Schema**（获取 schema）操作查看格式要求。

## 删除凭据 <a href="#delete-credential" id="delete-credential"></a>

使用以下参数配置此操作：

* **Credential ID**（凭据 ID）：要删除的凭据 ID。

## 获取凭据 schema <a href="#get-credential-schema" id="get-credential-schema"></a>

使用以下参数配置此操作：

* **Credential Type**（凭据类型）：可用类型取决于实例已安装的节点，内置类型包括 `githubApi`、`notionApi` 和 `slackApi`。

## 获取一次执行 <a href="#get-execution" id="get-execution"></a>

使用以下参数配置此操作：

* **Execution ID**（执行 ID）：要获取的执行 ID。

### 获取执行的选项 <a href="#get-execution-option" id="get-execution-option"></a>

还可配置以下 **Option**（选项）：

* **Include Execution Details**（包含执行详情）：开启时包含详细执行数据，关闭时不包含。

## 获取多个执行 <a href="#get-many-executions" id="get-many-executions"></a>

使用以下参数配置此操作：

* **Return All**（返回全部）：开启时返回全部结果，关闭时按 **Limit**（数量上限）限制结果数量。
* **Limit**（数量上限）：关闭 **Return All**（返回全部）时，设置要返回的结果数量。

### 获取多个执行的筛选条件 <a href="#get-many-executions-filters" id="get-many-executions-filters"></a>

还可配置以下 **Filters**（筛选条件）：

* **Workflow**（工作流）：按工作流筛选执行：
  * **From list**（从列表选择）：选择工作流。
  * **By URL**（按 URL）：输入工作流 URL。
  * **By ID**（按 ID）：输入工作流 ID。
* **Status**（状态）：按执行状态筛选：
  * **Error**（错误）
  * **Success**（成功）
  * **Waiting**（等待）

### 获取多个执行的选项 <a href="#get-many-execution-options" id="get-many-execution-options"></a>

还可配置以下 **Option**（选项）：

* **Include Execution Details**（包含执行详情）：开启时包含详细执行数据，关闭时不包含。

## 删除执行 <a href="#delete-execution" id="delete-execution"></a>

使用以下参数配置此操作：

* **Execution ID**（执行 ID）：要删除的执行 ID。

## 发布、取消发布、删除和获取工作流 <a href="#activate-deactivate-delete-and-get-workflow" id="activate-deactivate-delete-and-get-workflow"></a>

**Publish**（发布）、**Unpublish**（取消发布）、**Delete**（删除）和 **Get**（获取）操作使用同一个 **Workflow**（工作流）参数选择目标，可选：

* **From list**（从列表选择）：从列表中选择工作流。
* **By URL**（按 URL）：输入工作流 URL。
* **By ID**（按 ID）：输入工作流 ID。

## 创建工作流 <a href="#create-workflow" id="create-workflow"></a>

使用以下参数配置此操作：

* **Workflow Object**（工作流对象）：输入包含新工作流详情的有效 JSON 对象，必须具有以下字段：
  * `name`
  * `nodes`
  * `connections`
  * `settings`

更多信息，请参阅 [n8n API 参考](../../../connect/n8n-api/api-reference.md)。

## 获取多个工作流 <a href="#get-many-workflows" id="get-many-workflows"></a>

使用以下参数配置此操作：

* **Return All**（返回全部）：开启时返回全部结果，关闭时按 **Limit**（数量上限）限制结果数量。
* **Limit**（数量上限）：关闭 **Return All**（返回全部）时，设置要返回的结果数量。

### 获取多个工作流的筛选条件 <a href="#get-many-workflows-filters" id="get-many-workflows-filters"></a>

还可配置以下 **Filters**（筛选条件）：

* **Return Only Published Workflows**（仅返回已发布工作流）：开启时只返回已发布工作流，关闭时同时返回已发布和未发布工作流。
* **Tags**（标签）：输入以逗号分隔的标签列表，返回的工作流必须具有这些标签。

## 更新工作流 <a href="#update-workflow" id="update-workflow"></a>

使用以下参数配置此操作：

* **Workflow**（工作流）：选择要更新的工作流：
  * **From list**（从列表选择）：从列表中选择工作流。
  * **By URL**（按 URL）：输入工作流 URL。
  * **By ID**（按 ID）：输入工作流 ID。
* **Workflow Object**（工作流对象）：输入用于更新工作流的有效 JSON 对象，必须具有以下字段：
  * `name`
  * `nodes`
  * `connections`
  * `settings`

更多信息，请参阅 [n8n API 的更新工作流文档](../../../connect/n8n-api/workflow.md#update-a-workflow)。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n 集成模板](https://n8n.io/integrations/n8n)，或[搜索所有模板](https://n8n.io/workflows/)
