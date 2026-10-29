---
title: FileMaker 凭据
description: FileMaker 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 FileMaker 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: FileMaker 凭据
originalFilePath: integrations/builtin/credentials/filemaker.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/filemaker
url: https://docs.n8n.io/integrations/builtin/credentials/filemaker
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# FileMaker 凭据 <a href="#filemaker-credentials" id="filemaker-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [FileMaker](../app-nodes/n8n-nodes-base.filemaker.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [FileMaker Server](https://www.claris.com/filemaker/) 上创建用户账户，并授予 `fmrest` 扩展权限，以[访问 FileMaker Data API](https://help.claris.com/en/data-api-guide/content/enable-access.html)。
- 确保 FileMaker Server 可以使用 [FileMaker Data API](https://help.claris.com/en/data-api-guide/content/index.html)：
    1. 使用 FileMaker Pro 准备数据库，以供 FileMaker Data API 访问。可创建数据库，也可准备现有数据库。
        - 更多信息，请参阅[准备数据库以供 FileMaker Data API 访问](https://help.claris.com/en/data-api-guide/content/prepare-databases-for-access.html)。
    1. 编写调用 FileMaker Data API 方法的代码，查找、创建、编辑、复制和删除托管数据库中的记录。
        - 更多信息，请参阅[编写 FileMaker Data API 调用](https://help.claris.com/en/data-api-guide/content/write-data-api-calls.html)。
    1. 启用 FileMaker Data API 访问，并托管你的解决方案。
        - 更多信息，请参阅[托管 FileMaker Data API 解决方案](https://help.claris.com/en/data-api-guide/content/host-data-api-app.html)。
    1. 测试 FileMaker Data API 访问是否正常。
        - 更多信息，请参阅[测试 FileMaker Data API 解决方案](https://help.claris.com/en/data-api-guide/content/test-data-api-app.html)。
    1. 使用 Admin Console（管理控制台）监控托管的解决方案。
        - 更多信息，请参阅[监控 FileMaker Data API 解决方案](https://help.claris.com/en/data-api-guide/content/monitor-data-api-app.html)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Database connection（数据库连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [FileMaker Data API 指南](https://help.claris.com/en/data-api-guide/content/index.html)。

## 使用数据库连接 <a href="#using-database-connection" id="using-database-connection"></a>

配置此凭据的步骤如下：

1. 输入 FileMaker Server 的 **Host**（主机）名称或 IP 地址。
2. 输入 **Database**（数据库）名称，应与 FileMaker 的 **Databases**（数据库）列表中显示的名称一致。
3. 输入具有 `fmrest` 扩展权限的用户账户的 **Login**（登录名）。更多信息，请参阅前面的[前置条件](#prerequisites)。
4. 输入该用户账户的 **Password**（密码）。

