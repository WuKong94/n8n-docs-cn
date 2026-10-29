---
title: Microsoft Agent 365 凭据
description: Microsoft Agent 365 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Microsoft Agent 365
  的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Microsoft Agent 365 凭据
originalFilePath: integrations/builtin/credentials/microsoftagent365.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365
url: https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft Agent 365 凭据 <a href="#microsoft-agent-365-credentials" id="microsoft-agent-365-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Microsoft Agent 365 Trigger（触发器）](../cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger.md)

{% hint style="info" %}
**预览状态**

Microsoft Agent 365 是早期预览功能，需要加入 [Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)才能提前使用。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 已加入 [Microsoft Frontier 预览计划](https://adoption.microsoft.com/copilot/frontier-program/)
- [Microsoft Azure](https://azure.microsoft.com/) 账户
- 使用 Agent 365 CLI 创建的 Agent 365 蓝图

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2（应用注册）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Agent 365 开发者文档](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

配置此凭据需要：

- **Tenant ID**（租户 ID）：Microsoft Entra 租户 ID
- **Client ID**（客户端 ID）：Azure 应用注册的应用程序（客户端）ID
- **Client Secret**（客户端密钥）：为应用注册生成的秘密值

设置凭据的步骤如下：

1. 在 [Microsoft Entra ID](https://entra.microsoft.com/#home) 中找到租户 ID，复制后填入 n8n 的 **Tenant ID**（租户 ID）。
2. 打开 [Microsoft 应用注册门户](https://aka.ms/appregistrations)，按照 Microsoft Agent 365 的[自定义客户端应用注册指南](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/custom-client-app-registration)操作。创建自定义客户端应用后，复制应用程序（客户端）ID，填入 n8n 的 **Client ID**（客户端 ID）。
3. 按照[凭据指南](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret)生成客户端密钥，复制 **Value**（值）列中的 **Secret**（秘密值），填入 n8n 的 **Client Secret**（客户端密钥）。

{% hint style="info" %}
**传入请求验证**

Microsoft Agent 365 Trigger 节点还会使用 **Client ID**（客户端 ID）验证传入的 webhook 请求，因此该值必须与智能体应用注册的应用程序（客户端）ID 匹配。请参阅 [Webhook 身份验证](../cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger.md#webhook-authentication)。
{% endhint %}

建议使用 [Agent 365 CLI](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/agent-365-cli) 创建智能体蓝图和清单。
