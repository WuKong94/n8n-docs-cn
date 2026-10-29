---
title: Workable 凭据
description: Workable 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Workable 的身份验证。
contentType:
- integration
- reference
nodeTitle: Workable 凭据
originalFilePath: integrations/builtin/credentials/workable.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/workable
url: https://docs.n8n.io/integrations/builtin/credentials/workable
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Workable 凭据 <a href="#workable-credentials" id="workable-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Workable Trigger（触发器）](../trigger-nodes/n8n-nodes-base.workabletrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Workable](https://www.workable.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Workable API 文档](https://workable.readme.io/reference/generate-an-access-token)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- 一个 **Subdomain（子域名）**：即 Workable 域名中位于 `https://` 与 `.workable.com` 之间的部分。例如，完整域名为 `https://n8n.workable.com` 时，子域名为 `n8n`。也可以在 Workable 的 **Company Profile（公司资料）** 页面查看子域名。
- 一个 **Access Token（访问令牌）**：进入 **profile（个人资料）>** [**Integrations（集成）**](https://workable.com/backend/settings/integrations) **> Apps（应用）**，选择 **Generate API token（生成 API 令牌）**。更多信息请参阅[生成新令牌](https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#Generateanewtoken)。<br>

    
    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>令牌权限范围</strong></p><p>如果将此凭据用于 <a href="../trigger-nodes/n8n-nodes-base.workabletrigger.md">Workable Trigger</a> 节点，生成令牌时请选择 <code>r_candidates</code> 和 <code>r_jobs</code> 权限范围。如果将此凭据用于其他用途，请选择与使用场景相关的权限范围。</p><p>更多信息请参阅<a href="https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#SupportedAPIscopes">支持的 API 权限范围</a>。</p></div>
    
