---
title: 指定用户文件夹路径
description: 指定存储用户专属数据的文件夹位置。
contentType: howto
nodeTitle: 指定用户文件夹路径
originalFilePath: hosting/configuration/configuration-examples/user-folder.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 指定用户文件夹路径 <a href="#specify-user-folder-path" id="specify-user-folder-path"></a>

n8n 将加密密钥、SQLite 数据库文件、
隧道 ID（如果使用隧道）等用户专属数据，保存在启动 n8n 的用户目录下的 `.n8n` 子文件夹中。可以通过环境变量覆盖用户文件夹位置。

```bash
export N8N_USER_FOLDER=/home/jim/n8n
```
此变量的更多信息请参阅[环境变量参考](../use-environment-variables/deployment.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
