---
title: Google 服务账户
contentType:
- integration
- reference
nodeTitle: Google 服务账户
originalFilePath: integrations/builtin/credentials/google/service-account.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google/service-account
url: https://docs.n8n.io/integrations/builtin/credentials/google/service-account
description: Google 服务账户凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Google 的身份验证。
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
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google 服务账户 <a id="google-service-account"></a>

使用服务账户比 OAuth2 更复杂。开始前：

* 检查节点是否[兼容](./README.md#compatible-nodes)服务账户。
* 确认确实需要使用服务账户。对于大多数使用场景，[OAuth2](oauth-single-service.md) 是更好的选择。
* 阅读 Google 的[创建和管理服务账户](https://cloud.google.com/iam/docs/creating-managing-service-accounts)文档。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建 [Google Cloud](https://cloud.google.com/) 账户。

## 设置服务账户 <a href="#set-up-service-account" id="set-up-service-account"></a>

将 n8n 凭据连接到 Google 服务账户需要四个步骤：

1. [创建 Google Cloud Console 项目](service-account.md#create-a-google-cloud-console-project)。
2. [启用 API](service-account.md#enable-apis)。
3. [设置 Google Cloud 服务账户](service-account.md#set-up-google-cloud-service-account)。
4. [完成 n8n 凭据设置](service-account.md#finish-your-n8n-credential)。

### 创建 Google Cloud Console 项目 <a href="#create-a-google-cloud-console-project" id="create-a-google-cloud-console-project"></a>

首先创建 Google Cloud Console 项目。如果已有项目，请跳到下一节：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/create-google-cloud-project.md" %}

### 启用 API <a href="#enable-apis" id="enable-apis"></a>

创建项目后，启用需要访问的 API：

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/enable-apis.md" %}

### 设置 Google Cloud 服务账户 <a href="#set-up-google-cloud-service-account" id="set-up-google-cloud-service-account"></a>

1. 进入 [Google Cloud Console - Library（库）](https://console.cloud.google.com/apis/library)，确认当前位于正确的项目中。

    <figure><img src="../../../.gitbook/assets/google-cloud-project-dropdown (1).png" alt=""><figcaption><p>检查 Google Cloud 顶部导航栏中的项目下拉菜单</p></figcaption></figure>
2. 打开左侧导航菜单，进入 **APIs & Services > Credentials**（API 和服务 > 凭据）。Google 会打开 **Credentials**（凭据）页面。
3. 选择 **+ Create credentials > Service account**（+ 创建凭据 > 服务账户）。
4. 在 **Service account name**（服务账户名称）中输入名称，在 **Service account ID**（服务账户 ID）中输入 ID。更多信息，请参阅[创建服务账户](https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=en#creating)。
5. 选择 **Create and continue**（创建并继续）。
6. 根据使用场景，可在相应部分 **Select a role**（选择角色），以及 **Grant users access to this service account**（授予用户访问此服务账户的权限）。
7. 选择 **Done**（完成）。
8. 在 **Service Accounts**（服务账户）部分选择新建的服务账户，打开 **Keys**（密钥）选项卡。
9. 选择 **Add key > Create new key**（添加密钥 > 创建新密钥）。
10. 在弹窗中选择 **JSON**，再选择 **CREATE**（创建）。Google 会将文件保存到你的计算机。

### 完成 n8n 凭据设置 <a href="#finish-your-n8n-credential" id="finish-your-n8n-credential"></a>

Google 项目和凭据配置完成后，完成 n8n 凭据设置：

1. 打开下载的 JSON 文件。
2. 复制 `client_email`，填入 n8n 凭据的 **Service Account Email**（服务账户邮箱）。
3. 复制 `private_key`，不要包含两侧的 `"` 引号。将其填入 n8n 凭据的 **Private Key**（私钥）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>旧版 n8n</strong></p><p>如果使用早于 0.156.0 的 n8n 版本，请将 JSON 文件中所有 <code>\n</code> 替换为实际换行。</p></div>
4. **可选**：选择是否启用 [**Impersonate a User**（模拟用户）](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority)。
   1. 要使用此选项，必须以 Google Workspace 超级管理员身份，为服务账户[启用全域委派](service-account.md#enable-domain-wide-delegation)。
   2. 输入要模拟用户的 **Email**（电子邮件地址）。
5. 如果计划将此凭据用于 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/README.md) 节点，请开启 **Set up for use in HTTP Request node**（设置为在 HTTP Request 节点中使用）。
   1. 开启此设置后，需要为节点添加 **Scope(s)**（作用域）。n8n 会预填部分作用域。更多信息，请参阅 [Google API 的 OAuth 2.0 作用域](https://developers.google.com/identity/protocols/oauth2/scopes)。
6. **Save**（保存）凭据。

## 视频 <a href="#video" id="video"></a>

{% embed url="https://www.youtube.com/embed/FzQzGODb5Gk?si=YR9vDaTet8vsj-y2" %}

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 服务账户无法访问 Google Drive 文件 <a href="#service-account-cant-access-google-drive-files" id="service-account-cant-access-google-drive-files"></a>

{% hint style="danger" %}
**无法访问“我的云端硬盘”**

Google 不再允许 2025 年 4 月 15 日之后创建的服务账户访问 `my drive`。服务账户现在只能访问共享云端硬盘。

虽然不推荐，但如果需要使用服务账户访问 `my drive`，可通过[启用全域委派](service-account.md#enable-domain-wide-delegation)实现。更多信息，请参阅[这篇社区帖子](https://community.n8n.io/t/please-please-help-upload-file-google-drive-node-with-service-account-not-working/147750/15)。
{% endhint %}

服务账户无法访问未与其关联邮箱共享的 Google Drive 文件和文件夹。

1. 进入 [Google Cloud Console](https://console.cloud.google.com)，复制服务账户邮箱。
2. 进入 [Google Drive](https://drive.google.com)，找到目标文件或文件夹。
3. 右键点击文件或文件夹，选择 **Share**（共享）。
4. 将服务账户邮箱粘贴到 **Add People and groups**（添加用户和群组）。
5. 选择 **Editor**（编辑者）授予读写访问权限，或选择 **Viewer**（查看者）授予只读访问权限。

### 启用全域委派 <a href="#enable-domain-wide-delegation" id="enable-domain-wide-delegation"></a>

要通过服务账户模拟用户，必须为服务账户启用全域委派。

{% hint style="warning" %}
**不推荐**

Google 建议[避免使用全域委派](https://cloud.google.com/iam/docs/best-practices-service-accounts#domain-wide-delegation)，因为它允许模拟任何用户，包括超级管理员，可能带来安全风险。
{% endhint %}

要将全域权限委派给服务账户，必须是 Google Workspace 网域的超级管理员。然后执行以下步骤：

1. 在 Google Workspace 网域的[管理控制台](https://admin.google.com/)中选择汉堡菜单，再选择 **Security > Access and data control > API Controls**（安全性 > 访问权限和数据控制 > API 控制）。
2. 在 **Domain wide delegation**（全域委派）面板中选择 **Manage Domain Wide Delegation**（管理全域委派）。
3. 选择 **Add new**（新增）。
4. 在 **Client ID**（客户端 ID）字段输入服务账户的 **Client ID**。获取方式如下：
   * 打开 Google Cloud Console 项目，再打开 [Service Accounts（服务账户）](https://console.cloud.google.com/iam-admin/serviceaccounts)页面。
   * 复制 **OAuth 2 Client ID**（OAuth 2 客户端 ID），将其用作 **Domain Wide Delegation**（全域委派）的 **Client ID**。
5. 在 **OAuth scopes**（OAuth 作用域）字段中，输入以逗号分隔的作用域列表，授予应用访问权限。例如，如果应用需要全域完整访问 Google Drive API 和 Google Calendar API，请输入 `https://www.googleapis.com/auth/drive, https://www.googleapis.com/auth/calendar`。
6. 选择 **Authorize**（授权）。

可能需要等待 5 分钟至 24 小时，才能模拟 Workspace 中的所有用户。
