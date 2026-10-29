---
title: AWS Certificate Manager 节点
description: 了解如何在 n8n 中使用 AWS Certificate Manager 节点，并将其集成到工作流。
contentType:
- integration
- reference
nodeTitle: AWS Certificate Manager 节点
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS Certificate Manager 节点 <a href="#aws-certificate-manager-node" id="aws-certificate-manager-node"></a>

使用 AWS Certificate Manager 节点自动处理 AWS Certificate Manager 中的工作，并将其与其他应用集成。n8n 内置支持多种 AWS Certificate Manager 功能，包括删除、获取和续期 SSL 证书。译注：原文还提及创建证书，但本页操作列表及所核对版本的节点源码未提供创建操作。

本页列出了 AWS Certificate Manager 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [AWS Certificate Manager 凭据](../credentials/aws.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Certificate（证书）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多个）
    * Get Metadata（获取元数据）
    * Renew（续期）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS Certificate Manager 集成模板](https://n8n.io/integrations/aws-certificate-manager)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AWS Certificate Manager 文档](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

