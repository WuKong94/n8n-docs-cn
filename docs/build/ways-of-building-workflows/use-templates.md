---
description: 使用工作流模板。
contentType: howto
nodeTitle: 使用模板
originalFilePath: workflows/templates.md
originalUrl: https://docs.n8n.io/workflows/templates
url: https://docs.n8n.io/build/ways-of-building-workflows/use-templates
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流模板 <a href="#workflow-templates" id="workflow-templates"></a>

创建新工作流时，可以选择从空工作流开始，也可以使用已有模板[^1]。

模板可以提供：

* 入门帮助：n8n 可能已经有能满足需求的模板。
* 可以构建哪些内容的示例
* 创建自己的工作流时可参考的最佳实践

## 访问模板 <a href="#access-templates" id="access-templates"></a>

选择 <img src="../.gitbook/assets/templates.png" alt="查看模板图标" data-size="line"> **Templates（模板）**，查看模板库。

如果使用 n8n 模板库，会跳转到 [n8n 网站的工作流页面](https://n8n.io/workflows/)进行浏览。如果使用组织提供的自定义模板库，则可以在应用内搜索和浏览模板。


## 将工作流添加到 n8n 模板库 <a href="#add-your-workflow-to-the-n8n-library" id="add-your-workflow-to-the-n8n-library"></a>

{% include "../../reusable-content/.gitbook/includes/workflows/templates/submit-templates.md" %}

## 自托管 n8n：使用自己的模板库 <a href="#self-hosted-n8n-use-your-own-library" id="self-hosted-n8n-use-your-own-library"></a>

{% include "../../reusable-content/.gitbook/includes/workflows/templates/custom-templates-library.md" %}

[^1]: n8n 模板是由 n8n 和社区成员设计的预构建工作流，可以导入自己的 n8n 实例。使用模板时，可能需要填写凭据并按需求调整配置。

## 相关资源 <a id="related-resources"></a>

* [构建工作流的方式](./)
* [使用 n8n Assistant](n8n-assistant.md)
* [使用 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
* [使用 Ask n8n AI](use-the-ai-assistant.md)
* [使用 Chat Hub](chat-hub.md)
