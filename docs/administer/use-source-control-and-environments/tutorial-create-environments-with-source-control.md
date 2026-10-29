---
title: 教程：使用源代码管理创建环境
description: 如何使用 n8n 源代码管理功能创建环境。
contentType: tutorial
nodeTitle: 教程：使用源代码管理创建环境
originalFilePath: source-control-environments/create-environments.md
originalUrl: https://docs.n8n.io/source-control-environments/create-environments
url: https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 教程：使用源代码管理创建环境 <a href="#tutorial-create-environments-with-source-control" id="tutorial-create-environments-with-source-control"></a>

{% include "../../reusable-content/.gitbook/includes/source-control-environments/feature-availability.md" %}

本教程完整介绍设置环境的过程，你将创建开发和生产两个环境。教程使用 GitHub 作为 Git 托管平台，其他平台的流程类似。

n8n 在版本控制软件 Git 的基础上构建了环境功能。将 n8n 实例连接到 Git 分支后，通过推送和拉取在环境间迁移工作。你应对环境和 Git 有一定了解，如需更多信息，请参阅：

* [n8n 中的环境](work-with-environments.md)：环境的用途及其在 n8n 中的工作方式。
* [Git 与 n8n](use-git-in-n8n.md)：Git 概念和 n8n 中的源代码管理。

## 选择源代码管理模式 <a href="#choose-your-source-control-pattern" id="choose-your-source-control-pattern"></a>

设置源代码管理与环境前，需要规划环境及其与 Git 分支的关系。n8n 支持不同的[分支模式](choose-branching-patterns.md)。对于环境，需要在“多实例、多分支”和“多实例、单分支”两种模式中选择，本教程会介绍这两种模式。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/one-direction.md" %}

### 多实例、多分支 <a href="#multiple-instances-multiple-branches" id="multiple-instances-multiple-branches"></a>

![开发 n8n 实例连接开发分支，生产实例连接生产分支](../.gitbook/assets/vc-multi-multi.png)

{% include "../../reusable-content/.gitbook/includes/source-control-environments/multi-instance-multi-branch-pros-cons.md" %}


### 多实例、单分支 <a href="#multiple-instances-one-branch" id="multiple-instances-one-branch"></a>

![开发和生产 n8n 实例都连接到同一 Git 分支](../.gitbook/assets/vc-multi-one.png)

{% include "../../reusable-content/.gitbook/includes/source-control-environments/multi-instance-one-branch-pros-cons.md" %}

## 设置仓库 <a href="#set-up-your-repository" id="set-up-your-repository"></a>

选定模式后，需要设置 GitHub 仓库。

{% tabs %}
{% tab title="多分支" %}
1. [创建新仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。
    * 请确保仓库为私有，除非希望将工作流、标签，以及变量和凭据存根公开到互联网上。
    * 创建仓库时添加 README，以便立即创建分支。
1. 创建一个名为 `production` 的分支，另一个名为 `development`。操作方法请参阅[在仓库中创建和删除分支](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)。
{% endtab %}

{% tab title="单分支" %}
[创建新仓库](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。

  * 请确保仓库为私有，除非希望将工作流、标签，以及变量和凭据存根公开到互联网上。
  * 创建仓库时添加 README，这会创建 `main` 分支，之后将连接到该分支。
{% endtab %}
{% endtabs %}

## 将 n8n 实例连接到仓库 <a href="#connect-your-n8n-instances-to-your-repository" id="connect-your-n8n-instances-to-your-repository"></a>

创建两个 n8n 实例，一个用于开发，另一个用于生产。

### 在 n8n 中配置 Git <a href="#configure-git-in-n8n" id="configure-git-in-n8n"></a>

{% include "../../reusable-content/.gitbook/includes/source-control-environments/configure-git-in-n8n.md" %}

### 设置部署密钥 <a href="#set-up-a-deploy-key" id="set-up-a-deploy-key"></a>

使用 n8n 提供的 SSH 密钥，为仓库创建部署密钥，以设置 SSH 访问。密钥必须具有写入权限。操作方法请参阅 [GitHub | 管理部署密钥](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)。

### 连接 n8n 并配置实例 <a href="#connect-n8n-and-configure-your-instance" id="connect-n8n-and-configure-your-instance"></a>

{% tabs %}
{% tab title="多分支" %}
1. 在 n8n 的 **Settings**（设置）> **Environments**（环境）中，选择 **Connect**（连接）。n8n 会连接到 Git 仓库。
1. 在 **Instance settings**（实例设置）下，选择当前 n8n 实例要使用的分支。将生产分支连接到生产实例，开发分支连接到开发实例。
1. 仅生产实例：选择 **Protected instance**（受保护实例），阻止用户编辑该实例中的工作流。
1. 选择 **Save settings**（保存设置）。
{% endtab %}

{% tab title="单分支" %}
1. 在 n8n 的 **Settings**（设置）> **Environments**（环境）中，选择 **Connect**（连接）。
  1. 在 **Instance settings**（实例设置）下，选择主分支。
1. 仅生产实例：选择 **Protected instance**（受保护实例），阻止用户编辑该实例中的工作流。
1. 选择 **Save settings**（保存设置）。
{% endtab %}
{% endtabs %}

## 从开发环境推送工作 <a href="#push-work-from-development" id="push-work-from-development"></a>

在开发实例中创建一些工作流、标签、变量和凭据。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/push.md" %}

## 将工作拉取到生产环境 <a href="#pull-work-to-production" id="pull-work-to-production"></a>

工作现在已保存在 GitHub 中。如果采用多分支配置，工作位于开发分支；如果采用单分支配置，则位于 main。

{% tabs %}
{% tab title="多分支" %}
1. 在 GitHub 中创建拉取请求，将 development 合并到 production。
1. 合并拉取请求。
1. 在生产实例的主菜单中，选择 **Pull**（拉取）<img src="../.gitbook/assets/pull-icon.png" alt="拉取图标" data-size="line">。
{% endtab %}

{% tab title="单分支" %}
在生产实例的主菜单中，选择 **Pull**（拉取）<img src="../.gitbook/assets/pull-icon.png" alt="拉取图标" data-size="line">。
{% endtab %}
{% endtabs %}

{% include "../../reusable-content/.gitbook/includes/source-control-environments/push-pull-menu-state.md" %}

### 可选：使用 GitHub Action 自动拉取 <a href="#optional-use-a-github-action-to-automate-pulls" id="optional-use-a-github-action-to-automate-pulls"></a>

如果希望无需登录生产实例就能拉取，可以使用 [GitHub Action](https://docs.github.com/en/actions/creating-actions/about-custom-actions) 和 [n8n API](../../connect/n8n-api/README.md)，在每次向 production 或 main 分支推送新工作时自动拉取。

{% include "../../reusable-content/.gitbook/includes/source-control-environments/github-action.md" %}


## 后续步骤 <a href="#next-steps" id="next-steps"></a>

了解更多：

* [n8n 中的环境](work-with-environments.md)与 [Git 与 n8n](use-git-in-n8n.md)。
* [源代码管理模式](choose-branching-patterns.md)。

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [设置源代码管理](set-up-source-control.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [比较版本](compare-versions.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
