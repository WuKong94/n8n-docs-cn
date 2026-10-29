---
title: Git 节点
description: 了解 n8n 中 Git 节点的用法，并查看相关示例。
contentType:
- integration
- reference
nodeTitle: Git 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.git.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Git <a href="#git" id="git"></a>

[Git](https://git-scm.com/) 是免费开源的分布式版本控制系统，旨在快速、高效地管理从小型到大型的各类项目。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Git 凭据文档](../credentials/git.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Add**（添加）：添加要提交的文件或文件夹，执行 [git add](https://git-scm.com/docs/git-add)。
* **Add Config**（添加配置）：添加配置属性，执行 [git config](https://git-scm.com/docs/git-config) 的设置或追加操作。
* **Clone**（克隆）：克隆仓库，执行 [git clone](https://git-scm.com/docs/git-clone)。
* **Commit**（提交）：将文件或文件夹提交到 Git，执行 [git commit](https://git-scm.com/docs/git-commit)。
* **Fetch**（获取）：从远程仓库获取，执行 [git fetch](https://git-scm.com/docs/git-fetch)。
* **List Config**（列出配置）：返回当前配置，执行 [git config](https://git-scm.com/docs/git-config) 查询。
* **Log**（日志）：返回 Git 提交历史，执行 [git log](https://git-scm.com/docs/git-log)。
* **Pull**（拉取）：从远程仓库拉取，执行 [git pull](https://git-scm.com/docs/git-pull)。
* **Push**（推送）：推送到远程仓库，执行 [git push](https://git-scm.com/docs/git-push)。
* **Push Tags**（推送标签）：将标签推送到远程仓库，执行 [git push --tags](https://git-scm.com/docs/git-push#Documentation/git-push.txt---tags)。
* 返回当前仓库的 **Status**（状态），执行 [git status](https://git-scm.com/docs/git-status)。
* **Switch Branch:**（切换分支）执行 [git switch](https://git-scm.com/docs/git-switch)。
* 创建新的 **Tag**（标签），执行 [git tag](https://git-scm.com/docs/git-tag)。
* **User Setup**（用户设置）：设置用户。

各操作的详细参数和选项见下文。

## Add（添加） <a href="#add" id="add"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Paths to Add**（要添加的路径）：输入以逗号分隔的文件或文件夹路径列表。可以使用绝对路径，也可以使用相对于 **Repository Path**（仓库路径）的路径。



## Add Config（添加配置） <a href="#add-config" id="add-config"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Key**（键）：输入要设置的配置键名称。
* **Value**（值）：输入要设置的配置值。

### Add Config（添加配置）选项 <a href="#add-config-options" id="add-config-options"></a>

Add Config 操作增加 **Mode**（模式）选项，选择在本地配置中 **Set**（设置）或 **Append**（追加）此配置。


## Clone（克隆） <a href="#clone" id="clone"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Authentication**（身份验证）：选择 **Authenticate**（认证）来传入凭据，选择 **None**（无）则不使用身份验证。
    * **Credential for Git**（Git 凭据）：选择 **Authenticate**（认证）后，必须选择或创建供节点使用的凭据。更多信息，请参阅 [Git 凭据](../credentials/git.md)。
* **New Repository Path**（新仓库路径）：输入克隆后仓库的本地存放路径。
* **Source Repository**（源仓库）：输入要克隆仓库的 URL 或路径。

## Commit（提交） <a href="#commit" id="commit"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Message**（消息）：输入提交消息。

### Commit（提交）选项 <a href="#commit-options" id="commit-options"></a>

Commit 操作增加 **Paths to Add**（要添加的路径）选项。留空时，提交所有已“添加”的文件和文件夹；要提交特定的已“添加”文件或文件夹，输入以逗号分隔的路径列表。

可以使用绝对路径，也可以使用相对于 **Repository Path**（仓库路径）的路径。

## Fetch（获取） <a href="#fetch" id="fetch"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。



## List Config（列出配置） <a href="#list-config" id="list-config"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。


## Log（日志） <a href="#log" id="log"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Return All**（返回全部）：开启时返回所有结果，关闭时返回不超过 **Limit**（数量上限）的结果。
* **Limit**（数量上限）：仅在关闭 **Return All**（返回全部）时可用，输入最多返回的结果数。

### Log（日志）选项 <a href="#log-options" id="log-options"></a>

Log 操作增加 **File**（文件）选项，输入要获取历史的文件或文件夹路径。

可以使用绝对路径，也可以使用相对于 **Repository Path**（仓库路径）的路径。

## Pull（拉取） <a href="#pull" id="pull"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。

## Push（推送） <a href="#push" id="push"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Authentication**（身份验证）：选择 **Authenticate**（认证）来传入凭据，或选择 **None**（无）以不使用身份验证。
    * 选择 **Authenticate**（认证）后，必须选择或创建供节点使用的 **Credential for Git**（Git 凭据）。更多信息，请参阅 [Git 凭据](../credentials/git.md)。

### Push（推送）选项 <a href="#push-options" id="push-options"></a>

Push 操作增加 **Target Repository**（目标仓库）选项，输入要推送到的仓库 URL 或路径。

## Push Tags（推送标签） <a href="#push-tags" id="push-tags"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。

## Status（状态） <a href="#status" id="status"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。

## Switch Branch（切换分支） <a href="#switch-branch" id="switch-branch"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Branch Name**（分支名称）：输入要切换到的分支名称。

## Tag（标签） <a href="#tag" id="tag"></a>

使用以下参数配置此操作：

* **Repository Path**（仓库路径）：输入 Git 仓库的本地路径。
* **Name**（名称）：输入要创建的标签名称。

## User Setup（用户设置） <a href="#user-setup" id="user-setup"></a>

此操作仅要求在 **Repository Path**（仓库路径）参数中输入 Git 仓库的本地路径。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Git 集成模板](https://n8n.io/integrations/git)，或[搜索所有模板](https://n8n.io/workflows/)
