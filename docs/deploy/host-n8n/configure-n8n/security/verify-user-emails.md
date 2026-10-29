---
title: 仅允许邮箱已验证的用户注册账号
description: 要求所有新账号通过邮箱验证。
contentType: howto
nodeTitle: 验证用户邮箱
originalFilePath: hosting/securing/restrict-by-email-verification.md
originalUrl: https://docs.n8n.io/hosting/securing/restrict-by-email-verification
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 仅允许邮箱已验证的用户注册账号 <a href="#restrict-account-registration-to-email-verified-users" id="restrict-account-registration-to-email-verified-users"></a>

可以要求所有新账号通过邮箱验证，防止恶意管理员在未经邮箱验证的情况下注册账号。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 必须配置 SMTP，并确保 n8n 能发送邮件。

## 如何限制账号注册 <a href="#how-to-restrict-account-registration" id="how-to-restrict-account-registration"></a>

将环境变量 `N8N_INVITE_LINKS_EMAIL_ONLY` 设为 `true`。这样可以限制实例，仅允许邮箱已验证的用户注册。

SMTP 配置详情请参阅[设置 SMTP](../user-management.md#step-one-smtp)。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
