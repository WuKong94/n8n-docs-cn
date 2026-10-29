---
description: n8n Docs 如何定义面向智能体的友好文档，以及这一标准与风格指南的关系。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 面向智能体的友好文档 <a id="agent-friendly-docs"></a>

人类和 AI 智能体都会阅读 n8n 文档。两类用户对文档的需求大多相同，但智能体在高效解析和浏览文档时，也有一些特定需求。

本文说明 n8n Docs 如何定义“对智能体友好”，以及它为何重要。这些指南适用于文档贡献者，也适用于希望了解 n8n 文档编写方式的用户。

## 为什么这对 n8n 文档很重要 <a id="why-this-matters-for-n8n-docs"></a>

有两类相互重叠的读者，会通过智能体而非浏览器使用 n8n 文档：

* **人们向 AI 智能体提问，而非自行搜索。**越来越多的文档访问来自 AI 助手和搜索智能体：它们检索页面来回答问题，而不是由用户点击网站导航后直接阅读。
* **人们使用编程智能体开发 n8n 内容。**编写工作流、节点或集成时，越来越多用户会借助 AI 编程工具。这些工具直接检索 n8n 文档，以最新、准确的信息为依据，避免依赖过时的训练数据。

## “对智能体友好”的含义 <a id="what-agent-friendly-means"></a>

这一标准分为四个层面。

### 机器可读的内容交付 <a id="machine-readable-delivery"></a>

智能体需要无需渲染完整网页就能获取内容的方式。n8n 文档提供多种入口：

* **Markdown：**每个页面都提供简洁的 Markdown 版本，而非仅有渲染后的 HTML。
* **llms.txt：**[`llms.txt`](https://docs.n8n.io/llms.txt) 和 [`llms-full.txt`](https://docs.n8n.io/llms-full.txt) 列出所有已发布页面，供支持此格式的智能体使用。
* **MCP 服务器：**通过 MCP 服务器直接向 MCP 客户端提供文档。请参阅[连接 n8n 文档 MCP 服务器](../../connect/connect-to-n8n-docs-mcp-server.md)。
* **AI 搜索：**由 Kapa.ai 提供支持的 AI 搜索，直接根据文档、博客和社区论坛回答问题。
* **Context7：**[Context7](https://context7.com/) 会为 n8n 文档建立索引，让编辑器中的编程智能体在开发过程中检索最新文档。

### 全站一致性 <a id="site-wide-consistency"></a>

* **术语：**n8n 文档在所有页面中对同一概念使用相同术语，减少读者和智能体的困惑。请参阅[术语与命名](terminology.md)。
* **稳定的 URL：**页面重命名时保持 URL 稳定；确需更改 URL 时，设置重定向。
* **功能可用范围：**依赖特定 n8n 版本或方案的信息，应放在其实际适用范围内：适用于整页或整节时使用提示框，顺带提及时写在正文中，适用于某表格行时放在对应单元格中。这样，即使智能体只检索到页面片段，也能获得正确上下文。请参阅[功能可用范围](style-guide-for-n8n-docs.md#feature-availability)。
* **审核流程：**新页面和修改内容在发布前，会在 n8n 文档的[公开 GitHub 仓库](https://github.com/n8n-io/n8n-docs)中接受人工审核，以及 n8n 文档 AI 审核工具 [cubic](https://www.cubic.dev/) 的检查，核对一致性和技术准确性。

### 结构与导航 <a id="structure-and-navigation"></a>

* **页面长度：**n8n 文档将内容拆分为主题明确的页面，使智能体能够在不被截断的情况下检索。搜索功能和文档助手按 `##`/`###` 标题划分内容，每次检索一个章节。过小的页面或章节反而会与无关的相邻内容合并。将主题过度拆分为许多小页面，会明显降低回答质量。请参阅[页面长度与粒度](style-guide-for-n8n-docs.md#page-length-and-granularity)。
* **章节独立完整：**每节都能独立理解，不依赖“如上所述”等指代。智能体可能只获取页面的一个片段或章节，甚至只有标题，而非全文。请参阅[让每节内容独立完整](style-guide-for-n8n-docs.md#keep-each-section-self-contained)。
* **开头直接回答：**每页在 H1 标题之后，用一句通俗语言直接回答主题问题。AI 助手和搜索界面经常只将这一句作为引用，因此具体明确的开头能提高被引用的概率和回答准确性。请参阅[以一句话回答开篇](style-guide-for-n8n-docs.md#lead-with-a-one-sentence-answer)。
* **交叉链接：**页面明确链接到前提条件、后续步骤和相关主题，让智能体沿链接浏览，无需猜测 URL。相互链接的页面也会形成主题集群，AI 搜索将其视为内容深度的信号，比起独立页面更愿意引用。请参阅[链接到相关页面、前提条件和后续步骤](style-guide-for-n8n-docs.md#link-to-related-pages-prerequisites-and-next-steps)。

### 内容与示例 <a id="content-and-examples"></a>

* **文字优先于图片：**操作说明应使用易解析的文字，而非放在图片中。智能体和屏幕阅读器只能获取图片的替代文本和文件路径，无法获得图片本身。截图只能辅助确认读者已经从文字中了解到的信息，不能单独承载含义。请参阅[图片](style-guide-for-n8n-docs.md#images)。
* **完整示例：**对于涉及代码、表达式或配置的功能，n8n 文档力求提供完整示例。示例要覆盖常见情况和容易出错的情况，因为智能体会直接复制示例，无法推断未展示的内容。请参阅[为每个功能提供完整示例](style-guide-for-n8n-docs.md#show-worked-examples-for-each-feature)。
* **标签页内容：**标签页应少而简短，因为人一次只看到一个标签页，智能体却会读取全部标签页。请参阅[标签页内容](style-guide-for-n8n-docs.md#tabbed-content)。

## 与风格指南的关系 <a id="how-this-relates-to-the-style-guide"></a>

本文解释背后的原因。[贡献指南](README.md)介绍贡献流程，[风格指南](style-guide-for-n8n-docs.md)提供具体规则。其中多项规则，包括页面长度、章节独立性、内链、功能可用范围、图片和标签页内容，专门用于让文档同时适合人类和智能体阅读。贡献文档时，请直接遵循风格指南。需要了解规则的原因，或考虑是否值得新增规则时，再参考本文。

## 仍在持续发展的部分 <a id="where-this-is-still-evolving"></a>

并非每条指南都有定论。n8n 文档持续测试和研究怎样的文档更适合智能体，并开发新系统来帮助满足这些标准。面向智能体的文档实践变化很快，本文也会随实践成熟而更新。

## 相关资源 <a id="related-resources"></a>

* [n8n 文档贡献指南](./)
* [n8n 文档风格指南](style-guide-for-n8n-docs.md)
* [术语与命名](terminology.md)
