---
title: MCP 凭据
description: MCP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MCP 服务器的身份验证。
layout:
  description:
    visible: false
contentType:
- integration
- reference
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MCP 凭据 <a id="mcp-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [MCP Client Tool（客户端工具）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)

## 前置条件 <a id="prerequisites"></a>

需要一个支持 OAuth2 身份验证的 MCP 服务器。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

* OAuth2

## 使用 OAuth2 <a id="using-oauth2"></a>

此凭据扩展了 n8n 通用的 [OAuth2 API 凭据](./httprequest.md#using-oauth2)，为 MCP 授权流程增加两个字段：

* **Use Dynamic Client Registration**（使用动态客户端注册）：默认开启。开启时，n8n 自动向 MCP 服务器注册为 OAuth2 客户端（[RFC 7591](https://www.rfc-editor.org/rfc/rfc7591)），无需手动创建应用或粘贴 Client ID 和 Client Secret。如果 MCP 服务器不支持动态客户端注册，或已经从服务器自身的开发者设置中取得 Client ID 和 Client Secret，请关闭此选项。此时，与其他通用 OAuth2 凭据一样，填写标准 OAuth2 字段：**Authorization URL**（授权 URL）、**Access Token URL**（访问令牌 URL）、**Client ID**（客户端 ID）和 **Client Secret**（客户端密钥）。
* **Resource URL**（资源 URL）：可选。MCP 服务器要求的确切受保护资源 URL。留空可让 n8n 自动从服务器发现该地址。

{% hint style="info" %}
**动态客户端注册出现问题？**

如果在 OAuth2 流程中遇到重定向 URI 不匹配或无效的错误，请确认 MCP 服务器的动态客户端注册端点配置为接受 n8n 的 OAuth Redirect URL，且与凭据中显示的值完全一致。
{% endhint %}
