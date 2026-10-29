---
title: Notion 节点常见问题
contentType:
- integration
- reference
priority: high
nodeTitle: Notion 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues
description: 了解 n8n 工作流自动化平台中 Notion 节点的常见错误和问题，包括问题详情及建议的解决方法。
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


# 常见问题 <a id="common-issues"></a>

以下介绍 [Notion 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 关联属性不显示 <a href="#relation-property-not-displaying" id="relation-property-not-displaying"></a>

Notion 节点仅支持显示[双向关联](https://www.notion.com/help/relations-and-rollups)的数据关联属性。使用双向关联连接两个 Notion 数据库后，即可在 Notion 节点的 **Database Page**（数据库页面）资源中选择关联属性，或按该属性筛选。

要启用双向关联，请在 Notion 中编辑关联属性，启用 **Show on \[name of related database]**（在关联数据库中显示）选项，创建反向关联。为新场景下的关联选择名称。之后即可在 n8n 中筛选或选择该关联。

如需处理具有单向关联的 Notion 数据库，可使用 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/README.md) 节点和已有 Notion 凭据。例如，要更新单向关联，可向以下 URL 发送 `PATCH` 请求：

```
https://api.notion.com/v1/pages/<page_id>
```

启用 **Send Body**（发送请求体），将 **Body Content Type**（请求体内容类型）设为 **JSON**，**Specify Body**（指定请求体）设为 **Using JSON**（使用 JSON）。然后在 **JSON** 字段中输入如下对象：

```json
{
	"properties": {
		"Account": {
			"relation": [
				{
					"id": "<your_relation_ID>"
				}
			]
		}
	}
}
```

## 创建可折叠标题 <a href="#create-toggle-heading" id="create-toggle-heading"></a>

向 **Page**（页面）、**Database Page**（数据库页面）或 **Block**（块）资源添加块时，Notion 节点允许创建标题和折叠块，但节点本身尚不支持直接创建可折叠标题。

可先创建普通标题，再修改它以启用 [`is_toggleable` 属性](https://developers.notion.com/reference/block#headings)，作为替代方案：

1. 使用 Notion 节点添加标题。
2. 选择要添加标题的资源：
   * 要添加包含标题的新页面，请选择 **Page**（页面）或 **Database Page**（数据库页面）资源，以及 **Create**（创建）操作。
   * 要向已有页面添加标题，请选择 **Block**（块）资源，以及 **Append After**（在后方追加）操作。
3. 选择 **Add Block**（添加块），将 **Type Name or ID**（类型名称或 ID）设为 **Heading 1**（一级标题）、**Heading 2**（二级标题）或 **Heading 3**（三级标题）。
4. 在 Notion 节点后连接一个 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/README.md) 节点，选择 `GET` 方法。
5. 将 **URL** 设为 `https://api.notion.com/v1/blocks/<block_ID>`。例如，向已有页面添加标题时，可使用 URL `https://api.notion.com/v1/blocks/{{ $json.results[0].id }}`。如果创建了新页面，而非追加块，可能需要先查询页面内容来查找块 ID。
6. 选择 **Predefined Credential Type**（预定义凭据类型），连接已有 Notion 凭据。
7. 在 HTTP Request 节点后添加 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点。
8. 添加新的 **Boolean**（布尔）字段 `heading_1.is_toggleable`，将其设为 `true`。根据需要，将 `heading_1` 替换为其他标题级别。
9. 在 Edit Fields (Set) 节点后添加第二个 HTTP Request 节点。
10. 将 **Method**（方法）设为 `PATCH`，**URL** 的值设为 `https://api.notion.com/v1/blocks/{{ $json.id }}`。
11. 选择 **Predefined Credential Type**（预定义凭据类型），连接已有 Notion 凭据。
12. 启用 **Send Body**（发送请求体）并设置一个参数。
13. 将参数 **Name**（名称）设为 `heading_1`，将其中的 `heading_1` 替换为实际使用的标题级别。
14. 将参数 **Value**（值）设为 `{{ $json.heading_1 }}`，将其中的 `heading_1` 替换为实际使用的标题级别。

上述步骤先创建普通标题块，再查询新创建的标题，添加 `is_toggleable` 属性并更新标题块。

## 处理 null 和空值 <a href="#handle-null-and-empty-values" id="handle-null-and-empty-values"></a>

使用 Notion 节点时，提交空值或 null 值字段可能导致验证错误。使用前序节点的数据填充字段，而该数据缺失时，就可能出现此情况。

可在向 Notion 发送数据前检查字段数据是否存在，或使用默认值来解决。

要在执行 Notion 节点前检查数据，请使用 [If](../../core-nodes/n8n-nodes-base.if.md) 节点检查字段是否未设置。这样便可通过 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点，在字段没有有效值时有条件地移除它。

另一种方法是，在输入数据未提供值时设置默认值。
