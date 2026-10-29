---
title: SeaTable 凭据
description: SeaTable 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SeaTable 的身份验证。
contentType:
- integration
- reference
nodeTitle: SeaTable 凭据
originalFilePath: integrations/builtin/credentials/seatable.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/seatable
url: https://docs.n8n.io/integrations/builtin/credentials/seatable
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SeaTable 凭据 <a href="#seatable-credentials" id="seatable-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SeaTable](../app-nodes/n8n-nodes-base.seatable.md)
- [SeaTable Trigger（触发器）](../trigger-nodes/n8n-nodes-base.seatabletrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在云端或自托管 SeaTable 服务器上创建 [SeaTable](https://seatable.io/en/) 账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [SeaTable API 文档](https://api.seatable.io)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Environment**（环境）：选择与 SeaTable 实例相符的环境：
    - **Cloud-Hosted**（云托管）
    - **Self-Hosted**（自托管）
- **API Token (of a Base)**（Base 的 API 令牌）：从 SeaTable 的 Base 选项进入 **Advanced > API Token**（高级 > API 令牌），生成 **Base-Token**。
    - 为令牌使用 **Read-Write**（读写）权限。
    - 更多信息请参阅[创建 API 令牌](https://seatable.io/en/docs/seatable-api/erzeugen-eines-api-tokens/)。
- **Timezone**（时区）：选择 SeaTable 服务器的时区。

