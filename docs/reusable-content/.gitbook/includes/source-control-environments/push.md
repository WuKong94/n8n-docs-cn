---
title: 将工作推送到 Git
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


将工作推送到 Git：

1. 在主菜单中选择 **Push**（推送）<img src="../../assets/push-icon.png" alt="推送图标" data-size="line">。
2. 在 **Commit and push changes**（提交并推送更改）弹窗中，选择要推送的工作流和数据表。可以按状态（新增、修改、删除）筛选并搜索项目。n8n 会自动推送标签，以及变量和凭据存根。

    n8n 推送的是工作流当前保存的版本，而非已发布版本。之后还需要在远程服务器上单独发布版本。
3. 输入提交说明，用一句话描述本次更改。
4. 选择 **Commit and Push**（提交并推送）。n8n 会将工作发送到 Git，完成后显示成功消息。
