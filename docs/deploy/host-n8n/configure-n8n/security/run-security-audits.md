---
title: 安全审计
description: 在 n8n 实例上运行安全审计。
contentType: howto
nodeTitle: 运行安全审计
originalFilePath: hosting/securing/security-audit.md
originalUrl: https://docs.n8n.io/hosting/securing/security-audit
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安全审计 <a href="#security-audit" id="security-audit"></a>

可以在 n8n 实例上运行安全审计，检测常见安全问题。

## 如何在 n8n 中运行安全审计？ <a href="#run-an-audit" id="run-an-audit"></a>

可以通过 CLI、公共 API 或 n8n 节点运行审计。


### CLI <a href="#cli" id="cli"></a>

运行 `n8n audit`。

### API <a href="#api" id="api"></a>

发送 `POST` 请求到 `/audit` 端点，必须以实例所有者身份验证。

### n8n 节点 <a href="#n8n-node" id="n8n-node"></a>

在工作流中添加 [n8n 节点](../../../../integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)。选择 **Resource（资源）** > **Audit（审计）**，以及 **Operation（操作）** > **Generate（生成）**。

## 安全审计报告包含什么？ <a href="#report-contents" id="report-contents"></a>

审计会生成五份风险报告：

### 凭据 <a href="#credentials" id="credentials"></a>

此报告显示：

* 未在任何工作流中使用的凭据。
* 未在激活工作流中使用的凭据。
* 未在近期活动的工作流中使用的凭据。

### 数据库 <a href="#database" id="database"></a>

此报告显示：

* SQL 节点的 **Execute Query（执行查询）**字段中使用的表达式。
* SQL 节点的 **Query Parameters（查询参数）**字段中使用的表达式。
* SQL 节点中未使用的 **Query Parameters（查询参数）**字段。

### 文件系统 <a href="#file-system" id="file-system"></a>

此报告列出与文件系统交互的节点。

### 节点 <a href="#nodes" id="nodes"></a>

此报告显示：

* 官方高风险节点。这些 n8n 内置节点可以在主机系统上获取并运行任意代码，使实例面临被利用的风险。可在 [n8n 代码 | 审计常量](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/security-audit/constants.ts#L51)的 `OFFICIAL_RISKY_NODE_TYPES` 下查看列表。
* 社区节点。
* 自定义节点。

### 实例 <a href="#instance" id="instance"></a>

此报告显示：

* 实例中未受保护的 Webhook。
* 缺失的安全设置。
* 实例是否过时。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
