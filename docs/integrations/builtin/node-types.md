---
description: 了解 n8n 的核心节点、集群节点、凭据和社区节点。
contentType: overview
nodeTitle: 节点类型
originalFilePath: integrations/builtin/node-types.md
originalUrl: https://docs.n8n.io/integrations/builtin/node-types
url: https://docs.n8n.io/integrations/builtin/node-types
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 内置集成 <a href="#built-in-integrations" id="built-in-integrations"></a>

本节为节点[^1]库，提供 n8n 每个内置节点及其凭据的参考文档。

{% include "../../reusable-content/.gitbook/includes/integrations/builtin/node-operations.md" %}

## 核心节点 <a href="#core-nodes" id="core-nodes"></a>

核心节点可以是动作节点或触发器[^2]。大多数节点连接特定外部服务，而核心节点提供逻辑、调度或通用 API 调用等功能。

## 集群节点 <a href="#cluster-nodes" id="cluster-nodes"></a>

{% include "../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/cluster-nodes-summary.md" %}

## 凭据 <a href="#credentials" id="credentials"></a>

外部服务需要识别和验证用户身份，所需信息可能是 API 密钥、邮箱与密码组合，或多行私钥。可以在 n8n 中将这些信息保存为凭据[^3]。

随后 n8n 中的节点即可请求这些凭据信息。作为另一层安全保障，只有具有特定访问权限的节点类型才能访问凭据。

为保障数据安全，凭据会加密存储到数据库。n8n 使用随机的个人加密密钥，在首次运行时自动生成，并保存到 `~/.n8n/config`。

创建、管理和共享凭据的更多信息，请参阅[管理凭据](../../build/understand-workflows/create-and-edit-credentials.md)。

## 社区节点 <a href="#community-nodes" id="community-nodes"></a>

n8n 支持社区节点。安装和使用方法，请参阅[社区节点](../community-nodes/installation-and-management/README.md)。

要了解如何构建自己的社区节点并发布到 [npm](https://www.npmjs.com/)，请参阅[创建节点](../../connect/create-nodes/overview.md)。

其他集成主题，请参阅[内置节点](./)。

[^1]: 在 n8n 中，节点是组成工作流的独立组件。节点可以决定工作流何时运行，获取、发送和处理数据，定义流程控制逻辑，以及连接外部服务。
[^2]: 触发器节点是一种特殊节点，负责在特定条件下执行工作流。所有生产工作流至少需要一个触发器，以决定何时运行。
[^3]: 在 n8n 中，凭据存储连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，即可通过对应的应用节点与服务交互。
