---
title: HaloPSA 凭据
description: HaloPSA 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 HaloPSA 的身份验证。
contentType:
- integration
- reference
nodeTitle: HaloPSA 凭据
originalFilePath: integrations/builtin/credentials/halopsa.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/halopsa
url: https://docs.n8n.io/integrations/builtin/credentials/halopsa
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# HaloPSA 凭据 <a href="#halopsa-credentials" id="halopsa-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [HaloPSA](../app-nodes/n8n-nodes-base.halopsa.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [HaloPSA](https://halopsa.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [HaloPSA API 文档](https://usehalo.com/halopsa/guides/1823/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 选择 **Hosting Type**（托管类型）：
    - **On Premise Solution**（本地部署方案）：如果在自己的服务器上托管 Halo 应用，选择此项。
    - **Hosted Solution Of Halo**（Halo 托管方案）：如果应用由 Halo 托管，选择此项。选择后还需提供 **Tenant**（租户）。
- **HaloPSA Authorisation Server URL**（授权服务器 URL）：可在 HaloPSA 的 **Configuration > Integrations > Halo API**（配置 > 集成 > Halo API）中的 [API Details（API 详情）](https://halopsa.com/guides/article/?kbid=1737)查看授权服务器 URL。
- **Resource Server**（资源服务器）URL：可在 HaloPSA 的 **Configuration > Integrations > Halo API**（配置 > 集成 > Halo API）中的 [API Details（API 详情）](https://halopsa.com/guides/article/?kbid=1737)查看资源服务器。
- 一个 **Client ID**（客户端 ID）：在 Halo API 设置中注册应用后获得。详细步骤请参阅 [HaloPSA 授权文档](https://usehalo.com/halopsa/guides/1823/)。n8n 建议使用以下设置：
    - 将 **Authentication Method**（身份验证方式）设为 `Client Credentials`。
    - 使用 `all` 权限。
- 一个 **Client Secret**（客户端密钥）：在 Halo API 设置中注册应用后获得。
- 你的 **Tenant**（租户）名称：**Hosting Type**（托管类型）为 **Hosted Solution of Halo**（Halo 托管方案）时，必须提供租户名称。可在 HaloPSA 的 **Configuration > Integrations > Halo API**（配置 > 集成 > Halo API）中的 [API Details（API 详情）](https://halopsa.com/guides/article/?kbid=1737)查看。

HaloPSA 综合应用权限与客服人员权限确定 API 的访问权限。
