---
title: Microsoft SharePoint 触发器节点文档
description: 了解如何在 n8n 中使用 Microsoft SharePoint 触发器节点，在 Microsoft SharePoint 中的文件或列表项变更时启动工作流。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Microsoft SharePoint 触发器节点 <a id="microsoft-sharepoint-trigger-node"></a>

使用 Microsoft SharePoint Trigger 节点，在 [Microsoft SharePoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration) 中的文件或列表项变更时启动工作流。

节点监控一个站点中的一个文档库或列表，按你设置的计划检查变更。每次检查最多启动一次工作流。如果自上次检查以来有多个条目发生变更，它们会一并进入该次执行；检查读取的每个条目各对应一个数据项。如果没有变更，节点不会启动执行。

本页介绍节点的监控范围、产生的事件，以及开始构建前应了解的常见问题。

{% hint style="info" %}
**凭据**

此节点支持 [Microsoft OAuth2 凭据](../credentials/microsoft.md)和 [Microsoft Entra 服务主体凭据](../credentials/microsoftentraserviceprincipal.md)，不支持 Microsoft SharePoint 凭据。

使用 OAuth2 凭据时，在 **Scope**（作用域）字段中输入 `openid offline_access Sites.Read.All`。使用服务主体凭据时，为应用注册授予 `Sites.Read.All` [应用权限](../credentials/microsoftentraserviceprincipal.md#required-application-permissions-by-node)。如果组织按站点分别授权，请改用 `Sites.Selected`，并由管理员[为应用授予各站点的访问权限](../credentials/microsoftentraserviceprincipal.md#grant-access-per-site)。

触发器需要在无人登录时持续检查，因此生产环境应使用服务主体凭据。用户凭据会在该用户的会话被撤销后失效。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果使用政府云租户（US Government、US Government DOD 或 China），请在 Microsoft 凭据配置中选择适当的 **Microsoft Graph API Base URL**（Microsoft Graph API 基础 URL）。
{% endhint %}

## 节点监控的内容 <a id="what-the-node-watches"></a>

选择 **Site**（站点），然后将 **Resource**（资源）设为要监控的内容：

* **Document Library**（文档库）：监控一个文档库中的文件。在 **Document Library** 中选择文档库。
* **List**（列表）：监控一个列表中的条目。在 **List** 中选择列表。

每个字段都支持选择器和手动输入值。除非选择器无法访问所需内容，例如组织按站点分别授权，否则请使用选择器。**Site**（站点）字段也支持在 **By URL**（按 URL）模式下输入站点地址。

节点监控整个文档库或整个列表，无法限定为单个文件夹。Microsoft Graph 的变更源不支持在服务器端筛选，也不报告变更文件的文件夹路径，因此没有可靠的筛选依据。

## 事件 <a id="events"></a>

在 **Events**（事件）中选择事件。两个事件默认均开启。

* **Changed**（已变更）：文件或条目被添加、编辑、重命名、移动，或其元数据发生变更。
* **Deleted**（已删除）：文件或条目被删除。

无论监控哪种资源，文件夹都不会产生事件。

### 为什么没有单独的 Created（已创建）事件 <a id="why-theres-no-separate-created-event"></a>

Microsoft Graph 的变更源报告每个条目的最新状态，而不是每次变更。新创建的条目与被编辑的条目在返回结果中没有区别，因此节点将两者都报告为 **Changed**（已变更），不会尝试猜测。

如果需要区分新条目和已编辑条目，可在工作流中比较 `createdDateTime` 与 `lastModifiedDateTime`，并仅将结果作为提示，而非确定事实。在两次检查之间创建后又被编辑的条目，只会到达一次，且两个时间戳不同。

## 节点检查的频率 <a id="how-often-the-node-checks"></a>

**Poll Times**（轮询时间）设置节点检查变更的频率，默认每分钟一次。

预设选项最短为每分钟一次。**Custom**（自定义）cron 表达式可以细化到秒级，但远未达到这一频率时 Microsoft 就会限制请求，因此实际难以从如此高的频率中受益。

变更会在下一次检查时被读取。默认设置下，一次检查大约读取 40 页变更；如果时间耗尽，则提前结束。如果还有变更等待处理，节点会保存读取位置，在下次检查时继续。因此，短时间内大量发生的变更会分散在多次执行中到达，清理完毕可能需要超过一个检查间隔。

## 输出 <a id="output"></a>

节点按 Microsoft Graph 返回的原样输出每个变更条目，不调整结构。字段取决于所监控的资源，以及条目发生了什么。

包含 `deleted` 属性的条目表示删除；不包含此属性的条目表示变更。

监控列表时，条目携带列表项的标识信息。节点读取 Microsoft Graph 的默认载荷，不展开条目的 `fields`，因此不要依赖条目包含列值。要读取列，请在触发器后添加 Microsoft SharePoint 节点，并按 `id` 获取列表项。

删除条目携带的信息远少于变更条目，因为 Microsoft Graph 会移除大多数字段。可预期包含条目的 `id` 和 `deleted` 属性，不要依赖其他字段一定存在。如果工作流需要已删除条目的名称，请自行维护已见条目的记录，以 `id` 作为键。

监控文档库时，不要依赖条目包含 `parentReference.path`。请使用 `webUrl` 查找文件所在位置。

## 常见问题 <a id="common-issues"></a>

### 已有文件和条目不会触发工作流 <a id="existing-files-and-items-dont-trigger-the-workflow"></a>

发布工作流时，节点从该时刻开始监控。已有文件和条目不会产生事件。要处理文档库中已有的内容，请使用 [Microsoft SharePoint 节点](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)。

### 编辑节点后缺少变更 <a id="changes-are-missing-after-i-edited-the-node"></a>

更改 **Authentication**（身份验证）方式、**Site**（站点）、**Resource**（资源）、**Document Library**（文档库）或 **List**（列表）会重置已保存的读取位置。节点从该时刻重新开始监控，不报告此前的变更。选择相同类型的其他凭据会保留读取位置。

### 工作流停用一段时间后缺少变更 <a id="changes-are-missing-after-the-workflow-was-inactive"></a>

如果节点长时间未运行，已保存的读取位置可能在 Microsoft 端过期。此时节点会从当前时刻重新开始监控，并记录警告。读取位置过期期间发生的变更不会被报告。

### 同一条目重复到达 <a id="the-same-item-arrives-more-than-once"></a>

同一次检查中，节点会合并同一条目的重复变更。处理短时间内大量发生的变更时，同一条目可能在不同检查中重复到达。请确保工作流能够安全处理同一条目的重复数据。

### 测试显示条目，却没有显示我的变更 <a id="the-test-shows-items-but-not-my-change"></a>

在编辑器中测试节点不会移动已保存的读取位置，因此不会消耗真实事件。测试会列出现有文档库或列表中的条目，最多一页。它不会等待变更，也不会显示删除事件。请用测试查看条目的结构，不要用它验证事件选择。

### 节点提示找不到文档库或列表 <a id="the-node-reports-that-the-library-or-list-cant-be-found"></a>

如果所监控的文档库或列表无法再访问，例如被删除，节点会报错，指出查找的文档库或列表及其所在站点。它会保留读取位置，因此目标恢复后可以继续。由于节点按 ID 监控，重命名不会使其失效；但如果你在 **By ID or Title**（按 ID 或标题）模式下输入的是列表标题，重命名会使其失效。

### 权限错误未指出文档库或列表名称 <a id="a-permission-error-doesnt-name-the-library-or-list"></a>

如果凭据失去访问权限，Microsoft Graph 通常会返回权限错误。节点原样报告此错误，因此不会指出文档库或列表名称。请检查凭据的作用域，以及登录账户对站点的访问权限。

### 同一错误并非每次检查都会出现 <a id="the-same-error-doesnt-appear-on-every-check"></a>

检查失败时，节点会报告失败。同一故障持续重复时，最多每小时再报告一次，其间向日志写入警告，以免持续的问题塞满执行列表。不同的故障会立即报告，检查成功则会清除此记录。在编辑器中测试时，总会报告失败。

## 相关资源 <a id="related-resources"></a>

n8n 为 Microsoft SharePoint 提供应用节点。更多信息请参阅 [Microsoft SharePoint 节点文档](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)。

节点所读取变更源的详情，请参阅 [Microsoft 的 driveItem delta 文档](https://learn.microsoft.com/en-us/graph/api/driveitem-delta)和 [listItem delta 文档](https://learn.microsoft.com/en-us/graph/api/listitem-delta)。
