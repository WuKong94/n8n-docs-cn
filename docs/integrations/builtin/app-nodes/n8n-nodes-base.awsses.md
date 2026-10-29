---
title: AWS SES 节点文档
description: 了解如何在 n8n 中使用 AWS SES 节点，并按照技术文档将 AWS SES 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: AWS SES 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awsses.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsses
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsses
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS SES 节点 <a href="#aws-ses-node" id="aws-ses-node"></a>

使用 AWS SES 节点自动处理 AWS SES 中的工作，并将其与其他应用集成。n8n 内置支持多种 AWS SES 功能，包括创建、获取、删除、发送、更新和添加模板与电子邮件。

本页列出了 AWS SES 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [AWS SES 凭据](../credentials/aws.md)。
{% endhint %}

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## 操作 <a href="#operations" id="operations"></a>

* Custom Verification Email（自定义验证邮件）
    * Create a new custom verification email template（创建自定义验证邮件模板）
    * Delete an existing custom verification email template（删除已有自定义验证邮件模板）
    * Get the custom email verification template（获取自定义邮件验证模板）
    * Get all the existing custom verification email templates for your account（获取账户中全部已有自定义验证邮件模板）
    * Add an email address to the list of identities（将电子邮件地址添加到身份列表）
    * Update an existing custom verification email template.（更新已有自定义验证邮件模板）
* Email（电子邮件）
    * Send（发送）
    * Send Template（发送模板）
* Template（模板）
    * Create a template（创建模板）
    * Delete a template（删除模板）
    * Get a template（获取模板）
    * Get all templates（获取全部模板）
    * Update a template（更新模板）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS SES 集成模板](https://n8n.io/integrations/aws-ses)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

