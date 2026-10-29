---
contentType: reference
nodeTitle: 用户体验指南
originalFilePath: integrations/creating-nodes/build/reference/ux-guidelines.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/ux-guidelines
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/ux-guidelines
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 社区节点用户体验指南 <a href="#ux-guidelines-for-community-nodes" id="ux-guidelines-for-community-nodes"></a>

节点界面必须符合以下指南，才有资格成为[经过验证的社区节点](../../deploy-your-node/submit-community-nodes.md#submit-your-node-for-verification-by-n8n)。

## 凭据 <a href="#credentials" id="credentials"></a>

API 密钥和敏感凭据应始终使用密码字段。

### OAuth <a href="#oauth" id="oauth"></a>

如果服务支持 OAuth，请始终提供 OAuth 凭据。

## 节点结构 <a href="#node-structure" id="node-structure"></a>

### 应包含的操作 <a href="#operations-to-include" id="operations-to-include"></a>

尽量为每种资源类型提供 **CRUD**（创建、读取、更新、删除）操作。

尽量在节点中为每种资源提供常见操作。n8n 使用一组 CRUD 操作保持体验一致，让用户能够对资源执行基本操作。建议的操作包括：

* **Create（创建）**
* **Create or Update (Upsert)（创建或更新）**
* **Delete（删除）**
* **Get（获取）**
* **Get Many（获取多个）：**也适用于支持筛选或搜索的情况。
* **Update（更新）**

说明：

1. 这些操作可以作用于资源本身，也可以作用于资源内的实体，例如 Google Sheet 中的一行。对资源内的实体执行操作时，必须在操作名称中注明**实体名称**。
2. 名称可能因节点和资源而异，详情见下文指南。

### 资源定位器 <a href="#resource-locator" id="resource-locator"></a>

* 尽可能使用资源定位器组件，为用户提供更好的使用体验。需要选择单个数据项时，资源定位器通常最有用。
* 资源定位器组件的默认选项应为 `From list`（如果可用）。

### 与其他节点保持一致 <a href="#consistency-with-other-nodes" id="consistency-with-other-nodes"></a>

* 保持用户体验一致：n8n 力求保持体验一致，因此应遵循已有的交互模式，尤其是最近新增或全面改版的节点所采用的模式。
* 参考相似节点：例如，开发数据库节点时，可以参考 Postgres 节点。

### 排序选项 <a href="#sorting-options" id="sorting-options"></a>

* 可以为某些 Get Many 操作提供排序选项，以增强功能。
* 将排序设置放在独立集合中，位于 Options 集合下方。示例请参阅 [Airtable Record:Search](https://github.com/n8n-io/n8n/blob/92e2a8e61a4189025e5d4bac8be81576b624fe85/packages/nodes-base/nodes/Airtable/v2/actions/record/search.operation.ts#L85-L135)。

## 节点功能 <a href="#node-functionality" id="node-functionality"></a>

### 删除操作的输出 <a href="#deleting-operations-output" id="deleting-operations-output"></a>

删除数据项（例如记录或行）时，返回一个仅包含单个对象的数组：`{"deleted": true}`。这既向用户确认删除成功，也能让该数据项触发后续节点。

### 简化输出字段 <a href="#simplifying-output-fields" id="simplifying-output-fields"></a>

#### 普通节点：Simplify 参数 <a href="#normal-nodes-simplify-parameter" id="normal-nodes-simplify-parameter"></a>

端点返回的数据超过 10 个字段时，请添加 Simplify（简化）布尔参数，用于返回最多包含 10 个字段的简化输出。

* 数据量过大可能是使用 n8n 时的一项主要问题，Simplify 参数通过减少数据量缓解此问题。
* 为简化输出选择最有用的字段，并将最常用的字段排在前面。
* Simplify 模式通常最好将嵌套字段展开为扁平结构。
* 显示名称：`Simplify`
* 描述：`Whether to return a simplified version of the response instead of the raw data`

#### AI 工具节点：Output 参数 <a href="#ai-tool-nodes-output-parameter" id="ai-tool-nodes-output-parameter"></a>

端点返回的数据超过 10 个字段时，请添加具有 3 种模式的 Output（输出）选项参数。

在 AI 工具节点中，应允许用户更细致地选择输出字段。工具可能耗尽上下文窗口，过多字段也可能造成干扰，因此最好只传递所需字段。

选项：

* **Simplified（简化）：**行为与上文的 Simplify 参数相同。
* **Raw（原始）：**返回所有可用字段。
* **Selected fields（指定字段）：**显示多选参数，供用户选择要加入输出并发送给 AI 智能体的字段。默认情况下，此选项始终返回记录或实体的 ID。

## 文案 <a href="#copy" id="copy"></a>

### 英文大小写 <a href="#text-case" id="text-case"></a>

节点的 `name`、`parameters display names`（标签）和 `dropdown titles` 应使用**标题式大小写（Title Case）**，即每个单词的首字母大写，但冠词和短介词等小词除外。

节点的 `action` 名称、节点 `descriptions`、`parameters descriptions`（工具提示）、`hints` 和 `dropdown descriptions` 应使用**句首式大小写（Sentence case）**。

### 术语 <a href="#terminology" id="terminology"></a>

* **沿用第三方服务的术语：**尽量使用所集成服务的相同术语，例如使用 Notion 的 blocks（块），而不是 paragraphs（段落）。
* **沿用界面中的术语：**使用服务用户界面中的术语，而非 API 或技术文档中的术语。例如，Trello 界面中称为 archive（归档）卡片，API 中则显示为 closed（关闭）；这种情况应使用 archive。
* **避免技术行话：**能用简单词语表达时，就不要使用技术行话。例如，用 field（字段）替代 key（键）。
* **保持命名一致：**对同一概念选定一个术语并始终使用，例如不要混用 directory 和 folder。

### 占位文字 <a href="#placeholders" id="placeholders"></a>

在参数占位文字中提供内容示例通常很有帮助。示例应以 e.g. 开头，字段中的演示内容应使用**驼峰命名**。

可直接使用的占位文字示例：

* 图片：`e.g. https://example.com/image.png`
* 视频：`e.g. https://example.com/video.mp4`
* 搜索词：`e.g. automation`
* 电子邮件：`e.g. nathan@example.com`
* Twitter 用户（或类似用户名）：`e.g. n8n`
* 姓名：`e.g. Nathan Smith`
* 名：`e.g. Nathan`
* 姓：`e.g. Smith`

### 操作名称、action 和描述 <a href="#operations-name-action-and-description" id="operations-name-action-and-description"></a>

* **Name（名称）：**节点在画布上打开时，显示在选择框中的名称。必须使用标题式大小写，不必包含资源名称，例如 Delete。
* **Action：**在用户选择节点的面板中显示的操作名称。必须使用句首式大小写，并包含资源名称，例如 Delete record。
* **Description（描述）：**节点在画布上打开时，显示在选择框名称下方的辅助文字。必须使用句首式大小写，并包含资源名称。可以补充信息，也可以使用不同于基本资源名或操作名的措辞，例如 Retrieve a list of users。
* 如果操作作用于资源内部的实体，例如 Google Sheet 中的一行，应在操作名称中注明，例如 Delete Row。

通常，应先明确操作的**对象**是什么。有时操作对象就是资源本身，例如用 `Sheet:Delete` 删除工作表。

有时操作对象并非资源本身，而是资源内部的内容。例如 `Table:Delete rows` 中，资源是表，但实际操作对象是表中的行。

#### 为 `name` 命名 <a href="#naming-name" id="naming-name"></a>

节点在画布上打开时，这是选择框中显示的名称。

* 参数：`name`
* 大小写：标题式大小写（Title Case）

命名指南：

* **上方已有资源选择项时，不重复资源名称：**资源通常显示在操作上方，因此操作名称无需重复资源名称。这适用于操作对象就是资源本身的情况。
	* 例如：`Sheet:Delete` → 无需重复 `Sheet` 到 `Delete` 中，因为 n8n 已在上方字段显示 `Sheet`，且要删除的对象就是工作表。
* **上方没有资源选择项时，注明资源：**有些节点只有一种资源，因此没有资源选择项。这时应在操作名称中注明资源。
	* 例如：`Delete Records` → Airtable 中没有资源选择项，因此最好说明 Delete 操作删除的是记录。
* **操作对象并非资源本身时，注明对象：**有时操作对象不是资源本身，这时也应在操作名称中注明对象。
	* 例如：`Table:Get Columns` → 应注明 `Columns`，因为资源是 `Table`，而操作对象是 `Columns`。

#### 为 `action` 命名 <a href="#naming-action" id="naming-action"></a>

这是用户选择节点的面板中显示的操作名称。
* 参数：`action`
* 大小写：句首式大小写（Sentence case）

命名指南：

* **省略冠词：**为保持文字简短，省略 a、an、the 等冠词。
	* **正确**：`Update row in sheet`
	* **错误**：`Update a row in a sheet`
* **重复资源名称：**这种情况下可以重复资源名称。即使列表中已显示资源，用户也可能没有注意到，因此在操作标签中重复资源名称是有益的。
* **操作对象并非资源本身时，注明对象：**规则与操作名称相同，此时无需重复资源名称。
	* 例如：`Append Rows` → 必须注明 `Rows`，因为实际追加的是行。不应添加资源名称（`Sheet`），因为追加操作并非直接作用于资源本身。

#### 为 `description` 命名 <a href="#naming-description" id="naming-description"></a>

节点在画布上打开时，这是选择框中显示在名称下方的辅助文字。

* 参数：`description`
* 大小写：句首式大小写（Sentence case）

命名指南：

* 尽可能提供比操作 `name` 更丰富的信息。
* 使用不同措辞帮助用户理解操作的作用。有些人可能看不懂操作中的文字，例如英语并非其母语；换一种说法可能更容易理解。

#### 用词 <a href="#vocabulary" id="vocabulary"></a>

n8n 使用一组通用词汇，并为数据库、电子表格等相似应用提供特定场景下的词汇。

通用词汇借鉴 CRUD 操作：

* **Clear（清空）**
    * 删除资源中的全部内容，将资源清空。
    * 描述：`Delete all the <CHILD_ELEMENT>s inside the <RESOURCE>`
* **Create（创建）**
    * 创建资源的新实例。
    * 描述：`Create a new <RESOURCE>`
* **Create or Update（创建或更新）**
    * 创建资源实例，或更新已有实例。
    * 描述：`Create a new <RESOURCE> or update an existing one (upsert)`
* **Delete（删除）**
    * Delete 有两种用法：
        1. 删除资源：
            * 描述：`Delete a <RESOURCE> permanently`（只有确实永久删除时才使用 permanently）
        2. 删除资源**内部**的内容，例如一行：
            * 此时，**务必注明操作对象**，例如 `Delete Rows` 或 `Delete Records`。
            * 描述：`Delete a <CHILD_ELEMENT> permanently`
* **Get（获取）**
    * Get 有两种用法：
        1. 获取资源：
            * 描述：`Retrieve a <RESOURCE>`
        2. 获取资源**内部**的数据项，例如记录：
            * 此时，**务必注明操作对象**，例如 `Get Row` 或 `Get Record`。
            * 描述：`Retrieve a <CHILD_ELEMENT> from the/a <RESOURCE>`
* **Get Many（获取多个）**
    * Get Many 有两种用法：
        1. 获取资源列表，不进行筛选：
            * 描述：`Retrieve a list of <RESOURCE>s`
        2. 获取资源**内部**的数据项列表，例如记录：
            * 此时，**务必注明操作对象**，例如 `Get Many Rows` 或 `Get Many Records`。
            * 可以省略 `Many`：例如 `Get Many Rows` 可以简写为 `Get Rows`。
            * 描述：`List all <CHILD_ELEMENT>s in the/a <RESOURCE>`
* **Insert（插入）**或 **Append（追加）**
    * 在资源内部添加内容。
    * 数据库节点应使用 `insert`。
    * 描述：`Insert <CHILD_ELEMENT>(s) in a <RESOURCE>`
* **Insert or Update（插入或更新）**或 **Append or Update（追加或更新）**
    * 在资源内部添加或更新内容。
    * 数据库节点应使用 `insert`。
    * 描述：`Insert <CHILD_ELEMENT>(s) or update an existing one(s) (upsert)`
* **Update（更新）**
    * Update 有两种用法：
        1. 更新资源：
            * 描述：`Update one or more <RESOURCE>s`
        2. 更新资源**内部**的内容，例如一行：
            * 此时，**务必注明操作对象**，例如 `Update Rows` 或 `Update Records`。
            * 描述：`Update <CHILD_ELEMENT>(s) inside a <RESOURCE>`

### 引用参数和字段名称 <a href="#referring-to-parameter-and-field-name" id="referring-to-parameter-and-field-name"></a>

在文案中引用参数名称或字段名称时，请用英文单引号括起来，例如“请填写 `'name'` 参数”。

### 布尔字段描述 <a href="#boolean-description" id="boolean-description"></a>

布尔组件的描述应以 Whether...（是否……）开头。

## 错误 <a href="#errors" id="errors"></a>

### 基本原则 <a href="#general-philosophy" id="general-philosophy"></a>

错误会让用户困扰，因此 n8n 希望始终告诉用户：

* **发生了什么：**描述错误以及具体哪里出了问题。
* **如何解决：**至少应说明如何解除阻碍并继续正常使用 n8n。不要让用户一直受阻，应借此引导用户完成任务。

### Output 面板中的错误结构 <a href="#error-structure-in-the-output-panel" id="error-structure-in-the-output-panel"></a>

#### 错误消息：发生了什么 <a href="#error-message-what-happened" id="error-message-what-happened"></a>

此消息向用户解释发生了什么，以及当前什么问题导致执行无法完成。

* 如果知道触发错误的参数的 `displayName`，请将其加入错误消息或描述中，也可以同时加入两者。
* 数据项索引：如果知道触发错误的数据项 ID，请在错误消息末尾添加 `[Item X]`，例如 `The ID of the release in the parameter “Release ID” for could not be found [item 2]`。
* 避免使用 error、problem、failure、mistake 等词。

#### 错误描述：如何解决或解除阻碍 <a href="#error-description-how-to-solve-or-get-unstuck" id="error-description-how-to-solve-or-get-unstuck"></a>

描述应告诉用户如何解决问题、需要如何修改节点配置（如适用），或如何解除阻碍。应在此引导用户执行下一步，使其能够继续操作。

避免使用 error、problem、failure、mistake 等词。

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
