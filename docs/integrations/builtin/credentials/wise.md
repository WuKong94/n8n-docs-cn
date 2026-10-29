---
title: Wise 凭据
description: Wise 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Wise 的身份验证。
contentType:
- integration
- reference
nodeTitle: Wise 凭据
originalFilePath: integrations/builtin/credentials/wise.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/wise
url: https://docs.n8n.io/integrations/builtin/credentials/wise
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Wise 凭据 <a href="#wise-credentials" id="wise-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Wise](../app-nodes/n8n-nodes-base.wise.md)
- [Wise Trigger（触发器）](../trigger-nodes/n8n-nodes-base.wisetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Wise](https://wise.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Wise API 文档](https://docs.wise.com/api-docs/api-reference)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- **API Token**（API 令牌）：在 **user menu > Settings > API tokens**（用户菜单 > 设置 > API 令牌）中生成 API 令牌。将生成的 API 密钥填入 n8n 凭据。更多信息，请参阅 [API 入门](https://wise.com/help/articles/2958107/getting-started-with-the-api)。
- **Environment**（环境）：选择与你的 Wise 账户环境最匹配的环境。
    - 使用 Wise 测试沙盒账户时，选择 **Test**（测试）。
    - 否则选择 **Live**（正式）。
- **Private Key (Optional)**（私钥，可选）：对于需要强客户身份验证（SCA）的正式端点，请生成公钥和私钥，并在此输入私钥。更多信息，请参阅[添加私钥](#add-a-private-key)。
    - 使用 **Test**（测试）环境时，仅当你在[公钥管理页面](https://wise-sandbox.com/your-account/integrations-and-tools/api-tokens/public-keys)启用了强客户身份验证，才需要输入私钥。

## 添加私钥 <a href="#add-a-private-key" id="add-a-private-key"></a>

Wise 通过强客户身份验证（SCA）保护部分正式端点和操作。详情请参阅[强客户身份验证与 2FA](https://docs.wise.com/guides/developer/auth-and-security/sca-and-2fa)。

请求需要 SCA 的端点时，Wise 会返回 403 Forbidden HTTP 状态码，错误内容如下：

> 此请求需要强客户身份验证（SCA）。请为你的账户及 n8n 凭据添加密钥对。详情见 https://docs.wise.com/guides/developer/auth-and-security/sca-and-2fa

如需使用要求 SCA 的端点，请生成 RSA 密钥对，并将相应密钥信息添加到 Wise 和 n8n：

1. 生成 RSA 密钥对：

    ```sh
    $ openssl genrsa -out private.pem 2048 
    $ openssl rsa -pubout -in private.pem -out public.pem
    ```

2. 将公钥 `public.pem` 的内容添加到 Wise 的 **user menu > Settings > API tokens > Manage public keys**（用户菜单 > 设置 > API 令牌 > 管理公钥）。
3. 在 n8n 中，将私钥 `private.pem` 的内容填入 **Private Key (Optional)**（私钥，可选）。

更多信息，请参阅[个人 API 令牌](https://docs.wise.com/guides/developer/auth-and-security/personal-api-token)。

