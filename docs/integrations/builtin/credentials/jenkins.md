---
title: Jenkins 凭据
description: Jenkins 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Jenkins 的身份验证。
contentType:
- integration
- reference
nodeTitle: Jenkins 凭据
originalFilePath: integrations/builtin/credentials/jenkins.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/jenkins
url: https://docs.n8n.io/integrations/builtin/credentials/jenkins
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Jenkins 凭据 <a href="#jenkins-credentials" id="jenkins-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Jenkins](../app-nodes/n8n-nodes-base.jenkins.md)


## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Jenkins](https://www.jenkins.io/) 实例上创建账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Jenkins 不提供公开 API 文档；各页面的 API 文档可从用户界面右下角访问。该服务的更多信息，请参阅对应页面的详细文档。API 和 API 封装库的说明，请参阅 [Jenkins Remote Access API](https://www.jenkins.io/doc/book/using/remote-access-api/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- **Jenkins Username**（Jenkins 用户名）：令牌所属用户的用户名。
- **Personal API Token**（个人 API 令牌）：从用户的 **profile details > Configure > Add new token**（个人资料详情 > 配置 > 添加新令牌）中生成。更多细节请参阅[这些 Stack Overflow 说明](https://stackoverflow.com/questions/45466090/how-to-get-the-api-token-for-jenkins)。
- **Jenkins Instance URL**（Jenkins 实例 URL）。

Jenkins 在 2018 年重新设计了 API 令牌配置。如果使用较旧的 Jenkins 实例，请确保使用非旧式 API 令牌。更多信息请参阅 [Security Hardening: New API token system in Jenkins 2.129+](https://www.jenkins.io/blog/2018/07/02/new-api-token-system/)。

