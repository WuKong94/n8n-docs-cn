---
title: 隧道
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## 通过隧道运行 n8n <a href="#n8n-with-tunnel" id="n8n-with-tunnel"></a>

{% hint style="danger" %}
此功能用于本地开发和测试，不适合安全地用于生产环境。
{% endhint %}

{% hint style="warning" %}
**开发工具**

隧道功能是方便本地开发的工具，其底层实现可能随 n8n 版本变化。
{% endhint %}

观看视频指南，了解如何通过 Cloudflare 或 ngrok 配置隧道：

{% embed url="https://www.youtube.com/embed/O9dpO81dEQ0" %}

要使用 GitHub 等外部服务触发器节点的 Webhook，n8n 必须能从互联网访问。n8n 提供基于 [cloudflared](https://github.com/cloudflare/cloudflared) 的隧道服务，将互联网请求转发到本地 n8n 实例。隧道运行需要安装 Docker。

根据 n8n 的运行方式，可以通过两种方式使用隧道：
