---
title: AWS IAM 节点文档
description: 了解如何在 n8n 中使用 AWS IAM 节点，并按照技术文档将 AWS IAM 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: AWS IAM 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS IAM 节点 <a href="#aws-iam-node" id="aws-iam-node"></a>

使用 AWS IAM 节点自动处理 AWS Identity and Access Management（IAM）中的工作，并将 AWS IAM 与其他应用集成。n8n 内置支持多种 AWS IAM 功能，包括创建、更新、获取和删除用户及群组，以及管理群组成员关系。

本页列出了 AWS IAM 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [AWS 凭据文档](../credentials/aws.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **User**（用户）：
    * **Add to Group**（添加到群组）：将已有用户添加到群组。
    * **Create**（创建）：创建新用户。
    * **Delete**（删除）：删除用户。
    * **Get**（获取）：获取用户。
    * **Get Many**（获取多条）：获取用户列表。
    * **Remove From Group**（从群组移除）：将用户从群组移除。
    * **Update**（更新）：更新已有用户。
* **Group**（群组）：
    * **Create**（创建）：创建新群组。
    * **Delete**（删除）：删除群组。
    * **Get**（获取）：获取群组。
    * **Get Many**（获取多条）：获取群组列表。
    * **Update**（更新）：更新已有群组。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS IAM 集成模板](https://n8n.io/integrations/aws-iam)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关该服务的更多信息，请参阅 [AWS IAM 文档](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
