---
title: 阻止访问节点
description: 防止 n8n 用户访问指定节点。
contentType: howto
nodeTitle: 阻止特定节点
originalFilePath: hosting/securing/blocking-nodes.md
originalUrl: https://docs.n8n.io/hosting/securing/blocking-nodes
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 阻止访问节点 <a href="#block-access-to-nodes" id="block-access-to-nodes"></a>

出于安全原因，你可能希望禁止用户访问或使用特定 n8n 节点。用户可能不可信时，这种限制尤其有用。

使用 `NODES_EXCLUDE` 环境变量，阻止用户访问指定节点。

如需按项目阻止节点，或不重启 n8n 就应用限制，请使用[节点类型策略](../../../../administer/manage-users-and-access/control-node-availability.md)。`NODES_EXCLUDE` 会完全阻止 n8n 加载节点，因此对于绝不应运行的节点，这是更强的限制方式。

## 排除节点 <a href="#exclude-nodes" id="exclude-nodes"></a>

更新 `NODES_EXCLUDE` 环境变量，将所有要禁止用户使用的节点写入字符串数组。

例如，按以下方式设置变量：

```
NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"
```

会阻止 [Execute Command](../../../../integrations/builtin/core-nodes/n8n-nodes-base.executecommand/README.md) 和 [Read/Write Files from Disk](../../../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) 节点。

n8n 用户将无法搜索或使用这些节点。

## 建议阻止的节点 <a href="#suggested-nodes-to-block" id="suggested-nodes-to-block"></a>

可能带来安全风险的节点取决于使用场景和用户类型。可以先考虑以下节点：

* [Execute Command](../../../../integrations/builtin/core-nodes/n8n-nodes-base.executecommand/README.md)
* [Read/Write Files from Disk](../../../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)

## 启用默认被阻止的节点 <a href="#enable-nodes-that-are-blocked-by-default" id="enable-nodes-that-are-blocked-by-default"></a>

Execute Command 等部分节点默认被阻止。要启用，请将它们从排除列表中移除：

```
NODES_EXCLUDE: "[]"
```

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [节点环境变量](../basic-configuration/use-environment-variables/nodes.md)：此环境变量的更多信息。
* [配置](../basic-configuration.md)：如何设置环境变量。
