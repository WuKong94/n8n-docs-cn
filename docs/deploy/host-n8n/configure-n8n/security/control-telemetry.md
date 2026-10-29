---
title: 退出数据收集
contentType: howto
nodeTitle: 控制遥测
originalFilePath: hosting/securing/telemetry-opt-out.md
originalUrl: https://docs.n8n.io/hosting/securing/telemetry-opt-out
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry
description: 在 n8n 实例中退出遥测数据收集。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 控制遥测 <a id="control-telemetry"></a>

n8n 从自托管安装中收集匿名遥测数据。你可以选择退出。

## 收集的数据 <a href="#collected-data" id="collected-data"></a>

n8n 收集的数据详情，请参阅[隐私 | 自托管 n8n 的数据收集](../../../../privacy-and-security/README.md#data-collection-in-self-hosted-n8n)。

## 收集方式 <a href="#how-collection-works" id="how-collection-works"></a>

大多数数据在事件发生时发送。工作流执行次数和实例心跳每六小时定期发送。

## 退出数据收集 <a href="#opting-out-of-data-collection" id="opting-out-of-data-collection"></a>

n8n 默认启用遥测收集。要禁用，请配置以下环境变量。

### 退出遥测事件收集 <a href="#opt-out-of-telemetry-events" id="opt-out-of-telemetry-events"></a>

要退出诊断遥测，将 `N8N_DIAGNOSTICS_ENABLED` 环境变量设为 false：

```bash
export N8N_DIAGNOSTICS_ENABLED=false
```

### 退出 n8n 新版本检查 <a href="#opt-out-of-checking-for-new-versions-of-n8n" id="opt-out-of-checking-for-new-versions-of-n8n"></a>

要退出版本通知，将 `N8N_VERSION_NOTIFICATIONS_ENABLED` 环境变量设为 false：

```bash
export N8N_VERSION_NOTIFICATIONS_ENABLED=false
```

## 禁止连接 n8n 服务器 <a href="#disable-all-connection-to-n8n-servers" id="disable-all-connection-to-n8n-servers"></a>

要禁止与 n8n 服务器的全部通信，请参阅[隔离 n8n](../basic-configuration/configuration-examples/isolate-n8n.md)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [部署环境变量](../basic-configuration/use-environment-variables/deployment.md)：这些环境变量的更多信息。
* [配置](../basic-configuration.md)：如何设置环境变量。
