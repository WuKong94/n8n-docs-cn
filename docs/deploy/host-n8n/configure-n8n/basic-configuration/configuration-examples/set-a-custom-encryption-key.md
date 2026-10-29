---
title: 设置自定义加密密钥
description: 为 n8n 设置自定义密钥，以安全加密凭据。
contentType: howto
nodeTitle: 设置自定义加密密钥
originalFilePath: hosting/configuration/configuration-examples/encryption-key.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置自定义加密密钥 <a href="#set-a-custom-encryption-key" id="set-a-custom-encryption-key"></a>

n8n 首次启动时自动生成随机加密密钥，并将其
保存在 `~/.n8n` 文件夹中。n8n 使用此密钥加密凭据，
然后将凭据保存到数据库。如果设置文件中还没有密钥，
可以通过环境变量指定，
让 n8n 使用你的自定义密钥，而不生成新密钥。

在[队列模式](../../scaling/enable-queue-mode.md)中，必须为所有工作进程指定加密密钥环境变量。

```bash
export N8N_ENCRYPTION_KEY=<SOME RANDOM STRING>
```
此变量的更多信息请参阅[环境变量参考](../use-environment-variables/deployment.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
