---
title: 在 Code 节点中启用模块
description: 允许在 Code 节点中使用内置模块和外部模块。
contentType: howto
nodeTitle: 在 Code 节点中启用模块
originalFilePath: hosting/configuration/configuration-examples/modules-in-code-node.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/modules-in-code-node
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Code 节点中启用模块 <a href="#enable-modules-in-code-node" id="enable-modules-in-code-node"></a>

出于安全原因，Code 节点会限制导入模块。可以通过以下环境变量，解除对内置模块和外部模块的限制：

- `NODE_FUNCTION_ALLOW_BUILTIN`：用于内置模块。
- `NODE_FUNCTION_ALLOW_EXTERNAL`：用于 n8n/node_modules 目录中的外部模块。未设置此环境变量时，禁用外部模块支持。

```bash
# Allows usage of all builtin modules <a href="#allows-usage-of-all-builtin-modules" id="allows-usage-of-all-builtin-modules"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=*

# Allows usage of only crypto <a href="#allows-usage-of-only-crypto" id="allows-usage-of-only-crypto"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=crypto

# Allows usage of only crypto and fs <a href="#allows-usage-of-only-crypto-and-fs" id="allows-usage-of-only-crypto-and-fs"></a>
export NODE_FUNCTION_ALLOW_BUILTIN=crypto,fs

# Allow usage of external npm modules. <a href="#allow-usage-of-external-npm-modules" id="allow-usage-of-external-npm-modules"></a>
export NODE_FUNCTION_ALLOW_EXTERNAL=moment,lodash
```
{% hint style="info" %}
**使用任务运行器时**

如果 n8n 实例已配置[任务运行器](../../set-up-task-runners.md)，请将环境变量添加到任务运行器，而非 n8n 主节点。
{% endhint %}

这些变量的更多信息请参阅[环境变量参考](../use-environment-variables/nodes.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
