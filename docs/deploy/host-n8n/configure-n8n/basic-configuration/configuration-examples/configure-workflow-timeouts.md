---
title: 配置工作流超时设置
description: 设置执行超时，决定工作流最多可以运行多久。
contentType: howto
nodeTitle: 配置工作流超时
originalFilePath: hosting/configuration/configuration-examples/execution-timeout.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/execution-timeout
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 配置工作流超时设置 <a href="#configure-workflow-timeout-settings" id="configure-workflow-timeout-settings"></a>

工作流超过此时长后会超时并取消，单位为秒。如果工作流在主进程中运行，则采用软超时，在当前节点执行完毕后生效。如果工作流在独立进程中运行，n8n 会先尝试软超时，再等待所设超时时长的五分之一，随后终止进程。

`EXECUTIONS_TIMEOUT` 的默认值为 `-1`。例如，要将超时设为一小时：

```bash
export EXECUTIONS_TIMEOUT=3600
```

也可以设置各个工作流允许配置的最大执行时长，单位为秒。例如，要将最大执行时长设为两小时：

```bash
export EXECUTIONS_TIMEOUT_MAX=7200
```
这些变量的更多信息请参阅[环境变量参考](../use-environment-variables/executions.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
