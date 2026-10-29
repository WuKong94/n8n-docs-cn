---
title: Motorhead 凭据
description: Motorhead 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Motorhead 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Motorhead 凭据
originalFilePath: integrations/builtin/credentials/motorhead.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/motorhead
url: https://docs.n8n.io/integrations/builtin/credentials/motorhead
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Motorhead 凭据 <a href="#motorhead-credentials" id="motorhead-credentials"></a>

{% hint style="warning" %}
**功能可用范围**

Motorhead 项目已停止维护。[Motorhead 节点](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)从 n8n 2.8.0 起弃用，并将在未来版本移除。详细信息请参阅[已弃用和具有版本的节点](../deprecated-nodes.md)。
{% endhint %}

这些凭据可用于以下节点的身份验证：

* [Motorhead](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Motorhead API 文档](https://docs.getmetal.io/rest-api/introduction)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个 [Motorhead](https://www.metal.ai/) 账号，以及：

- 你的 **Host**（主机）URL
- 一个 **API Key（API 密钥）**
- 一个 **Client ID（客户端 ID）**

配置时需要生成 API 密钥：

1. 如果自行托管 Motorhead，请将 **Host**（主机）URL 更新为你的 Motorhead URL。
2. 在 Motorhead 中进入 **Settings > Organization**（设置 > 组织）。
3. 在 **API Keys**（API 密钥）部分选择 **Create**（创建）。
4. 为 API 密钥输入 **Name**（名称），例如 `n8n integration`。
5. 选择 **Generate**（生成）。
6. 复制 **apiKey**，填入 n8n 凭据。
7. 返回 API 密钥列表。
8. 复制该密钥的 **clientID**，填入 n8n 凭据的 **Client ID**（客户端 ID）字段。

更多信息请参阅[生成 API 密钥](https://docs.getmetal.io/guides/misc-get-keys)。
