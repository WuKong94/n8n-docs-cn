---
title: 设置 SSL
description: 为自托管 n8n 实例设置 SSL。
contentType: howto
nodeTitle: 设置 SSL
originalFilePath: hosting/securing/set-up-ssl.md
originalUrl: https://docs.n8n.io/hosting/securing/set-up-ssl
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 SSL <a href="#set-up-ssl" id="set-up-ssl"></a>

n8n 有两种支持 TLS/SSL 的方式。

## 使用反向代理，推荐 <a href="#use-a-reverse-proxy-recommended" id="use-a-reverse-proxy-recommended"></a>

在 n8n 实例前使用 [Traefik](https://doc.traefik.io/traefik/) 等反向代理，或网络负载均衡器（NLB）。这种方式也应负责处理证书续期。

更多信息请参阅[安全 | 数据加密](https://n8n.io/legal/#security)。

## 直接向 n8n 提供证书 <a href="#pass-certificates-into-n8n-directly" id="pass-certificates-into-n8n-directly"></a>

也可以直接向 n8n 提供证书。将 `N8N_SSL_CERT` 和 `N8N_SSL_KEY` 环境变量分别指向生成的证书和密钥文件。

需要自行确保持续续期，保持证书有效。

这些变量的更多信息请参阅[部署环境变量](../basic-configuration/use-environment-variables/deployment.md)，设置环境变量的方法请参阅[配置](../basic-configuration.md)。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
