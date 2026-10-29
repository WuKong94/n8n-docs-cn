---
title: Google Sheets 节点常见问题
contentType:
- integration
- reference
priority: critical
nodeTitle: Google Sheets 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues
description: 了解 n8n 工作流自动化平台中 Google Sheets 节点的常见问题及解决方法，包括问题详情及建议的处理方式。
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

以下介绍 [Google Sheets 节点](./README.md)的常见错误和问题，以及解决或排查步骤。

## 追加数组 <a href="#append-an-array" id="append-an-array"></a>

要将数据数组插入 Google Sheets，必须先将数组转换为有效的 JSON 键值对格式。

可考虑使用以下节点：

1. [Split Out](../../core-nodes/n8n-nodes-base.splitout.md)（拆分）节点。
2.  [AI Transform](../../core-nodes/n8n-nodes-base.aitransform.md)（AI 转换）节点。例如，可尝试输入：

    ```
    将 languages 数组转换为 JSON 键值对。
    ```
3. [Code](../../core-nodes/n8n-nodes-base.code/README.md)（代码）节点。

## 节点设置后列名发生变化 <a href="#column-names-were-updated-after-the-nodes-setup" id="column-names-were-updated-after-the-nodes-setup"></a>

设置节点后，如果 Google 表格的列名发生变化，就会出现此错误。

要刷新列名，请重新选择 **Mapping Column Mode**（列映射模式），使节点重新获取列名。

列名刷新后，更新节点参数。
