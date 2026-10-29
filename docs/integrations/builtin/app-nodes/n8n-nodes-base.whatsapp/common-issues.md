---
title: WhatsApp Business Cloud 节点常见问题
description: 了解 n8n 工作流自动化平台中 WhatsApp Business Cloud 节点的常见问题，包括问题详情和建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: WhatsApp Business Cloud 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# WhatsApp Business Cloud 节点常见问题 <a href="#whatsapp-business-cloud-node-common-issues" id="whatsapp-business-cloud-node-common-issues"></a>

本页介绍 [WhatsApp Business Cloud 节点](README.md)的一些常见错误和问题，以及解决或排查步骤。

## Bad request - please check your parameters（请求无效，请检查参数） <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

当 WhatsApp Business Cloud 因参数问题拒绝请求时，会出现此错误。使用 **Send Template**（发送模板）操作时，如果发送的数据与模板格式不匹配，就常会遇到此问题。

要解决此问题，请检查[消息模板](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)中的参数，注意每个参数的数据类型及其在模板中的定义顺序。

检查 n8n 映射到模板参数的数据。如果使用表达式设置参数值，请检查输入数据，确保每个数据项都能解析为有效值。可以使用 [Edit Fields (Set) 节点](../../core-nodes/n8n-nodes-base.set.md)，或设置回退值，确保发送的值格式正确。

## 处理非文本媒体 <a href="#working-with-non-text-media" id="working-with-non-text-media"></a>

WhatsApp Business Cloud 节点可以处理非文本消息，以及图片、音频、文档等媒体。

如果操作包含 **Input Data Field Name**（输入数据字段名称）或 **Property Name**（属性名称）参数，请将其设为字段名称本身，而不是使用表达式引用字段数据。

例如，要发送“Image”（图片）类型的 **MessageType**（消息类型），并将 **Take Image From**（图片来源）设为“n8n”时，应将 **Input Data Field Name**（输入数据字段名称）设为 `data` 这样的字段名称，而不是 `{{ $json.input.data }}` 这样的表达式。
