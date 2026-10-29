---
title: Venafi TLS Protect Cloud 节点文档
description: 了解如何在 n8n 中使用 Venafi TLS Protect Cloud 节点，并按照技术文档将 Venafi TLS Protect
  Cloud 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: Venafi TLS Protect Cloud 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Venafi TLS Protect Cloud 节点 <a href="#venafi-tls-protect-cloud-node" id="venafi-tls-protect-cloud-node"></a>

使用 Venafi TLS Protect Cloud 节点自动处理 Venafi TLS Protect Cloud 中的工作，并将其与其他应用集成。n8n 内置支持多种 Venafi TLS Protect Cloud 功能，包括删除和下载证书，以及创建证书请求。

本页列出了 Venafi TLS Protect Cloud 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [Venafi TLS Protect Cloud 凭据](../credentials/venafitlsprotectcloud.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Certificate（证书）
	* Delete（删除）
	* Download（下载）
	* Get（获取）
	* Get Many（获取多条）
	* Renew（续期）
* Certificate Request（证书请求）
	* Create（创建）
	* Get（获取）
	* Get Many（获取多条）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Venafi TLS Protect Cloud 集成模板](https://n8n.io/integrations/venafi-tls-protect-cloud)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Venafi REST API 文档](https://docs.venafi.cloud/api/vaas-rest-api/)。

n8n 还提供：

* Venafi TLS Protect Cloud 的[触发器节点](../trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md)。
* Venafi TLS Protect Datacenter 的[节点](n8n-nodes-base.venafitlsprotectdatacenter.md)。


{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
