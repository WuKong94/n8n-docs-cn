---
title: Trellix ePO 凭据
description: Trellix ePO 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Trellix ePO 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Trellix ePO 凭据
originalFilePath: integrations/builtin/credentials/trellixepo.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/trellixepo
url: https://docs.n8n.io/integrations/builtin/credentials/trellixepo
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Trellix ePO 凭据 <a href="#trellix-epo-credentials" id="trellix-epo-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Trellix ePolicy Orchestrator](https://www.trellix.com/products/epo/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Trellix ePO 文档](https://docs.trellix.com/docs/trellix-epolicy-orchestrator-on-prem-web-api-scripting-reference-guide)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/trellix-epo/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 用于连接的 **Username**（用户名）。
- 该用户账户的 **Password**（密码）。

n8n 使用这些字段构造 `-u` 参数，格式为 `-u username:pw`。更多信息请参阅 [Web API 基础](https://docs.trellix.com/docs/web-api-basics)。
