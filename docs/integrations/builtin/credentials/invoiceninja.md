---
title: Invoice Ninja 凭据
description: Invoice Ninja 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Invoice Ninja 的身份验证。
contentType:
- integration
- reference
nodeTitle: Invoice Ninja 凭据
originalFilePath: integrations/builtin/credentials/invoiceninja.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/invoiceninja
url: https://docs.n8n.io/integrations/builtin/credentials/invoiceninja
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Invoice Ninja 凭据 <a href="#invoice-ninja-credentials" id="invoice-ninja-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Invoice Ninja](../app-nodes/n8n-nodes-base.invoiceninja.md)
- [Invoice Ninja Trigger（触发器）](../trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Invoice Ninja](https://www.invoiceninja.com/) 账户。仅 Pro 和 Enterprise 方案支持 API 集成。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

API 的更多信息，请参阅 Invoice Ninja 的 [v4 API 文档](https://invoice-ninja.readthedocs.io/en/latest/api.html)和 [v5 API 文档](https://api-docs.invoicing.co/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **URL**：如果由 Invoice Ninja 托管安装，使用文中所列任一默认 URL；如果自行托管，使用你的 Invoice Ninja 实例 URL。
- **API Token**（API 令牌）：在 **Settings > Account Management > API Tokens**（设置 > 账户管理 > API 令牌）中生成。
- 可选的 **Secret**（密钥），仅适用于 v5 API 用户。

