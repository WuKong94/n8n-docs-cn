---
title: Local File Trigger 节点
description: 了解如何在 n8n 工作流中配置和使用 Local File Trigger 节点。
contentType:
- integration
- reference
priority: high
nodeTitle: Local File Trigger 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Local File Trigger（本地文件触发器）节点 <a href="#local-file-trigger-node" id="local-file-trigger-node"></a>

Local File Trigger 节点检测到文件系统变化时启动工作流，变化包括文件或文件夹的新增、修改和删除。

{% hint style="warning" %}
**安全注意事项**

在存在不可信用户的环境中，Local File Trigger 节点可能带来较大的安全风险，因此从 n8n 2.0 起默认[禁用](../../../deploy/host-n8n/configure-n8n/security/block-specific-nodes.md#exclude-nodes)。
{% endhint %}

{% hint style="info" %}
**仅限自托管 n8n**

n8n Cloud 不提供此节点。
{% endhint %}

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

通过 **Trigger On**（触发事件）参数，选择要监听的事件。

## 特定文件的变化 <a href="#changes-to-a-specific-file" id="changes-to-a-specific-file"></a>

指定文件发生变化时，节点触发。

在 **File to Watch**（监听的文件）中输入文件路径。

## 特定文件夹中的变化 <a href="#changes-involving-a-specific-folder" id="changes-involving-a-specific-folder"></a>

所选文件夹中发生变化时，节点触发。

配置以下参数：

- **Folder to Watch**（监听的文件夹）：输入文件夹路径。
- **Watch for**（监听类型）：选择要监听的变化类型。


## 节点选项 <a href="#node-options" id="node-options"></a>

使用节点 **Options**（选项）来包含或排除文件和文件夹。

- **Include Linked Files/Folders**（包含链接文件／文件夹）：同时监听链接文件或文件夹的变化。
- **Ignore**（忽略）：要忽略的文件或路径。n8n 会匹配整个路径，而不只是文件名，支持 [Anymatch](https://github.com/micromatch/anymatch) 语法。
- **Max Folder Depth**（最大文件夹深度）：设置向下监听文件夹结构的深度。

### Ignore（忽略）示例 <a href="#examples-for-ignore" id="examples-for-ignore"></a>

忽略单个文件：

```sh
**/<fileName>.<suffix>
# For example, **/myfile.txt <a href="#for-example-myfiletxt" id="for-example-myfiletxt"></a>
```

忽略所监听目录中的子目录：

```sh
**/<directoryName>/**
# For example, **/myDirectory/** <a href="#for-example-mydirectory" id="for-example-mydirectory"></a>
```

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Local File Trigger 节点集成模板](https://n8n.io/integrations/local-file-trigger)，或[搜索所有模板](https://n8n.io/workflows/)
