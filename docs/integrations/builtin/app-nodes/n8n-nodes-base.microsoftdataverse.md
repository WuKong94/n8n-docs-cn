---
description: 在 n8n 工作流中创建、更新、删除和查询 Microsoft Dataverse 数据行。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Dataverse 节点 <a id="microsoft-dataverse-node"></a>

使用 Microsoft Dataverse 节点自动处理 Microsoft Dataverse 中的工作，并将其与其他应用集成。你可以通过 Dataverse Web API，在标准表和自定义表中创建、读取、更新和删除数据行。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Microsoft Dataverse 凭据](../credentials/microsoftdataverse.md)。此节点通过 **Microsoft Dataverse OAuth2 API** 凭据支持用户委派访问和仅应用访问。
{% endhint %}

## 操作 <a id="operations"></a>

* **Row**（数据行）
    * **Create**（创建）：添加新行。
    * **Create or Update**（创建或更新）：通过行 ID 或替代键创建新行，或更新已有行。
    * **Delete**（删除）：删除一行。
    * **Get**（获取）：按 ID 获取一行。
    * **Get Many**（获取多行）：获取多行，可选筛选和排序。
    * **Update**（更新）：更新已有行。此操作不会创建不存在的行。

## 选择表和数据行 <a id="select-a-table-and-row"></a>

将 **Resource**（资源）设为 **Row**（数据行），然后选择 **Operation**（操作）。

在 **Table Name or ID**（表名称或 ID）中，选择 **From List**（从列表）以搜索环境中的表。要手动输入表，选择 **By ID**（按 ID），并填写其 Web API 实体集名称，例如 `accounts` 或 `contacts`。这不是表的显示名称、单数形式的逻辑名称或 GUID。

对于 **Get**（获取）、**Update**（更新）和 **Delete**（删除），使用 **Row ID**（行 ID）从 **From List**（从列表）选择数据行，或通过 **By ID**（按 ID）输入其 GUID。例如，`00000000-0000-0000-0000-000000000001` 符合所需格式，请替换为你所在环境中实际数据行的 ID。

