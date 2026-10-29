---
title: Airtop 节点文档
description: 了解如何在 n8n 中使用 Airtop 节点，并按照技术文档将 Airtop 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Airtop 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtop.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Airtop 节点 <a href="#airtop-node" id="airtop-node"></a>

使用 Airtop 节点自动处理 Airtop 中的工作，并将其与其他应用集成。n8n 内置支持多种 Airtop 功能，让你控制云端浏览器，完成查询、抓取和网页交互等任务。

本页列出了 Airtop 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Airtop 凭据](../credentials/airtop.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Agent（智能体）
    * Run an agent（运行智能体）
* Session（会话）
    * Create session（创建会话）
    * Save profile on termination（终止时保存浏览器配置文件）
    * Terminate session（终止会话）
    * Wait for download（等待下载）
* Window（窗口）
    * Create a new browser window（创建新浏览器窗口）
    * Load URL（加载 URL）
    * Take screenshot（截图）
    * Get live view（获取实时视图）
    * List windows（列出窗口）
    * Close window（关闭窗口）
* Extraction（提取）
    * Query page（查询页面）
    * Query page with pagination（分页查询页面）
    * Smart scrape page（智能抓取页面）
* Interaction（交互）
    * Click an element（点击元素）
    * Fill form（填写表单）
    * Hover on an element（悬停在元素上）
    * Scroll（滚动）
    * Type（输入）
* File（文件）
    * Upload a file（上传文件）
    * Get a file（获取文件）
    * Get many files（获取多条文件）
    * Load a file（加载文件）
    * Delete a file（删除文件）


## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Airtop 集成模板](https://n8n.io/integrations/airtop)，或[搜索所有模板](https://n8n.io/workflows/)


## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Airtop 文档](https://docs.airtop.ai/api-reference/airtop-api)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

如需协助或提交功能请求，请联系 [Airtop 支持团队](https://docs.airtop.ai/guides/misc/support)。

## 节点参考 <a href="#node-reference" id="node-reference"></a>

### 运行智能体 <a id="run-an-agent"></a>

运行已发布的 Airtop 智能体。在 **Agent**（智能体）字段中选择要运行的智能体，再映射输入参数。如果要使用指定浏览器配置文件运行，请在可选的 **Browser Profile ID**（浏览器配置文件 ID）中填写其 ID。留空则使用智能体的默认配置文件。

### 创建会话和窗口 <a href="#create-a-session-and-window" id="create-a-session-and-window"></a>

创建 Airtop 浏览器会话以获取 **Session ID**（会话 ID），再用它创建新浏览器窗口。之后即可使用任一提取或交互操作。

### 管理窗口 <a id="manage-windows"></a>

管理会话中的浏览器窗口：

- **Load URL**（加载 URL）：让窗口导航到指定页面。
- **Get live view**（获取实时视图）：获取 Live View URL，实时查看和控制窗口。
- **Take screenshot**（截图）：捕获窗口图像。
- **List windows**（列出窗口）：列出会话中打开的窗口。
- **Close window**（关闭窗口）：关闭指定窗口。

### 提取内容 <a href="#extract-content" id="extract-content"></a>

通过以下操作从浏览器提取内容：

- **Query page**（查询页面）：从当前窗口提取信息。
- **Query page with pagination**（分页查询页面）：从分页或无限滚动的页面提取信息。
- **Smart scrape page**（智能抓取页面）：以 Markdown 格式获取窗口内容。

在查询操作中使用 **JSON Output Schema**（JSON 输出架构）参数，可获得 JSON 响应。

### 与页面交互 <a href="#interacting-with-pages" id="interacting-with-pages"></a>

使用自然语言描述要操作的元素，即可与会话中的页面交互：

- **Click an element**（点击元素）、**Hover on an element**（悬停在元素上），或 **Type**（输入）文本。
- **Fill form**（填写表单）：使用自然语言描述各字段值，一次填写多个字段。
- **Scroll**（滚动）：滚动到所描述的元素，或朝页面边缘滚动指定距离。

### 处理文件 <a id="work-with-files"></a>

上传文件到 Airtop，在浏览器自动化中使用：

- **Upload a file**（上传文件）：从 URL 或二进制数据上传文件，可选将其附加到会话中页面的文件输入控件。
- **Load a file**（加载文件）：将已上传的文件附加到现有会话中页面的文件输入控件。
- **Get a file**（获取文件）和 **Get many files**（获取多个文件）：获取文件详情，或将已准备好的文件下载为二进制数据。
- **Delete a file**（删除文件）：按 **File ID**（文件 ID）永久移除已上传文件。

### 等待下载 <a id="wait-for-a-download"></a>

在会话中触发下载后，使用 **Wait for download**（等待下载）等待文件准备就绪，再获取文件 ID 和下载 URL。

### 终止会话 <a href="#terminate-a-session" id="terminate-a-session"></a>

结束会话以节省资源。会话会根据 **Create Session**（创建会话）操作中设置的 **Idle Timeout**（空闲超时）自动终止，也可通过 **Terminate Session**（终止会话）操作手动终止。
