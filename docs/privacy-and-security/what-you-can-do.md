---
title: 你可以采取的措施
description: 使用 n8n 时，可以采取哪些措施来改善隐私保护和数据安全。
contentType: howto
nodeTitle: 你可以采取的措施
originalFilePath: privacy-security/what-you-can-do.md
originalUrl: https://docs.n8n.io/privacy-security/what-you-can-do
url: https://docs.n8n.io/privacy-and-security/what-you-can-do
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 你可以采取的措施 <a href="#what-you-can-do" id="what-you-can-do"></a>

作为客户，你也有责任确保代码和数据的安全。本文列出一些可以采取的措施。

## 所有用户 <a href="#all-users" id="all-users"></a>

* 将安全问题和违反[服务条款](https://n8n.io/legal/#terms)的情况报告给 security@n8n.io。
* 如果多人使用同一个 n8n 实例，请设置[用户管理](../administer/manage-users-and-access/README.md)，并遵循[最佳实践](../administer/manage-users-and-access/follow-best-practices.md)。
* 尽可能使用 OAuth 连接集成服务。

## 自托管用户 <a href="#self-hosted-users" id="self-hosted-users"></a>

如果自行托管 n8n，还可以采取以下措施：

* 设置反向代理处理 TLS，确保传输中的数据经过加密。
* 使用加密分区或硬件级加密，确保静态数据加密，并确保 n8n 及其数据库的数据写入该位置。
* 运行[安全审计](../deploy/host-n8n/configure-n8n/security/run-security-audits.md)。
* 安装社区节点前了解相关[风险](../integrations/community-nodes/risks.md)，也可以选择禁用社区节点。
* 确保用户无法在 Code 节点中导入外部模块。更多信息请参阅[环境变量 | 节点](../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)。
* 选择排除某些节点，例如禁用 Execute Command 或 SSH 等节点。更多信息请参阅[环境变量 | 节点](../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)。
* 为获得最大程度的隐私保护，可以[隔离 n8n](../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n.md)。

### 自托管用户的 GDPR 事项 <a href="#gdpr-for-self-hosted-users" id="gdpr-for-self-hosted-users"></a>

{% include "../reusable-content/.gitbook/includes/privacy-security/gdpr-self-hosted.md" %}


