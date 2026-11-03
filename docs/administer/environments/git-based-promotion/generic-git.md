---
description: 使用 SSH 部署密钥或用户名和访问令牌，将环境连接到任意 Git 仓库，包括 GitHub 和 Bitbucket。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 通用 Git <a id="generic-git"></a>

通用 Git 提供方通过 URL 将环境连接到任意 Git 仓库，包括 GitHub 和 Bitbucket 上的仓库。它使用 SSH 密钥，或者用户名和访问令牌进行身份验证。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## 通用 Git 支持的功能 <a id="what-generic-git-supports"></a>

| 功能 | 支持情况 |
|---|---|
| 身份验证 | SSH 密钥，或用户名和访问令牌 |
| 从列表选择仓库和分支 | 不支持，需要输入仓库 URL 和分支。 |
| 将每次晋级推送到功能分支 | 支持 |
| 晋级审核 | 不支持，需要在 Git 托管服务上手动合并功能分支。 |

## 使用 SSH 密钥连接 <a id="connect-with-an-ssh-key"></a>

1. 在 **Connect Generic Git（连接通用 Git）**对话框中，输入 **Name（名称）**，并将 **Authentication（身份验证）**设为 **SSH key（SSH 密钥）**。
2. 选择 **SSH key type（SSH 密钥类型）**。n8n 会生成密钥对。
3. 选择 **Continue（继续）**，然后选择 **Copy deploy key（复制部署密钥）**。
4. 在 Git 托管服务上，将此密钥添加为仓库的部署密钥，并赋予写权限。

Bitbucket Cloud 只提供只读的仓库访问密钥，因此应使用用户名和访问令牌连接 Bitbucket Cloud，或者将部署密钥添加到 Bitbucket 账号，而不是仓库。账号密钥会让 n8n 访问该账号可访问的所有仓库，因此请使用专用账号。

{% hint style="warning" %}
使用以 `ssh://` 开头的 SSH 仓库 URL，例如 `ssh://git@github.com/acme/n8n.git`。经典环境支持的 `git@github.com:acme/n8n.git` 形式在此不可用。
{% endhint %}

要替换密钥，请编辑提供方并选择 **Generate a new key（生成新密钥）**。将新密钥添加到 Git 托管服务后，再删除该服务中的旧密钥。

## 使用用户名和访问令牌连接 <a id="connect-with-a-username-and-access-token"></a>

1. 在 **Connect Generic Git（连接通用 Git）**对话框中，输入 **Name（名称）**，并将 **Authentication（身份验证）**设为 **Username and password（用户名和密码）**。
2. 输入 **Username（用户名）**，并在 **Password or access token（密码或访问令牌）**中输入具有仓库写权限的访问令牌。
3. 选择 **Continue（继续）**。

使用不包含凭据的 HTTPS 仓库 URL，例如 `https://github.com/acme/n8n.git`。

### 令牌需要哪些访问权限 <a id="what-access-the-token-needs"></a>

通用 Git 仅运行 Git 命令，不调用 Git 托管服务的 API。令牌需要仓库代码的读写权限。如果将每次晋级推送到功能分支，还需要创建分支的权限。

常见 Git 托管服务：

| Git 托管服务 | 用户名 | 令牌 |
|---|---|---|
| GitHub | 你的 GitHub 用户名 | 对该仓库具有 **Contents（内容）**：**Read and write（读写）**权限的细粒度个人访问令牌。这也包含创建分支的权限。 |
| GitLab | 你的 GitLab 用户名 | 具有 `write_repository` 作用域的个人、群组或项目访问令牌。使用细粒度个人访问令牌时，添加 **Code（代码）**：**Download（下载）**、**Push（推送）**，以及 **Branch（分支）**：**Create（创建）**权限。 |
| Bitbucket Cloud | 你的 Bitbucket 用户名 | 具有 `read:repository:bitbucket` 和 `write:repository:bitbucket` 作用域的 API 令牌。 |

无法更改提供方的身份验证方式。要切换方式，请创建另一个提供方。

## 相关资源 <a id="related-resources"></a>

- [基于 Git 的晋级](./)
- [GitLab](gitlab.md)
- [规划环境](../plan-your-environments.md)
