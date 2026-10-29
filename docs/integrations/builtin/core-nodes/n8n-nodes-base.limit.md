---
title: Limit（限制）
description: 工作流自动化平台 n8n 中的 Limit（限制） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
priority: high
nodeTitle: Limit（限制）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.limit.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Limit（限制） <a href="#limit" id="limit"></a>

使用 Limit 节点移除超出指定数量上限的数据项。可选择从输入数据的开头还是末尾保留数据项。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置节点。

### Max Items（最大数据项数） <a href="#max-items" id="max-items"></a>

输入 n8n 应保留的数据项数量上限。如果输入数据超过此值，n8n 会移除超出的数据项。

### Keep（保留） <a href="#keep" id="keep"></a>

需要移除数据项时，选择从输入数据的哪一端保留数据项：

* **First Items**（开头的数据项）：从输入数据的开头保留 **Max Items** 指定数量的数据项。
* **Last Items**（末尾的数据项）：从输入数据的末尾保留 **Max Items** 指定数量的数据项。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Limit（限制） 集成模板](https://n8n.io/integrations/limit)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md" %}
