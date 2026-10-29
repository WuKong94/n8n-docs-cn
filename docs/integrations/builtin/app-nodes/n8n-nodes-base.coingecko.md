---
title: CoinGecko 节点文档
description: 了解如何在 n8n 中使用 CoinGecko 节点，并按照技术文档将 CoinGecko 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: CoinGecko 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.coingecko.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.coingecko
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.coingecko
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# CoinGecko 节点 <a href="#coingecko-node" id="coingecko-node"></a>

使用 CoinGecko 节点自动处理 CoinGecko 中的工作，并将其与其他应用集成。n8n 内置支持多种 CoinGecko 功能，包括获取加密货币和事件。

本页列出了 CoinGecko 节点支持的操作，并提供更多资源的链接。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Coin（币种）
    * 获取所选币种的开盘价、最高价、最低价和收盘价（OHLC）蜡烛图。
    * Get current data for a coin（获取币种的当前数据）
    * Get all coins（获取全部币种）
    * 获取某个币种在指定日期的历史数据，包括名称、价格、市场和统计信息。
    * 获取与所选币种匹配的全部交易对的价格及市场相关数据。
    * 获取历史市场数据，包括价格、市值和 24 小时交易量，粒度自动确定。
    * 获取任意加密货币以所需的其他受支持货币计价的当前价格。
    * Get coin tickers（获取币种的行情数据）
* Event（事件）
    * Get all events（获取全部事件）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 CoinGecko 集成模板](https://n8n.io/integrations/coingecko)，或[搜索所有模板](https://n8n.io/workflows/)
