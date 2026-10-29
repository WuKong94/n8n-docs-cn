---
title: Confluence 节点文档
description: 了解如何在 n8n 中使用 Confluence 节点，并按照技术文档将 Confluence 节点集成到工作流中。
contentType:
- integration
- reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Confluence 节点 <a id="confluence-node"></a>

使用 Confluence 节点自动处理 [Confluence Cloud](https://www.atlassian.com/software/confluence) 中的工作，并将其与其他应用集成。n8n 内置支持创建、读取、更新和删除页面，处理页面标签及评论，上传和下载附件，列出空间，以及使用 CQL 搜索内容。

本页列出了 Confluence 节点支持的操作、选择站点和页面的指引，以及更多资源的链接。

{% hint style="info" %}
**凭据**

节点提供两种登录方式，通过 **Authentication**（身份验证）下拉菜单选择：

* **Cloud OAuth2**：使用 [Confluence Cloud OAuth2 API 凭据](../credentials/confluence.md)以个人身份登录。凭据保存 OAuth 应用的客户端 ID 和密钥。
* **Service Account**（服务账户）：通过 **Atlassian Service Account**（Atlassian 服务账户）凭据，以 Atlassian 服务账户身份登录，适用于没有用户参与的无人值守工作流。凭据的作用域在创建时确定，与其他用户一样，还需满足空间权限。

无论使用哪种方式，都需在节点中选择 Confluence 站点。
{% endhint %}

## 选择站点 <a id="choosing-a-site"></a>

每项操作都从 **Site**（站点）参数开始，选择要操作的 Confluence Cloud 站点：

* **Pick from a list**（从列表选择，默认）：从连接可访问的站点中选择。
* **By URL**（按 URL）：粘贴站点地址，例如 `https://example.atlassian.net`。
* **Leave it empty**（留空）：如果连接恰好只能访问一个站点，节点会自动使用它。如果可访问多个站点，节点会要求选择一个，并在错误中列出站点。

## 选择页面 <a id="choosing-a-page"></a>

针对页面的操作提供四种指定页面的方式：

* **Pick from a list**（从列表选择，默认）：按标题搜索页面。先选择 **Space**（空间），可将列表限定在一个空间内。
* **By URL**（按 URL）：直接粘贴浏览器或 Confluence **Share**（共享）按钮提供的页面链接。
* **By ID**（按 ID）：粘贴页面的数字 ID。
* **By Title**（按标题）：输入页面标题，且必须恰好匹配一个页面。如果多个页面同名，请选择 **Space**（空间）以缩小查找范围。

## 页面正文 <a id="page-bodies"></a>

写入页面或评论内容的操作提供 **Body Format**（正文格式）选项：

* **Plain Text**（纯文本，默认）：输入纯文本，每一行会成为一个段落，无需标记语法。
* **Storage**（存储格式）：输入 Confluence 存储格式的 XHTML，例如 `<h2>Title</h2><p>Text</p>`。
* **Atlas Doc Format**：输入原始 [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/) JSON 文档。

读取内容的操作会以 **Storage**（存储格式，默认）或 **Atlas Doc Format** 返回正文，也可从文档提取 **Plain Text**（纯文本），便于将页面内容用于 AI 和搜索工作流。

**Append**（追加）操作会按所选格式写入页面，无论页面原先以何种格式保存。两种格式不同时，Confluence 会转换整个页面。内容和宏会保留，但存储的标记会重写，因此版本历史会显示整页差异，而非仅追加内容的差异。要缩小差异，请选择页面现有格式。

## 创建和发布 Confluence 页面草稿 <a id="create-and-publish-confluence-page-drafts"></a>

Confluence 会在页面已发布版本之外保留草稿，因此草稿不会取代读者看到的内容：

* 执行 **Create**（创建）并启用 **Create as Draft**（创建为草稿）时，会创建未发布的页面。作者可在空间树中看到带 **Draft**（草稿）标记的页面。
* 执行 **Update**（更新）并将 **Status**（状态）设为 **Draft**（草稿）时，会将更改保存为未发布草稿，不会取消页面发布。线上页面继续显示最近发布的版本，Confluence 会将页面标记为 **Unpublished changes**（未发布的更改）。

要发布草稿，请对其执行 **Update**（更新），将 **Status**（状态）设为 **Published**（已发布）。

## 操作 <a id="operations"></a>

* **Attachment**（附件）：
  * Delete: move an attachment to the trash, or permanently delete it.（删除：将附件移至回收站，或永久删除）
  * Get Many: list the attachments on a page, optionally downloading each file.（获取多项：列出页面附件，可选择下载每个文件）
  * Upload: upload a file as an attachment on a page. Uploading a file with the same name as an existing attachment creates a new version of it.（上传：将文件作为页面附件上传。上传与现有附件同名的文件，会为该附件创建新版本）
* **Page**（页面）：
  * Add Comment: add a footer comment to a page, or reply to an existing comment.（添加评论：为页面添加页脚评论，或回复已有评论）
  * Add Labels: add one or more labels to a page.（添加标签：为页面添加一个或多个标签）
  * Append: append content to the bottom of an existing page.（追加：在现有页面底部追加内容）
  * Create: create a new page in a space, optionally as a draft, private, at the space root, or under a parent page.（创建：在空间中创建页面，可选创建为草稿、私有页面、空间根页面或父页面下的子页面）
  * Delete: move a page to trash, or permanently delete it. Child pages aren't deleted. They move up to the deleted page's parent.（删除：将页面移至回收站，或永久删除。子页面不会删除，而会移至被删除页面的父页面下）
  * Delete Comment: permanently delete a footer comment.（删除评论：永久删除页脚评论）
  * Get: retrieve a page, optionally with its full sub-tree, returning one item per page in tree order, the page itself first.（获取：获取页面，可选包含其完整子树。按树顺序为每个页面返回一个数据项，当前页面排在首位）
  * Get Comments: list the top-level footer comments on a page.（获取评论：列出页面顶层页脚评论）
  * Get Labels: list the labels on a page.（获取标签：列出页面标签）
  * Get Many by Label: retrieve all pages carrying a label, optionally within one space.（按标签获取多项：获取带有指定标签的全部页面，可选限定在一个空间内）
  * Remove Label: remove a label from a page.（移除标签：从页面移除标签）
  * Update: replace the title and body of an existing page, or change its draft/published status.（更新：替换现有页面的标题和正文，或更改其草稿/发布状态）
* **Search**（搜索）：
  * Query: search content with a [CQL](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/) query, optionally fetching each result's full page content on the same request.（查询：使用 CQL 查询搜索内容，可选在同一请求中获取每条结果的完整页面内容）
* **Space**（空间）：
  * Get: retrieve a space.（获取：获取空间）
  * Get Many: retrieve many spaces.（获取多项：获取多个空间）

## 模板与示例 <a id="templates-and-examples"></a>

[搜索所有模板](https://n8n.io/workflows/)，查看使用此节点的示例。

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 [Atlassian Confluence Cloud REST API 文档](https://developer.atlassian.com/cloud/confluence/rest/v2/intro/)。
