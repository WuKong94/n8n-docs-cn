---
description: 使用访问令牌将环境连接到 GitLab，选择仓库和分支，并通过 GitLab 合并请求审核晋级。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitLab <a id="gitlab"></a>

GitLab 提供方将环境连接到 GitLab.com 或自管理 GitLab 实例上的仓库。它可以列出仓库和分支，并支持基于合并请求的晋级审核，让你在 n8n 中以可视化方式审查变更。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## GitLab 支持的功能 <a id="what-gitlab-supports"></a>

| 功能 | 支持情况 |
|---|---|
| 身份验证 | 访问令牌 |
| 从列表选择仓库和分支 | 支持 |
| 将每次晋级推送到功能分支 | 支持，通过合并请求实现 |
| 晋级审核 | 支持：将 GitLab 合并请求同步到 n8n，在 **Reviews（审核）**中以可视化方式查看变更差异 |

## 创建访问令牌 <a id="create-an-access-token"></a>

n8n 需要一个 GitLab 令牌。可以创建经典访问令牌或细粒度个人访问令牌。无论选择哪一种，令牌所属用户在仓库中至少需要 Developer 角色，因为 n8n 只列出该用户具有此角色的仓库。要将晋级审核合并到受保护分支，该用户还必须具有分支保护规则允许合并的角色，默认为 Maintainer。

### 经典访问令牌 <a id="classic-access-token"></a>

创建具有 `api` 和 `write_repository` 作用域的个人、群组或项目访问令牌。n8n 建议使用群组访问令牌，因为它不绑定到可能离职的个人。

### 细粒度个人访问令牌 <a id="fine-grained-personal-access-token"></a>

如果 GitLab 版本支持，可以使用细粒度个人访问令牌。

1. 在 GitLab 中开始创建细粒度个人访问令牌。请参阅 GitLab 文档中的[细粒度个人访问令牌](https://docs.gitlab.com/auth/tokens/fine_grained_access_tokens/)。
2. 在 **Group and project access（群组和项目访问）**下，选择 **Only specific groups or projects that I'm a member of（仅限我所属的特定群组或项目）**，并添加仓库所属项目或群组。
3. 在 **Add resource permissions（添加资源权限）**下，添加下表中的每项资源并选择对应权限。令牌需要全部这些权限。在资源选择器中，每项资源都位于某个 **Resource access（资源访问）**选项卡及其分类中。
4. 选择 **Generate token（生成令牌）**并复制令牌。

| 资源访问选项卡 | 分类 | 资源 | 权限 | n8n 的用途 |
|---|---|---|---|---|
| **User（用户）** | **System Access（系统访问）** | **User（用户）** | Read（读取） | 检查令牌 |
| **User（用户）** | **Projects（项目）** | **Project（项目）** | Read（读取） | 列出仓库 |
| **Group and project（群组和项目）** | **Repository（仓库）** | **Branch（分支）** | Create（创建）、Read（读取）、Delete（删除） | 列出分支、推送功能分支，以及在合并后删除功能分支 |
| **Group and project（群组和项目）** | **Repository（仓库）** | **Code（代码）** | Download（下载）、Push（推送） | 读取仓库并向其推送 |
| **Group and project（群组和项目）** | **Repository（仓库）** | **Merge Request（合并请求）** | Create（创建）、Read（读取）、Approve（批准）、Merge（合并） | 创建、批准和合并晋级审核 |
| **Group and project（群组和项目）** | **Project Planning（项目规划）** | **Work Item（工作项）** | Create（创建）、Read（读取） | 向合并请求添加批准备注，并读取评论 |

## 设置 GitLab 提供方 <a id="set-up-the-gitlab-provider"></a>

1. 在 **Connect GitLab（连接 GitLab）**对话框中，输入 **Name（名称）**、**GitLab base URL（GitLab 基础 URL）**（例如 `https://gitlab.com` 或 `https://gitlab.example.com`）和 **Access token（访问令牌）**。
2. 选择 **Continue（继续）**。
3. 在环境设置中，从列表选择 **Repository（仓库）**和 **Branch（分支）**。

对于位于内部网络或使用私有证书颁发机构的自管理 GitLab 实例，请参阅[基于 Git 的晋级](README.md#self-hosted-n8n)。

## 通过合并请求进行晋级审核 <a id="promotion-reviews-with-merge-requests"></a>

要通过合并请求审核晋级，请在晋级目标环境中开启 **Open a merge request in GitLab（在 GitLab 中创建合并请求）**。有关如何审查和批准，请参阅[使用 GitLab 进行晋级审核](../promotion-reviews.md#promotion-reviews-with-gitlab)。

## 相关资源 <a id="related-resources"></a>

- [基于 Git 的晋级](./)
- [通用 Git](generic-git.md)
- [晋级审核](../promotion-reviews.md)
- [规划环境](../plan-your-environments.md)
