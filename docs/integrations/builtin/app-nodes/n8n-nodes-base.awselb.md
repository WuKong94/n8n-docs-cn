---
title: AWS Elastic Load Balancing 节点文档
description: 了解如何在 n8n 中使用 AWS Elastic Load Balancing 节点，并按照技术文档将 AWS Elastic Load
  Balancing 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: AWS Elastic Load Balancing 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.awselb.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS Elastic Load Balancing 节点 <a href="#aws-elastic-load-balancing-node" id="aws-elastic-load-balancing-node"></a>

使用 AWS Elastic Load Balancing 节点自动处理 AWS ELB 中的工作，并将 AWS ELB 与其他应用集成。n8n 内置支持多种 AWS ELB 功能，包括添加、获取、移除和删除证书与负载均衡器。

本页列出了 AWS ELB 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

身份验证设置说明，请参阅 [AWS ELB 凭据](../credentials/aws.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Listener Certificate（监听器证书）
	* Add（添加）
	* Get Many（获取多条）
	* Remove（移除）
* Load Balancer（负载均衡器）
	* Create（创建）
	* Delete（删除）
	* Get（获取）
	* Get Many（获取多条）

此节点支持创建和管理应用程序负载均衡器与网络负载均衡器，目前不支持网关负载均衡器。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 AWS Elastic Load Balancing 集成模板](https://n8n.io/integrations/aws-elb)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [AWS ELB 文档](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}

