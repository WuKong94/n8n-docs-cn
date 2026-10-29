---
title: Cisco Umbrella 凭据
description: Cisco Umbrella 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Cisco Umbrella 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Cisco Umbrella 凭据
originalFilePath: integrations/builtin/credentials/ciscoumbrella.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella
url: https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cisco Umbrella 凭据 <a href="#cisco-umbrella-credentials" id="cisco-umbrella-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Cisco DevNet 开发者账号](https://developer.cisco.com)。
- 一个具有 **Full Admin（完全管理员）** 角色的 [Cisco Umbrella 用户账号](https://umbrella.cisco.com/)。

## 身份验证方式 <a href="#authentication-methods" id="authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cisco Umbrella API 文档](https://developer.cisco.com/docs/cloud-security/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/cisco-umbrella/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**
- 一个 **Secret（密钥机密值）**：生成 API 密钥时提供

创建 Umbrella API 密钥的方法，请参阅 [Cisco Umbrella 的管理 API 密钥文档](https://developer.cisco.com/docs/cloud-security/authentication/#manage-api-keys)。
