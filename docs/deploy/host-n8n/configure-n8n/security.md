---
title: 保护 n8n 的安全
contentType: overview
nodeTitle: 安全
originalFilePath: hosting/securing/overview.md
originalUrl: https://docs.n8n.io/hosting/securing/overview
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 保护 n8n 的安全 <a href="#securing-n8n" id="securing-n8n"></a>

可以通过运行安全审计、设置 SSL 和 SSO、限制节点及公共 API、对执行数据脱敏等方式，保护自托管 n8n 实例中的凭据和工作流数据。

保护 n8n 实例安全有多种方式。

## 本节内容 <a id="in-this-section"></a>

* [管理安全策略](security/manage-security-policies.md)：管理实例级安全策略，包括强制 MFA 和个人空间控制。
* [运行安全审计](security/run-security-audits.md)：运行安全审计以识别风险。
* [设置 SSL](security/set-up-ssl.md)：强制使用安全连接。
* [配置 SSO](security/configure-sso.md)：设置 SAML 或 OIDC 单点登录。
* [轮换加密密钥](security/rotate-encryption-keys.md)：定期更换用于加密凭据和其他敏感数据的密钥。
* [使用 JWE 解密 OAuth 2.0 令牌](security/decrypt-oauth-20-tokens-with-jwe.md)：让身份提供商加密访问令牌和 ID 令牌，仅允许你的实例解密。
* [加固任务运行器](security/harden-task-runners.md)：提高 Code 节点执行的隔离性。
* [执行数据脱敏](security/redact-execution-data.md)：隐藏工作流执行的输入和输出数据。
* [禁用公共 API](security/disable-the-public-api.md)：防止其他人使用 n8n 公共 REST API。
* [控制遥测](security/control-telemetry.md)：退出 n8n 自动收集的匿名数据遥测。
* [阻止特定节点](security/block-specific-nodes.md)：防止 n8n 用户访问指定节点。
* [启用 SSRF 防护](security/enable-ssrf-protection.md)：控制工作流节点可以连接的主机和 IP 范围。
* [验证用户邮箱](security/verify-user-emails.md)：仅允许邮箱已验证的用户注册账号。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
* [设置令牌交换](../deploy-as-an-oem-integration/set-up-token-exchange.md)：嵌入 n8n 时，通过你自己的身份提供商验证用户。
* [要求双因素身份验证](../../../administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md)：为用户启用 2FA。
