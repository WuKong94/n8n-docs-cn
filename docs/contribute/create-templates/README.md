---
description: 创建、测试工作流模板，并将其提交到 n8n 模板库。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 创建工作流模板 <a id="create-workflow-templates"></a>

将解决实际问题的工作流提交到 [n8n 模板库](https://n8n.io/workflows/)，与他人分享。

模板包含工作流和设置说明。其他人应能导入模板、按照说明操作并获得预期结果。Creator 门户会自动生成标题和描述，因此无需自行编写。

## 本节内容 <a id="in-this-section"></a>

* [模板提交指南](submission-guidelines.md)：选择有用的问题、检查工作内容，并在提交前测试工作流。
* [为模板添加便笺](sticky-note-guidelines.md)：在画布上说明工作流及其设置方式。
* [工作流模板创意](workflow-template-ideas.md)：寻找使用场景，并将其发展为完整解决方案。

## 提交模板 <a id="submit-a-template"></a>

提交模板需要[创作者账号](https://creators.n8n.io/register)。

1. 阅读[提交指南](submission-guidelines.md)，选择能够为模板库增加价值的使用场景。
2. 构建工作流，为节点设置含义清晰的名称，并添加必需的便笺。
3. 从头到尾测试工作流，包括说明中覆盖的执行路径和输入。
4. [将工作流导出为 JSON](../../build/manage-workflows/export-and-import.md)。移除密钥、个人数据，以及对自己账号或资源的引用。
5. 将该 JSON 导入新的工作流。按照自己的设置说明操作并检查输出，补齐缺失的步骤或依赖。
6. 登录 [Creator 门户](https://creators.n8n.io/login)并提交 JSON。

{% hint style="info" %}
**欢迎使用 AI 辅助**

可以使用 AI 构建工作流和编写设置说明。提交前，请检查每个部分、测试导出的工作流并修正说明。你需要对最终结果负责。
{% endhint %}

## 模板审核 <a id="template-review"></a>

n8n 会按模板指南审核投稿。符合要求后，n8n 会发布模板并发送确认邮件；如需修改，会通过邮件反馈。

新创作者一次只能提交一个模板。请等 n8n 批准当前投稿后，再提交下一个。

三个模板获批后，即成为认证创作者。认证创作者会获得网站徽标，可以每批提交最多四个模板，并可以提供付费模板。

## 提供付费模板 <a id="offer-paid-templates"></a>

只有认证创作者才能提供付费模板。免费和付费模板适用相同的质量、测试和文档要求。

你需要自行追踪付款，在买家购买后交付模板，并确保买家能够持续访问。未交付付费模板可能导致账号暂停或封禁。

## 相关资源 <a id="related-resources"></a>

* [为 n8n 作贡献](../)
* [创建节点](../../connect/create-nodes/README.md)
* [n8n 文档贡献指南](../contribution-guide-for-n8n-docs/README.md)
* [获取帮助的途径](../where-to-get-help.md)
* [使用工作流模板](../../build/ways-of-building-workflows/use-templates.md)
