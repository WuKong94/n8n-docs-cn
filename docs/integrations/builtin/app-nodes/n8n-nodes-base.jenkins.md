---
title: Jenkins 节点文档
description: 了解如何在 n8n 中使用 Jenkins 节点，并按照技术文档将 Jenkins 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Jenkins 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jenkins 节点 <a href="#jenkins-node" id="jenkins-node"></a>

使用 Jenkins 节点自动处理 Jenkins 中的工作，并将其与其他应用集成。n8n 内置支持多种 Jenkins 功能，包括列出构建、管理实例，以及创建和复制任务。

本页列出了 Jenkins 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Jenkins 凭据](../credentials/jenkins.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Build（构建）
    * List Builds（列出构建）
* Instance（实例）
    * Cancel quiet down state（取消静默等待状态）
    * 将 Jenkins 置于静默模式，禁止启动新构建，使 Jenkins 准备好关闭。
    * 在支持的环境中立即重启 Jenkins。
    * 在支持的环境中，等没有任务运行时再重启 Jenkins。
    * 等没有任务运行时关闭。
    * 立即关闭 Jenkins。
* Job（任务）
    * Copy a specific job（复制指定任务）
    * Create a new job（创建任务）
    * Trigger a specific job（触发指定任务）
    * Trigger a specific job（触发指定任务）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Jenkins 集成模板](https://n8n.io/integrations/jenkins)，或[搜索所有模板](https://n8n.io/workflows/)
