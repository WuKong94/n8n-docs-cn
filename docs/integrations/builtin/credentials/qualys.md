---
title: Qualys 凭据
description: Qualys 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Qualys 的身份验证。
contentType:
- integration
- reference
nodeTitle: Qualys 凭据
originalFilePath: integrations/builtin/credentials/qualys.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/qualys
url: https://docs.n8n.io/integrations/builtin/credentials/qualys
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Qualys 凭据 <a href="#qualys-credentials" id="qualys-credentials"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/cred-only-statement.md" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Qualys](https://www.qualys.com/) 用户账号，用户角色可为 Contact 之外的任意角色。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Qualys 文档](https://qualysguard.qg2.apps.qualys.com/qwebhelp/fo_portal/api_doc/index.htm)。

此节点仅提供凭据。更多信息请参阅[自定义 API 操作](../custom-api-actions-for-existing-nodes.md)，也可以在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/qualys/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

- 一个 **Username（用户名）**
- 一个 **Password（密码）**
- 一个 **Requested With** 字符串：输入用户说明，例如用户代理，也可以保留默认值 `n8n application`。此字段用于设置必需的 `X-Requested-With` 请求头。
