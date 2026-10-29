---
title: 启用 Google API
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

1. 进入 [Google Cloud 控制台的 API 库](https://console.cloud.google.com/apis/library)，确保已选择正确的项目。
	<figure>
	<img src="../../../../../assets/google-cloud-project-dropdown.png" alt="">
	<figcaption>检查 Google Cloud 顶部导航中的项目下拉菜单</figcaption>
	</figure>
1. 进入 **APIs & Services > Library（API 和服务 > 库）**。
1. 搜索并选择要启用的 API。例如，对于 Gmail 节点，搜索并启用 Gmail API。
1. 部分集成还需要其他 API，或需要申请访问权限：<br>
	* Google Perspective：[申请 API 访问权限](https://developers.perspectiveapi.com/s/docs-get-started)。
	* Google Ads：获取[开发者令牌](https://developers.google.com/google-ads/api/docs/first-call/dev-token)。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>需要 Google Drive API</strong></p><p>以下集成除了各自的 API 外，还需要 Google Drive API：</p><ul><li>Google Docs</li><li>Google Sheets</li><li>Google Slides</li></ul></div>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Google Vertex AI API</strong></p><p>除 Vertex AI API 外，还需要启用 <a href="https://console.cloud.google.com/apis/api/cloudresourcemanager.googleapis.com/">Cloud Resource Manager API</a>。</p></div>

1. 选择 **ENABLE（启用）**。
