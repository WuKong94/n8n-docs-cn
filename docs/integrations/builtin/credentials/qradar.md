---
title: QRadar 凭据
description: QRadar 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 QRadar 的身份验证。
contentType:
- integration
- reference
nodeTitle: QRadar 凭据
originalFilePath: integrations/builtin/credentials/qradar.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/qradar
url: https://docs.n8n.io/integrations/builtin/credentials/qradar
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# QRadar 凭据 <a href="#qradar-credentials" id="qradar-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Qradar](https://www.ibm.com/qradar) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [QRadar 文档](https://ibmsecuritydocs.github.io/qradar_api_overview/)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/qradar/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Key（API 密钥）**，也称为授权服务令牌。使用 **Admin（管理）** 标签页中的 **Manage Authorized Services（管理授权服务）** 窗口创建身份验证令牌。更多信息请参阅[创建身份验证令牌](https://www.ibm.com/docs/en/qradar-common?topic=forwarding-creating-authentication-token)。
