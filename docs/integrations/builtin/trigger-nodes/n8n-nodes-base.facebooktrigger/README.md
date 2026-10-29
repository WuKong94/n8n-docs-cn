---
title: Facebook 触发器
description: 了解如何在 n8n 中使用 Facebook 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: n8n-nodes-base.facebooktrigger
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Facebook 触发器节点 <a href="#facebook-trigger-node" id="facebook-trigger-node"></a>

[Facebook](https://www.facebook.com/) 是社交网络网站，可在线联系家人朋友并分享内容。

使用 Facebook Trigger 节点，在 Facebook 事件发生时触发工作流。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [Facebook App 凭据文档](../../credentials/facebookapp.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [Facebook Trigger 集成](https://n8n.io/integrations/facebook-trigger/)页面。
{% endhint %}

## 对象 <a href="#objects" id="objects"></a>

- [**Ad Account（广告账户）**](ad-account.md)：获取某些广告变更的更新。
- [**Application（应用）**](application.md)：获取发送给应用的更新。
- [**Certificate Transparency（证书透明度）**](certificate-transparency.md)：订阅的域名生成新安全证书时获取更新，包括新证书及潜在钓鱼攻击。
- [**Group（群组）**](group.md)中的活动和事件。
- [**Instagram**](instagram.md)：有人评论你的应用用户的 Media（媒体）对象、@提及你的应用用户，或这些用户的 Stories（快拍）过期时获取更新。
- [**Link（链接）**](link.md)：获取由外部提供方生成丰富预览的链接的更新。
- [**Page（主页）**](page.md)更新。
- [**Permissions（权限）**](permissions.md)：授予或撤销权限时的更新。
- [**User（用户）**](user.md)个人资料更新。
- [**WhatsApp Business Account（WhatsApp 商业账户）**](whatsapp.md)<br>
    
    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>使用 WhatsApp 触发器</strong></p><p>对于这些事件，n8n 建议使用配有 <a href="../../credentials/whatsapp.md">WhatsApp 凭据</a>的 <a href="../n8n-nodes-base.whatsapptrigger.md">WhatsApp Trigger 节点</a>来替代 Facebook Trigger 节点。WhatsApp Trigger 节点可监听的事件更多。</p></div>

- [**Workplace Security（Workplace 安全）**](workplace-security.md)

对于每个 **Object**（对象），可使用 **Field Names or IDs**（字段名称或 ID）下拉菜单进一步选择要接收的数据。详细信息请参阅相应链接页面。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/facebook-trigger/)。

API 的详细信息，请参阅 Meta 的 [Graph API 文档](https://developers.facebook.com/docs/graph-api/webhooks/reference)。
