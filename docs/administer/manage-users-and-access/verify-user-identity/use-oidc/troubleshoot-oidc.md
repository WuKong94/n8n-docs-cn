---
title: 排查 OIDC SSO 问题
description: 在 n8n 中使用 OIDC 时的注意事项与故障排查。
contentType: howto
nodeTitle: 排查 OIDC 问题
originalFilePath: user-management/oidc/troubleshooting.md
originalUrl: https://docs.n8n.io/user-management/oidc/troubleshooting
url: https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 排查 OIDC SSO 问题 <a href="#troubleshooting-oidc-sso" id="troubleshooting-oidc-sso"></a>

## 已知问题 <a href="#known-issues" id="known-issues"></a>

### 不支持 state 参数 <a href="#state-parameter-not-supported" id="state-parameter-not-supported"></a>

使用要求必须提供 `state` CSRF 令牌参数的 OIDC 提供方时，身份验证会失败并报错：

```json
{"code":0,"message":"authorization response from the server is an error"}
```

n8n 当前的 OIDC 实现不会处理 `state` 参数；部分 OIDC 提供方会发送该参数，以防止 CSRF 攻击。

目前唯一的临时解决办法是，在 OIDC 提供方允许的情况下，将其配置为禁用 `state` 参数。

n8n 正在开发对 OIDC `state` 参数的完整支持，计划在未来版本中提供。

### 不支持 PKCE <a href="#pkce-not-supported" id="pkce-not-supported"></a>

要求 PKCE（Proof Key for Code Exchange，代码交换证明密钥）的 OIDC 提供方可能会导致身份验证失败，或拒绝 n8n 的授权请求。n8n 当前的 OIDC 实现不支持 PKCE。

唯一的临时解决办法是，如果提供方设置中有此选项，将其配置为不要求 n8n 客户端使用 PKCE。

n8n 计划在未来版本中增加 PKCE 支持。

## 相关资源 <a id="related-resources"></a>

* [使用 OIDC](./)
* [设置 OIDC](set-up-oidc.md)
