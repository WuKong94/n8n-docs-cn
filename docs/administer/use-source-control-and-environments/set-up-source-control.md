---
title: 设置源代码管理
description: 将 n8n 连接到 Git 托管平台。
contentType: howto
nodeTitle: 设置源代码管理
originalFilePath: source-control-environments/setup.md
originalUrl: https://docs.n8n.io/source-control-environments/setup
url: https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 为环境设置源代码管理 <a href="#set-up-source-control-for-environments" id="set-up-source-control-for-environments"></a>

将 Git 仓库连接到 n8n 实例，并配置源代码管理。

n8n 使用源代码管理提供环境功能。更多信息请参阅 [n8n 中的环境](work-with-environments.md)。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

要在 n8n 中使用源代码管理，需要一个支持以下任一访问方式的 Git 仓库：

- SSH 访问（使用部署密钥），或
- HTTPS 访问（使用个人访问令牌）。

本文假定你已熟悉 Git 及所用的 Git 托管平台。

## 第一步：设置仓库和分支 <a href="#step-1-set-up-your-repository-and-branches" id="step-1-set-up-your-repository-and-branches"></a>

全新配置的操作如下：

1. 创建供 n8n 使用的新仓库。
1. 创建所需分支。例如，计划使用不同的测试和生产环境时，为每个环境设置一个分支。

如需确定使用场景所需的分支，请参阅[分支模式](choose-branching-patterns.md)。

## 第二步：在 n8n 中配置 Git <a href="#step-2-configure-git-in-n8n" id="step-2-configure-git-in-n8n"></a>

{% include "../../reusable-content/.gitbook/includes/source-control-environments/configure-git-in-n8n.md" %}

## 第三步：设置身份验证 <a href="#step-3-set-up-authentication" id="step-3-set-up-authentication"></a>

根据所选连接方式配置身份验证。

### SSH 身份验证（使用部署密钥） <a href="#ssh-authentication-using-deploy-keys" id="ssh-authentication-using-deploy-keys"></a>

使用 n8n 提供的 SSH 密钥，为仓库创建部署密钥，以设置 SSH 访问。该密钥必须具有写入权限。

具体步骤取决于 Git 托管平台。常用平台的帮助链接：

* [GitHub | 管理部署密钥](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
* [GitLab | 部署密钥](https://docs.gitlab.com/ee/user/project/deploy_keys/)

### HTTPS 身份验证（使用个人访问令牌） <a href="#https-authentication-using-personal-access-tokens" id="https-authentication-using-personal-access-tokens"></a>

创建具有仓库访问权限的个人访问令牌（PAT）。

常用平台创建 PAT 的帮助链接：

* [GitHub | 管理个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
* [GitLab | 个人访问令牌](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
* [Bitbucket | 应用密码](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)

令牌需要具备以下权限：

- 仓库读写权限。
- Contents 读写权限（GitHub）。
- 源代码拉取和推送权限（GitLab）。

#### 使用私有证书颁发机构的 Git 主机 <a id="git-hosts-with-a-private-certificate-authority"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.40.0 起，Git 连接支持私有证书颁发机构。
{% endhint %}

如果 Git 主机使用私有证书颁发机构（CA）签发的证书，请在 n8n 实例上将 `GIT_SSL_CAINFO` 环境变量设为包含 CA 证书的 PEM 文件路径。Git 使用自己的信任存储，因此 n8n 的[自定义证书颁发机构](../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities.md)配置不适用于 Git 连接。如果将证书保存在使用 `c_rehash` 建立索引的目录中，则将 `GIT_SSL_CAPATH` 设为该目录。

该文件或目录会替代 Git 的默认信任存储。如果实例还需要连接公共 Git 主机，请同时包含其根证书。

## 第四步：连接 n8n 并配置实例 <a href="#step-4-connect-n8n-and-configure-your-instance" id="step-4-connect-n8n-and-configure-your-instance"></a>

1. 在 n8n 的 **Settings**（设置）> **Environments**（环境）中，选择 **Connect**（连接）。n8n 会连接到 Git 仓库。
1. 在 **Instance settings**（实例设置）下，选择当前 n8n 实例要使用的分支。
1. **可选**：选择 **Protected instance**（受保护实例），阻止用户编辑本实例中由源代码管理控制的资源。此选项适合保护生产实例。
1. **可选**：为实例选择自定义颜色。此颜色会显示在菜单中源代码管理推送、拉取按钮旁，帮助用户识别当前实例。
1. 选择 **Save settings**（保存设置）。

## 相关资源 <a id="related-resources"></a>

* [使用源代码管理与环境](./)
* [理解源代码管理](understand-source-control.md)
* [使用环境](work-with-environments.md)
* [在 n8n 中使用 Git](use-git-in-n8n.md)
* [选择分支模式](choose-branching-patterns.md)
* [推送和拉取更改](push-and-pull-changes.md)
* [比较版本](compare-versions.md)
* [在环境间迁移工作](move-work-between-environments.md)
* [通过公共 API 以编程方式使用环境](use-environments-via-api.md)
* [教程：使用源代码管理创建环境](tutorial-create-environments-with-source-control.md)

