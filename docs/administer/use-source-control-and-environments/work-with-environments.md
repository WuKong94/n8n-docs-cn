---
title: n8n 中的环境
description: 了解 n8n 环境背后的概念。
contentType: explanation
nodeTitle: 使用环境
originalFilePath: source-control-environments/understand/environments.md
originalUrl: https://docs.n8n.io/source-control-environments/understand/environments
url: https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 中的环境 <a href="#environments-in-n8n" id="environments-in-n8n"></a>

n8n 在版本控制软件 Git 的基础上构建了环境功能。本文帮助你了解：

* 环境的用途。
* 环境在 n8n 中的工作方式。

## 环境是什么，为什么需要环境 <a href="#environments-what-and-why" id="environments-what-and-why"></a>

在软件开发中，环境是围绕代码的全部基础设施与工具，包括运行软件的工具及其具体配置。更详细的介绍请参阅 [Codecademy | 环境](https://www.codecademy.com/article/environments)。

n8n 中的低代码开发也类似。你在 n8n 中构建和运行工作流，实例可能有特定配置：Cloud 的配置由 n8n 决定；自托管实例有丰富的[配置选项](../../deploy/host-n8n/configure-n8n/basic-configuration.md)。你也可能调整过实例设置。n8n 与实例的具体配置和设置共同构成工作流的运行环境。

使用多个环境有一些优势，常见方式是区分开发与生产环境：

* 开发：进行工作并做出更改。
* 生产：正式运行的环境。

这样的配置可以让你修改工作流，同时避免影响正在使用的工作流。

## n8n 中的环境 <a href="#environments-in-n8n" id="environments-in-n8n"></a>

在 n8n 中，一个环境包含两部分：一个 n8n 实例和一个 Git 分支。

* n8n 实例用于构建和运行工作流。
* Git 分支保存工作流副本，以及标签、变量存根和凭据存根。

n8n 不会将凭据和变量的值同步到 Git。设置新实例时，必须手动设置凭据和变量的值。更多信息请参阅[推送和拉取 | 提交的内容](push-and-pull-changes.md#what-gets-committed)。

如何在环境间复制工作，取决于分支与 n8n 实例的配置：

* 多实例、单分支：从一个实例推送到 Git 分支，再将工作拉取到另一个实例。
* 多实例、多分支：需要在 Git 托管平台创建拉取请求并合并。例如，开发、测试和生产分支分别连接各自的实例时，需要将开发分支合并到测试分支，才能让测试实例获得开发实例中的工作。更多信息及部分自动化步骤，请参阅[在环境间复制工作](move-work-between-environments.md)。

有关推送和拉取工作的详细指南，请参阅[推送和拉取](push-and-pull-changes.md)。

如需了解如何将 n8n 实例连接到 Git，请参阅[设置源代码管理](set-up-source-control.md)；也可按照[教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)，采用 n8n 推荐的配置之一来设置环境。

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [比较版本](compare-versions.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)
