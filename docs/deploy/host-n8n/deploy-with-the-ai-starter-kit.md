---
title: 自托管 AI 入门套件
description: 使用 n8n 精选的自托管 AI 入门套件，快速获得构建 AI 工作流所需的 AI 组件。
contentType: howto
nodeTitle: 使用 AI 入门套件部署
originalFilePath: hosting/starter-kits/ai-starter-kit.md
originalUrl: https://docs.n8n.io/hosting/starter-kits/ai-starter-kit
url: https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自托管 AI 入门套件 <a href="#self-hosted-ai-starter-kit" id="self-hosted-ai-starter-kit"></a>

自托管 AI 入门套件是一个开放的 Docker Compose 模板，用于快速建立功能完整的本地 AI 和低代码开发环境。

由 [n8n](https://github.com/n8n-io) 精选，将自托管 n8n 平台与一组兼容的 AI 产品和组件组合，帮助你开始构建自托管 AI 工作流。

## 包含哪些内容 <a href="#whats-included" id="whats-included"></a>

✅ [**自托管 n8n**](README.md)：具有 400 多种集成和高级 AI 组件的低代码平台。

✅ [**Ollama**](https://ollama.com/)：跨平台 LLM 平台，用于安装和运行最新的本地 LLM。

✅ [**Qdrant**](https://qdrant.tech/)：开源、高性能向量存储，提供全面的 API。

✅ [**PostgreSQL**](https://www.postgresql.org/)：数据工程中的可靠基础，安全处理大量数据。

## 可以构建什么 <a href="#what-you-can-build" id="what-you-can-build"></a>

⭐️ 可以安排预约的 [AI 智能体](#user-content-fn-1)[^1]{ data-preview}

⭐️ 不泄露数据的企业 PDF 摘要。

⭐️ 用于企业沟通和 IT 运维的更智能 Slack 机器人。

⭐️ 私密、低成本的财务文档分析。

## 获取套件 <a href="#get-the-kit" id="get-the-kit"></a>


前往 [GitHub 仓库](https://github.com/n8n-io/self-hosted-ai-starter-kit)，克隆仓库并开始使用！


{% hint style="info" %}
**仅供测试**

n8n 设计此套件是为了帮助你开始使用自托管 AI 工作流。虽然尚未针对生产环境充分优化，但其中组合的可靠组件可很好地配合，用于概念验证项目。请按需定制，并在用于生产前采取安全保护和加固措施。
{% endhint %}

<a id="user-content-fn-1"></a>
[^1]: AI 智能体是能够响应请求、做出决策并为用户完成实际任务的人工智能系统。它们使用大语言模型（LLM）理解用户输入，并根据可用信息和资源，决定如何最佳处理请求。

## 相关资源 <a id="related-resources"></a>

* [自托管 n8n](./)
* [安装方式](install-options/README.md)
* [配置 n8n](configure-n8n/README.md)
* [保持 n8n 运行](keep-n8n-running/README.md)
* [理解架构](understand-the-architecture/README.md)
* [作为 OEM 集成部署](deploy-as-an-oem-integration/README.md)
* [比较版本](community-edition-features.md)
