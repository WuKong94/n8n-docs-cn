---
title: Webhook 节点工作流开发
description: 了解如何在 n8n 工作流中构建、测试和使用 Webhook 节点。
priority: critical
contentType: howto
nodeTitle: Webhook 节点工作流开发
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 工作流开发 <a href="#workflow-development" id="workflow-development"></a>

[Webhook 节点](README.md)的工作方式与其他核心节点略有不同。n8n 建议按以下流程构建、测试并在生产环境使用 Webhook 节点。

n8n 为每个 Webhook 节点生成两个 **Webhook URLs**（Webhook URL）：**Test URL**（测试 URL）和 **Production URL**（生产 URL）。

## 构建与测试工作流 <a href="#build-and-test-workflows" id="build-and-test-workflows"></a>

构建或测试工作流时，使用 **Test**（测试）webhook URL。

使用测试 webhook 时，可以在编辑器界面查看传入数据，方便调试。向测试 webhook 发送数据前，先选择 **Listen for test event**（监听测试事件）来注册 webhook。测试 webhook 保持有效 120 秒。

如果在 localhost 上的[自托管](../../../../deploy/host-n8n/README.md) n8n 实例中使用 Webhook 节点，请以隧道模式运行 n8n：

* [使用 npm 的隧道模式](../../../../deploy/host-n8n/install-options/install-with-npm.md#n8n-with-tunnel)
* [使用 Docker 的隧道模式](../../../../deploy/host-n8n/install-options/install-with-docker.md#n8n-with-tunnel)

## 生产工作流 <a href="#production-workflows" id="production-workflows"></a>

工作流准备就绪后，切换到 **Production**（生产）webhook URL，然后发布工作流。外部服务调用此 webhook URL 时，n8n 会自动运行工作流。

使用生产 webhook 时，确保已保存并发布工作流。生产 webhook 接收的数据不会显示在编辑器界面中。

关于发布工作流的更多信息，请参阅[创建工作流](../../../../build/understand-workflows/create-and-run-workflows.md)。
