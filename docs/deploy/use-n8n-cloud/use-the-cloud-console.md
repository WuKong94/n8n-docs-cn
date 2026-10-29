---
description: 了解如何打开和使用 n8n Cloud 控制台，供实例所有者管理 Cloud 实例、套餐和额度。
contentType: howto
nodeTitle: 使用 Cloud 控制台
originalFilePath: manage-cloud/cloud-admin-dashboard.md
originalUrl: 'https://docs.n8n.io/manage-cloud/cloud-admin-dashboard'
url: 'https://docs.n8n.io/deploy/use-n8n-cloud/use-the-cloud-console'
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Cloud 控制台 <a id="use-the-cloud-console"></a>

实例所有者可以通过 [app.n8n.cloud](https://app.n8n.cloud) 上的 n8n Cloud 控制台，管理 n8n Cloud 实例、套餐、账单和额度。

只有实例所有者可以打开 Cloud 控制台。实例中的其他用户通过 n8n 编辑器工作，无权访问该控制台。

## Cloud 控制台中的页面 <a id="pages-in-the-cloud-console"></a>

Cloud 控制台的左侧边栏包含以下页面：

* **Overview（概览）**：显示实例状态，选择 **Open instance（打开实例）** 可进入编辑器。还会显示套餐、执行用量、额度余额、n8n 版本、最新备份和近期活动。
* **Instance settings（实例设置）**：更改 n8n 版本、发布通道、更新频率和维护窗口；设置时区及需要保存的执行类型；启用或关闭 Gateway 额度和已验证社区节点。你也可以在这里重启实例或删除账号。
* **Assistant credits（Assistant 额度）**：查看和充值用于支付 n8n Assistant 使用费用的 [Assistant 额度](assistant-credits/README.md)。
* **Gateway credits（Gateway 额度）**：查看和充值用于支付工作流中 AI 模型和服务费用的 [Gateway 额度](gateway-credits/README.md)。
* **Billing（账单）**：查看、变更或取消当前套餐，更改付款方式，并查看交易记录。
* **Export（导出）**：从备份中[下载工作流](download-workflows.md)。

只有实例支持相应功能时，才会显示 **Assistant credits** 和 **Gateway credits** 页面。

选择侧边栏底部的 **Help & resources（帮助与资源）**，可找到帮助中心、文档、社区论坛和工作流模板的链接。

## 从 n8n 打开 Cloud 控制台 <a id="open-the-cloud-console-from-n8n"></a>

1. 以实例所有者身份登录 n8n 实例。
1. 在左侧菜单中选择 **Admin Panel（管理面板）**。n8n 会打开 Cloud 控制台。

## 使用免密登录链接打开 Cloud 控制台 <a id="open-the-cloud-console-with-a-magic-link"></a>

你可以使用发送到邮箱的免密登录链接进入 Cloud 控制台。即使实例由于无法启动等原因处于离线状态，这种方式仍然有效。

1. 前往 [app.n8n.cloud/magic-link](https://app.n8n.cloud/magic-link)。
1. 在 **Instance owner email（实例所有者邮箱）** 中输入实例所有者账号的邮箱地址。
1. 选择 **Send magic link（发送免密登录链接）**。
1. 打开 n8n 发送的邮件，点击其中的链接登录。

你也可以在 [app.n8n.cloud](https://app.n8n.cloud) 登录页面选择 **Don't know your instance name?（不知道实例名称？）**，再选择 **Sign in to the Cloud console（登录 Cloud 控制台）**，进入同一个页面。

## 重启实例 <a id="restart-your-instance"></a>

如果实例离线或无响应，可以通过 Cloud 控制台重启：

1. 打开 Cloud 控制台，选择 **Instance settings（实例设置）**。
1. 在页面顶部的实例状态旁选择 **Restart（重启）**。
1. 选择 **Restart instance（重启实例）** 进行确认。

重启完成前，实例会处于离线状态，所有正在运行的执行任务都会停止。

## 相关资源 <a id="related-resources"></a>

* [使用 n8n Cloud](./)
* [免费试用并选择套餐](start-your-free-trial.md)
* [更新版本](update-your-version.md)
* [配置 Cloud](configure-cloud/README.md)
* [Gateway 额度](gateway-credits/README.md)
* [Assistant 额度](assistant-credits/README.md)
* [理解并发](understand-concurrency.md)
* [下载工作流](download-workflows.md)
