---
title: MSG91 凭据
description: MSG91 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MSG91 的身份验证。
contentType:
- integration
- reference
nodeTitle: MSG91 凭据
originalFilePath: integrations/builtin/credentials/msg91.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/msg91
url: https://docs.n8n.io/integrations/builtin/credentials/msg91
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MSG91 凭据 <a href="#msg91-credentials" id="msg91-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [MSG91](../app-nodes/n8n-nodes-base.msg91.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MSG91](https://msg91.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MSG91 API 文档](https://docs.msg91.com/overview)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Authentication Key**（身份验证密钥）：打开用户菜单，选择 **Authkey** 获取。更多信息请参阅 MSG91 的[在哪里查找身份验证密钥文档](https://msg91.com/help/api/where-can-i-find-my-authentication-ke)。

## IP 安全 <a href="#ip-security" id="ip-security"></a>

MSG91 默认为 authkey 启用 [IP Security](https://msg91.com/help/api/what-do-you-mean-by-api-security)（IP 安全）。

启用此设置时，要使 n8n 凭据正常工作，需将所有 [n8n IP 地址](../../../deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses.md)加入 MSG91 的 IP 允许名单。可以根据需要的安全级别，在以下两个位置之一添加：

- 要允许账户中的所有 authkey 与 n8n 配合使用，在 **Authkey** 页面的 **Company's whitelisted IPs**（公司 IP 允许名单）部分添加 n8n IP 地址。
- 要仅允许特定 authkey 与 n8n 配合使用，在该 authkey 详情的 **Whitelisted IPs**（IP 允许名单）部分添加 n8n IP 地址。
