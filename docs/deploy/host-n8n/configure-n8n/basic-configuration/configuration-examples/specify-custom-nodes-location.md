---
title: 指定自定义节点的位置
description: 添加文件夹并指定自定义节点的路径。
contentType: howto
nodeTitle: 指定自定义节点位置
originalFilePath: hosting/configuration/configuration-examples/custom-nodes-location.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 指定自定义节点的位置 <a href="#specify-location-for-your-custom-nodes" id="specify-location-for-your-custom-nodes"></a>

每个用户都可以添加自定义节点，n8n 会在启动时加载。默认位置
是启动 n8n 的用户目录下的 `.n8n/custom` 子文件夹。

可以通过环境变量定义更多文件夹：

```bash
export N8N_CUSTOM_EXTENSIONS="/home/jim/n8n/custom-nodes;/data/n8n/nodes"
```
此变量的更多信息请参阅[环境变量参考](../use-environment-variables/nodes.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
