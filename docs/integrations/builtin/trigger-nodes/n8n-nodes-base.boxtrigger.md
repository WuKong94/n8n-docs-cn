---
title: Box 触发器节点文档
description: 了解如何在 n8n 中使用 Box 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Box 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Box 触发器节点 <a href="#box-trigger-node" id="box-trigger-node"></a>

[Box](https://www.box.com/) 是一家云计算公司，提供文件共享、协作等工具，用于处理上传到其服务器的文件。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Box 凭据文档](../credentials/box.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Box Trigger 集成](https://n8n.io/integrations/box-trigger/)页面。
{% endhint %}

## 查找 Box Target ID <a href="#find-your-box-target-id" id="find-your-box-target-id"></a>

获取 Box 中的 Target ID：

1. 打开要监控的文件或文件夹。
2. 复制 URL 中 `folder/` 后面的字符串，即目标 ID。例如，URL 为 `https://app.box.com/folder/12345` 时，目标 ID 为 `12345`。
3. 将其粘贴到 n8n 的 **Target ID** 字段。

