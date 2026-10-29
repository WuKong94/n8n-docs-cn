---
title: Brandfetch 节点文档
description: 了解如何在 n8n 中使用 Brandfetch 节点，并按照技术文档将 Brandfetch 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Brandfetch 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.brandfetch.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Brandfetch 节点 <a href="#brandfetch-node" id="brandfetch-node"></a>

使用 Brandfetch 节点自动处理 Brandfetch 中的工作，并将其与其他应用集成。n8n 内置支持多种 Brandfetch 功能，包括获取标志、颜色和品牌数据。

本页列出了 Brandfetch 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Brandfetch 凭据](../credentials/brandfetch.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Return Logos, Symbols and Icon**（返回标志、符号和图标）：获取品牌标志的全部变体，包括符号和图标。
* **Return Accent and Brand Colors**（返回强调色和品牌色）：获取品牌的强调色与品牌配色。
* **Return All of a Brand's Data**（返回品牌的全部数据）：获取所有可用的 Brandfetch 属性，包括名称、描述、标志、颜色、公司数据等。
* **Return Brand Context**（返回品牌背景）：获取互联网上任意公司的结构化品牌背景，包括表达风格、使命、定位、受众和竞争对手等。

## 标识符类型 <a id="identifier-types"></a>

所有操作都需要通过 **Type**（类型）和 **Identifier**（标识符）确定品牌。

从以下选项中选择 **Type**：

* **Domain**（域名）：公司网站的域名，例如 `n8n.io`。
* **Stock/ETF Ticker**（股票或 ETF 代码）：股票或 ETF 的交易代码，例如 `AAPL`。
* **Crypto Symbol**（加密货币符号）：加密货币的代码，例如 `BTC`。
* **ISIN**：国际证券识别码，例如 `US0378331005`。

在 **Identifier** 字段中输入对应值。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Brandfetch 集成模板](https://n8n.io/integrations/brandfetch)，或[搜索所有模板](https://n8n.io/workflows/)
