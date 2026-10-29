---
description: 保护、管理和运行 n8n 实例。
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 管理 <a id="administer"></a>

通过控制访问、保护凭据、管理更改和监控活动来管理 n8n。

本节帮助你在使用规模增长时，安全、可靠地运行 n8n。

{% hint style="info" %}
企业团队通常会更多地使用本节内容。规模扩大后，SSO、目录集成、变更控制和集中日志会更重要。此处许多功能，包括基础用户管理、凭据安全和运行监控，也适用于 Enterprise 之外的使用场景。
{% endhint %}

### 典型管理流程 <a id="a-typical-administration-workflow"></a>

{% stepper %}
{% step %}
### 控制访问 <a id="control-access"></a>

决定谁能登录、能执行哪些操作，以及如何组织工作。从[管理用户与访问](manage-users-and-access/README.md)开始。
{% endstep %}

{% step %}
### 保护密钥 <a id="protect-secrets"></a>

安全地保存和共享凭据。使用[管理凭据](manage-credentials/README.md)中的方法，减少密钥分散存放。
{% endstep %}

{% step %}
### 安全迁移更改 <a id="move-changes-safely"></a>

使用基于 Git 的工作流程，在环境间推进更改。参阅[使用源代码管理与环境](use-source-control-and-environments/README.md)。
{% endstep %}

{% step %}
### 监控活动 <a id="monitor-activity"></a>

跟踪使用情况，并向日志工具发送信号。使用[观测与日志](observe-and-log/README.md)提高可见性。
{% endstep %}
{% endstepper %}
