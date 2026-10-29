---
title: Magento 2 凭据
description: Magento 2 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Magento 2 的身份验证。
contentType:
- integration
- reference
nodeTitle: Magento 2 凭据
originalFilePath: integrations/builtin/credentials/magento2.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/magento2
url: https://docs.n8n.io/integrations/builtin/credentials/magento2
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Magento 2 凭据 <a href="#magento-2-credentials" id="magento-2-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Magento 2](../app-nodes/n8n-nodes-base.magento2.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 [Magento（Adobe Commerce）](https://business.adobe.com/products/commerce.html)账户。
- 为商店启用 **Allow OAuth Access Tokens to be used as standalone Bearer tokens**（允许将 OAuth 访问令牌用作独立 Bearer 令牌）。
    - 进入 **Admin > Stores > Configuration > Services > OAuth > Consumer Settings**（管理 > 商店 > 配置 > 服务 > OAuth > 消费者设置）。
    - 将 **Allow OAuth Access Tokens to be used as standalone Bearer tokens**（允许将 OAuth 访问令牌用作独立 Bearer 令牌）选项设为 **Yes**（是）。
    - 也可在 CLI 中运行以下命令启用此设置：

        ```
        bin/magento config:set oauth/consumer/enable_integration_as_bearer 1
        ```

在 n8n 将 Magento 2 凭据更新为使用 OAuth 之前，此步骤是必需的。更多信息，请参阅 [Integration Tokens（集成令牌）](https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token#integration-tokens)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Magento API 文档](https://developer.adobe.com/commerce/docs/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要：

- **Host**（主机）：输入 Magento 商店的地址。
- **Access Token**（访问令牌）：从[**Admin Panel**（管理面板）](https://docs.magento.com/user-guide/stores/admin.html)获取访问令牌：
    1. 进入 **System > Extensions > Integrations**（系统 > 扩展 > 集成）。
    2. 添加新的 Integration（集成）。
    3. 打开 **API** 选项卡，选择希望 n8n 集成可以访问的 Magento 资源。
    4. 在 **Integrations**（集成）页面，**Activate**（激活）新集成。
    5. 选择 **Allow**（允许），显示访问令牌，复制后填入 n8n。
