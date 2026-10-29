---
title: 生成 Outlook 应用密码
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

如果希望使用应用密码代替邮箱账号密码：

1. 登录 [My Account（我的账号）](https://myaccount.microsoft.com/)页面。
2. 如果左侧导航中有 **Security Info（安全信息）** 选项，请跳至[安全信息中的应用密码](#security-info-app-password)；如果没有，请继续执行以下步骤。
3. 进入[其他安全验证页面](https://account.activedirectory.windowsazure.com/Proofup.aspx)。
4. 选择 **App passwords（应用密码）**，再选择 **Create（创建）**。
5. 为应用密码输入 **Name（名称）**，例如 `n8n credential`。
6. 使用 **copy password to clipboard（将密码复制到剪贴板）** 选项，将其填入 n8n 的 **Password（密码）** 字段，替代邮箱账号密码。

更多信息请参阅 Outlook 的[管理两步验证的应用密码](https://support.microsoft.com/en-us/account-billing/manage-app-passwords-for-two-step-verification-d6dc8c6d-4bf7-4851-ad95-6d07799387e9)页面。

### 安全信息中的应用密码 <a href="#security-info-app-password" id="security-info-app-password"></a>

如果左侧导航中有 **Security Info（安全信息）** 选项：

1. 选择 **Security Info（安全信息）**，打开安全信息页面。
2. 选择 **+ Add method（添加方法）**。
3. 在 **Add a method（添加方法）** 页面上，选择 **App password（应用密码）**，再选择 **Add（添加）**。
4. 为应用密码输入 **Name（名称）**，例如 `n8n credential`。
5. 复制 **Password（密码）**，填入 n8n 的 **Password** 字段，替代邮箱账号密码。

更多信息请参阅 Outlook 的[从安全信息创建应用密码（预览版）](https://support.microsoft.com/en-us/account-billing/create-app-passwords-from-the-security-info-preview-page-d8bc744a-ce3f-4d4d-89c9-eb38ab9d4137)页面。
