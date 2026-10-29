---
title: Google 凭据
contentType: overview
nodeTitle: Google
originalFilePath: integrations/builtin/credentials/google/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/google
url: https://docs.n8n.io/integrations/builtin/credentials/google
description: Google 凭据文档。使用这些凭据在 n8n 中完成 Google 的身份验证。
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


# Google <a id="google"></a>

本节包含：

* [单一服务 OAuth2](oauth-single-service.md)：为特定服务节点（例如 Gmail 节点）创建 OAuth2 凭据。有两种方式：
  * [托管 OAuth2](oauth-single-service.md#managed-oauth2)：在 n8n 中直接使用 Google 登录，无需在 Google Cloud Console 中设置。仅向 n8n Cloud 用户开放，适用于部分 Google 节点。
  * [自定义 OAuth2](oauth-single-service.md#custom-oauth2)：在 Google Cloud Console 中配置 OAuth2 应用，并将其连接到 n8n 凭据。
* [OAuth2 API（通用）](oauth-generic.md)：创建用于[自定义操作](../../custom-api-actions-for-existing-nodes.md)的 OAuth2 凭据。
* [服务账户](service-account.md)：为部分特定服务节点创建[服务账户](https://cloud.google.com/iam/docs/service-account-overview)凭据。
* [Google PaLM 和 Gemini](../googleai.md)：获取 Google Gemini/Google PaLM API 密钥。

## OAuth2 和服务账户 <a href="#oauth2-and-service-account" id="oauth2-and-service-account"></a>

Google 服务节点支持两种身份验证方式：

* [OAuth2](https://developers.google.com/identity/protocols/oauth2)：推荐使用，支持范围更广，设置也更简单。
* [服务账户](https://cloud.google.com/iam/docs/understanding-service-accounts)：何时需要服务账户，请参阅 [Google 文档：了解服务账户](https://cloud.google.com/iam/docs/understanding-service-accounts)。

### 面向 n8n Cloud 用户的托管 OAuth2 <a href="#managed-oauth2-for-n8n-cloud-users" id="managed-oauth2-for-n8n-cloud-users"></a>

{% hint style="info" %}
**功能可用范围**

下列 Google 节点的托管 OAuth2 适用于：

- **n8n Cloud：**所有套餐

自托管版本不提供此功能。自托管时，请配置自己的 OAuth2 凭据。

{% include "../../../../reusable-content/.gitbook/includes/integrations/managed-google-oauth.md" %}

{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/integrations/managed-google-oauth.md" %}

## 兼容节点 <a href="#compatible-nodes" id="compatible-nodes"></a>

配置完成后，可使用凭据为以下节点进行身份验证。大多数节点兼容 OAuth2 身份验证，n8n 对服务账户身份验证的支持有限。

| 节点 | OAuth | 服务账户 |
| ----------------------------------------------------------------------------------------------- | :---: | :-------------: |
| [Google Ads](../../app-nodes/n8n-nodes-base.googleads.md)                                       |   ✅   |        ❌        |
| [Gmail](../../app-nodes/n8n-nodes-base.gmail/README.md)                                                  |   ✅   |        ⚠️       |
| [Google Analytics](../../app-nodes/n8n-nodes-base.googleanalytics.md)                           |   ✅   |        ❌        |
| [Google BigQuery](../../app-nodes/n8n-nodes-base.googlebigquery.md)                             |   ✅   |        ✅        |
| [Google Books](../../app-nodes/n8n-nodes-base.googlebooks.md)                                   |   ✅   |        ✅        |
| [Google Calendar](../../app-nodes/n8n-nodes-base.googlecalendar/README.md)                               |   ✅   |        ❌        |
| [Google Chat](../../app-nodes/n8n-nodes-base.googlechat.md)                                     |   ✅   |        ✅        |
| [Google Cloud Storage](../../app-nodes/n8n-nodes-base.googlecloudstorage.md)                    |   ✅   |        ✅        |
| [Google Contacts](../../app-nodes/n8n-nodes-base.googlecontacts.md)                             |   ✅   |        ❌        |
| [Google Cloud Firestore](../../app-nodes/n8n-nodes-base.googlecloudfirestore.md)                |   ✅   |        ✅        |
| [Google Cloud Natural Language](../../app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md)   |   ✅   |        ❌        |
| [Google Cloud Realtime Database](../../app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) |   ✅   |        ❌        |
| [Google Docs](../../app-nodes/n8n-nodes-base.googledocs.md)                                     |   ✅   |        ✅        |
| [Google Drive](../../app-nodes/n8n-nodes-base.googledrive/README.md)                                     |   ✅   |        ✅        |
| [Google Drive Trigger](../../trigger-nodes/n8n-nodes-base.googledrivetrigger/README.md)                  |   ✅   |        ✅        |
| [Google Perspective](../../app-nodes/n8n-nodes-base.googleperspective.md)                       |   ✅   |        ❌        |
| [Google Sheets](../../app-nodes/n8n-nodes-base.googlesheets/README.md)                                   |   ✅   |        ✅        |
| [Google Slides](../../app-nodes/n8n-nodes-base.googleslides.md)                                 |   ✅   |        ✅        |
| [Google Tasks](../../app-nodes/n8n-nodes-base.googletasks.md)                                   |   ✅   |        ❌        |
| [Google Translate](../../app-nodes/n8n-nodes-base.googletranslate.md)                           |   ✅   |        ✅        |
| [Google Workspace Admin](../../app-nodes/n8n-nodes-base.gsuiteadmin.md)                         |   ✅   |        ❌        |
| [YouTube](../../app-nodes/n8n-nodes-base.youtube.md)                                            |   ✅   |        ❌        |

{% hint style="warning" %}
**Gmail 和服务账户**

Google 在技术上支持通过服务账户使用 Gmail，但这需要启用全域委派，而 Google 不建议这样做，且其行为可能不一致。

n8n 建议 Gmail 节点使用 OAuth2。
{% endhint %}
