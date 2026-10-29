---
title: 隔离 n8n
description: 阻止 n8n 实例连接到 n8n 服务器。
contentType: howto
nodeTitle: 隔离 n8n
originalFilePath: hosting/configuration/configuration-examples/isolation.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/isolation
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 隔离 n8n <a href="#isolate-n8n" id="isolate-n8n"></a>

默认情况下，自托管 n8n 实例会向 n8n 服务器发送数据，用于通知用户可用更新、工作流模板和诊断信息。

要阻止实例连接到 n8n 服务器，请将以下环境变量设为 false：

```
N8N_DIAGNOSTICS_ENABLED=false
N8N_VERSION_NOTIFICATIONS_ENABLED=false
N8N_TEMPLATES_ENABLED=false
```

清空 n8n 的诊断配置：

```
EXTERNAL_FRONTEND_HOOKS_URLS=
N8N_DIAGNOSTICS_CONFIG_FRONTEND=
N8N_DIAGNOSTICS_CONFIG_BACKEND=
```

这些变量的更多信息请参阅[环境变量参考](../use-environment-variables/deployment.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
