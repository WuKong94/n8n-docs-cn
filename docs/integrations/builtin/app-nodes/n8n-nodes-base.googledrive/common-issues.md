---
title: Google Drive 节点常见问题
description: 了解 n8n 工作流自动化平台中 Google Drive 节点的常见问题及解决方法，包括问题详情及建议的处理方式。
contentType:
- integration
- reference
priority: high
nodeTitle: Google Drive 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Google Drive 节点常见问题 <a href="#google-drive-node-common-issues" id="google-drive-node-common-issues"></a>

以下介绍 [Google Drive 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## Google 尚未验证此应用 <a href="#google-hasnt-verified-this-app" id="google-hasnt-verified-this-app"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/unverified-app.md" %}

## Google Cloud 应用失去授权 <a href="#google-cloud-app-becoming-unauthorized" id="google-cloud-app-becoming-unauthorized"></a>

{% include "../../../../reusable-content/.gitbook/includes/integrations/builtin/credentials/google/app-becoming-unauthorized.md" %}

## Google Drive OAuth 错误 <a href="#google-drive-oauth-error" id="google-drive-oauth-error"></a>

使用 OAuth 身份验证时，可能出现无法登录的错误，提示应用不符合 Google 的应用安全要求。

最常见的实际原因是 Google OAuth 配置中的 URL 与 n8n 不一致。请先检查 Google 错误消息中包含的链接，其中会提供具体错误的详情。

如果自托管 n8n，请检查用于构建外部 URL 的 n8n 配置项。确认 [`N8N_EDITOR_BASE_URL`](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md) 和 [`WEBHOOK_URL`](../../../../deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy.md) 环境变量使用完全限定域名。

## 从 Google Drive 获取最近的文件 <a href="#get-recent-files-from-google-drive" id="get-recent-files-from-google-drive"></a>

要从 Google Drive 获取最近的文件，需要按修改时间排序。先搜索已有文件并获取其修改时间，再排序找出最近的文件，最后使用另一个 Google Drive 节点按 ID 操作该文件。

流程如下：

1. 向画布添加 **Google Drive** 节点。
2. 选择 **File/Folder**（文件/文件夹）资源及 **Search**（搜索）操作。
3. 启用 **Return All**（返回全部），以便对所有文件排序。
4. 将 **What to Search**（搜索对象）筛选项设为 **Files**（文件）。
5. 在 **Options**（选项）中，将 **Fields**（字段）设为 **All**（全部）。
6. 将 **Sort**（排序）节点连接到 **Google Drive** 节点的输出。
7. 选择 **Simple**（简单）排序类型。
8. 在 **Fields To Sort By**（排序字段）部分的 **Field Name**（字段名）中输入 `modifiedTime`。
9. 选择 **Descending**（降序）排列。
10. 将 **Limit**（限制数量）节点连接到 **Sort**（排序）节点的输出。
11. 将 **Max Items**（最大数据项数）设为 **1**，仅保留最近的文件。
12. 将另一个 **Google Drive** 节点连接到 **Limit**（限制数量）节点的输出。
13. 选择 **File**（文件）作为 **Resource**（资源），再选择所需操作。
14. 在 **File**（文件）选择器中选择 **By ID**（按 ID）。
15. 选择 **Expression**（表达式），输入 `{{ $json.id }}`。

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%22cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7%22%0A%20%20%7D%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22operation%22%3A%20%22download%22%2C%0A%20%20%20%20%20%20%20%20%22fileId%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22__rl%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%20%20%22value%22%3A%20%22%3D%7B%7B%20%24json.id%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22mode%22%3A%20%22id%22%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2245b53bcd-7dcf-4266-8b6e-bfc12008f9e2%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Google%20Drive1%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.googleDrive%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201500%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22ba223e7c-4fed-41dd-8c80-2e8fd742629f%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.manualTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20620%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22resource%22%3A%20%22fileFolder%22%2C%0A%20%20%20%20%20%20%20%20%22searchMethod%22%3A%20%22query%22%2C%0A%20%20%20%20%20%20%20%20%22returnAll%22%3A%20true%2C%0A%20%20%20%20%20%20%20%20%22filter%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22whatToSearch%22%3A%20%22files%22%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22fields%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22%2A%22%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%2242799909-16f3-4f0a-9ad9-4dd0375814a0%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Google%20Drive%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.googleDrive%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20840%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22sortFieldsUi%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22sortField%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22fieldName%22%3A%20%22modifiedTime%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22order%22%3A%20%22descending%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22bfb8baa6-1b8c-4540-9ad6-b5d7c3f7521b%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sort%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.sort%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201060%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%222883d39a-f7d9-4244-bf7d-b06878678ccc%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Limit%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.limit%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201280%2C%0A%20%20%20%20%20%20%20%20300%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Google%20Drive%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Google%20Drive%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Sort%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Sort%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Limit%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Limit%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Google%20Drive1%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/get-most-recent-file.json" %}
