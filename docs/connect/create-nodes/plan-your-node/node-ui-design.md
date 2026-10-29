---
contentType: reference
nodeTitle: 节点界面设计
originalFilePath: integrations/creating-nodes/plan/node-ui-design.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/plan/node-ui-design
url: https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设计节点的用户界面 <a href="#design-your-nodes-user-interface" id="design-your-nodes-user-interface"></a>

大多数节点是 API 的图形用户界面（GUI）。设计界面，就是以易用的方式呈现 API 端点和参数。直接将整个 API 映射为节点中的表单字段，不一定能带来良好的用户体验。

本文提供应遵循的设计指南和标准，与 n8n 自身采用的标准相同，有助于用户混合使用社区节点和内置节点时获得流畅、一致的体验。

## 设计指南 <a href="#design-guidance" id="design-guidance"></a>

所有节点都使用 n8n 的[节点界面元素](../build-your-node/reference/node-ui-elements.md)，因此无需考虑颜色、边框等样式细节。不过，仍建议遵循基本设计流程：

* 阅读待集成 API 的文档，并思考：
    * 哪些内容可以省略？
    * 哪些内容可以简化？
    * API 的哪些部分容易令人困惑？如何帮助用户理解？
* 使用线框图工具尝试布局字段。如果字段过多、界面开始难以理解，请参考 n8n 关于[显示和隐藏字段](#showing-and-hiding-fields)的建议。

## 标准 <a href="#standards" id="standards"></a>

### 界面文本样式 <a href="#ui-text-style" id="ui-text-style"></a>

| 元素 | 样式 |
| ------- | ----- |
| 下拉选项值 | 标题式大小写（Title case） |
| 提示 | 句首大写（Sentence case） |
| 信息框 | 句首大写。只有一句话时不加句点（`.`），多于一句时必须加句点。此字段可包含链接，链接应在新选项卡中打开。 |
| 节点名称 | 标题式大小写（Title case） |
| 参数名称 | 标题式大小写（Title case） |
| 副标题 | 标题式大小写（Title case） |
| 工具提示 | 句首大写。只有一句话时不加句点（`.`），多于一句时必须加句点。此字段可包含链接，链接应在新选项卡中打开。 |

### 界面文本术语 <a href="#ui-text-terminology" id="ui-text-terminology"></a>

* 使用与节点所连接服务相同的术语。例如，Notion 将相关元素称为 block，因此 Notion 节点应使用 Notion 块，而不是 Notion 段落。此规则有例外，通常是为了避免技术术语，例如 [upsert 操作的名称和描述](#upsert-operations)指南。
* 服务的 API 与图形界面有时会使用不同术语。节点应采用图形界面中的用语，因为多数用户更熟悉它。如果认为部分用户需要查阅服务的 API 文档，可考虑在提示中补充对应信息。
* 存在更简单的说法时，不要使用技术术语。
* 命名应保持一致。例如，选择 `directory` 或 `folder` 之一，并一直使用。

### 节点命名约定 <a href="#node-naming-conventions" id="node-naming-conventions"></a>

| 约定 | 正确 | 错误 |
| ---------- | ------- | --------- |
| 如果是触发节点，<br>显示名称应以“Trigger”结尾，<br>前面加一个空格。 | Shopify Trigger | ShopifyTrigger, Shopify trigger |
| 名称中不要包含“node”。 | Asana | Asana Node, Asana node |

### 显示和隐藏字段 <a href="#showing-and-hiding-fields" id="showing-and-hiding-fields"></a>

字段可以：

* 打开节点时就显示：适用于资源、操作和必填字段。
* 隐藏在 **Optional fields**（可选字段）中，直到用户点击该部分才显示：适用于可选字段。

逐步呈现复杂度：在前置依赖字段尚未填写时，隐藏依赖它的字段。例如，有 **Filter by date**（按日期筛选）开关和 **Date to filter by**（筛选日期）日期选择器时，应在用户启用 **Filter by date** 后再显示 **Date to filter by**。


### 各类字段的约定 <a href="#conventions-by-field-type" id="conventions-by-field-type"></a>

#### 凭据 <a href="#credentials" id="credentials"></a>

n8n 会自动将凭据字段显示在节点顶部。

#### 资源与操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

API 通常对数据执行某种操作。例如，“获取所有任务”中，“任务”是资源，“获取所有”是操作。

节点采用这种资源与操作模式时，第一个字段应为 **Resource**（资源），第二个字段应为 **Operation**（操作）。

#### 必填字段 <a href="#required-fields" id="required-fields"></a>

字段按以下方式排序：

* 从最重要到最不重要。
* 按范围从大到小。例如，**Document**（文档）、**Page**（页面）和 **Text to insert**（要插入的文本）应依此顺序排列。

#### 可选字段 <a href="#optional-fields" id="optional-fields"></a>

* 按字母顺序排列。可通过重命名将相关内容放在一起。例如，将 **Email** 和 **Secondary Email** 改为 **Email (primary)**（主要邮箱）和 **Email (secondary)**（次要邮箱）。
* 如果未设置可选字段时节点会使用默认值，请预填该默认值，并在字段描述中说明，例如 **Defaults to false**（默认为 false）。
* 关联字段：如果一个可选字段依赖另一个，请将二者组合在单个选项下，选择后同时显示。
* 可选字段很多时，考虑按主题分组。

#### 帮助 <a href="#help" id="help"></a>

图形界面内置五类帮助：

* 信息框：显示在字段之间的黄色框，详情请参阅[界面元素 | Notice](../build-your-node/reference/node-ui-elements.md#notice)。
    * 用于重要信息，避免滥用。较少出现能让信息框更突出，更容易吸引用户注意。
* 参数提示：显示在用户输入字段下方的文本。用户需要了解某些信息，但使用信息框又过于突出时，可采用参数提示。
* 节点提示：在输入面板、输出面板或节点详情视图中提供帮助。详情请参阅[界面元素 | Hints](../build-your-node/reference/node-ui-elements.md#hints)。
* 工具提示：用户悬停在工具提示图标 ![工具提示图标：灰色圆圈中的问号](../../.gitbook/assets/help-tooltip.png) 上时显示的浮层，用于提供用户可能需要的额外信息。
    * 无需为每个字段都提供工具提示，仅在有用时添加。
    * 编写工具提示时，应考虑用户需求，不要直接复制粘贴 API 参数描述。如果原描述难懂或有错误，请改进它。
* 占位文本：用户尚未输入值时，n8n 可在字段中显示占位文本，帮助用户了解应填写的内容。

信息框、提示和工具提示可包含指向更多信息的链接。

#### 错误 <a href="#errors" id="errors"></a>

明确标示必填字段。

尽可能为字段添加验证规则。例如，要求邮箱的字段可检查邮箱格式是否有效。

显示错误时，红色错误标题中只显示主要错误消息，更多信息放在 **Details**（详情）中。

更多信息请参阅[节点错误处理](../build-your-node/reference/error-handling.md)。

#### 开关 <a href="#toggles" id="toggles"></a>

* 二元状态的工具提示应以 **Whether to . . .**（是否……）之类的表述开头。
* 某些情况应使用列表而非开关：
    * false 状态含义明确时，使用开关。例如 **Simplify Output?**（是否简化输出）：另一种状态“不简化输出”很明确。
    * 需要更清晰地表达含义时，使用带有明确选项名称的下拉列表。例如 **Append?**（是否追加）：不追加时会发生什么并不明确，可能是不处理、覆盖或丢弃信息。

#### 列表 <a href="#lists" id="lists"></a>

* 尽可能为列表设置默认值，应选择最常用的选项。
* 按字母顺序排列列表选项。
* 可为列表选项添加描述，但仅在提供有用信息时添加。
* 如果有 **All**（全部）之类的选项，请使用 **All** 这个词，不要使用 ***** 之类的简写。

#### 触发节点输入 <a href="#trigger-node-inputs" id="trigger-node-inputs"></a>

触发节点包含用于指定触发事件的参数时：

* 将参数命名为 **Trigger on**（触发事件）。
* 不要添加工具提示。

#### 副标题 <a href="#subtitles" id="subtitles"></a>

根据主要参数的值设置副标题，例如：

```js
subtitle: '={{$parameter["operation"] + ": " + $parameter["resource"]}}',
```

#### ID <a href="#ids" id="ids"></a>

对特定记录执行操作（例如“更新任务评论”）时，需要提供指定待修改记录的方式。

* 尽可能提供两种指定记录的方式：
    * 从预填列表中选择。可使用 `loadOptions` 参数生成此列表，更多信息请参阅[基础文件](../build-your-node/reference/base-files/README.md)。
    * 输入 ID。
* 将字段命名为 `<Record name> name or ID`，例如 **Workspace Name or ID**（工作区名称或 ID）。添加工具提示：“从列表中选择名称，或使用表达式指定 ID。”并链接到 n8n 的[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)文档。
* 设计节点时，应允许用户提供超出要求的信息。例如：
    * 需要相对路径时，也能处理用户粘贴的绝对路径。
    * 用户需要从 URL 获取 ID 时，也能处理粘贴的完整 URL。

#### 日期与时间戳 <a href="#dates-and-timestamps" id="dates-and-timestamps"></a>

n8n 使用 [ISO 时间戳字符串](https://en.wikipedia.org/wiki/ISO_8601)表示日期和时间。新增的日期或时间戳字段应支持全部 ISO 8601 格式。

#### JSON <a href="#json" id="json"></a>

对于要求 JSON 的文本输入，应支持两种内容指定方式：

* 直接在文本框中输入 JSON：需要将输入字符串解析为 JSON 对象。
* 使用返回 JSON 的表达式。



#### 节点图标 <a href="#node-icons" id="node-icons"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/creating-nodes/node-icons.md" %}


### 常见模式与例外 <a href="#common-patterns-and-exceptions" id="common-patterns-and-exceptions"></a>

本节介绍常见设计模式，包括边界情况及主要标准的例外。

#### 简化响应 <a href="#simplify-responses" id="simplify-responses"></a>

API 可能返回大量无用数据，可考虑添加开关，让用户选择是否简化响应：

  * 名称：**Simplify Response**（简化响应）。
  * 描述：**Whether to return a simplified version of the response instead of the raw data**（是否返回简化的响应，而非原始数据）。

#### Upsert 操作 <a href="#upsert-operations" id="upsert-operations"></a>

此操作应始终独立提供，并使用：

  * 名称：**Create or Update**（创建或更新）。
  * 描述：**Create a new record, or update the current one if it already exists (upsert)**（创建新记录，如果已存在则更新当前记录，即 upsert）。

#### 布尔运算符 <a href="#boolean-operators" id="boolean-operators"></a>

n8n 图形界面对 AND、OR 等布尔运算符的组合支持不佳。尽可能提供“全部使用 AND”或“全部使用 OR”的选项。


例如，有一个 **Must match**（必须匹配）字段用于判断值是否匹配，应将 **Any**（任意）和 **All**（全部）作为两个独立选项。

#### 源键或二进制属性 <a href="#source-keys-or-binary-properties" id="source-keys-or-binary-properties"></a>

二进制数据是电子表格、图片等文件数据。在 n8n 中，需要使用命名键引用这些数据。不要将此字段称为“binary data”（二进制数据）或“binary property”（二进制属性），应使用更明确的名称：**Input data field name**（输入数据字段名称）或 **Output data field name**（输出数据字段名称）。

## 相关资源 <a id="related-resources"></a>

* [规划节点](./)
* [选择节点类型](choose-a-node-type.md)
* [选择节点开发方式](choose-a-node-building-style.md)
* [选择节点文件结构](choose-node-file-structure.md)






