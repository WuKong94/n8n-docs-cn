---
title: Form.io Trigger 凭据
description: Form.io Trigger 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Form.io Trigger 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Form.io Trigger 凭据
originalFilePath: integrations/builtin/credentials/formiotrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/formiotrigger
url: https://docs.n8n.io/integrations/builtin/credentials/formiotrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Form.io Trigger 凭据 <a href="#formio-trigger-credentials" id="formio-trigger-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Form.io Trigger](../trigger-nodes/n8n-nodes-base.formiotrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Form.io API 文档](https://apidocs.form.io/)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要一个 [Form.io](https://www.form.io/) 账户，以及：

- 你的 **Environment**（环境）
- 登录用的 **Email address**（电子邮箱地址）
- 你的 **Password**（密码）

设置凭据的步骤如下：

1. 选择 **Environment**（环境）：
    - 如果不是自行托管 Form.io，选择 **Cloud hosted**（云托管）。
    - 如果自行托管 Form.io，选择 **Self-hosted**（自行托管），然后添加：
        - 你的 **Self-Hosted Domain**（自行托管域名）。仅填写域名本身。例如，表单地址为 `https://yourserver.com/yourproject/manage/view` 时，自行托管域名为 `https://yourserver.com`。
2. 输入登录 Form.io 的 **Email address**（电子邮箱地址）。
3. 输入登录 Form.io 的 **Password**（密码）。
