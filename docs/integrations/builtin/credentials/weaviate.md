---
title: Weaviate 凭据
description: Weaviate 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Weaviate 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Weaviate 凭据
originalFilePath: integrations/builtin/credentials/weaviate.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/weaviate
url: https://docs.n8n.io/integrations/builtin/credentials/weaviate
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Weaviate 凭据 <a href="#weaviate-credentials" id="weaviate-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Weaviate Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

如何连接 Weaviate 的更多信息，请参阅 [Weaviate 连接文档](https://docs.weaviate.io/weaviate/connections)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

### 连接类型：Weaviate Cloud <a href="#connection-type-weaviate-cloud" id="connection-type-weaviate-cloud"></a>

创建 [Weaviate Cloud Database](https://docs.weaviate.io/cloud/quickstart)，并[按照这些说明获取以下参数值](https://docs.weaviate.io/cloud/quickstart#13-connect-to-your-weaviate-cloud-instance)：

* **Weaviate Cloud Endpoint**（云端点）
* **Weaviate Api Key**（API 密钥）

注意：Weaviate 提供免费的沙盒选项，供测试使用。

### 连接类型：Custom Connection（自定义连接） <a href="#connection-type-custom-connection" id="connection-type-custom-connection"></a>

此连接类型需要在自己的服务器上[部署 Weaviate](https://docs.weaviate.io/deploy)，并配置为允许 n8n 访问。创建及使用 API 密钥的方法，请参阅 [Weaviate 身份验证文档](https://docs.weaviate.io/deploy/configuration/authentication#api-key-authentication)。

然后可为自定义连接提供以下参数：

* **Weaviate Api Key**（API 密钥）：Weaviate API 密钥。
* **Custom Connection HTTP Host**（自定义连接 HTTP 主机）：HTTP API 调用使用的 Weaviate 实例域名或 IP 地址。
* **Custom Connection HTTP Port**（自定义连接 HTTP 端口）：Weaviate 实例用于 HTTP API 调用的端口，默认值为 8080。
* **Custom Connection HTTP Secure**（自定义连接 HTTP 安全连接）：HTTP API 调用是否通过 HTTPS 连接 Weaviate。
* **Custom Connection gRPC Host**（自定义连接 gRPC 主机）：gRPC 使用的 Weaviate 实例主机名或 IP 地址。
* **Custom Connection gRPC Port**（自定义连接 gRPC 端口）：Weaviate 实例的 gRPC API 端口，默认值为 50051。
* **Custom Connection gRPC Secure**（自定义连接 gRPC 安全连接）：gRPC 是否通过 HTTPS 连接 Weaviate。

社区支持，请参阅 [Weaviate 论坛](https://forum.weaviate.io/)。
