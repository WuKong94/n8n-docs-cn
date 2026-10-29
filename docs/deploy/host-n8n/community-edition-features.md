---
title: 比较套餐和版本
contentType: explanation
hide:
- tags
nodeTitle: 比较套餐和版本
originalFilePath: hosting/community-edition-features.md
originalUrl: https://docs.n8n.io/hosting/community-edition-features
url: https://docs.n8n.io/deploy/host-n8n/community-edition-features
description: 比较自托管 n8n 的套餐和版本：社区版、已注册社区版、商业版和企业版。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
tags:
- Community edition
- Enterprise edition
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 比较套餐和版本 <a id="compare-plans-and-editions"></a>

所有自托管安装使用相同的底层产品。你可以一直使用免费的社区版，也可以免费注册以解锁额外功能，或订阅付费套餐，获得许可证密钥并解锁相应功能。

- **社区版（Community edition）**：免费版本，n8n 在没有许可证密钥时运行此版本。
- **已注册社区版（Registered Community edition）**：通过注册邮箱解锁额外功能的社区版，仍然免费。
- **商业版（Business）**和**企业版（Enterprise）**套餐：付费套餐，订阅后可获得用于解锁相应功能的许可证密钥。

{% hint style="info" %}
**套餐、版本还是许可证？**

**版本（edition）**指运行的自托管软件类型：社区版、已注册社区版、商业版或企业版。**套餐（plan）**指购买的自托管或 [n8n Cloud](../use-n8n-cloud/start-your-free-trial.md) 付费订阅层级。订阅付费套餐后，会获得用于解锁相应功能的**许可证（license）**密钥。注册免费社区版也会使用许可证密钥。定义请参阅[术语表](../../get-started/key-concept-glossary.md#edition-n8n)。
{% endhint %}

{% hint style="info" %}
**以定价页面为准**

各套餐和版本的具体功能可能变化。最新功能划分请参阅[定价页面](https://n8n.io/pricing/)。本页解释套餐、版本及其主要区别，并非完整功能清单。
{% endhint %}

## 社区版 <a href="#community-edition" id="community-edition"></a>

社区版包含 n8n 几乎全部功能，但不包含以下功能：

* [自定义变量](../../build/code-in-n8n/define-custom-variables.md)
* [环境](../../administer/use-source-control-and-environments/README.md)
* [外部密钥](../../administer/manage-credentials/use-external-secret-stores.md)
* [二进制数据外部存储](configure-n8n/scaling/use-external-storage.md)
* [日志流](../../administer/observe-and-log/stream-logs-to-external-systems.md)（但*包含*[日志记录](keep-n8n-running/set-up-logging.md)功能）
* [多主节点模式](configure-n8n/scaling/enable-queue-mode.md#multi-main-setup)（但*包含*[队列模式](configure-n8n/scaling/enable-queue-mode.md)）
* [项目](../../administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)
* SSO（[SAML](configure-n8n/security/configure-sso.md)、[LDAP](../../administer/manage-users-and-access/verify-user-identity/connect-ldap.md)）
* 共享[工作流](../../build/manage-workflows/share-with-others.md)和[凭据](../../administer/manage-credentials/share-credentials-securely.md)（只有实例所有者和创建者可以访问工作流与凭据）
* [通过 Git 进行版本控制](../../administer/use-source-control-and-environments/README.md)

这些功能在自托管商业版和企业版套餐中提供，部分也在 n8n Cloud 中提供。最新划分请参阅[定价页面](https://n8n.io/pricing/)。

## 已注册社区版 <a href="#registered-community-edition" id="registered-community-edition"></a>

使用邮箱注册社区版，即可获得免费许可证密钥，解锁以下功能：

* 文件夹：通过文件夹整理工作流。
* [在编辑器中调试](../../build/understand-workflows/understand-executions/debug-executions.md)：编辑工作流时，复制并固定[^1]执行数据。
* [自定义执行数据](../../build/understand-workflows/understand-executions/customize-executions-data.md)：保存、查找并注释执行元数据。

注册新的社区版实例时，在首次创建账号时选择相应选项即可。

注册现有社区版实例：

1. 选择左下角的**三点图标** <img src="../.gitbook/assets/three-dots-horizontal (1).png" alt="three dots icon" data-size="line">。
2. 选择 **Settings（设置）**，再选择 **Usage and plan（使用情况与套餐）**。
3. 选择 **Unlock（解锁）**，输入邮箱，再选择 **Send me a free license key（向我发送免费许可证密钥）**。
4. 查看所填邮箱收到的邮件。

获得许可证密钥后，可以点击许可证邮件中的按钮激活，或进入 **Options > Settings > Usage and plan（选项 > 设置 > 使用情况与套餐）**，选择 **Enter activation key（输入激活密钥）**。

## 商业版和企业版套餐 <a href="#business-and-enterprise-editions" id="business-and-enterprise-editions"></a>

商业版和企业版套餐解锁社区版不包含的付费功能，例如 SSO、环境、外部密钥和日志流。企业版还提供更高级的安全、扩展和治理功能。

订阅付费套餐后，会获得解锁相应功能的许可证密钥。将密钥添加到实例中即可激活。密钥的获取和激活方法请参阅[管理许可证](configure-n8n/manage-your-license.md)；各套餐包含的功能请参阅[定价页面](https://n8n.io/pricing/)。

## 如何选择套餐或版本 <a href="#which-edition-is-right-for-you" id="which-edition-is-right-for-you"></a>

- 使用**社区版**，可以免费自托管 n8n，并获得几乎全部功能。
- 免费**注册**社区版，还可获得文件夹、编辑器调试和自定义执行数据功能。
- 需要 SSO、环境、项目或外部密钥等付费功能时，可以订阅**商业版**或**企业版**。如果完全不想管理基础设施，也可以考虑 [n8n Cloud](../use-n8n-cloud/start-your-free-trial.md)。

[^1]: 数据固定允许你在工作流开发过程中暂时冻结节点的输出，使用可预期的数据开发工作流，无需反复请求外部服务。生产工作流会忽略固定数据，每次执行时请求新数据。

## 相关资源 <a id="related-resources"></a>

* [自托管 n8n](./)
* [安装方式](install-options/README.md)
* [配置 n8n](configure-n8n/README.md)
* [保持 n8n 运行](keep-n8n-running/README.md)
* [理解架构](understand-the-architecture/README.md)
* [作为 OEM 集成部署](deploy-as-an-oem-integration/README.md)
* [使用 AI 入门套件部署](deploy-with-the-ai-starter-kit.md)
