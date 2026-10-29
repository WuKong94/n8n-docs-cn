---
title: Zabbix 凭据
description: Zabbix 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zabbix 的身份验证。
contentType:
- integration
- reference
nodeTitle: Zabbix 凭据
originalFilePath: integrations/builtin/credentials/zabbix.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zabbix
url: https://docs.n8n.io/integrations/builtin/credentials/zabbix
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zabbix 凭据 <a href="#zabbix-credentials" id="zabbix-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zabbix Cloud](https://www.zabbix.com/) 账号，或自行托管 Zabbix 服务器。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zabbix API 文档](https://www.zabbix.com/documentation/current/en/manual/api)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/zabbix/)。


## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **API Token（API 令牌）**：即 Zabbix 用户的 API 密钥。
- 一个 **URL**：即 Zabbix 服务器的 URL，不要在其中包含 `/zabbix`。

有关该服务身份验证的更多信息，请参阅 [Zabbix API 文档](https://www.zabbix.com/documentation/current/en/manual/api#authentication)。
