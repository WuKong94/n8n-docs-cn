---
title: 配置反向代理下的 Webhook URL
description: 自定义 n8n Webhook URL，使其兼容反向代理设置。
contentType: howto
nodeTitle: 配置反向代理下的 Webhook URL
originalFilePath: hosting/configuration/configuration-examples/webhook-url.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在反向代理后配置 n8n Webhook <a href="#configure-n8n-webhooks-with-reverse-proxy" id="configure-n8n-webhooks-with-reverse-proxy"></a>

n8n 通过组合 `N8N_PROTOCOL`、`N8N_HOST` 和 `N8N_PORT` 创建 Webhook URL。如果 n8n 位于反向代理后，这种方式无法正常工作，因为 n8n 在内部运行于 5678 端口，而反向代理通过 443 端口对外提供访问。

在反向代理后运行 n8n 时，请完成以下设置：

* 使用 `N8N_WEBHOOK_URL` 环境变量手动设置 Webhook URL，让 n8n 能在编辑器中显示，并向外部服务注册正确的 Webhook URL。（`N8N_WEBHOOK_URL` 替代了 `WEBHOOK_URL`；后者自 n8n 2.35.0 起已弃用，继续使用 `WEBHOOK_URL` 时，n8n 会记录弃用警告。）
* 将 `N8N_PROXY_HOPS` 环境变量设为 `1`。
* 在请求路径的最后一个代理上，设置以下请求头，以传递原始请求的信息：
    * [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-For)
    * [`X-Forwarded-Host`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-Host)
    * [`X-Forwarded-Proto`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-Proto)

```bash
export N8N_WEBHOOK_URL=https://n8n.example.com/
export N8N_PROXY_HOPS=1
```
此变量的更多信息请参阅[环境变量参考](../use-environment-variables/endpoints.md)。

如果还通过同一反向代理运行 n8n 的[实例级 MCP 服务器](../../../../../connect/connect-to-n8n-mcp-server.md)，请确认代理也转发了 [MCP 请求头](../../../../../connect/connect-to-n8n-mcp-server.md#mcp-request-headers)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
