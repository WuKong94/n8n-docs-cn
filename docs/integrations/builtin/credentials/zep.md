---
title: Zep 凭据
description: Zep 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Zep 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Zep 凭据
originalFilePath: integrations/builtin/credentials/zep.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/zep
url: https://docs.n8n.io/integrations/builtin/credentials/zep
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Zep 凭据 <a href="#zep-credentials" id="zep-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Zep](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)
* [Zep Vector Store（向量存储）](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Zep Cloud SDK 文档](https://help.getzep.com/install-sdks)；API 的更多信息，请参阅 [Zep REST API 文档](https://getzep.github.io/zep/)。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-overview-link.md" %}

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要一个至少包含一个项目的 [Zep 服务器](https://www.getzep.com/)，以及：

- **API URL**
- 一个 **API Key（API 密钥）**

设置方法取决于你使用的是 Zep Cloud，还是自托管的 Zep Open Source。

### Zep Cloud 设置 <a href="#zep-cloud-setup" id="zep-cloud-setup"></a>

如果使用 [Zep Cloud](https://app.getzep.com)，请按以下步骤操作：

1. 在 Zep 中打开 **Project Settings**（项目设置）。
2. 在 **Project Keys**（项目密钥）部分，选择 **Add Key**（添加密钥）。
3. 输入 **Key Name**（密钥名称），例如 `n8n integration`。
4. 选择 **Create**（创建）。
5. 复制密钥，填入 n8n 集成的 **API Key**（API 密钥）。
6. 开启 **Cloud**（云）开关。

### 自托管 Zep Open Source 设置 <a href="#self-hosted-zep-open-source-setup" id="self-hosted-zep-open-source-setup"></a>

{% hint style="warning" %}
**功能可用范围**

Zep 团队于 2025 年 4 月[弃用了开源 Zep Community Edition](https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/)。这些说明在该日期之后可能不再适用。
{% endhint %}

如果自托管 Zep Open Source，请按以下步骤操作：

1. 将 Zep 服务器的 JWT 令牌填入 n8n 的 **API Key**（API 密钥）。
2. 确保 **Cloud**（云）开关处于关闭状态。
3. 将 Zep 服务器的 URL 填入 **API URL**。
