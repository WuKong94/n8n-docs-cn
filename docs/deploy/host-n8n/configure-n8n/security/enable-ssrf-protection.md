---
title: SSRF 防护
description: 保护自托管 n8n 实例免受服务端请求伪造（SSRF）攻击。
contentType: howto
nodeTitle: 启用 SSRF 防护
originalFilePath: hosting/securing/ssrf-protection.md
originalUrl: https://docs.n8n.io/hosting/securing/ssrf-protection
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SSRF 防护 <a href="#ssrf-protection" id="ssrf-protection"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.12.0 起提供 SSRF 防护。
{% endhint %}

服务端请求伪造（SSRF）攻击会滥用工作流节点，向本不应访问的内部网络资源、云元数据端点或本机服务发出请求。

{% hint style="warning" %}
SSRF 防护是额外的应用层防线。仍应始终在基础设施上配置防火墙、安全组和网络策略等网络层保护，作为主要防线。n8n 的 SSRF 防护在此基础上提供纵深防御。
{% endhint %}

## 启用 SSRF 防护 <a href="#enable-ssrf-protection" id="enable-ssrf-protection"></a>

```
N8N_SSRF_PROTECTION_ENABLED=true
```

启用后，n8n 会依据配置的允许和阻止范围，验证用户可控节点，例如 HTTP Request 节点的全部出站 HTTP 请求。检查包含重定向目标和 DNS 解析，以防止 DNS 重绑定等绕过方式。

## 默认阻止的范围 <a href="#default-blocked-ranges" id="default-blocked-ranges"></a>

启用 SSRF 防护后，默认阻止以下 IP 范围：

| 范围 | 说明 |
| :---- | :---------- |
| `10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16` | RFC 1918 私有地址 |
| `127.0.0.0/8`、`::1/128` | 环回地址 |
| `169.254.0.0/16`、`fe80::/10` | 链路本地地址 |
| `fc00::/7`、`fd00::/8` | IPv6 唯一本地地址 |
| `0.0.0.0/8`、`192.0.0.0/24`、`192.0.2.0/24`、`198.18.0.0/15`、`198.51.100.0/24`、`203.0.113.0/24` | 保留或特殊用途地址 |

可以通过 `N8N_SSRF_BLOCKED_IP_RANGES=default,100.0.0.0/8` 扩展此列表。

## 允许访问内部服务 <a href="#allow-access-to-internal-services" id="allow-access-to-internal-services"></a>

工作流需要访问合法内部服务时，请使用允许列表。允许列表优先于阻止列表，顺序为：主机名允许列表 > IP 允许列表 > IP 阻止列表。

按主机名模式允许，支持 `*.n8n.internal` 等通配符：

```
N8N_SSRF_ALLOWED_HOSTNAMES=*.n8n.internal,*.company.local
```

按 IP 范围允许：

```
N8N_SSRF_ALLOWED_IP_RANGES=10.0.1.0/24,10.0.2.50/32
```

{% hint style="warning" %}
只将你控制的主机名，例如内部 DNS 区域，加入允许列表。主机名允许列表会绕过 IP 阻止列表检查。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [SSRF 防护环境变量](../basic-configuration/use-environment-variables/ssrf-protection.md)：完整配置选项列表。
* [配置方式](../basic-configuration.md)：设置环境变量的更多说明。
