---
title: 使用 Browser Use
description: 连接 n8n Browser Use 扩展，让 n8n Assistant 在浏览器中操作并代为设置凭据。
status: preview
tags:
- tag: preview
  primary: true
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Browser Use <a id="work-with-browser-use"></a>

Browser Use 让 n8n Assistant 能够在你自己的浏览器中操作。安装并连接 **n8n Browser Use** Chrome 扩展后，助手可以打开标签页、浏览网站、点击、输入、读取页面，并代为设置凭据。

Browser Use 使用真实浏览器配置文件，因此可以利用你已登录的网站，无需安装其他软件。

{% hint style="info" %}
**功能可用范围**

以下套餐提供 Browser Use：

- **n8n Cloud：** Starter、Pro

自托管 n8n 不提供此功能。
{% endhint %}

{% hint style="info" %}
**预览状态**

Browser Use 属于 n8n Assistant 的一部分，目前处于预览阶段，可能出错，开发期间行为也可能变化。
{% endhint %}

## Browser Use 可以做什么 <a id="what-browser-use-can-do"></a>

连接 Browser Use 后，可以要求 n8n Assistant：

- **设置凭据：** 在服务控制台中创建 API 密钥或应用，并保存为 n8n 凭据。请参阅[通过 Browser Use 设置凭据](#set-up-credentials-with-browser-use)。
- **浏览和研究：** 打开页面、访问链接并读取页面内容。
- **填写表单：** 输入文本、选择选项、上传文件并提交表单。
- **操作标签页：** 打开、切换和关闭标签页。

## 要求 <a id="requirements"></a>

- 使用 Google Chrome 或其他基于 Chromium 的浏览器，例如 Microsoft Edge 或 Brave。手机和平板电脑不支持 Browser Use。
- 实例管理员必须在 **Settings（设置）** > **Assistant** 中开启 **Browser use（浏览器操作）**。

## 连接 Browser Use <a id="connect-browser-use"></a>

1. 在 n8n Assistant 中，选择聊天输入框旁的 **+**，再选择 **Connect browser（连接浏览器）**。
2. 如果尚未安装扩展，选择 **Install Chrome extension（安装 Chrome 扩展）**，从 Chrome 网上应用店添加 [n8n Browser Use](https://chromewebstore.google.com/detail/n8n-browser-use/cegmdpndekdfpnafgacidejijecomlhh)，再返回 n8n。
3. 扩展会弹出窗口，请求允许 n8n 访问浏览器。在弹窗中：
   1. 可选：选择 **Always allow（始终允许） `<your-instance-host>`**，下次连接时不再提示。
   2. 可选：展开 **Allow access to existing tabs（允许访问已有标签页）**，选择要共享的标签页。
   3. 选择 **Allow connection（允许连接）**。

连接成功后，n8n 会显示 **Browser Use is connected（Browser Use 已连接）**。

如果弹窗关闭或未出现，在 n8n 中选择 **Try again（重试）**。

## 通过 Browser Use 设置凭据 <a id="set-up-credentials-with-browser-use"></a>

要让 n8n Assistant 代为创建凭据，在聊天中提出请求即可。例如：

```text
使用我的浏览器创建一个 OpenAI API 密钥，并将其保存为 n8n 凭据。
```

随后，n8n Assistant 会：

1. 打开服务网站，按照步骤创建密钥或应用。如果需要你作出选择，例如项目名或应用名，会在聊天中询问。
2. 需要登录、完成双因素验证或处理验证码时暂停，并请你在浏览器中完成。完成后，在聊天中回复。
3. 从页面获取机密值，并请求你批准创建凭据。

机密值从页面直接写入 n8n 凭据。n8n Assistant 不会看到，也无需你将其粘贴到聊天中。

## 控制 Browser Use 的访问范围 <a id="control-what-browser-use-can-access"></a>

- **标签页：** n8n Assistant 只能使用自己打开的标签页，以及你连接时共享的标签页。共享仅对当前连接有效。
- **网站：** 使用新网站前，n8n Assistant 会请求许可。选择 **Allow once（允许一次）**，仅对当前回复有效；选择 **Allow for session（在本次会话中允许）**，对剩余对话有效；也可以选择 **Deny（拒绝）**。
- **页面上的机密信息：** n8n 读取页面时，会向助手隐藏 API 密钥、密码和其他机密信息；也会禁止对显示机密信息的页面截图。
- **管理员权限：** 实例管理员可以在 **Settings（设置）** > **Assistant** > **Permissions（权限）** 中修改。每项可设为 **Allow（允许）**、**Ask first（先询问，默认）** 或 **Block（禁止）**：
  - **Fetch URLs（获取 URL）**（位于 **Web（网页）** 下）：控制上述网站访问提示。**Allow** 会跳过提示，**Block** 会阻止助手打开网站。此设置也适用于 Browser Use 之外的助手网页访问。
  - **Create credentials from a browser session（从浏览器会话创建凭据）**（位于 **Credentials（凭据）** 下）：控制助手在保存其通过浏览器设置的凭据之前，是否先询问。

{% hint style="warning" %}
Browser Use 使用你已登录的会话执行操作。批准请求前，请检查助手请求访问的网站和执行的操作。
{% endhint %}

## 断开 Browser Use <a id="disconnect-browser-use"></a>

选择聊天输入框旁的 **+**，再选择 Browser Use 旁的 **Disconnect（断开）**。也可以在扩展弹窗中选择 **Disconnect**。

断开只结束当前连接。如果连接时选择了 **Always allow `<your-instance-host>`**，下次 n8n Assistant 发起浏览器连接时，扩展会直接重新连接该实例，不再询问。要停止此行为，打开扩展，从 **Allowed instances（允许的实例）** 中移除该实例。

## 限制 <a id="limitations"></a>

- n8n Assistant 无法代为登录、完成双因素验证或处理验证码，会请你完成这些步骤。
- 无法读取下载的文件，也无法打开浏览器内部页面，例如 `chrome://` 页面。
- Browser Use 仅在浏览器打开且保持连接时工作，不能作为已发布工作流的一部分运行。
- 同一时间只能连接一个浏览器。

## 故障排查 <a id="troubleshooting"></a>

### n8n 检测不到扩展 <a id="n8n-cant-detect-the-extension"></a>

n8n 无法找到 n8n Browser Use 扩展。请在浏览器扩展设置中确认已安装并启用，再选择 **Try again（重试）**。

### Browser Use 要求 Google Chrome 或其他基于 Chromium 的浏览器 <a id="browser-use-requires-google-chrome-or-another-chromium-based-browser"></a>

当前浏览器不支持此扩展，例如 Safari 或 Firefox。请在 Google Chrome、Microsoft Edge 或 Brave 中打开 n8n。

### Browser Use 设置失败 <a id="browser-use-setup-failed"></a>

n8n 无法创建连接链接。选择 **Try again（重试）**；如果问题持续，刷新页面。

### 无法连接到实例 <a id="cant-connect-to-your-instance"></a>

实例不是 n8n Cloud 实例时，扩展会显示 **Can't connect to `<host>`（无法连接到该实例）**。自托管 n8n 不提供 Browser Use。

## 相关资源 <a id="related-resources"></a>

* [使用 n8n Assistant](../n8n-assistant.md)
