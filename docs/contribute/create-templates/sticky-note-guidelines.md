---
description: 使用便笺说明模板行为、设置方式和工作流各个部分。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 为模板添加便笺 <a id="add-sticky-notes-to-templates"></a>

添加便笺，让其他人可以直接从工作流画布理解并设置模板。

每个模板都需要一个主概览便笺。包含四个或更多节点的工作流，还需要用分区便笺对相关节点进行分组。

## 添加主概览便笺 <a id="add-the-main-overview-note"></a>

在画布左上角放置一个黄色便笺。内容写 100 到 300 个单词，并使用以下标题：

* `### How it works`：描述工作流的目的、触发方式、主要阶段和结果。
* `### Setup`：列出需要配置的账号、凭据、资源和值。
* `### Customization`：可选，说明用户可以作出的有用调整。

提供足够上下文，让用户无需返回模板库页面就能使用工作流。说明工作流适合谁、会产生什么结果，以及有哪些限制。

以下示例展示销售线索接收工作流的便笺结构。请根据自己的工作流调整，并验证每个步骤：

```markdown
### How it works
This workflow helps sales teams process incoming lead submissions. It checks
required fields, looks for an existing contact in HubSpot, and creates or updates
the matching record. It sends qualified leads to a Slack channel and routes
incomplete submissions for manual review. Matching by email avoids creating a
new contact for each submission from the same person.

### Setup
Connect your HubSpot and Slack credentials. In the configuration node, set the
destination channel and qualification rules. Configure your form to send the
expected name, email, and company fields to the workflow. Send a test submission,
then check the HubSpot record and Slack message. Also test an existing contact
and a submission with a missing email address before publishing the workflow.

### Customization
Change the qualification rules to match your sales process. Update the Slack
message to include the fields your team uses when reviewing a lead.
```

## 使用分区便笺对节点分组 <a id="group-nodes-with-section-notes"></a>

对于包含四个或更多节点的工作流，使用白色便笺标识相关区域；在深色模式下，这些便笺显示为灰色。

拉伸每个便笺，使其覆盖或标识多个节点。使用 `## Validate lead data` 等简短标题，必要时最多补充两行短说明。每个便笺应少于 50 个单词。

说明该部分的目的，不要逐一重复节点名称。例如，说明哪些记录会进入某个分支，或者工作流为何要转换某个字段。

## 突出关键设置步骤 <a id="highlight-a-critical-setup-step"></a>

可以用红色警告便笺提醒关键设置步骤或风险，将其放在对应的单个节点上方。请谨慎、少量使用警告便笺。

例如，说明用户在运行发消息的节点前，必须先修改目标地址。

## 添加操作演示视频 <a id="add-a-walkthrough-video"></a>

对于复杂工作流或面向初学者的工作流，可以考虑添加设置视频。书面说明仍应完整，让用户无需观看视频也能使用模板。

要在便笺中嵌入 YouTube 视频，请使用 `@[youtube](RScKsGfrhs4)`，并将 `RScKsGfrhs4` 替换为视频 ID。

可以将[便笺生成工作流](https://n8n.io/workflows/13868-auto-generate-sticky-notes-and-rename-nodes/)作为起点。提交前，请按这些要求检查生成的便笺和节点名称。

添加便笺后，请按照[提交指南](submission-guidelines.md)测试并准备模板。

## 相关资源 <a id="related-resources"></a>

* [创建工作流模板](./)
* [模板提交指南](submission-guidelines.md)
* [工作流模板创意](workflow-template-ideas.md)
* [添加笔记和说明](../../build/understand-workflows/workflow-components/add-notes-and-documentation.md)
