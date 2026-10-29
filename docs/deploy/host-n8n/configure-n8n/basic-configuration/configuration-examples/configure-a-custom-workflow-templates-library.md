---
title: 配置自定义工作流模板库
description: 为自托管 n8n 实例设置自定义工作流模板库。
contentType: howto
nodeTitle: 配置自定义工作流模板库
originalFilePath: hosting/configuration/configuration-examples/custom-templates.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/custom-templates
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 配置自定义工作流模板库 <a href="#configure-a-custom-workflow-templates-library" id="configure-a-custom-workflow-templates-library"></a>

n8n 提供工作流模板[^1]库。自托管 n8n 时，可以选择：

* 继续使用 n8n 的工作流模板库，这是默认行为。
* 禁用工作流模板。
* 创建自己的工作流模板库。

## 禁用工作流模板 <a href="#disable-workflow-templates" id="disable-workflow-templates"></a>

{% include "../../../../../reusable-content/.gitbook/includes/workflows/templates/disable-templates.md" %}

## 使用自己的工作流模板库 <a href="#use-your-own-workflow-templates-library" id="use-your-own-workflow-templates-library"></a>

{% include "../../../../../reusable-content/.gitbook/includes/workflows/templates/custom-templates-library.md" %}

## 将工作流添加到 n8n 模板库 <a href="#add-your-workflows-to-the-n8n-library" id="add-your-workflows-to-the-n8n-library"></a>

{% include "../../../../../reusable-content/.gitbook/includes/workflows/templates/submit-templates.md" %}

[^1]: n8n 模板是 n8n 和社区成员设计的预构建工作流，可以导入到自己的 n8n 实例中。使用模板时，可能需要填写凭据并调整配置，以满足实际需求。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
