---
title: 发送并等待回复操作
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## 等待回复 <a href="#waiting-for-a-response" id="waiting-for-a-response"></a>

选择 **Send and Wait for a Response**（发送并等待回复）操作后，可以发送消息并暂停工作流执行，直到有人确认操作或提供更多信息。

### 回复类型 <a href="#response-type" id="response-type"></a>

可以选择以下等待与审批操作类型：

* **Approval**（审批）：用户可以直接在消息中批准或拒绝。
* **Free Text**（自由文本）：用户可以通过表单提交回复。
* **Custom Form**（自定义表单）：用户可以通过自定义表单提交回复。

可以根据所选回复类型，自定义等待和回复行为。以上所有回复类型都可以配置以下选项：

* **Limit Wait Time**（限制等待时间）：是否在指定时间限制后自动恢复工作流执行。可以设置一段时长，也可以指定具体时间。
* **Append n8n Attribution**（附加 n8n 标识）：开启时，在消息中说明该消息由 n8n 自动发送；关闭时不附加此说明。

### 自定义审批回复 <a href="#approval-response-customization" id="approval-response-customization"></a>

使用 Approval 回复类型时，可以选择只显示批准按钮，或同时显示批准*和*拒绝按钮。

也可以自定义所显示按钮的文字。

### 自定义自由文本回复 <a href="#free-text-response-customization" id="free-text-response-customization"></a>

使用 Free Text 回复类型时，可以自定义消息按钮文字、表单标题和描述，以及回复按钮文字。

### 自定义表单回复 <a href="#custom-form-response-customization" id="custom-form-response-customization"></a>

使用 Custom Form 回复类型时，可以使用所需的字段和选项构建表单。

可以使用 [n8n Form 触发器的表单元素](../../../../../integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md#form-elements)中介绍的设置，自定义各表单元素。要添加更多字段，选择 **Add Form Element**（添加表单元素）按钮。

也可以自定义消息按钮文字、表单标题和描述，以及回复按钮文字。
