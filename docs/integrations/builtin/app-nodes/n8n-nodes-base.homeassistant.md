---
title: Home Assistant 节点文档
description: 了解如何在 n8n 中使用 Home Assistant 节点，并按照技术文档将 Home Assistant 节点集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: Home Assistant 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Home Assistant 节点 <a href="#home-assistant-node" id="home-assistant-node"></a>

使用 Home Assistant 节点自动处理 Home Assistant 中的工作，并将其与其他应用集成。n8n 内置支持多种 Home Assistant 功能，包括获取、创建和检查摄像头代理、配置、日志、服务和模板。

本页列出了 Home Assistant 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Home Assistant 凭据](../credentials/homeassistant.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Camera Proxy（摄像头代理）
    * Get the camera screenshot（获取摄像头截图）
* Config（配置）
    * Get the configuration（获取配置）
    * Check the configuration（检查配置）
* Event（事件）
    * Create an event（创建事件）
    * Get all events（获取全部事件）
* Log（日志）
    * Get a log for a specific entity（获取指定实体的日志）
    * Get all logs（获取全部日志）
* Service（服务）
    * Call a service within a specific domain（调用指定域中的服务）
    * Get all services（获取全部服务）
* State（状态）
    * Create a new record, or update the current one if it already exists (upsert)（创建新记录；如果已存在则更新现有记录（upsert））
    * Get a state for a specific entity（获取指定实体的状态）
    * Get all states（获取全部状态）
* Template（模板）
    * Create a template（创建模板）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Home Assistant 集成模板](https://n8n.io/integrations/home-assistant)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Home Assistant 文档](https://developers.home-assistant.io/docs/api/rest/)。
