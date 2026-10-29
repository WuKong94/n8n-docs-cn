---
title: Travis CI 凭据
description: Travis CI 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Travis CI 的身份验证。
contentType:
- integration
- reference
nodeTitle: Travis CI 凭据
originalFilePath: integrations/builtin/credentials/travisci.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/travisci
url: https://docs.n8n.io/integrations/builtin/credentials/travisci
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Travis CI 凭据 <a href="#travis-ci-credentials" id="travis-ci-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Travis CI](../app-nodes/n8n-nodes-base.travisci.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Travis CI](https://travis-ci.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（API 令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Travis CI API 文档](https://docs.travis-ci.com/user/developer/)。

## 使用 API 令牌 <a href="#using-api-token" id="using-api-token"></a>

配置此凭据需要：

- 一个 **API Token（API 令牌）**：从 **Account Settings（账号设置）>** [**API Token（API 令牌）**](https://packagecloud.io/api_token) 获取令牌，或通过 Travis CI [命令行客户端](https://github.com/travis-ci/travis.rb#installation)生成。

