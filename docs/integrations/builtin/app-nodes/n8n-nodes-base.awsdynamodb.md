---
title: AWS DynamoDB 节点文档
description: 了解如何在 n8n 中使用 AWS DynamoDB 节点，并按照技术文档将 AWS DynamoDB 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: AWS DynamoDB 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS DynamoDB 节点 <a href="#aws-dynamodb-node" id="aws-dynamodb-node"></a>

使用 AWS DynamoDB 节点自动处理 AWS DynamoDB 中的工作，并将其与其他应用集成。n8n 内置支持多种 AWS DynamoDB 功能，包括创建、读取、更新和删除数据库中的数据项与记录。

本页列出了 AWS DynamoDB 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [AWS 凭据](../credentials/aws.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Item（数据项）
    * Create a new record, or update the current one if it already exists (upsert/put)（创建新记录；如果已存在则更新现有记录（upsert/put））
    * Delete an item（删除数据项）
    * Get an item（获取数据项）
    * Get all items（获取全部数据项）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS DynamoDB 集成模板](https://n8n.io/integrations/aws-dynamodb)，或[搜索所有模板](https://n8n.io/workflows/)

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

