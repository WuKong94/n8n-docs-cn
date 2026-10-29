---
title: Twilio 凭据
description: Twilio 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Twilio 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Twilio 凭据
originalFilePath: integrations/builtin/credentials/twilio.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/twilio
url: https://docs.n8n.io/integrations/builtin/credentials/twilio
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Twilio 凭据 <a href="#twilio-credentials" id="twilio-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Twilio](../app-nodes/n8n-nodes-base.twilio.md)
- [Twilio trigger（触发器）](../trigger-nodes/n8n-nodes-base.twiliotrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **Auth token**（身份验证令牌）：Twilio 建议仅用于本地测试。
- **API key**（API 密钥）：Twilio 建议用于生产环境。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Twilio API 文档](https://www.twilio.com/docs)。

## 使用 Auth Token <a href="#using-auth-token" id="using-auth-token"></a>

配置此凭据需要一个 [Twilio](https://twilio.com/) 账号，以及：

- Twilio 的 **Account SID**（账户 SID）
- Twilio 的 **Auth Token**（身份验证令牌）

设置凭据的步骤如下：

1. 在 n8n 中，将 **Auth Type**（身份验证类型）设为 **Auth Token**（身份验证令牌）。
2. 在 Twilio 中进入 **Console Dashboard > Account Info**（控制台仪表板 > 账户信息）。
3. 复制 **Account SID**（账户 SID），填入 n8n 凭据，它用作用户名。
4. 复制 **Auth Token**（身份验证令牌），填入 n8n 凭据，它用作密码。

更多信息，请参阅[身份验证令牌及其更改方法](https://help.twilio.com/articles/223136027-Auth-Tokens-and-How-to-Change-Them)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Twilio](https://twilio.com/) 账号，以及：

- Twilio 的 **Account SID**（账户 SID）
- **API Key SID**（API 密钥 SID）：创建 API 密钥时生成。
- **API Key Secret**（API 密钥秘密值）：创建 API 密钥时生成。

设置凭据的步骤如下：

1. 在 n8n 中，将 **Auth Type**（身份验证类型）设为 **API Key**（API 密钥）。
2. 在 Twilio 中进入 **Console Dashboard > Account Info**（控制台仪表板 > 账户信息）。
3. 复制 **Account SID**（账户 SID），填入 n8n 凭据。
4. 在 Twilio 中打开账户的 [**API keys & tokens**（API 密钥与令牌）](https://www.twilio.com/console/project/api-keys)页面。
5. 选择 **Create API Key**（创建 API 密钥）。
6. 输入 API 密钥的 **Friendly name**（易记名称），例如 `n8n integration`。
7. 选择 **Key type**（密钥类型）。n8n 支持 **Main**（主密钥）或 **Standard**（标准密钥）。更多信息，请参阅[选择 API 密钥类型](#selecting-an-api-key-type)。
8. 选择 **Create API Key**（创建 API 密钥），完成创建。
5. 在 **Copy secret key**（复制秘密密钥）页面，复制密钥旁显示的 **SID**，填入 n8n 凭据的 **API Key SID**（API 密钥 SID）。
6. 在 **Copy secret key**（复制秘密密钥）页面，复制密钥旁显示的 **Secret**（秘密值），填入 n8n 凭据的 **API Key Secret**（API 密钥秘密值）。

更详细的说明，请参阅[创建 API 密钥](https://www.twilio.com/docs/iam/api-keys#create-an-api-key)。

### 选择 API 密钥类型 <a href="#selecting-an-api-key-type" id="selecting-an-api-key-type"></a>

创建 Twilio API 密钥时，必须选择密钥类型。n8n 凭据支持 **Main**（主密钥）和 **Standard**（标准密钥）类型。

各 API 密钥类型的详情如下：

* **Main**（主密钥）：提供与在 API 请求中使用 Account SID 和 Auth Token 相同级别的访问权限。
* **Standard**（标准密钥）：提供 Twilio API 中除 API 密钥资源和账户资源以外的全部功能的访问权限。
* **Restricted**（受限密钥）：此密钥类型处于 Beta 阶段。n8n 尚未针对此类型测试凭据；如果尝试使用时遇到问题，请反馈给 n8n。

密钥类型的更多信息，请参阅 [API 密钥类型](https://www.twilio.com/docs/iam/api-keys#types-of-api-keys)。
