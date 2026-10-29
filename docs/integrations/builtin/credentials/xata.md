---
title: Xata 凭据
description: Xata 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Xata 的身份验证。
contentType:
- integration
- reference
nodeTitle: Xata 凭据
originalFilePath: integrations/builtin/credentials/xata.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/xata
url: https://docs.n8n.io/integrations/builtin/credentials/xata
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Xata 凭据 <a href="#xata-credentials" id="xata-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Xata](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建 [Xata](https://xata.io/) 数据库，或在现有数据库中创建账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Xata 文档](https://xata.io/docs/rest-api/authentication)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Database Endpoint**（数据库端点）：Workspace API 要求按以下格式标识要查询的数据库：`https://{workspace-display-name}-{workspace-id}.{region}.xata.sh/db/{dbname}`。更多信息请参阅 [Workspace API](https://xata.io/docs/rest-api#workspace-api)。
    - `{workspace-display-name}`：工作区显示名称，是可包含在 Database Endpoint 中的可选标识符。API 会忽略此值，但保存多份凭据时，包含它有助于辨认数据库所属工作区。
    - `{workspace-id}`：工作区的唯一 ID，由 6 个字母或数字组成。
    - `{region}`：数据库的托管地区，必须与数据库的地区配置一致。
    - `{dbname}`：要操作的数据库名称。
- **Branch**（分支）：输入数据库的 GitHub 分支名称。
- **API Key**（API 密钥）：进入 [**Account Settings**](https://app.xata.io/settings)（账户设置），选择 **+ Add a key**（添加密钥）生成 API 密钥。更多信息请参阅[生成 API 密钥](https://xata.io/docs/rest-api#generate-an-api-key)。
