---
title: Guardrails 节点
description: 了解 n8n 中 Guardrails 节点的用法，并查看相关示例。
contentType:
- integration
- reference
nodeTitle: Guardrails 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Guardrails（内容防护）节点 <a href="#guardrails-node" id="guardrails-node"></a>

使用 Guardrails 节点对文本实施安全与内容策略。可在发送给 AI 模型_之前_验证用户输入，也可在工作流使用模型_输出_前进行检查。

{% hint style="info" %}
**使用大语言模型防护时必须连接聊天模型**

使用 **Check Text for Violations**（检查违规文本）操作中的大语言模型防护时，必须将 Chat Model 节点连接到 Model 输入。Jailbreak、NSFW、Topical Alignment 等检查依赖此连接评估文本。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Guardrails 节点。

### Operation（操作） <a href="#operation" id="operation"></a>

选择决定节点行为的操作模式。

- **Check Text for Violations**（检查违规文本）：提供完整的防护检查，任一违规会将数据项送入 **Fail**（失败）分支。
- **Sanitize Text**（清理文本）：提供部分检查，可检测 URL、正则模式、密钥或手机号、信用卡号等个人身份信息（PII），并用占位符替换检测到的违规内容。

### Text To Check（待检查文本） <a href="#text-to-check" id="text-to-check"></a>

防护规则需要评估的文本。通常使用表达式映射前置节点中的用户问题或 AI 模型响应。

### Guardrails（防护规则） <a href="#guardrails" id="guardrails"></a>

选择一个或多个规则应用到 **Text To Check**（待检查文本）。添加规则后，下方会显示其专用配置选项。

- **Keywords:**（关键词）检查输入中是否出现指定关键词。
    - **Keywords**（关键词）：以逗号分隔的禁止词列表。
- **Jailbreak:**（越狱）检测绕过 AI 安全措施或利用模型的尝试。
    - **Customize Prompt**（自定义提示词）：布尔选项，开启时显示含默认越狱检测提示词的输入框，可修改以调整规则。
    - **Threshold**（阈值）：0.0 到 1.0 之间的值，表示将输入标记为越狱所需的模型置信度。阈值越高，作出越狱判定所需的置信度越高。
- **NSFW:**（不适合工作场所的内容）检测生成 NSFW 内容的尝试。
    - **Customize Prompt**（自定义提示词）：布尔选项，开启时显示含默认 NSFW 检测提示词的输入框，可修改以调整规则。
    - **Threshold**（阈值）：0.0 到 1.0 之间的值，表示将内容标记为 NSFW 所需的置信度。
- **PII:**（个人身份信息）检测文本中的个人身份信息。
    - **Type**（类型）：选择要扫描的 PII 实体：
        - **All**（全部）：扫描所有可用实体类型。
        - **Selected**（指定）：从列表中选择特定实体。
    - **Entities**（实体）：仅在 **Type**（类型）为 **Selected**（指定）时出现，用于多选待检测的 PII 类型，例如 `CREDIT_CARD`、`EMAIL_ADDRESS`、`PHONE_NUMBER` 和 `US_SSN`。
- **Secret Keys:**（密钥）检测文本中的密钥或 API 凭据。
    - **Permissiveness**（宽松程度）：检测密钥时的严格或宽松程度：
        - **Strict**（严格）
        - **Permissive**（宽松）
        - **Balanced**（平衡）
- **Topical Alignment:**（主题一致性）确保对话处于预定义的范围或主题内，也称“业务范围”。
    - **Prompt**（提示词）：定义_允许_主题的预设提示词，规则检查 **Text To Check**（待检查文本）是否与其一致。
    - **Threshold**（阈值）：0.0 到 1.0 之间的值，表示将输入标记为_偏题_所需的置信度。
- **URLs:**（URL）管理输入中的 URL。除 **Block All URLs Except**（阻止以下列表以外的所有 URL）中指定的 URL 外，所有 URL 均视为违规。
    - **Block All URLs Except**（阻止以下列表以外的所有 URL）：可选，填写以逗号分隔的允许 URL 列表。
    - **Allowed Schemes**（允许的协议）：选择允许的 URL 协议，例如 `https`、`http`、`ftp` 和 `mailto`。
    - **Block userinfo**（阻止用户信息）：布尔选项，开启时阻止包含用户凭据的 URL，例如 `user:pass@example.com`，防止凭据注入。
    - **Allow subdomain**（允许子域名）：布尔选项，开启时自动允许 **Block All URLs Except** 列表中 URL 的子域名。例如，`sub.example.com` 在 `example.com` 已列入允许列表时会被放行。
- **Custom:**（自定义）定义基于大语言模型的自定义防护规则。
    - **Name**（名称）：自定义规则的描述性名称，例如“检查粗鲁用语”。
    - **Prompt**（提示词）：说明 AI 模型应检查什么的提示词。
    - **Threshold**（阈值）：0.0 到 1.0 之间的值，表示将输入标记为违规所需的置信度。
- **Custom Regex**（自定义正则）：定义自己的正则表达式模式。
    - **Name**（名称）：模式名称，在 **Sanitize Text**（清理文本）模式中用作占位符。
    - **Regex**（正则表达式）：自定义正则表达式模式。

### Customize System Message（自定义系统消息） <a href="#customize-system-message" id="customize-system-message"></a>

开启时显示消息输入框，防护规则用此消息实施阈值要求，并按 schema 输出 JSON。修改它会影响全局防护行为。
