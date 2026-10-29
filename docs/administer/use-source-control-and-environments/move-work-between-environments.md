---
title: 在环境间复制工作
description: 如何将一个环境中的更改迁移到另一个环境。
contentType: howto
nodeTitle: 在环境间迁移工作
originalFilePath: source-control-environments/using/copy-work.md
originalUrl: https://docs.n8n.io/source-control-environments/using/copy-work
url: https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在环境间复制工作 <a href="#copy-work-between-environments" id="copy-work-between-environments"></a>

将工作从一个 n8n 实例迁移到另一个实例的步骤，取决于使用单个还是多个 Git 分支。

## 单分支 <a href="#single-branch" id="single-branch"></a>

使用单个 Git 分支时，复制工作的步骤如下：

1. 将工作从一个实例推送到 Git 分支。
1. 登录另一个实例，从 Git 拉取工作。可以[自动拉取](#automatically-send-changes-to-n8n)。

## 多分支 <a href="#multiple-branches" id="multiple-branches"></a>

使用多个 Git 分支时，需要在 Git 托管平台合并分支，才能在环境间复制工作。无法在 n8n 中直接跨环境复制工作。

常见流程如下：

1. 在开发实例中工作。
1. 将工作推送到 Git 的开发分支。
1. 将开发分支合并到生产分支。操作指南请参阅 Git 托管平台的文档：
	* [GitHub：创建拉取请求](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
	* [GitLab：创建合并请求](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
	* [Git：基本分支与合并](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
1. 在生产 n8n 实例中拉取更改。可以[自动拉取](#automatically-send-changes-to-n8n)。

## 自动将更改发送到 n8n <a href="#automatically-send-changes-to-n8n" id="automatically-send-changes-to-n8n"></a>

可以使用 `/source-control/pull` API 端点将复制工作的部分流程自动化。在合并更改后调用该 API：

```curl
curl --request POST \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/pull' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{"force": true}'
```

这样就能通过 GitHub Action 或 GitLab CI/CD，在合并时自动将更改拉取到生产实例。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/github-action.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [比较版本](compare-versions.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)

