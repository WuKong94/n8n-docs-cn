---
title: Bitbucket 凭据
description: Bitbucket 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Bitbucket 的身份验证。
contentType:
- integration
- reference
nodeTitle: Bitbucket 凭据
originalFilePath: integrations/builtin/credentials/bitbucket.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/bitbucket
url: https://docs.n8n.io/integrations/builtin/credentials/bitbucket
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Bitbucket 凭据 <a href="#bitbucket-credentials" id="bitbucket-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Bitbucket Trigger（触发器）](../trigger-nodes/n8n-nodes-base.bitbuckettrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Bitbucket](https://www.bitbucket.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token（访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bitbucket API 文档](https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication)。

## 配置 Bitbucket 访问令牌 <a href="#configuring-bitbucket-access-token" id="configuring-bitbucket-access-token"></a>

1. 登录 Bitbucket，打开账户设置或个人设置。
2. 找到 API 令牌或安全设置部分。
3. 创建新 API 令牌，为其指定名称，并根据使用场景设置到期日期。
4. 选择 Bitbucket 作为应用，再选择所需作用域（权限）：

    ```bash
    read:user:bitbucket
    read:workspace:bitbucket
    read:repository:bitbucket
    read:webhook:bitbucket
    write:webhook:bitbucket
    delete:webhook:bitbucket
    ```

5. 检查并创建令牌。复制生成的令牌，填入 n8n。Bitbucket 只会显示令牌一次。

详细步骤请参阅[创建 API 令牌](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/)。

