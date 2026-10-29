---
title: TOTP（基于时间的一次性密码）
description: 工作流自动化平台 n8n 中的 TOTP（基于时间的一次性密码） 节点文档，包括使用说明和示例链接。
contentType:
- integration
- reference
nodeTitle: TOTP（基于时间的一次性密码）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.totp.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# TOTP（基于时间的一次性密码） <a href="#totp" id="totp"></a>

TOTP 节点用于生成 TOTP（基于时间的一次性密码）。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [TOTP 凭据](../credentials/totp.md)。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

使用以下参数配置节点。

### Credential to connect with（连接凭据） <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建供节点使用的 [TOTP 凭据](../credentials/totp.md)。

### Operation（操作） <a href="#operation" id="operation"></a>

目前仅支持 **Generate Secret**（生成密钥）操作。

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下 **Options**（选项）进一步配置节点。

### Algorithm（算法） <a href="#algorithm" id="algorithm"></a>

选择要使用的 HMAC 哈希算法，默认为 SHA1。

### Digits（位数） <a href="#digits" id="digits"></a>

输入生成的验证码位数，默认为 `6`。

### Period（有效期） <a href="#period" id="period"></a>

输入 TOTP 的有效秒数，默认为 `30`。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 TOTP（基于时间的一次性密码） 集成模板](https://n8n.io/integrations/totp)，或[搜索所有模板](https://n8n.io/workflows/)
