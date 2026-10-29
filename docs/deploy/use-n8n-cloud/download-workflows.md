---
title: 下载工作流
description: 如何在 n8n Cloud 控制台中从 n8n Cloud 备份下载工作流。
contentType: howto
nodeTitle: 下载工作流
originalFilePath: manage-cloud/download-workflows.md
originalUrl: 'https://docs.n8n.io/manage-cloud/download-workflows'
url: 'https://docs.n8n.io/deploy/use-n8n-cloud/download-workflows'
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 下载工作流 <a href="#download-workflows" id="download-workflows"></a>

n8n Cloud 实例所有者可以在 [n8n Cloud 控制台](use-the-cloud-console.md)中，从 n8n Cloud 备份下载工作流。n8n 会自动创建备份。备份只包含工作流，不包含凭据。

## 如何下载工作流 <a href="#how-to-download-workflows" id="how-to-download-workflows"></a>

1. 打开 [Cloud 控制台](use-the-cloud-console.md)。
1. 在侧边栏选择 **Export（导出）**。n8n 会打开 **Data export（数据导出）** 页面。
1. 在 **Workflow backups（工作流备份）** 中，使用 **Backup（备份）** 下拉列表选择要导出的备份。如果只有一个备份，n8n 会直接显示该备份，而不是下拉列表。
1. 选择 **Download workflows（下载工作流）**。导出内容会在新标签页中打开。

**Overview（概览）** 页面的 **Latest backup（最新备份）** 卡片会显示最近一次备份的创建时间。选择卡片上的 **Download（下载）** 即可进入 **Export（导出）** 页面。

如果实例刚创建或已经离线很久，可能尚无备份。此时 **Export（导出）** 页面会显示 **No backups available yet（暂时没有可用备份）**。

对于 n8n 使用 PostgreSQL 托管的实例，目前暂不支持导出工作流。这些实例的 **Export（导出）** 页面会显示 **Export is unavailable for this instance（此实例无法导出）**，并提供创建支持工单的链接，你可以请求 n8n 支持团队导出工作流。

## 免费试用结束后访问工作流 <a href="#accessing-workflows-after-your-free-trial" id="accessing-workflows-after-your-free-trial"></a>

免费试用结束后，你有 **90 天**时间下载工作流。超过该期限，所有工作流将被**永久删除**，且无法恢复。

## 相关资源 <a id="related-resources"></a>

* [使用 n8n Cloud](./)
* [免费试用并选择套餐](start-your-free-trial.md)
* [使用 Cloud 控制台](use-the-cloud-console.md)
* [更新版本](update-your-version.md)
* [配置 Cloud](configure-cloud/README.md)
* [Gateway 额度](gateway-credits/README.md)
* [Assistant 额度](assistant-credits/README.md)
* [理解并发](understand-concurrency.md)
