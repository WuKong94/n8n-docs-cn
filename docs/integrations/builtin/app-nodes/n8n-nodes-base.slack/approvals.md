---
description: 了解如何通过 Slack 节点的发送并等待响应操作，让审批人直接在 Slack 中批准或拒绝 n8n 工作流操作。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Slack 中的审批 <a id="approvals-in-slack"></a>

使用 **Message**（消息）> **Send and Wait for Response**（发送并等待响应）操作，审批人可直接在 Slack 中批准或拒绝。无需打开浏览器页面：有人响应后，工作流立即恢复，输出会记录响应者。

## 与链接按钮的区别 <a id="how-it-differs-from-link-buttons"></a>

| 对比项 | 链接按钮（默认） | Slack 内审批 |
|------|------------------------|--------------------|
| 作出决定的位置 | 在浏览器中打开 n8n 页面 | 在 Slack 内点击一次 |
| 谁能响应 | 任何能够点击链接的人 | 仅你列出的审批人；列表为空时，任何能看到消息的人都可响应。其他人会收到一条可自行设置措辞的私密提示，工作流继续等待。 |
| 输出 | `approved` 和 `respondedAt` | 额外包含响应者的 ID、姓名、用户名和邮箱，以及频道和消息信息 |
| 决定后的消息 | 保持原样，按钮仍可点击，但后续点击会显示“no action required”（无需操作）页面。以首次决定为准。 | 可选择：显示结果并移除按钮（默认）、仅移除按钮，或保持消息不变 |
| 安全性 | 签名链接：无法篡改 URL 或操作，但任何持有链接的人都能响应，n8n 无法得知点击者身份 | n8n 使用 Slack 请求签名验证每个回调确实来自 Slack，并检查响应者是否在审批人列表中 |

## 要求 <a id="requirements"></a>

要在 Slack 内审批，需要：

- Slack 可通过公共 HTTPS 访问 n8n 实例。有人响应时，Slack 会回调实例，因此仅运行在 localhost 上的实例无法使用此功能。
- 使用 API 访问令牌或 OAuth2 的 Slack 凭据。
- Slack 凭据的 **Signature Secret**（签名密钥）字段必须包含 Slack 应用的签名密钥，可在 **Settings**（设置）> **Basic Information**（基本信息）中找到。没有此值，按钮仍会显示，但点击不会恢复工作流。
- **Response Type**（响应类型）设为 **Approval**（审批）。
- `users:read` 和 `users:read.email` 作用域。响应者的 ID、姓名和用户名来自 Slack 交互载荷，邮箱通过 Slack API 获取，需要这些作用域。缺少作用域只会让输出不包含邮箱。如果使用在此功能推出前创建的 OAuth2 凭据，请重新连接以获得 `users:read.email` 作用域。

## 设置审批 <a id="set-up-approvals"></a>

### 1. 创建 Slack 应用和凭据 <a id="1-create-a-slack-app-and-credential"></a>

