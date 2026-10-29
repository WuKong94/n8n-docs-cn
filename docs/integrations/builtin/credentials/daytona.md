---
title: Daytona 凭据
description: Daytona 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Daytona 的身份验证。
contentType:
- integration
- reference
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Daytona 凭据 <a id="daytona-credentials"></a>

## 前置条件 <a id="prerequisites"></a>

创建一个 [Daytona](https://app.daytona.io/) 账号。

## 支持的身份验证方式 <a id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a id="related-resources"></a>

有关该服务的更多信息，请参阅 [Daytona API 文档](https://www.daytona.io/docs/en/tools/api/)。

## 使用 API 密钥 <a id="using-api-key"></a>

配置此凭据需要：

- **API URL**：Daytona API 端点的 URL。
- **API Key**（API 密钥）：Daytona API 密钥。

获取 API 密钥的步骤如下：

1. 登录 [Daytona Dashboard](https://app.daytona.io/dashboard/keys)（控制台）。
2. 选择 **Create Key**（创建密钥）。
3. 为密钥输入名称，例如 `n8n integration`。
4. 设置到期日期，并选择密钥所需权限。
5. 选择 **Create**（创建）生成密钥。
6. 复制 API 密钥，填入 n8n 凭据的 **API Key** 字段。

**API URL**：Daytona 托管服务使用 `https://app.daytona.io/api`，自托管实例则使用自己的 Daytona 实例 URL。

更多信息请参阅 [Daytona API Keys 文档](https://www.daytona.io/docs/en/api-keys/)。