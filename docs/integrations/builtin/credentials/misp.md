---
title: MISP 凭据
description: MISP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MISP 的身份验证。
contentType:
- integration
- reference
nodeTitle: MISP 凭据
originalFilePath: integrations/builtin/credentials/misp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/misp
url: https://docs.n8n.io/integrations/builtin/credentials/misp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MISP 凭据 <a href="#misp-credentials" id="misp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [MISP](../app-nodes/n8n-nodes-base.misp.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

安装并运行一个 [MISP](https://misp.github.io/MISP/) 实例。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [MISP Automation API 文档](https://www.circl.lu/doc/misp/automation)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **API Key**（API 密钥）：在 MISP 中称为 Automation key（自动化密钥）。可从 **Event Actions > Automation**（事件操作 > 自动化）中获取。如何生成更多密钥，请参阅 [MISP 自动化密钥文档](https://www.circl.lu/doc/misp/automation/#automation-key)。
- **Base URL**（基础 URL）：你的 MISP URL。
- 选择是否 **Allow Unauthorized Certificates**（允许未经验证的证书）：开启后，即使 SSL 证书验证失败，凭据仍会建立连接。

