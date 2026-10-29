---
title: SSRF 防护环境变量
description: 配置自托管 n8n 实例的 SSRF 防护。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: SSRF 防护
originalFilePath: hosting/configuration/environment-variables/ssrf-protection.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/ssrf-protection
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SSRF 防护环境变量 <a href="#ssrf-protection-environment-variables" id="ssrf-protection-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

服务端请求伪造（SSRF）是一种诱导服务器向攻击者指定地址发送 HTTP 请求的攻击，例如仅限内部访问的 `localhost`、私有网段或云提供商的元数据端点 `169.254.169.254`。工作流可能根据用户可控的输入构造请求 URL，因此 n8n 可以对目标源自此类输入的出站请求进行防护。

SSRF 防护默认关闭。本页列出启用和调整该功能的变量。

## 防护范围 <a id="what-protection-covers"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_SSRF_PROTECTION_ENABLED` | Boolean | `false` | 为目标可由用户控制的请求启用 SSRF 防护。 |
| `N8N_SSRF_BLOCKED_IP_RANGES` | String | `default` | 要阻止的 CIDR 范围，以逗号分隔。关键字 `default` 不区分大小写，会展开为 n8n 内置集合。可以追加自定义范围：`default,100.64.0.0/10`。 |
| `N8N_SSRF_ALLOWED_IP_RANGES` | String | `-` | 允许的 CIDR 范围，以逗号分隔，优先于阻止列表。可用于访问已知内部主机。 |
| `N8N_SSRF_ALLOWED_HOSTNAMES` | String | `-` | 允许的主机名，以逗号分隔。支持前导 `*.` 通配符：`*.internal.example.com` 匹配所有子域名，包括多级子域名，但不匹配根域名。匹配不区分大小写。 |
| `N8N_SSRF_BLOCKED_HOSTNAMES` | String | `-` | 按名称拒绝的主机名，以逗号分隔，在 DNS 解析前检查。支持前导 `*.` 通配符及不区分大小写匹配，与 `N8N_SSRF_ALLOWED_HOSTNAMES` 相同。允许的主机名始终覆盖被阻止的主机名。 |
| `N8N_SSRF_DNS_CACHE_MAX_SIZE` | Number | `1048576` | 内部 DNS 解析缓存的大小上限，单位为字节，默认为 1 MB。缓存满时，n8n 移除最近最少使用的条目。 |

对于 `N8N_SSRF_BLOCKED_IP_RANGES` 或 `N8N_SSRF_ALLOWED_IP_RANGES` 中无效的 CIDR 范围，n8n 会记录警告并跳过，因此拼写错误不会阻止实例启动。

### 默认阻止的范围 <a id="blocked-by-default"></a>

当 `N8N_SSRF_BLOCKED_IP_RANGES` 包含 `default` 时，n8n 会阻止以下范围：

- 私有网络（[RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)）：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`
- 环回地址：`127.0.0.0/8`、`::1/128`
- 链路本地地址，包括云元数据：`169.254.0.0/16`、`fe80::/10`
- IPv6 唯一本地地址：`fc00::/7`、`fd00::/8`
- 保留或特殊用途地址：`0.0.0.0/8`、`192.0.0.0/24`、`192.0.2.0/24`、`198.18.0.0/15`、`198.51.100.0/24`、`203.0.113.0/24`

## n8n 如何评估请求 <a id="how-n8n-evaluates-a-request"></a>

n8n 按以下顺序检查每个目标，遇到首个匹配规则即停止：

1. **允许的主机名**：请求主机名匹配 `N8N_SSRF_ALLOWED_HOSTNAMES` 时，允许请求。
2. **阻止的主机名**：请求主机名匹配 `N8N_SSRF_BLOCKED_HOSTNAMES` 时，阻止请求。此检查在 DNS 解析前进行，因此即使该名称最终会解析到公网 IP，也会直接拒绝而不查询 DNS。
3. **允许的 IP 范围**：解析后的 IP 匹配 `N8N_SSRF_ALLOWED_IP_RANGES` 时，允许请求。
4. **阻止的 IP 范围**：解析后的 IP 匹配 `N8N_SSRF_BLOCKED_IP_RANGES` 时，阻止请求。
5. **其他情况**：允许请求。

由于 n8n 优先检查允许列表，允许项始终覆盖阻止列表。

## 常见场景 <a id="common-scenarios"></a>

有意访问内部服务。工作流必须调用内部主机时，只允许该目标，不要关闭防护：

```bash
N8N_SSRF_PROTECTION_ENABLED=true
N8N_SSRF_ALLOWED_IP_RANGES=10.20.0.5/32
```

允许内部主机名：

```bash
N8N_SSRF_ALLOWED_HOSTNAMES=*.svc.cluster.local
```

在默认规则基础上进一步收紧限制，添加当前环境专用的网段：

```bash
N8N_SSRF_BLOCKED_IP_RANGES=default,100.64.0.0/10
```

按名称拒绝主机。阻止某个主机及其全部子域名，不论最终解析到哪个 IP：

```bash
N8N_SSRF_BLOCKED_HOSTNAMES=example.com,*.example.com
```

{% hint style="info" %}
**按主机名阻止属于出站访问治理，不能替代 SSRF 加固**

`N8N_SSRF_BLOCKED_HOSTNAMES` 按名称拒绝请求，因此调用方仍可能通过 IP 字面值、其他主机名或 DNS 重绑定访问同一目标。可以用它限制已知的不期望目标，但 SSRF 防护仍应依赖基于 IP 的阻止列表。
{% endhint %}

## n8n 阻止请求时 <a id="when-n8n-blocks-a-request"></a>

按 IP 阻止时，请求会返回错误“The request was blocked because it resolves to a restricted IP address”（请求解析到受限 IP 地址，已被阻止）。按主机名阻止时，会返回“The request was blocked because the destination hostname is restricted”（目标主机名受限，请求已被阻止）。两种错误都会指出目标，并提示用户联系 n8n 管理员，允许相应主机名或 IP 范围。确认请求合法后，将预期目标添加到 `N8N_SSRF_ALLOWED_IP_RANGES` 或 `N8N_SSRF_ALLOWED_HOSTNAMES`。

{% hint style="warning" %}
**在生产环境启用前检查允许列表**

防护默认关闭，以免影响现有需要访问内部服务的自托管部署。启用前，列出工作流需要的内部主机并加入允许列表。优先使用单个主机或主机名等精确允许项，不要直接关闭防护。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