只有 **Create or Update**（创建或更新）支持[使用替代键寻址](#create-or-update-a-row)。

## 创建和更新数据行 <a id="create-and-update-rows"></a>

对于 **Create**（创建）、**Update**（更新）和 **Create or Update**（创建或更新），选择一种 **Input Mode**（输入模式）：

| 输入模式 | 值的输入方式 |
| --- | --- |
| **JSON**（默认） | 在 **Row Item (JSON)**（行数据 JSON）中输入对象。以列的逻辑名称作为键，并使用列所要求的数据类型。 |
| **Fields (Key / Value Pairs)**（字段：键值对） | 在 **Fields**（字段）下选择 **Add Field**（添加字段），选择 **Field Name or ID**（字段名称或 ID），然后输入 **Field Value**（字段值）。为每列重复此步骤。 |

至少提供一个字段，节点会拒绝空的行数据。字段选择器会显示适用于所选操作的可写列。对于 **Create or Update**（创建或更新），它会显示同时支持创建和更新的列。

**Field Value**（字段值）输入框是字符串字段。节点不会自动将文本字面量转换为数字或布尔值。需要保留这些类型或发送 `null` 时，请使用 **JSON**。

### 创建客户账户 <a id="create-an-account"></a>

要创建客户账户，选择 **Create**（创建），将 **Table Name or ID**（表名称或 ID）设为 `accounts`，并使用 **JSON** 输入。在 **Row Item (JSON)**（行数据 JSON）中输入以下对象：

```json
{
	"name": "Contoso",
	"accountnumber": "ACC-001",
	"numberofemployees": 25,
	"creditonhold": false
}
```

使用 **Update**（更新）时，选择已有客户账户的 **Row ID**（行 ID），并仅发送要修改的字段。例如，`{"telephone1": "555-0100"}` 会更新电话号码，而不替换其他字段。

### 设置查找列 <a id="set-lookup-columns"></a>

查找列用于引用另一个表中的数据行。能够访问关系元数据时，节点会将查找值转换为 Dataverse 要求的导航属性绑定。

| 查找类型 | 需要提供的值 |
| --- | --- |
| 单一目标表，例如客户账户中的 `primarycontactid` | 行 GUID，或 `/contacts(<contact-id>)` 这样的引用。 |
| 多个目标表，例如 Customer 列 | 显式引用，例如 `/accounts(<account-id>)` 或 `/contacts(<contact-id>)`。仅提供 GUID 会有歧义。 |
| Owner 列 | `/systemusers(<user-id>)` 或 `/teams(<team-id>)`。仅提供 GUID 会有歧义。 |

将尖括号占位符替换为你所在环境中数据行的 GUID。可以省略这些引用开头的斜杠。

例如，要设置客户账户的主要联系人和所有者，在 **Row Item (JSON)**（行数据 JSON）中包含以下字段：

```json
{
	"primarycontactid": "/contacts(<contact-id>)",
	"ownerid": "/systemusers(<user-id>)"
}
```

也可以直接提供显式绑定，例如 `{"primarycontactid@odata.bind": "/contacts(<contact-id>)"}`。节点会原样传递显式绑定。请使用表元数据中准确且区分大小写的导航属性名称；它可能与列的逻辑名称不同。

要清空单一目标的查找列，发送 `null`，例如 `{"primarycontactid": null}`。对于多表查找，应清空对应的具体导航属性，前提是 Dataverse 允许清除此关系。

## 创建或更新一行 <a id="create-or-update-a-row"></a>

选择 **Create or Update**（创建或更新），并通过以下任一种 **Identifier Type**（标识符类型）寻址数据行：

* **Row ID (GUID)**（行 ID）：选择或输入 **Row ID**（行 ID）。如果该行不存在，Dataverse 会使用此 GUID 创建数据行。
* **Alternate Key**（替代键）：输入 **Alternate Key Predicate**（替代键谓词），例如 `accountnumber='ACC-001'`。使用前，先在 Dataverse 中为该表配置替代键。

仅输入谓词，不包含表名称或外围括号。对于字符串键，保留值两侧的单引号。节点会拒绝谓词中的 URL 分隔符、路径分隔符和控制字符。

在 **Options**（选项）下，使用 **Behavior**（行为）控制写入方式：

| 行为 | 结果 |
| --- | --- |
| **Create or Update**（创建或更新，默认） | 行不存在时创建，存在时更新。 |
| **Update Only**（仅更新） | 更新已有行。行不存在时失败。 |
| **Create Only**（仅创建） | 创建新行。行已存在时失败。 |

例如，选择 `accounts` 表，选择 **Alternate Key**（替代键），然后输入 `accountnumber='ACC-001'`。在 **Row Item (JSON)**（行数据 JSON）中发送 `{"name": "Contoso"}`，即可创建或更新具有该账户编号的客户账户。

## 查询数据行 <a id="query-rows"></a>

**Get**（获取）操作支持 **Options**（选项）中的 **Select Column Names or IDs**（选择列名称或 ID）和 **Expand Query**（展开查询）。**Get Many**（获取多行）支持这些选项，以及额外的筛选、排序和结果数量限制。

### 使用 OData 获取多行 <a id="get-many-rows-with-odata"></a>

选择 **Get Many**（获取多行），并配置以下参数：

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| **Return All**（返回全部） | 关闭 | 跟随 OData 分页链接，直到没有更多结果。 |
| **Limit**（数量限制） | `50` | **Return All**（返回全部）关闭时，最多返回的行数。最小值：`1`。 |
| **Select Column Names or IDs**（选择列名称或 ID） | 未选择 | 选择要获取的列。留空时，使用 Dataverse 默认的投影。 |
| **Filter Rows**（筛选行） | 留空 | OData 筛选表达式，例如 `statecode eq 0`。不要包含 `$filter=` 前缀。 |
| **Expand Query**（展开查询） | 留空 | 用于获取关联数据行的 OData 表达式，例如 `primarycontactid($select=fullname)`。 |
| **Sort Column Name or ID**（排序列名称或 ID） | 未选择 | 要用于排序的列。 |
| **Sort Direction**（排序方向） | **Ascending**（升序） | 所选列的排序方向。 |
| **Sort By Override**（排序覆盖） | 留空 | 原始 OData 排序表达式，例如 `createdon desc, name asc`。仅在 **Sort Column Name or ID**（排序列名称或 ID）为空时使用。 |
| **Row Count ($Top)**（行数） | 未设置 | 服务端结果数量上限。会覆盖根据 **Limit**（数量限制）推导的 `$top` 值，并禁用服务端驱动的分页。 |

例如，要获取名称以 `Contoso` 开头、最多 100 个处于活动状态的客户账户：

1. 将 **Table Name or ID**（表名称或 ID）设为 `accounts`。
2. 保持 **Return All**（返回全部）关闭，并将 **Limit**（数量限制）设为 `100`。
3. 在 **Options**（选项）下，在 **Select Column Names or IDs**（选择列名称或 ID）中选择 `name` 和 `accountnumber`。
4. 将 **Filter Rows**（筛选行）设为 `statecode eq 0 and startswith(name,'Contoso')`。
5. 将 **Sort Column Name or ID**（排序列名称或 ID）设为 `name`，并将 **Sort Direction**（排序方向）设为 **Ascending**（升序）。

读取列的选择器会自动使用 `_primarycontactid_value` 这样的查找属性名称。编写原始筛选或排序表达式时，请使用这种属性形式表示查找 GUID。例如，通过 `_primarycontactid_value eq <contact-id>` 筛选，将 `<contact-id>` 替换为不带引号的 GUID。对于 **Expand Query**（展开查询），请使用导航属性名称。

### 分页和结果数量限制 <a id="pagination-and-result-limits"></a>

对于 OData 查询，节点会跟随 `@odata.nextLink`，直到达到 **Limit**（数量限制）或获取所有可用结果。

**Limit**（数量限制）为 5,000 或更小时，节点还会将其作为 `$top` 发送。限制更大时，节点不设置 `$top`，让 Dataverse 可以返回多页结果。显式设置的 **Row Count ($Top)**（行数）优先级更高，即使开启 **Return All**（返回全部），也可能限制结果数量。

要获取超过 5,000 行的数据，请保持 **Row Count ($Top)**（行数）未设置，并开启 **Return All**（返回全部），或将 **Limit**（数量限制）设为大于 5,000。这些分页规则适用于 OData 查询，不适用于 FetchXML。

### 使用 FetchXML <a id="use-fetchxml"></a>

设置 **Options**（选项）> **FetchXML Query**（FetchXML 查询）以运行 FetchXML 查询。它会替代 OData 的选择、筛选、排序、展开和 top 选项。保持 **Return All**（返回全部）关闭，并设置 **Limit**（数量限制）以限制返回行数。

例如，选择 `accounts` 表，并输入以下查询，以获取最多 50 个处于活动状态的客户账户：

```xml
<fetch top="50">
	<entity name="account">
		<attribute name="name" />
		<attribute name="accountnumber" />
		<filter>
			<condition attribute="statecode" operator="eq" value="0" />
		</filter>
	</entity>
</fetch>
```

FetchXML 使用表的逻辑名称 `account`，而 **Table Name or ID**（表名称或 ID）使用实体集名称 `accounts`。

{% hint style="warning" %}
**FetchXML 分页**

Microsoft Dataverse 节点不支持 FetchXML 分页。**FetchXML Query**（FetchXML 查询）与 **Return All**（返回全部）一起使用会报错。关闭 **Return All** 可以避免该错误，但提高 **Limit**（数量限制）不会获取更多 FetchXML 页。需要自动分页时，请使用 OData 查询。
{% endhint %}

## 使用弹性表 <a id="work-with-elastic-tables"></a>

对于 **Get**（获取）、**Get Many**（获取多行）和 **Delete**（删除），需要定位弹性表分区时，设置 **Options**（选项）> **Partition ID**（分区 ID）。

**Create**（创建）、**Update**（更新）和 **Create or Update**（创建或更新）不提供 **Partition ID**（分区 ID）选项。使用 **Create** 创建分区内的数据行时，在行 JSON 中包含 `partitionid`。

要更新分区内的数据行或执行创建或更新操作，使用 **Create or Update**（创建或更新），并将 **Identifier Type**（标识符类型）设为 **Alternate Key**（替代键）。在 **Alternate Key Predicate**（替代键谓词）中包含表的主键和 `partitionid`：

```text
<primary-key-column>=<row-id>,partitionid='<partition-id>'
```

将占位符替换为表主键列的逻辑名称、行 GUID 和分区 ID。如果要求该行必须已存在，将 **Behavior**（行为）设为 **Update Only**（仅更新）。有关表的具体行为和限制，请参阅 Microsoft 的[弹性表文档](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-elastic-tables)。

## 输出和元数据 <a id="output-and-metadata"></a>

* **Create**（创建）、**Update**（更新）和 **Create or Update**（创建或更新）会在写入后请求该行，并返回 Dataverse 的响应。
* **Get**（获取）返回单行。
* **Get Many**（获取多行）将每行作为单独的 n8n 数据项返回，而不是放在 `value` 字段中的集合。
* **Delete**（删除）成功后返回 `{"success": true, "id": "<row-id>"}`。

除 **Delete**（删除）外，所有操作都提供 **Options**（选项）> **Return Full Metadata**（返回完整元数据），默认关闭。开启后，会请求 OData 注解，包括 Dataverse 提供的格式化值。节点不会重命名列或简化注解。

## 常见问题 <a id="common-issues"></a>

### 表或列选项无法加载 <a id="table-or-column-options-dont-load"></a>

检查选择器显示的 HTTP 状态和 Dataverse 错误。验证环境 URL 和凭据访问权限，包括访问表元数据的权限。请参阅 [Microsoft Dataverse 凭据故障排查](../credentials/microsoftdataverse.md#common-issues)。

如果知道表的实体集名称，可以通过 **Table Name or ID**（表名称或 ID）> **By ID**（按 ID）输入。这不会绕过 Dataverse 权限检查。

### 查找值被拒绝 <a id="a-lookup-value-is-rejected"></a>

不要将显示名称用作查找值。对于单一目标查找，使用 GUID，或包含实体集名称和行 ID 的引用。Customer 和 Owner 列需要明确指定目标表。示例请参阅[设置查找列](#set-lookup-columns)。

### 查询返回的行数少于预期 <a id="a-query-returns-fewer-rows-than-expected"></a>

检查 **Limit**（数量限制）；需要分页时，移除 **Row Count ($Top)**（行数），并确认查询是否使用 FetchXML。请参阅[分页和结果数量限制](#pagination-and-result-limits)及[使用 FetchXML](#use-fetchxml)。

## 相关资源 <a id="related-resources"></a>

* [Microsoft Dataverse 凭据](../credentials/microsoftdataverse.md)
* [Dataverse Web API 文档](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview)
* [使用 Web API 查询数据](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query/overview)
* [通过 Web API 使用替代键](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-alternate-key-reference-record)