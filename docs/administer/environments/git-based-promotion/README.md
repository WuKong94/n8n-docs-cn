---
description: 了解环境如何使用 Git 仓库和分支、n8n 支持哪些 Git 提供方，以及如何排查 Git 连接问题。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 基于 Git 的晋级 <a id="git-based-promotion"></a>

基于 Git 的晋级通过 Git 仓库在 n8n 实例之间传递变更。每个环境对应一个仓库和分支。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

## n8n 会向仓库写入哪些内容 <a id="what-n8n-writes-to-the-repository"></a>

n8n 将已晋级的内容保存在仓库根目录的 `n8n/` 文件夹中。该文件夹包含一个 [n8n 包](../../../build/manage-workflows/n8n-packages/README.md)，n8n 在晋级时将其导出，在应用时将其导入。n8n 不会修改该文件夹之外的内容，因此仓库还可以保存 CI 配置等其他文件。

## 直接提交与功能分支 <a id="direct-commits-and-feature-branches"></a>

根据设置，实例晋级变更的目标环境会采用以下方式之一：

- 直接提交到其分支。
- 以其分支为基础，将每次晋级推送到名为 `n8n-promotion/<timestamp>` 的功能分支。n8n 绝不会强制推送。使用功能分支时，环境分支必须已存在于 Git 托管服务上。

从环境应用变更的实例会读取该环境的分支，因此只有在功能分支被合并后，才能看到其中的变更。

## 提供方 <a id="providers"></a>

提供方保存 n8n 连接 Git 托管服务并进行身份验证所需的信息。实例上的多个环境可以使用同一提供方。提供方类型决定可用功能：

| 功能 | 通用 Git | GitLab |
|---|---|---|
| 身份验证 | SSH 密钥，或用户名和访问令牌 | 访问令牌 |
| 从列表选择仓库和分支 | 不支持 | 支持 |
| 晋级审核 | 不支持 | 支持：将 GitLab 合并请求同步到 n8n，在 **Reviews（审核）**中以可视化方式查看变更差异 |

GitHub、Bitbucket 及其他 Git 托管服务可以通过通用 Git 使用，但不提供仓库列表或晋级审核。

## 自托管 n8n <a id="self-hosted-n8n"></a>

- 如果 GitLab 实例位于内部网络，请在 [SSRF 防护](../../../deploy/host-n8n/configure-n8n/security/enable-ssrf-protection.md)中使用 `N8N_SSRF_ALLOWED_HOSTNAMES` 或 `N8N_SSRF_ALLOWED_IP_RANGES`，允许对该实例进行 GitLab API 调用。
- 如果 Git 托管服务使用私有证书颁发机构签发的证书，请为 Git 设置 `GIT_SSL_CAINFO` 或 `GIT_SSL_CAPATH`，并为 API 调用[配置自定义证书颁发机构](../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities.md)。
- 要获取详细日志，请设置 `N8N_LOG_SCOPES=promotions`。

## 故障排查 <a id="troubleshooting"></a>

### 无法完成 Git 操作 <a id="could-not-complete-the-git-operation"></a>

请检查：

- 提供方中的身份验证信息是否正确且未过期。
- 使用 SSH 时，部署密钥是否具有写权限。
- Git 托管服务上是否存在该分支。
- 仓库 URL 的格式是否与身份验证方式相符。请参阅[通用 Git](generic-git.md)。

## 本节内容 <a id="in-this-section"></a>

- [通用 Git](generic-git.md)：通过 SSH 或 HTTPS 连接任意 Git 仓库。
- [GitLab](gitlab.md)：使用访问令牌连接 GitLab，并通过合并请求审核晋级。

## 相关资源 <a id="related-resources"></a>

- [环境管理](../)
- [规划环境](../plan-your-environments.md)
- [首次晋级](../first-promotion.md)
- [晋级变更](../promote-changes.md)
- [应用变更](../apply-changes.md)
- [晋级审核](../promotion-reviews.md)
- [已知限制](../known-limitations.md)
- [从经典环境升级](../upgrade-from-environments-classic.md)