按照[使用 API 访问令牌](../../credentials/slack.md#using-api-access-token)或[使用 OAuth2](../../credentials/slack.md#using-oauth2)的说明创建 Slack 应用并设置凭据。配置应用作用域时，添加 `users:read` 和 `users:read.email`，让输出能够包含响应者邮箱。

### 2. 启用交互功能 <a id="2-turn-on-interactivity"></a>

1. 在 Slack 中进入 [Your Apps（你的应用）](https://api.slack.com/apps)，选择要使用的应用。
2. 进入 **Features**（功能）> **Interactivity & Shortcuts**（交互与快捷方式），开启 **Interactivity**（交互功能）。
3. 在 **Request URL**（请求 URL）中输入 `https://<your-n8n-instance>/webhook-waiting-slack`。实例中的所有工作流共用这一个 URL。如果修改了 `N8N_ENDPOINT_WEBHOOK_WAIT` 环境变量，请相应调整路径。
4. 选择 **Save Changes**（保存更改）。

{% hint style="info" %}
Slack 每个应用只允许设置一个 **Request URL**（请求 URL），因此一个 Slack 应用对应一个 n8n 实例。
{% endhint %}

### 3. 将签名密钥添加到凭据 <a id="3-add-the-signing-secret-to-your-credential"></a>

1. 在 Slack 应用中进入 **Settings**（设置）> **Basic Information**（基本信息），复制 **App Credentials**（应用凭据）部分的 **Signing Secret**（签名密钥）。
2. 在 n8n 中，将其粘贴到 Slack 凭据的 **Signature Secret**（签名密钥）字段。

n8n 使用签名密钥验证每个回调来自 Slack，拒绝未通过验证的回调，工作流继续等待。

### 4. 配置节点 <a id="4-configure-the-node"></a>

在 Slack 节点中选择 **Message**（消息）资源和 **Send and Wait for Response**（发送并等待响应）操作，将 **Response Type**（响应类型）设为 **Approval**（审批）。随后会在 **Advanced Interactivity**（高级交互）标题下显示以下设置。

- **Capture Who Responded**（记录响应者）：开启后，将审批按钮切换为 Slack 交互按钮，并记录响应者。开启后才会显示其余设置。
- **Restrict Who Can Approve**（限制可审批人员）：选择允许操作的用户，也可通过表达式指定用户 ID。不在列表中的人点击时会收到私密提示，工作流继续等待。
- **Unauthorized Reply**（未授权响应提示）：向点击按钮但不在审批人列表中的用户显示的私密临时消息。默认值为 `You are not authorized to respond to this request.`
- **After Decision**（决定之后）：有人批准或拒绝后，如何处理原始 Slack 消息。
    - **Show Outcome and Remove Buttons**（显示结果并移除按钮，默认）：移除按钮，并添加一行文字，说明决定及响应者。
    - **Remove Buttons Only**（仅移除按钮）：移除按钮，不添加结果说明行。
    - **Keep Message Unchanged**（保持消息不变）：保留发送时的消息及按钮。后续点击不会改变已记录的决定，始终以首次决定为准。

审批人列表留空时，任何能看到消息的人都可以批准或拒绝；在频道中，即所有成员。该列表控制谁能响应，不控制谁能看到请求，因此敏感审批应发送到私密频道或私信。

### 5. 测试 <a id="5-test-it"></a>

执行工作流，在 Slack 中选择 **Approve**（批准），检查节点输出。

## 节点输出 <a id="node-output"></a>

有人在 Slack 中响应后，节点会输出决定及响应者信息：

```json
{
	"data": {
		"approved": true,
		"respondedAt": "2025-07-13T12:34:56.000Z",
		"channel": "C0123ABC456",
		"messageId": "1752407696.123456",
		"responder": {
			"id": "U0123ABC456",
			"name": "Jo Doe",
			"username": "jo.doe",
			"email": "jo@example.com",
			"source": "slack"
		}
	}
}
```

使用链接按钮时，输出仅包含 `approved` 和 `respondedAt`。

## 何时仍使用链接按钮 <a id="when-you-get-link-buttons-instead"></a>

满足以下任一条件时，节点维持原有行为，发送打开 n8n 确认页面的按钮：

- **Response Type**（响应类型）为 **Free Text**（自由文本）或 **Custom Form**（自定义表单）。
- **Capture Who Responded**（记录响应者）关闭。

已有工作流继续按原有方式运行。

## 故障排查 <a id="troubleshooting"></a>

- **按钮没有反应，或 Slack 显示警告**：**Request URL**（请求 URL）错误、实例无法通过公共 HTTPS 访问，或 **Signature Secret**（签名密钥）缺失/错误。无论是回调被拒绝，还是 URL 无法访问，Slack 都显示相同警告。
- **有人收到“not authorized”（未授权）回复**：该用户不在 **Restrict Who Can Approve**（限制可审批人员）中。提示措辞来自 **Unauthorized Reply**（未授权响应提示）。
- **有人响应后工作流仍未恢复**：**Signature Secret**（签名密钥）缺失，或与应用的 **Signing Secret** 不匹配。n8n 会拒绝无法验证的回调，工作流继续等待。
