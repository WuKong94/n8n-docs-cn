---
title: MQTT 凭据
description: MQTT 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 MQTT 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: MQTT 凭据
originalFilePath: integrations/builtin/credentials/mqtt.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mqtt
url: https://docs.n8n.io/integrations/builtin/credentials/mqtt
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MQTT 凭据 <a href="#mqtt-credentials" id="mqtt-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [MQTT](../app-nodes/n8n-nodes-base.mqtt.md)
- [MQTT Trigger（触发器）](../trigger-nodes/n8n-nodes-base.mqtttrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

安装 [MQTT 消息代理](https://mqtt.org/)。

MQTT 在 [MQTT Software](https://mqtt.org/software/) 中提供了服务器及消息代理列表。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Broker connection（消息代理连接）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 MQTT 协议的更多信息，请参阅 [MQTT 文档](https://mqtt.org/)。

更详细的配置及相关信息，请参阅消息代理提供商的文档。

## 使用消息代理连接 <a href="#using-broker-connection" id="using-broker-connection"></a>

配置此凭据需要：

- MQTT 消息代理的 **Protocol**（协议）
- **Host**（主机）
- **Port**（端口）
- 用于身份验证的 **Username**（用户名）和 **Password**（密码）
- 使用 **SSL** 时，需要相应证书及密钥

设置步骤如下：

1. 选择消息代理的 **Protocol**（协议），它决定 n8n 使用的 URL，可选：
    - **Mqtt**：URL 以标准的 `mqtt:` 协议开头。
    - **Mqtts**：URL 以安全的 `mqtts:` 协议开头。
    - **Ws**：URL 以 WebSocket `ws:` 协议开头。
2. 输入消息代理的 **Host**（主机）。
3. 输入 n8n 连接消息代理主机时使用的 **Port**（端口）号。
4. 输入登录消息代理所用的 **Username**（用户名）。
5. 输入该用户的 **Password**（密码）。
6. 如需在离线时接收 QoS 1 和 2 消息，请关闭 **Clean Session**（清理会话）开关。
7. 输入此凭据使用的 **Client ID**（客户端 ID）。留空时，n8n 会自动生成。可使用固定值或基于表达式的 Client ID。
    - Client ID 有助于识别和跟踪连接访问。n8n 建议在其中包含 `n8n`，便于审计。
8. 如果 MQTT 消息代理使用 SSL，请开启 **SSL** 开关。开启后：
    1. 选择是否使用基于证书的 **Passwordless**（无密码）连接，其方式类似 SASL 机制 EXTERNAL。开启时：
        1. 选择是否 **Reject Unauthorized Certificate**（拒绝未授权证书）：关闭时，即使证书验证失败，n8n 仍会连接。
        2. 添加 SSL **Client Certificate**（客户端证书）。
        3. 添加该客户端证书对应的 SSL **Client Key**（客户端密钥）。
    2. 一个或多个 SSL **CA Certificates**（CA 证书）。

更详细的配置说明，请参阅 MQTT 消息代理提供商的文档。
