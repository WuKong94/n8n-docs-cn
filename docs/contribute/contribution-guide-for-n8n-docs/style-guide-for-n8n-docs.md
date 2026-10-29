---
nodeTitle: n8n 文档风格指南
originalFilePath: dummy1.md
originalUrl: https://docs.n8n.io/dummy1
url: https://docs.n8n.io/contribute/contribution-guide-for-n8n-docs/style-guide-for-n8n-docs
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


# n8n 文档风格指南 <a id="style-guide-for-n8n-docs"></a>

## 写作风格 <a id="writing-style"></a>

n8n 使用 [Microsoft 写作风格指南](https://docs.microsoft.com/en-us/style-guide/welcome/)。本文重点介绍对 n8n 文档最重要的部分，并补充我们的自定义风格约定。

### 明确读者 <a id="who-youre-writing-for"></a>

面向使用、运维或基于 n8n 开发的读者写作，而非面向 n8n 内部工程师。

写清读者需要操作和看到的内容：控件、设置、字段、错误消息、限制，以及影响其构建结果的行为。

只有读者需要借助实现细节采取行动、选择方案或排查问题时，才加入这些细节。例如，执行数据的存储方式适合写在自托管页面中，不适合写在节点参考页中。其他情况下应省略。

工单、PR 和设计文档是事实来源，不是页面模板。保留读者需要的信息，省去其余内容。

### 通俗语言 <a id="plain-language"></a>

* 清楚说明所记录流程的每一步。
* 使用现在时。
* 尽量简洁。以下两款免费的浏览器应用可以提供帮助：
  * [Hemingway](https://hemingwayapp.com/) 衡量语言复杂度。没有规定必须达到哪个阅读年级，但阅读难度越低越好。
  * [Lexi](https://rebilly.github.io/lexi/) 衡量 Markdown 文字的写作复杂度，将多项指标综合为可读性评分。目标至少为 60 分，大多数页面应高于这一分数。

留意以下常见表达，优先使用更简单的说法：

| 避免使用 | 改为使用 |
| ------------------------------------------- | ---------------------- |
| utilize、leverage | use |
| in order to | to |
| functionality、capabilities | features、what it does |
| It’s important to note that X | X |
| n8n provides a powerful, seamless way to... | n8n lets you... |

几条实用原则：

* **删除赘词。**省去 It’s important to note that、Simply 等开场白。
* **避免营销用语。**省去 powerful、robust、seamless，直接说明功能的作用。
* **删除含糊的修饰词。**省去 very、quite、several，或给出具体数值。
* **句子保持简短。**每句少于 30 个英文单词，只表达一个意思。由分号或第二个 and 连接起来的句子应拆分。
* **以动作开头，不用 There is。**使用 To schedule a workflow, add a Schedule Trigger，而非 There is a node that can schedule workflows。

### 语态与人称 <a id="voice-and-person"></a>

像直接与读者交谈一样写作。

* **使用主动语态。**使用 n8n sends the request，而非 the request is sent by n8n。
* **用 you 称呼读者。**使用 You can add a node，而非 Users can add a node。
* **避免第一人称。**使用 n8n 代替 I、we 或 our。例如 n8n recommends，而非 we recommend。
* **使用英文缩略形式。**使用 Don’t 和 you’ll，而非 do not 和 you will。

### 包容性语言 <a id="inclusive-language"></a>

为所有人写作。

* **对未知性别的人使用 they。**使用 Every user can configure their settings，而非 his settings。
* **选择性别中立的用词。**使用 Chair 而非 chairman，使用 Main 而非 master。

### 术语与命名 <a id="terminology-and-naming"></a>

对同一概念始终使用相同术语，优先采用官方产品术语，而非看似合适的近义词。例如使用 publish a workflow，而非 activate a workflow。正文使用句首式大小写；直接引用界面标签或节点名称时，加粗并保持产品中的确切大小写。产品名称写作小写 n8n，即使位于句首也不例外。

完整的推荐与禁用术语请参阅[术语与命名](terminology.md)。

### 文字格式 <a id="text-formatting"></a>

* 标题：句首式大小写（[更多信息](https://docs.microsoft.com/en-us/style-guide/scannable-content/headings#formatting-headings)）。
* 界面元素：加粗（[更多信息](https://docs.microsoft.com/en-us/style-guide/procedures-instructions/formatting-text-in-instructions)）。
* 用户输入：使用代码格式。占位符采用以连字符连接的单词，并用尖括号包裹；默认小写，也可为匹配环境变量等约定使用大写。例如 `<your-root-directory>` 或 `<YOUR-API-KEY>`。
* 文件名、目录名和路径：使用代码格式。
* 品牌名称必须准确，例如 GitHub，而非 Github。

### 数字、日期与时间 <a id="numbers-dates-and-times"></a>

英文中零至九使用单词，10 及以上使用数字。

以下情况除外：

* **小数：**始终使用数字，即使小于 10，例如 3.5，而非 three point five。
* **百分比：**使用数字，例如 5%，而非 five percent。
* **版本及其他技术字符串：**使用数字，例如 n8n 2.1、step 3。
* **计量单位：**使用数字，例如 5px、3MB。

**日期与时间**

* 月份使用英文全称，不使用序数词。例如 July 31, 2016，而非 31/07/2016 或 July 31st。
* 使用 AM/PM，并在前面留空格，例如 9 AM，而非 9am。

**范围**

* 正文中使用 from X to Y 或 X through Y，例如 from 5 to 10 nodes。
* 表格或标签中的数字范围使用短破折号（–），而非连字符，例如 5–10。
* 时间范围使用 to，例如 9 AM to 5 PM，而非 9 AM–5 PM。

[更多信息](https://docs.microsoft.com/en-us/style-guide/numbers)

### 标点与空格 <a id="punctuation-and-spacing"></a>

* **英文句子之间只留一个空格**，不要两个。
* **标点放在英文引号内。**使用 “Select Save,” 而非 “Select Save”。
* **使用牛津逗号。**例如 triggers, nodes, and credentials。
* **避免长破折号（—）。**改用逗号或另起一句。例如 Add a node, then save，而非 Add a node — then save。
* **避免省略号（…）。**使用 Configure the settings, then continue，而非 Configure the settings...。

## 页面长度与粒度 <a id="page-length-and-granularity"></a>

将内容拆分为主题集中的页面，每页涵盖一个概念、任务或参考类别，避免整页过于庞大，也避免内容零散。内容独立完整、用标题组织的页面最适合读者和 AI 工具；原因见[面向智能体的友好文档](agent-friendly-docs.md)。

### 长度 <a id="length"></a>

* **合理范围：**约 1,500 至 20,000 个字符，或 250 至 3,000 个英文单词，方便读者浏览，也便于 AI 工具检索。
* **少于约 1,500 个字符时合并：**内容太短不利于检索，应将简略页面合并到父页面或同级页面。
* **超过约 25,000 个字符时拆分：**页面混合多种内容类型（概念、操作指南、参考），或某节不断扩张（例如逐个客户端列举示例）时，也应拆分。
* **绝不超过约 50,000 个字符。**智能体会截断超出此上限的内容。

### 如何拆分 <a id="how-to-split"></a>

* 按**类型或任务**边界拆分，例如概念、操作指南、参考、示例，不要仅按长度任意切分。这样符合读者的浏览方式，并使每个片段聚焦一个主题。
* 将相关事实放在**同一页面**，例如某类别的全部环境变量、某节点的全部参数。AI 搜索会将相邻内容放在一起，邻近排列有助于保留上下文。

### 让每节内容独立完整 <a id="keep-each-section-self-contained"></a>

确保读者即使只看到一节、没有相邻内容提供上下文，也能理解该节。原因见[面向智能体的友好文档](agent-friendly-docs.md)：

* **使用描述明确、句首式大小写的标题。**AI 搜索通常按标题检索，并可能不带页面其他内容，因此要完整说明主题。例如 Configure the Schedule Trigger，而非 Configuration。
* **每节都应能够独立理解。**重新说明关键背景，而非指回其他地方。避免 as mentioned above、as described in the previous section、see below 等表达；智能体乱序检索或读者从搜索直接进入时，这些指代会失去作用。
* **重述要点，不重复整段。**仅重复该节所需的一两项事实。如果两节都需要相同的长篇解释，说明它们可能应合并到同一标题下。重述应简短，使页面保持精炼，参阅[通俗语言](#plain-language)。

### 以一句话回答开篇 <a id="lead-with-a-one-sentence-answer"></a>

在 H1 之后、已有简介、提示框或复用片段之前，加入一句通俗文字，具体回答页面主题问题。原因见[面向智能体的友好文档](agent-friendly-docs.md)。

* 说明页面或节点能让读者做什么，写出实际产品、节点或技术名称，而非笼统地说“可以做一些事情”。
* 使用一句话；只有确实需要简短限定说明时才用两句。
* 如果现有简介已以类似句子开头，则无需添加。

例如：“Code 节点允许你在工作流中运行自己的 JavaScript 或 Python，以转换数据，或加入内置节点未涵盖的逻辑。”

### 链接到相关页面、前提条件和后续步骤 <a id="link-to-related-pages-prerequisites-and-next-steps"></a>

将各页面与同主题的其他页面连接起来，参阅[面向智能体的友好文档](agent-friendly-docs.md)。

**以下指南不适用于 `docs/integrations/`（节点）页面**，这些页面使用另一种结构。

* **始终链接到前提条件和下一步。**
* **章节入口页链接到子页面。**有两个及以上子页面时，在 In this section（本节内容）标题下用项目列表列出链接和简短说明。只有一个子页面时，省略列表，在正文首次提及时直接链接。
* **子页面在末尾 Related resources（相关资源）中链接回父页面和同级页面。**父页面和每个直接同级页面各放一个链接，不附说明。父链接使用 `./`（当前页面与父页面的 `README.md` 位于同一文件夹时），或使用 `../`（当前页本身是位于父页面下一层的章节入口页时），参阅[父页面](#parent-pages)。其他确实相关的页面可以酌情添加。
* **超过 10 个同级页面时，省略同级列表。**只链接父页面，因为父页面的 In this section 已有完整列表。
* **自身也是父页面的页面，两种链接都要提供。**使用 In this section 列出子页面，并在 Related resources 页脚链接到自己的父页面和同级页面；只向上一级及同级链接，不链接到祖父级。
* **扁平参考集合可以省略同级链接。**如果每页都采用相同的单项信息模板，例如每种表达式数据类型一页，则 Related resources 只链接父页面。
* **同一主题尽量形成至少五个相互链接页面的集群。**
* **正文只在首次有实际意义地提及时添加链接**，链接文字应描述目标，例如[配置 Schedule Trigger](../../integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/README.md)，而非“单击这里”。复用已有的主题提及，不要只为添加链接而新增句子。链接不能替代该节需要的上下文；必要时应重述关键事实，参阅[让每节内容独立完整](#keep-each-section-self-contained)。

## 功能可用范围 <a id="feature-availability"></a>

功能的可用范围可能受到三种限制：

* **方案或平台：**在哪些 n8n Cloud 方案或自托管版本上可用。
* **版本：**在哪个 n8n 版本中引入、弃用或移除。
* **预览状态：**是否仍在趋于稳定、可能变化，或尚未向所有人开放。

[方案、平台和版本限制](#plan-platform-and-version-limits)使用同一套文档规则。[预览状态](#preview-status)则采用不同方式，始终单独记录。

### 方案、平台与版本限制 <a id="plan-platform-and-version-limits"></a>

可以按三种范围记录：

* **页面或章节：**在页面标题或相关小节标题下，放置标题为 **Feature availability**（功能可用范围）的 `info` 提示框。参阅[功能可用范围提示框](#feature-availability-hints)。
* **行内或顺带提及：**对于小型选项、字段、角色或行为，或正文中提到但没有独立标题的整个功能或节点，在旁边加入简短说明，将限制融入句子。参阅[行内与顺带提及](#inline-and-passing-mentions)。
* **表格行：**某一行适用限制时，将其放入说明单元格；如果多行限制不同，则增加专用列。参阅[表格行](#table-rows)。

#### 功能可用范围提示框 <a id="feature-availability-hints"></a>

示例：

**同时限制方案与版本：**

```
{% hint style="info" %}
**Feature availability**

Environments are available on:

- **n8n Cloud:** Pro, Enterprise
- **Self-hosted:** Enterprise

Available from n8n 2.30.0.
{% endhint %}
```

**仅限制版本：**主体可以是功能，也可以是节点。

```
{% hint style="info" %}
**Feature availability**

Canvas Groups are available from n8n 2.28.0.
{% endhint %}
```

**弃用或移除：**使用 `warning`，而非 `info`。移除时调整措辞，例如“`N8N_RUNNERS_ENABLED` 从 n8n 3.0 起移除”。此处的主体是一项设置：

```
{% hint style="warning" %}
**Feature availability**

`N8N_RUNNERS_ENABLED` is deprecated from n8n 2.0.
{% endhint %}
```

如果整页介绍的功能已经弃用或移除，还应添加主要 `deprecated` 标签，参阅 Frontmatter 下的[标签](#tags)。不要添加 `status:` 字段，因为 `deprecated` 不是该字段经确认可用的值：

```
---
tags:
  - tag: deprecated
    primary: true
---
```

该标签需要在空间的 `.gitbook/tags.yaml` 中定义，显示文字为 Deprecated，颜色为红色。

规则：

* **提示框样式：**弃用或移除使用 `warning`，因为读者需要采取行动；其他情况使用 `info`。组合提示使用 `warning`。
* **正文中写明主体**，不能只在标题中说明。提示框标题没有指出什么内容可用，也不要依赖外部标题。保持 available from n8n X.Y.Z 连贯。仅限制版本时，可以说明替代对象，例如 The Chat Trigger node is available from n8n 1.24.0, replacing the Manual Chat Trigger node。
* **平台列表：**以“<Feature> <is/are> available on:”开头。始终写明两个平台；两者均支持时各列一项。仅支持其一时，在该项下方补充不可用说明，例如 It isn’t available on n8n Cloud 或 ...self-hosted。如果另一平台需满足条件才可用，例如需要申请，则用条件说明替代不可用说明，例如 On n8n Cloud Enterprise, contact n8n to enable it。
* **层级：**按低到高顺序列出，用逗号分隔，不使用 and。Cloud：Starter、Pro、Enterprise。自托管：Community、Registered Community、Business、Enterprise。名称和大小写必须准确，Registered Community 不缩写。
* **写作 n8n Cloud，不要单独使用 Cloud。**
* **整个平台：**使用 `All plans`/`All editions`，不要逐一列举层级。All plans 包含免费试用，试用功能与 Pro 对应；不要单列试用，仅在试用页面中介绍。
* **列表下方的顺序：**（1）不可用或附带条件说明；（2）版本说明；（3）其他功能特有的限制说明。
* **没有方案限制时：**仅限制版本、弃用或移除时，只保留标题和说明句，不使用列表。
* **不要链接到方案版本对比或发行说明。**在句子中直接说明事实，需要时由读者自行搜索。


#### 行内与顺带提及 <a id="inline-and-passing-mentions"></a>

较大功能中的小控件、选项、字段或角色，或正文中没有独立标题的整个功能或节点，使用行内说明。适用于整页或整节的限制应使用提示框，不使用行内说明。

* 写明具体对象，不使用 this feature 或 this option，确保脱离上下文也能理解。
* 每个对象用一句话；同时涉及方案或平台和版本时可用两句，先写方案或平台。
* 如果两个平台都相关，就都要提及，不要用省略暗示不可用。
* 直接说明版本、弃用或移除，例如 available from n8n X、deprecated from n8n X。省略提示框所用的 Available from 引导语。
* 如果超过两句，或需要列出两个平台，则改为适用范围明确的提示框。

对于控件、选项、字段或角色：

```
The **Scopes** option is available on n8n Cloud Pro, Enterprise, and self-hosted Enterprise.
```

```
The **Legacy format** field is deprecated from n8n 2.30.0.
```

对于没有独立标题的整个功能或节点，将限制融入句子：

```
The Data table node (available from n8n 2.17.0) stores data between executions.
```

```
The environments feature (n8n Cloud Enterprise, self-hosted Enterprise) lets you promote workflows between instances.
```

#### 表格行 <a id="table-rows"></a>

多行中的某一行适用限制时，沿用行内说明的用词和顺序，将限制放在说明单元格中：

| 变量 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `N8N_RUNNERS_ENABLED`（已弃用） | Boolean | `false` | 是否启用任务运行器。自 n8n 2.0 起弃用，无需再设置此变量。 |

如果多行限制不同，也可以增加专用列：

| 变量 | 可用范围 | 说明 |
| :--- | :--- | :--- |
| `N8N_LDAP_ENABLED` | 自托管 Business、Enterprise | 是否启用 LDAP 登录。 |
| `N8N_SMTP_HOST` | 所有版本 | 发送邮件所用 SMTP 服务器的主机名。 |

### 版本表述 <a id="versioning-wording"></a>

#### 两种版本类型 <a id="two-version-types"></a>

n8n 有两套独立版本号，不要让读者猜测具体指哪一种。

* **实例版本：**n8n 的发行版本，使用三段 semver，例如 2.30.0。用于功能、环境变量、API、CLI 命令和钩子。
* **节点版本：**某个节点的版本，通常为两段，例如 4.7。仅用于节点特有的信息。

正文中出现版本数字时应说明归属，例如 n8n 2.30.0 或 node version 4.7，而非 version 2。

#### 版本号写法 <a id="writing-version-numbers"></a>

遵循[数字规范](#numbers-dates-and-times)，并对 n8n 实例版本采用以下规则：

* **产品名加数字：**n8n 2.30.0。
* **不加 `v` 前缀：**不要写作 n8n v2.30.0。
* **n8n 后不加 version：**不要写作 n8n version 2.30.0。
* **正文中的版本不使用行内代码格式：**写作 n8n 2.30.0，而非 n8n `2.30.0`。只有版本实际出现在代码、命令或文件路径中时才使用代码格式，例如 `n8n@2.30.0`、Docker 标签或 `package.json` 的值。

### 预览状态 <a id="preview-status"></a>

Preview 功能已经可用，但尚未完整或稳定，可能发生变化。作为成熟度标签时，Preview 首字母大写，例如 is in Preview、a Preview feature、In Preview from n8n 2.20.0；使用 Preview，不使用 beta。链接预览、界面预览操作等其他含义仍使用小写。Frontmatter 和标签值作为字面标识符而非正文，保持小写，例如 `status: preview`、`tag: preview`。

**页面或章节：**提示框标题使用 `**Preview status**`，而非 `**Feature availability**`。稳定性和可用范围是不同问题，应各有提示框，不要沿用可用范围提示框的标签另加一个。节点或功能名写在下方句子中，不放在标题里，因为读者会脱离周围标题单独浏览提示框：

```
{% hint style="info" %}
**Preview status**

The Data table node is in Preview and may change in future releases. Avoid relying on it in production workflows.
{% endhint %}
```

如果整页介绍 Preview 功能，还应设置 `status: preview`，并添加主要 `preview` 标签，参阅 Frontmatter 下的[标签](#tags)：

```
---
status: preview
tags:
  - tag: preview
    primary: true
---
```

实际示例请参阅[构建和管理智能体](../../build/build-and-manage-agents/README.md)。

**行内或顺带提及：**适用于小型控件，或正文中没有独立标题的整个功能或节点：

```
The **Streaming response** option is in Preview and may change in future releases.
```

```
The Data table node is in Preview and may change in future releases.
```

* **有帮助时关联版本：**例如 In Preview from n8n 2.20.0。
* **与功能可用范围分开。**两者同时适用时，分别排列两个提示框或两个句子，不要混为一体。
* **行内说明需要超过一句话时：**改为页面级或章节级提示框。

## Vale 文字检查 <a id="vale-linting"></a>

n8n 使用 [Vale](https://vale.sh/) 按本指南的规则检查文档。

配置包括：

* 仓库根目录中的 `.vale.ini` 文件，包含检查配置。
* `styles` 目录，包含风格定义，包括现成的风格库和 n8n 专用风格。
* 在每个 PR 上运行 Vale 的 GitHub Action，直接在 PR 中报告违规内容。

可以按以下方式在本机运行 Vale：

1. 按照 Vale 文档[安装 Vale CLI](https://vale.sh/docs/install)。
2. 选择通过命令行检查，或安装文本编辑器插件：
   1. 运行 `vale docs/`，检查 `docs` 目录下的所有 Markdown 文件。
   2. 也可以安装插件，让文本编辑器自动显示问题。使用 VS Code 时，安装 ChrisChinchilla 提供的 [vale-vscode](https://github.com/ChrisChinchilla/vale-vscode)。

## Frontmatter <a id="frontmatter"></a>

Frontmatter 位于页面顶部，必须是有效的 YAML。n8n 文档使用以下 frontmatter 字段：

* `description`：页面内容的简短摘要。n8n 可能将其显示在搜索结果和链接预览中。
* `hidden`：设为 `true` 时，从网站侧边菜单中移除页面。页面需要出现在菜单中时，省略此字段，大多数页面均如此。
* `layout.description.visible`：设为 `false` 时，隐藏渲染页面中的 frontmatter 描述。始终包含此字段，并将其设为 `false`。
* `generated`：设为 `true` 时，表示页面完全由自动化管理，不要手动更新这类页面。

Frontmatter 示例：

```
---
description: Learn how to merge data streams in your n8n workflows.
layout:
  description:
    visible: false
---
```

{% hint style="info" %}
在已有 n8n 文档页面中，还可能看到 `contentType`、`nodeTitle`、`originalFilePath`、`originalUrl`、`url` 等 frontmatter 字段。这些字段用于已有页面的迁移管理，不要添加到新页面中。
{% endhint %}

### 标签 <a id="tags"></a>

**可视标签**会显示为页面标签；如果设置 `primary: true`，也会出现在侧边菜单中。只有在空间的 `.gitbook/tags.yaml` 中定义了标签文字和颜色，才会渲染。将其作为对象添加到 `tags` 数组：

```
---
tags:
  - release
  - tag: preview
    primary: true
---
```

此例中，只有 `tag: preview` 是可视标签。`release` 是普通字符串，没有匹配的 `.gitbook/tags.yaml` 定义，因此不会渲染。`tags` 数组可以同时包含真正的可视标签和这类不产生效果的字符串，两者不同，后者不是第二个可视标签。

* 应先在空间的 `.gitbook/tags.yaml` 中定义可视标签，再使用它。先检查是否存在，不存在则添加。
* 可视标签只是一个标记，不能替代页面中的解释性提示框。提示框负责解释状态的含义，标签仅在界面中提示该状态。
* 文档目前仅允许三种可视标签：**Deprecated**（整页介绍已弃用功能）、**Preview**（整页介绍处于[预览状态](#preview-status)的功能）、**Archived**（不再更新的页面）。不要创建或使用其他可视标签。

## 页面导航 <a id="page-navigation"></a>

每个空间的根目录都有 `SUMMARY.md` 文件，用于定义侧边栏中显示哪些页面、排序和嵌套关系。GitBook 根据该文件生成导航，因此新页面只有加入 `SUMMARY.md` 后才会出现在侧边栏；仅创建 `.md` 文件还不够。

`SUMMARY.md` 是嵌套的 Markdown 列表。各条目使用相对于空间根目录（即 `SUMMARY.md` 所在目录）的路径链接到页面，并包含 `.md` 扩展名。`README.md` 是空间或章节的入口页，缩进可将其他页面嵌套在其下方：

```
# Summary

* [Administer](README.md)
* [Manage credentials](manage-credentials/README.md)
  * [Share credentials securely](manage-credentials/share-credentials-securely.md)
  * [Credential overwrites](manage-credentials/credential-overwrites.md)
```

添加页面时：

* 在正确的 `SUMMARY.md` 中添加条目，放在希望显示的位置。
* 链接文字使用页面标题，无需与页面内的标题完全一致，但应尽量接近。
* 通过缩进将其嵌套在父章节下，条目顺序决定侧边栏顺序。

移动、重命名或删除页面时，同步更新其 `SUMMARY.md` 条目。

## Markdown 与 GitBook 块 <a id="markdown-and-gitbook-blocks"></a>

网站由 [GitBook](https://www.gitbook.com/) 生成。页面使用 [Markdown](https://commonmark.org/) 编写，并添加称为**块**的 GitBook 专用组件，例如提示框、标签页和其他结构化页面元素。下文介绍常用块。

{% hint style="info" %}
各类可用块的 Markdown 表示方式，请参阅 [GitBook 文档](https://gitbook.com/docs/creating-content/blocks)。
{% endhint %}

### 标题 <a id="headings"></a>

使用普通 Markdown（`## Heading text`）编写标题，采用句首式大小写。GitBook 会根据标题文字自动生成可点击锚点，因此不要自行添加锚点标记。

已有页面中可能包含显式锚点标签，例如：

```
## Heading text <a href="#heading-text" id="heading-text"></a>
```

这些标签固定锚点，使链接在标题文字变化后仍然有效。修改标题措辞时，请保留锚点标签，避免已有链接失效。

### 链接 <a id="links"></a>

#### 外链 <a id="external-links"></a>

使用标准 Markdown 链接语法：

```
[commits](https://github.com/n8n-io/n8n/compare/n8n@0.176.0...n8n@0.177.0)
```

外链会自动在新标签页中打开。

#### 内链 <a id="internal-links"></a>

链接方式取决于目标页面位于**同一空间**还是**不同空间**。`docs/` 下的每个顶层文件夹，例如 `build/`、`deploy/` 和 `administer/`，都是独立的 GitBook 空间。

**同一空间内**使用标准 Markdown 链接语法，指向目标文件的相对路径，并包含 `.md` 扩展名。应链接到目标文件，不要仅写裸路径，因为页面移动或重命名时，这类引用会自动更新。

相对路径取决于目标页面与当前编辑页面的位置关系。以下示例均假定你正在编辑此文件树中的 `current-page.md`：

```
docs/                                     # docs root
├── build/                                # current space
│   ├── README.md                         # space landing page
│   ├── understand-workflows/             # subfolder (section) in the space
│   │   ├── README.md                     # section landing page (parent of current-page.md)
│   │   ├── current-page.md               # <- you're editing this page
│   │   └── another-page.md               # sibling page, same level
│   └── manage-workflows/                 # another subfolder in the same space
│       ├── README.md                     # section landing page
│       └── export-import.md              # page in a different subfolder
├── deploy/                               # another space
│   ├── README.md                         # space landing page
│   └── hosting/                          # subfolder in another space
│       ├── environment-variables.md      # page in a different space
│       └── configure.md                  # another page in that subfolder
└── administer/                           # another space
```

| 目标位置 | 链接语法 |
| --- | --- |
| 同一空间、同一子文件夹 | `[link text](another-page.md)` |
| 父页面，且父页面是 `README.md` | `[link to a parent page](./)` |
| 父页面有具体文件名，当前文件夹没有 `README.md`，例如 `connect-to-n8n-mcp-server.md` | `[link to a parent page](connect-to-n8n-mcp-server.md)`，直接链接到文件，不使用 `./` |
| 父页面，当前页面自身也是章节入口页（`README.md`） | `[link to a parent page](../)`，因为 `./` 会指向当前页自身，而非父页面 |
| 同一空间、不同子文件夹 | `[link to a page](../manage-workflows/export-import.md)` |
| 不同空间 | `[link to a page](https://app.gitbook.com/s/<spaceId>/<page-path>)` |

#### 父页面 <a id="parent-pages"></a>

`./` 和 `../` 都是仅指向目录的引用，GitBook 会在任意相对层级将其解析为对应文件夹自身的 `README.md`。`./` 指向当前文件夹的入口页；只有当前页面作为子页面位于该文件夹中时，这才是父页面。如果当前页自身就是章节入口页（`README.md`），`./` 会指回自身，因此应通过 `../` 向上一级，访问真正的父页面。

#### 链接到其他空间的页面 <a id="link-to-a-page-in-a-different-space"></a>

相对文件路径只在同一空间内有效。GitBook 将跨空间链接解析为页面引用，而非文件路径，因此使用 `../../` 路径进入其他空间不会生效。此时应链接到目标页面的 GitBook URL：

```
https://app.gitbook.com/s/<spaceId>/<page-path>
```

URL 由两部分组成：

* `<spaceId>`：目标页面所属空间的 ID，可在 [`SPACE_INDEX.md`](https://github.com/n8n-io/n8n-docs/blob/main/SPACE_INDEX.md) 中查找。
* `<page-path>`：目标页面在所属空间文件夹中的路径，去掉 `.md` 扩展名。`README.md` 则转换为其文件夹路径，例如 `host-n8n/configure-n8n/README.md` 只需写作 `host-n8n/configure-n8n`。

例如，从 `administer` 空间中的页面链接到 `docs/deploy/host-n8n/configure-n8n/user-management.md`，而目标位于 `deploy` 空间时：

```
[link to a page](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/user-management)
```

仅在目标页面位于*其他*空间时使用此形式。目标与当前页面位于同一空间时，应使用相对 `.md` 链接。GitBook 两种形式都能渲染，但空间 URL 不受重命名跟踪管理，目标页面移动后链接可能失效；它还会跳出 GitBook 预览的当前修订，解析到已发布内容，而非你的修改。`internal-links` CI 检查会将此问题报告为 `same-space-absolute`。

`docs/` 下的每个顶层文件夹都是独立空间。可在仓库根目录的 [`SPACE_INDEX.md`](https://github.com/n8n-io/n8n-docs/blob/main/SPACE_INDEX.md) 中查找目标空间 ID，该文件每天根据各空间的 GitBook Git Sync 设置生成。

如果不想手动构造 URL，可以在 GitBook 中打开目标页面并复制链接。没有 GitBook 访问权限时，改用页面已发布的 `https://docs.n8n.io/...` 地址。

### 图片 <a id="images"></a>

图片用于补充文字，不能单独承载信息，原因见[面向智能体的友好文档](agent-friendly-docs.md)。读者必须操作或了解的内容，都应写在正文中：

* **每项操作说明都写成文字。**截图可以展示界面，但“选择 **Add trigger**，再选择 **On schedule**”等步骤必须写出。设置、值、菜单路径或点击目标不能只出现在图片中。
* **不要将文字截图。**代码、命令、错误消息和配置值放在代码块或表格中，让读者能复制、智能体能读取。不要粘贴终端或代码编辑器的图片。
* **截图用于确认，而非代替说明。**将截图放在文字步骤旁，帮助读者辨认位置或确认操作界面，不要用截图替代步骤。

每个空间只使用一个文件夹存放全部图片，位于空间根目录的 `.gitbook/assets/`：

```
docs/                                     # docs root
├── build/                                # space root
│   ├── .gitbook/
│   │   └── assets/                       # all images for this space live here
│   │       └── workflow-overview.png
│   ├── understand-workflows/
│   │   └── current-page.md
│   └── manage-workflows/
│       └── export-import.md
└── deploy/                               # another space
    ├── .gitbook/
    │   └── assets/                       # all images for this space live here
    │       └── hosting-diagram.png
```

图片必须存放在使用它的空间的 `.gitbook/assets/` 文件夹中，不能引用其他空间资源文件夹中的图片。

使用相对于当前编辑页面的路径引用图片。无论位于空间内哪一层，都先向上到空间根目录，再进入 `.gitbook/assets/`：

**从一层深的页面引用**，例如 `build-workflows/manage-workflows/export-import.md`：

​ `![Alt text](../.gitbook/assets/workflow-overview.png) ​`

**从两层深的页面引用**，例如 `build-workflows/understand-workflows/current-page.md`：

​ `![Alt text](../../.gitbook/assets/workflow-overview.png) ​`

**替代文本**

始终编写描述明确的替代文本，用于无障碍访问，并在图片无法加载时显示。

* 描述图片展示的内容，而非图片类型。例如“工作流画布上，Schedule Trigger 连接到 HTTP Request 节点”，不要只写“截图”。
* 保持在 125 个字符以内。
* 不要以 Image of 或 Screenshot of 开头。

**图片文件**

* 截图和图表使用 PNG。
* 图标和简单插图有 SVG 时优先使用 SVG。
* 文件大小应合理，提交前压缩 PNG。[Squoosh](https://squoosh.app/) 是免费的浏览器工具。
* 文件名使用小写和连字符，例如 `workflow-overview.png`，不要用 `WorkflowOverview.PNG`。

**行内图标**

当界面元素仅以图标显示，例如没有文字标签的菜单时，使用 HTML `<img>` 标签和 `data-size="line"` 在行内嵌入，使图标按文字高度显示，而非渲染为块级图片：

```
select **Workflow menu** <img src="../.gitbook/assets/three-dots-horizontal.png" alt="Workflow menu icon" data-size="line">
```

* 术语加粗，不要加粗 `<img>` 标签。
* 替代文本设为 `"<Name> icon"`，与加粗术语一致。
* 各界面元素对应哪个图标文件，请参阅[术语与命名](terminology.md)。

### 视频 <a id="videos"></a>

不要将视频文件存入 n8n-docs 仓库。将视频托管到外部平台，例如 YouTube、Loom 或其他[支持的域名](https://iframely.com/domains)，再嵌入页面。

嵌入视频时，将 URL 放入 embed 标签：

```
{% embed url="https://www.youtube.com/embed/your-video-id" %}
```

### 代码示例 <a id="code-examples"></a>

使用制表符，不使用空格。n8n 节点 linter 强制要求此约定。Creating nodes（创建节点）章节的代码示例可能被用户复制到节点中，若使用空格，会导致 linter 检查失败。

使用带语言标识的围栏代码块，以启用语法高亮：

````
```typescript
// Your code here
```
````

```typescript
// Your code here
```

GitBook 支持[可选代码块设置](https://gitbook.com/docs/creating-content/blocks/code-block)。在有助于读者理解时，可以添加标题、自动换行或行号：

````
{% code title="MyNode.node.ts" overflow="wrap" lineNumbers="true" %}
```typescript
// Your code here
```
{% endcode %}
````

{% code title="MyNode.node.ts" overflow="wrap" lineNumbers="true" %}
```typescript
// Your code here
```
{% endcode %}

### 为每个功能提供完整示例 <a id="show-worked-examples-for-each-feature"></a>

只要涉及代码、表达式或配置，就提供一个完整示例。读者和编程智能体对示例的依赖超过对说明文字的依赖。

* **先覆盖常见情况，再覆盖容易出错的情况。**先展示直接用法，再展示边界情况，例如空输入、分页和速率限制，以及失败情况，包括读者看到的错误和解决方法。
* **重视多样性，而非数量。**三个各有不同重点的示例，胜过六个近乎相同的示例。不要凑数，应展示不同情况。
* **用行内注释说明意图。**写明每个示例的作用和原因，避免被误认为另一条操作说明。
* **标明每个占位符。**按照[文字格式](#text-formatting)，使用尖括号包裹、以连字符连接的单词，例如 `<your-api-key>` 或 `<YOUR-API-KEY>`，不要使用 `YOUR_KEY` 或真实值。
* **结构化呈现约束，不用长段叙述。**将参数、默认值和限制放入表格或结构定义块中。

展示错误示例时，在旁边配上正确示例。单独留下错误代码，可能会被直接复制使用。

### 提示框 <a id="hints"></a>

提示框也称 admonitions 或 callouts，用于吸引读者注意某些重要信息。提示框有四种样式：`info`、`warning`、`danger`、`success`，使用方式如下：

* `info`：用于常规说明、需要突出显示的信息，以及功能限制提示框，例如功能仅在特定平台或付费层级可用。
* `warning`：用于存在风险或意外行为的情况。
* `danger`：用于安全风险较高的操作，例如向本地 n8n 实例开放隧道，或可能造成永久数据丢失等破坏性操作。
* `success`：用于正向确认或小提示，应少量使用。

**不要滥用提示框，过多会降低其效果。**

使用以下[提示框语法](https://gitbook.com/docs/creating-content/blocks/hint)：

```
{% hint style="info" %}
Some hint content.
{% endhint %}
```

{% hint style="info" %}
提示框的内容。
{% endhint %}

如果要为提示框添加标题块或标题，将其放在提示框第一行：

```
{% hint style="info" %}
## This is the hint title/heading

Some hint content.

{% endhint %}
```

{% hint style="info" %}
### 提示框的标题 <a id="this-is-the-hint-titleheading"></a>

提示框的内容。
{% endhint %}

### 可折叠块 <a id="collapsible-blocks"></a>

与提示框类似，但默认折叠，用户单击后展开。适合放置会使页面显得冗杂的补充细节。

可折叠内容通过标准 HTML `<details>` 块渲染：

```
<details>

<summary>Summary text the user clicks</summary>

Some collapsible content. Standard Markdown works inside the block.

</details>
```

<details>

<summary>供用户单击的摘要文字</summary>

可折叠内容，可在块内使用标准 Markdown。

</details>

### 标签页内容 <a id="tabbed-content"></a>

当内容因平台、编程语言等外部条件而不同时，使用标签页分隔**可能**很有帮助，让用户只看到与自己相关的内容。标签页会影响内容可发现性，应谨慎使用。

标签页仅适用于**简短**的并列变体，原因见[面向智能体的友好文档](agent-friendly-docs.md)。整个标签页块合计应小于约一屏，即约 3,000 个字符。变体内容超出此范围，例如每个都是完整流程，或有四个以上较复杂变体时，取消标签页，在同页为每个变体设置独立标题，让每节都清晰且独立完整。只有合并后的页面会超出[页面长度规范](#page-length-and-granularity)，或变体集合会持续扩展时，才按变体拆为独立页面。将共用设置和说明放在标签页块外，避免在各变体中重复。

标签页内容使用以下语法：

```
{% tabs %}
{% tab title="First tab" %}
The content is rendered following the normal Markdown syntax. To add a list:

* Item one
* Another item
* Still more items
{% endtab %}

{% tab title="Second tab" %}
1. Content for the second tab.
2. No indentation is required.
{% endtab %}
{% endtabs %}
```

{% tabs %}
{% tab title="第一个标签页" %}
内容按常规 Markdown 语法渲染。要添加列表：

* 第一项
* 另一项
* 更多项目
{% endtab %}

{% tab title="第二个标签页" %}
1. 第二个标签页的内容。
2. 无需缩进。
{% endtab %}
{% endtabs %}

### 嵌入式工作流 <a id="embedded-workflows"></a>

可以在页面中嵌入 n8n 工作流，供读者直接在文档中查看和交互。通过模板 API URL 引用已发布模板：

```
{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/1747" %}
```

将已发布模板的 ID 加到 `https://api.n8n.io/workflows/templates/` 后，即可得到模板 API URL。

## 相关资源 <a id="related-resources"></a>

* [n8n 文档贡献指南](./)
* [术语与命名](terminology.md)
* [面向智能体的友好文档](agent-friendly-docs.md)
