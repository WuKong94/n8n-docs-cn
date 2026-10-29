---
title: 源代码管理与环境
description: n8n 源代码管理与环境概览。
contentType: overview
hide:
- toc
nodeTitle: 使用源代码管理与环境
originalFilePath: source-control-environments/index.md
originalUrl: https://docs.n8n.io/source-control-environments
url: https://docs.n8n.io/administer/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 源代码管理与环境 <a href="#source-control-and-environments" id="source-control-and-environments"></a>

{% include "../../reusable-content/.gitbook/includes/source-control-environments/feature-availability.md" %}

n8n 使用基于 Git 的源代码管理来支持环境功能。将 n8n 实例连接到 Git 仓库后，就可以创建以 Git 分支为基础的多个 n8n 环境。

## 本节内容 <a id="in-this-section"></a>

* [理解源代码管理](understand-source-control.md)：n8n 中源代码管理与环境的工作方式。
* [使用环境](work-with-environments.md)：环境的用途及其在 n8n 中的工作方式。
* [在 n8n 中使用 Git](use-git-in-n8n.md)：n8n 如何使用 Git。
* [选择分支模式](choose-branching-patterns.md)：n8n 实例与 Git 分支之间可建立的关系。
* [设置源代码管理](set-up-source-control.md)：如何将 n8n 实例连接到 Git。
* [推送和拉取更改](push-and-pull-changes.md)：将工作推送到 Git，并从 Git 拉取到实例。
* [比较版本](compare-versions.md)：使用工作流差异视图比较本地与远程更改。
* [在环境间迁移工作](move-work-between-environments.md)：如何在不同 n8n 实例间复制工作。
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)：使用 n8n 公共 API 预览、推送和拉取源代码管理中的更改。
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)：使用 n8n 推荐配置设置环境的完整教程。

## 相关章节 <a id="related-sections"></a>

* [变量](../../build/code-in-n8n/define-custom-variables.md)：可复用的值。
* [外部密钥](../manage-credentials/use-external-secret-stores.md)：使用外部密钥库管理凭据[^1]。

## 相关资源 <a id="related-resources"></a>

* [管理](../)
* [管理用户与访问](../manage-users-and-access/README.md)
* [管理凭据](../manage-credentials/README.md)
* [观测与日志](../observe-and-log/README.md)

[^1]: 在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，就可以通过相应应用节点与服务交互。
