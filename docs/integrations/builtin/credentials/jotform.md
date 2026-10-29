---
title: Jotform 凭据
description: Jotform 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Jotform 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Jotform 凭据
originalFilePath: integrations/builtin/credentials/jotform.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jotform
url: https://docs.n8n.io/integrations/builtin/credentials/jotform
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jotform 凭据 <a href="#jotform-credentials" id="jotform-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Jotform Trigger（触发器）](../trigger-nodes/n8n-nodes-base.jotformtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Jotform API 文档](https://api.jotform.com/docs/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Jotform](https://www.jotform.com/) 账号，以及：

- 一个 **API Key（API 密钥）**
- **API Domain**（API 域名）

设置步骤如下：

1. 进入 **Settings >** [**API**](https://www.jotform.com/myaccount/api)（设置 > API）。
2. 选择 **Create New Key**（创建新密钥）。
3. 在 Jotform 中选择 **Name**（名称），将 API 密钥名称改为有意义的名称，例如 `n8n integration`。
4. 复制 **API Key**（API 密钥），填入 n8n 凭据。
5. 在 n8n 中，根据所用表单选择适用的 **API Domain**：
    - **api.jotform.com**：其他表单类型均不适用时，使用此域名。
    - **eu-api.jotform.com**：使用 Jotform [EU Safe Forms](https://www.jotform.com/eu-safe-forms/) 时选择此域名。
    - **hipaa-api.jotform.com**：使用 Jotform [HIPAA forms](https://www.jotform.com/hipaa/) 时选择此域名。

创建密钥和 API 域名的更多信息，请参阅 [Jotform API 文档](https://api.jotform.com/docs/)。
