---
title: VirusTotal 凭据
description: VirusTotal 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 VirusTotal 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: VirusTotal 凭据
originalFilePath: integrations/builtin/credentials/virustotal.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/virustotal
url: https://docs.n8n.io/integrations/builtin/credentials/virustotal
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# VirusTotal 凭据 <a href="#virustotal-credentials" id="virustotal-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [VirusTotal](https://www.virustotal.com) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [VirusTotal 文档](https://docs.virustotal.com/reference/overview)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/virustotal/)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Token（API 令牌）**：进入 **user account menu > API key（用户账号菜单 > API 密钥）** 获取密钥，并填入 n8n 凭据的 **API Token** 字段。更多信息请参阅 [API 身份验证](https://docs.virustotal.com/reference/authentication)。
