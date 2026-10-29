---
title: 设置自托管实例的时区
description: 更改自托管 n8n 实例的默认时区。
contentType: howto
nodeTitle: 设置时区
originalFilePath: hosting/configuration/configuration-examples/time-zone.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/time-zone
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置自托管实例的时区 <a href="#set-the-self-hosted-instance-timezone" id="set-the-self-hosted-instance-timezone"></a>

默认时区为 America/New_York。例如，Schedule 节点通过此时区判断工作流应何时启动。要更改默认时区，请为 `GENERIC_TIMEZONE` 设置相应值。例如，设置为德国柏林时区：

```bash
export GENERIC_TIMEZONE=Europe/Berlin
```

请在[时区名称列表](https://momentjs.com/timezone/)中查找所需时区。

此变量的更多信息请参阅[环境变量参考](../use-environment-variables/timezone-and-localization.md)。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
