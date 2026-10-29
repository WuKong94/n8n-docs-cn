---
title: Segment 凭据
description: Segment 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Segment 的身份验证。
contentType:
- integration
- reference
nodeTitle: Segment 凭据
originalFilePath: integrations/builtin/credentials/segment.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/segment
url: https://docs.n8n.io/integrations/builtin/credentials/segment
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Segment 凭据 <a href="#segment-credentials" id="segment-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Segment](../app-nodes/n8n-nodes-base.segment.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Segment](https://segment.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Segment 数据源文档](https://segment.com/docs/connections/sources/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Write Key（写入密钥）**：进入 **Sources > Add Source（数据源 > 添加数据源）**，添加 **Node.js** 数据源，再复制其写入密钥，填入 n8n 凭据。

更多信息请参阅[查找写入密钥](https://segment.com/docs/connections/find-writekey/)。

