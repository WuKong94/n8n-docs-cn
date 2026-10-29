---
title: WooCommerce 凭据
description: WooCommerce 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 WooCommerce 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: WooCommerce 凭据
originalFilePath: integrations/builtin/credentials/woocommerce.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/woocommerce
url: https://docs.n8n.io/integrations/builtin/credentials/woocommerce
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# WooCommerce 凭据 <a href="#woocommerce-credentials" id="woocommerce-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [WooCommerce](../app-nodes/n8n-nodes-base.woocommerce.md)
- [WooCommerce Trigger（触发器）](../trigger-nodes/n8n-nodes-base.woocommercetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 WordPress 网站上安装 [WooCommerce](https://woocommerce.com/) 插件。
- 在 WordPress 中，进入 **Settings > Permalinks**（设置 > 固定链接），将固定链接格式设为 **Plain**（朴素）以外的选项。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [WooCommerce REST API 文档](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Consumer Key**（消费者密钥）：生成 API 密钥时创建。
- **Consumer Secret**（消费者秘密值）：生成 API 密钥时创建。
- **WooCommerce URL**

生成 API 密钥并设置凭据的步骤如下：

1. 进入 **WooCommerce > Settings > Advanced > Rest API > Add key**（WooCommerce > 设置 > 高级 > REST API > 添加密钥）。
2. 在 **Permissions**（权限）下拉列表中选择 **Read/Write**（读写）。
3. 复制生成的 **Consumer Key**（消费者密钥）和 **Consumer Secret**（消费者秘密值），填入 n8n 凭据。
4. 将 WordPress 网站 URL 填入 **WooCommerce URL**。
5. 默认情况下，n8n 在 Authorization 请求头中传递凭据信息。如果需要改为通过查询字符串参数传递，请开启 **Include Credentials in Query**（在查询中包含凭据）。

更多信息，请参阅[生成密钥](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/#3-generate-keys)。

## 解决“Consumer key is missing”（缺少消费者密钥）错误 <a href="#resolve-consumer-key-is-missing-error" id="resolve-consumer-key-is-missing-error"></a>

尝试连接凭据时，可能收到如下错误：`Consumer key is missing`。

通过 SSL 进行身份验证时，服务器无法解析 Authorization 请求头中的信息，便会出现此错误。

解决方法是开启 **Include Credentials in Query**（在查询中包含凭据）开关，改为通过查询字符串参数传递 consumer key/secret，然后重试凭据。
