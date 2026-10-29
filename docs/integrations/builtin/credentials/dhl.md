---
title: DHL 凭据
description: DHL 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 DHL 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: DHL 凭据
originalFilePath: integrations/builtin/credentials/dhl.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/dhl
url: https://docs.n8n.io/integrations/builtin/credentials/dhl
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# DHL 凭据 <a href="#dhl-credentials" id="dhl-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [DHL](../app-nodes/n8n-nodes-base.dhl.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DHL 开发者文档](https://support-developer.dhl.com/support/home)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [DHL Developer](https://developer.dhl.com/user/register) 账户，以及：

- 一个 **API Key（API 密钥）**

如需获取 API 密钥，请创建应用：

1. 在 DHL Developer 门户中，选择用户图标，打开 [User Apps（用户应用）](https://developer.dhl.com/user/apps)。
2. 选择 **+ Create App**（创建应用）。
3. 输入 **App name**（应用名称），例如 `n8n integration`。
4. 输入 **Machine name**（机器名称），例如 `n8n_integration`。
4. 在 **SELECT APIs**（选择 API）中，选择 **Shipment Tracking - Unified**（货件跟踪，统一 API）。该 API 会添加到 **Add API to app**（向应用添加 API）部分。
5. 在 **Add API to app**（向应用添加 API）部分，选择 **Shipment Tracking - Unified** API 旁的 **+**。
6. 选择 **Create App**（创建应用）。随后打开 **Apps**（应用）页面，显示刚创建的应用。
7. 选择刚创建的应用，查看详情。
8. 选择 **API Key**（API 密钥）旁的 **Show key**（显示密钥）。
9. 复制 **API Key**（API 密钥），填入 n8n 凭据。

更多信息，请参阅[如何创建应用？](https://support-developer.dhl.com/support/solutions/articles/47001177011-how-to-create-an-app-)
