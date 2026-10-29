---
description: 了解如何在 n8n 中使用 Databricks Lakebase Chat Memory 节点，并按照技术文档将其集成到工作流中。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Databricks Lakebase Chat Memory（Databricks Lakebase 聊天记忆） 节点 <a id="databricks-lakebase-chat-memory-node"></a>

使用 Databricks Lakebase Chat Memory 节点，将聊天历史存储在 Databricks Lakebase 表中，作为 AI 智能体的记忆[^1]。节点通过 [Lakebase Data API](https://docs.databricks.com/aws/en/oltp/projects/data-api) 读写该表，因此无需连接字符串或数据库驱动。

本页介绍一次性的建表设置、节点参数、如何共享会话、相关资源及常见问题。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Databricks 凭据文档](../../credentials/databricks.md)。节点仅接受 Databricks OAuth2 凭据，使用[用户登录](../../credentials/databricks.md#using-oauth2-with-user-login)或[服务主体](../../credentials/databricks.md#using-oauth2-service-principal)。项目所有者不能使用 Data API，因此应使用不拥有该 Lakebase 项目的身份进行验证。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md" %}

## 创建表 <a id="create-the-table"></a>

与 [Postgres Chat Memory](n8n-nodes-langchain.memorypostgreschat.md) 节点不同，此节点不会自动创建表。Data API 无法运行 `CREATE TABLE`，因此首次执行前，需要在 Lakebase SQL 编辑器中运行一次 SQL。如果节点运行时表不存在，错误描述会显示同样的语句，并填入你选择的 **Schema**（架构）和 **Table Name**（表名称）。

设置需要两个身份。Lakebase SQL 编辑器中的身份是项目所有者或管理员，用于创建角色和表；凭据对应的身份不是所有者，它获得该角色并读写表。建表前，按[为 Data API 设置 Lakebase](../../credentials/databricks.md#set-up-lakebase-for-the-data-api)中的说明启用 Data API，为凭据身份创建 Postgres 角色，并将其授予 `authenticator`。可跳过 OpenAPI 规范步骤，以及[将角色授予 authenticator](../../credentials/databricks.md#grant-the-role-to-authenticator)下的第二段 SQL：此节点不列出表，下方 SQL 已包含所需授权。然后，在 Lakebase SQL 编辑器中，以创建角色的身份运行以下 SQL。该身份会成为表所有者，`GRANT` 语句需要这一身份：

```sql
CREATE TABLE "public"."n8n_chat_histories" (id SERIAL PRIMARY KEY, session_id VARCHAR(255) NOT NULL, message JSONB NOT NULL);
CREATE INDEX ON "public"."n8n_chat_histories" (session_id, id);
GRANT USAGE ON SCHEMA "public" TO "your-role";
GRANT SELECT, INSERT, DELETE ON "public"."n8n_chat_histories" TO "your-role";
GRANT USAGE ON SEQUENCE "public"."n8n_chat_histories_id_seq" TO "your-role";
```

* 将 `"your-role"` 替换为 OAuth2 身份的 Postgres 角色：用户的电子邮箱地址，或服务主体的应用 ID。这是设置时使用 `databricks_create_role` 创建的角色。
* 如果 **Schema**（架构）或 **Table Name**（表名称）不是 `public` 和 `n8n_chat_histories`，请在所有语句中替换相应名称，包括序列名称，即表名称后加 `_id_seq`。

## 节点参数 <a id="node-parameters"></a>

* **Project**（项目）：从列表选择 Lakebase 项目，或选择 **By ID**（按 ID）并输入项目 ID。
* **Branch**（分支）：从列表选择项目分支，或选择 **By ID**（按 ID）并输入分支 ID，例如 `production`。
* **Database**（数据库）：从列表选择分支上的 Postgres 数据库，或选择 **By ID**（按 ID）并输入 Postgres 数据库名称，例如 `databricks_postgres`。
* **Schema**（架构）：存放该表的 Postgres 架构，默认为 `public`，列表中仅提供 `public`。使用其他架构时，选择 **By ID**（按 ID）并输入其名称。Data API 必须暴露该架构。
* **Table Name**（表名称）：输入用于存储聊天历史的表名称，默认为 `n8n_chat_histories`。节点不会创建该表，请参阅[创建表](#create-the-table)。
* **Session ID**（会话 ID）：选择节点获取会话 ID 的方式：
    * **Connected Chat Trigger Node**（已连接的聊天触发器节点）：从直接连接的 [Chat Trigger](../../core-nodes/n8n-nodes-langchain.chattrigger/README.md) 节点的输入中读取 `sessionId` 字段。
    * **Define below**（在下方定义）：输入将会话 ID 存入记忆时使用的 **Key**（键）。多个记忆节点使用相同键，可共享同一会话。
* **Context Window Length**（上下文窗口长度）：输入作为上下文考虑的历史交互次数，默认为 `5`。

## 在记忆节点间共享会话 <a id="share-a-session-between-memory-nodes"></a>

**Session ID**（会话 ID）设为 **Connected Chat Trigger Node**（已连接的聊天触发器节点）时，每个 Databricks Lakebase Chat Memory 节点都会将自身节点名称加入会话范围，因此同一工作流中的两个记忆节点不会共享历史。重命名节点会改变该后缀，使智能体从空历史开始，旧记录仍保留在表中。要让记忆节点共享同一历史，请在每个节点中将 **Session ID** 设为 **Define below**（在下方定义），并使用相同的 **Key**（键）。执行会覆盖现有记忆内容的破坏性操作时，请谨慎，例如 [Chat Memory Manager](n8n-nodes-langchain.memorymanager.md) 节点的 **Override All Messages**（覆盖全部消息）插入模式。

## 相关资源 <a id="related-resources"></a>

该服务的更多信息，请参阅 [Lakebase Data API 文档](https://docs.databricks.com/aws/en/oltp/projects/data-api)。

在 [n8n-io/n8n#41795](https://github.com/n8n-io/n8n/pull/41795) 随版本发布之前，节点面板中不会显示此节点。该发布版本号确定后，本页会添加 Preview（预览）状态提示。

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 常见问题 <a id="common-issues"></a>

### 表不存在 <a id="the-table-is-missing"></a>

节点以 `Table <schema>.<table> does not exist` 失败。可能尚未创建表，或 **Schema**（架构）或 **Table Name**（表名称）与表不匹配（`PGRST205`），或 Data API 架构缓存仍列出已删除的表（`42P01`）。错误描述包含所选架构和表的 `CREATE TABLE`、`CREATE INDEX` 和 `GRANT` 语句。请在 Lakebase SQL 编辑器中，以创建角色的身份运行它们。请参阅[创建表](#create-the-table)。

### 角色缺少授权 <a id="the-role-lacks-a-grant"></a>

节点以 `The OAuth2 identity cannot use table <schema>.<table>` 失败。表存在，但角色缺少对架构、表或序列的授权（`42501`）。错误描述包含三条 `GRANT` 语句，请以表所有者身份运行。

### 会话过大，无法读取 <a id="the-session-is-too-large-to-read"></a>

节点以 `The session holds more rows than one run can read (100000)` 失败。每次请求最多读取 1,000 行，最多发出 100 次请求，因此会话超过 100,000 行后，节点会报错，而不会仅返回部分历史。如果 Lakebase 项目的 **Maximum rows**（最大行数）设置更低，此上限还会降低。请使用新的 **Session ID**（会话 ID），或以表所有者身份在 Lakebase SQL 编辑器中删除该会话的记录。[Chat Memory Manager](n8n-nodes-langchain.memorymanager.md) 节点无法清除此会话，因为它会先读取全部历史，也会遇到相同错误。**Session ID** 设为 **Connected Chat Trigger Node** 时，存储的 `session_id` 以 `__<node-name>` 结尾。

### 设置错误 <a id="setup-errors"></a>

`invalid token permissions`（`PGRST301`）、`permission denied to set role`（`42501`）、Data API 未暴露的架构（`PGRST106`）以及 `The branch has no read-write compute endpoint`，都源于 Data API 设置，而非表本身。请参阅 Databricks 节点页面的[常见 Lakebase 问题](../../app-nodes/n8n-nodes-base.databricks.md#common-lakebase-issues)。

[^1]: 在 AI 场景中，记忆让 AI 工具能够在多次交互之间保存消息上下文。例如，与 AI 智能体持续对话时，无需在每条消息中重复提交上下文。在 n8n 中，AI 智能体节点可以使用记忆，而 AI 链不能。
