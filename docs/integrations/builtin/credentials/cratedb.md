---
title: CrateDB 凭据
description: CrateDB 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 CrateDB 的身份验证。
contentType:
- integration
- reference
nodeTitle: CrateDB 凭据
originalFilePath: integrations/builtin/credentials/cratedb.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/cratedb
url: https://docs.n8n.io/integrations/builtin/credentials/cratedb
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# CrateDB 凭据 <a href="#cratedb-credentials" id="cratedb-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [CrateDB](../app-nodes/n8n-nodes-base.cratedb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

一个可用的 CrateDB 实例。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- account connection（账户连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [CrateDB 文档](https://cratedb.com/docs/crate/reference/en/latest/)。

## 使用账户连接 <a href="#using-account-connection" id="using-account-connection"></a>

配置此凭据需要：

- 你的 **Host**（主机）名称
- 你的 **Database**（数据库）名称
- 一个 **User**（用户名）
- 用户的 **Password**（密码）
- 设置 **SSL** 参数。更多信息请参阅 [CrateDB 安全通信（SSL/TLS）文档](https://cratedb.com/docs/crate/reference/en/5.7/admin/ssl.html#admin-ssl)。n8n 支持的选项包括：
    - Allow（允许）
    - Disable（禁用）
    - Require（要求）
- 一个 **Port**（端口）号

这些字段及其默认值的详细说明，请参阅[连接 CrateDB 集群文档](https://cratedb.com/docs/crate/clients-tools/en/latest/connect/)。

