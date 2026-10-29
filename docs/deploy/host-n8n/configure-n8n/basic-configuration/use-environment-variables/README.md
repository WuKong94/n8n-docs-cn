---
title: 环境变量概览
description: 自托管 n8n 的配置环境变量概览。
contentType: overview
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 使用环境变量
originalFilePath: hosting/configuration/environment-variables/index.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 环境变量概览 <a href="#environment-variables-overview" id="environment-variables-overview"></a>

本节列出自托管 n8n 时，可用于更改配置设置的环境变量。

{% hint style="info" %}
**通过文件配置**

可以向 n8n 提供[配置文件](../../basic-configuration.md)。也可以为某些变量添加 `_FILE` 后缀，通过单独的文件提供配置。
{% endhint %}

## 本节内容 <a id="in-this-section"></a>

* [Ask n8n AI](ai-assistant.md)：n8n 内置 AI 帮助助手的变量。
* [二进制数据](binary-data.md)：存储和处理二进制数据的变量。
* [凭据](credentials.md)：凭据覆盖和加密的变量。
* [数据库](database.md)：数据库连接与配置的变量。
* [部署](deployment.md)：实例标识、加密和公共 API 的变量。
* [端点](endpoints.md)：自定义 n8n REST 和 Webhook 端点路径的变量。
* [执行](executions.md)：执行超时、数据清理和进程模式的变量。
* [表达式引擎](expression-engine.md)：控制表达式求值的变量。
* [外部数据存储](external-data-storage.md)：在 n8n 数据库之外存储数据的变量。
* [外部钩子](external-hooks.md)：指定外部钩子文件位置的变量。
* [外部密钥](external-secrets.md)：外部密钥库的变量。
* [洞察](insights.md)：Insights 使用情况统计功能的变量。
* [日志](logs.md)：日志级别、格式和目标的变量。
* [许可证](license.md)：激活和管理 n8n 许可证的变量。
* [节点](nodes.md)：排除或包含特定节点的变量。
* [OpenTelemetry](opentelemetry.md)：导出执行追踪的变量。
* [队列模式](queue-mode.md)：通过多个工作进程运行 n8n 的变量。
* [调度器](scheduler.md)：持久调度器的变量。
* [安全](security.md)：加固自托管实例的变量。
* [源代码控制](source-control.md)：基于 Git 的源代码控制变量。
* [SSO](sso.md)：单点登录的变量。
* [SSRF 防护](ssrf-protection.md)：限制工作流节点出站请求的变量。
* [任务运行器](task-runners.md)：配置外部 Code 节点执行的变量。
* [时区与本地化](timezone-and-localization.md)：设置实例时区和区域的变量。
* [用户管理与 2FA](user-management-and-2fa.md)：用户管理和双因素身份验证的变量。
* [工作流](workflows.md)：工作流默认设置和模板的变量。
* [工作流历史](workflow-history.md)：工作流版本历史的变量。

## 相关资源 <a id="related-resources"></a>

* [基础配置](../../basic-configuration.md)
* [配置示例](../configuration-examples/README.md)


