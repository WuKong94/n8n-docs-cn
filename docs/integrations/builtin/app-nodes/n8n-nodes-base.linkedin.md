---
title: LinkedIn 节点文档
description: 了解如何在 n8n 中使用 LinkedIn 节点，并按照技术文档将 LinkedIn 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: LinkedIn 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkedin
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkedin
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# LinkedIn 节点 <a href="#linkedin-node" id="linkedin-node"></a>

使用 LinkedIn 节点自动处理 LinkedIn 中的工作，并将其与其他应用集成。n8n 支持创建帖子。

本页列出了 LinkedIn 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [LinkedIn 凭据](../credentials/linkedin.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Post（帖子）
    * Create（创建）

## 参数 <a href="#parameters" id="parameters"></a>

* **Post As**（发布身份）：选择以 **Person**（个人）还是 **Organization**（组织）身份发布。
* **Person Name or ID**（个人名称或 ID）和 **Organization URN**（组织 URN）：输入个人或组织的标识符。<br>

	<div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>以组织身份发布</strong></p><p>以组织身份发布时，在 URN 字段输入组织编号。例如，输入 <code>03262013</code>，不要输入 <code>urn:li:company:03262013</code>。</p></div>
	
* **Text**（文本）：帖子的内容。
* **Media Category**（媒体类别）：帖子中包含图片或文章 URL 时使用。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 LinkedIn 集成模板](https://n8n.io/integrations/linkedin)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LinkedIn API 文档](https://learn.microsoft.com/en-us/linkedin/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}


