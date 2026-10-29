---
title: Netscaler ADC 凭据
description: Netscaler ADC 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Netscaler ADC 的身份验证。
contentType:
- integration
- reference
nodeTitle: Netscaler ADC 凭据
originalFilePath: integrations/builtin/credentials/netscaleradc.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/netscaleradc
url: https://docs.n8n.io/integrations/builtin/credentials/netscaleradc
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Netscaler ADC 凭据 <a href="#netscaler-adc-credentials" id="netscaler-adc-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Netscaler ADC 节点](../app-nodes/n8n-nodes-base.netscaleradc.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

安装 [NetScaler/Citrix ADC 设备](https://docs.netscaler.com/en-us/citrix-adc/current-release/getting-started-with-citrix-adc)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth（基本身份验证）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

该服务的更多信息，请参阅 [Netscaler ADC 14.1 NITRO API 文档](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release)。

## 使用基本身份验证 <a href="#using-basic-auth" id="using-basic-auth"></a>

配置此凭据需要：

* **URL**：输入 NetScaler/Citrix ADC 实例的 URL。
* **Username**（用户名）：输入 NetScaler/Citrix ADC 用户名。
* **Password**（密码）：输入 NetScaler/Citrix ADC 密码。

更多信息请参阅[执行基本 Netscaler ADC 操作](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/performing-basic-netscaler-operations)。
