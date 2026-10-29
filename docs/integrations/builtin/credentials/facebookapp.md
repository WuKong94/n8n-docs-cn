---
title: Facebook App 凭据
contentType:
- integration
- reference
priority: medium
nodeTitle: Facebook App 凭据
originalFilePath: integrations/builtin/credentials/facebookapp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/facebookapp
url: https://docs.n8n.io/integrations/builtin/credentials/facebookapp
description: Facebook App 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Facebook App 的身份验证。
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


# Facebook App 凭据 <a id="facebook-app-credentials"></a>

这些凭据可用于以下节点的身份验证：

* [Facebook Trigger（触发器）](../trigger-nodes/n8n-nodes-base.facebooktrigger/README.md)

{% hint style="info" %}
**Facebook Graph API 凭据**

如果要为 [Facebook Graph API](../app-nodes/n8n-nodes-base.facebookgraphapi.md) 节点创建凭据，请按照 [Facebook Graph API 凭据](facebookgraph.md)文档中的说明操作。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* App access token（应用访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Meta Graph API 文档](https://developers.facebook.com/docs/graph-api/overview)。

## 使用应用访问令牌 <a href="#using-app-access-token" id="using-app-access-token"></a>

配置此凭据需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

* 应用 **Access Token**（访问令牌）
* 可选的 **App Secret**（应用密钥）：用于验证载荷的完整性及来源。

设置凭据需要五个步骤：

1. [创建 Meta 应用](facebookapp.md#create-a-meta-app)，添加 Webhooks 产品。
2. 为该应用[生成应用访问令牌](facebookapp.md#generate-an-app-access-token)。
3. [配置 Facebook 触发器](facebookapp.md#configure-the-facebook-trigger)。
4. 可选：[添加应用密钥](facebookapp.md#optional-add-an-app-secret)。
5. [应用审核](facebookapp.md#app-review)：仅当应用用户在应用本身中没有角色时才需要。如果仅供内部使用，则无需此步骤。

各步骤的详细说明如下。

### 创建 Meta 应用 <a href="#create-a-meta-app" id="create-a-meta-app"></a>

创建 Meta 应用的步骤如下：

1. 打开 Meta Developer 的[应用控制台](https://developers.facebook.com/apps)，选择 **Create App**（创建应用）。
2. 填写应用详情：
   * 添加 **App name**（应用名称）。
   * 添加 **App contact email**（应用联系邮箱）。
3. 选择符合应用用途的 **Use case**（使用场景）。Webhooks 产品属于 Meta 的 **Business**（业务）套件，因此选择 **Other**（其他），再选择 **Next**（下一步）。
4. 将 **App type**（应用类型）设为 **Business**（业务），再选择 **Next**（下一步）。
5. 如果你有业务资产组合，且已准备好将应用关联到它，请选择该业务资产组合。如果没有或尚未准备好关联，保留 **No business portfolio selected**（未选择业务资产组合）。
6. 选择 **Create app（创建应用）**。
7. 随后打开 **Add products to your app**（为应用添加产品）页面，选择 **Webhooks**。

创建应用、填写隐私政策 URL 等必需字段及添加产品的更多信息，请参阅 Meta 的[创建应用](https://developers.facebook.com/docs/development/create-an-app)文档。

### 将 Meta 应用上线 <a id="taking-a-meta-app-live"></a>

{% hint style="info" %}
**何时将应用切换为 Live（正式）模式**

在 **Development**（开发）模式下，只有在应用中具有角色（管理员、开发者或测试者）的人才能进行身份验证或生成令牌。如果仅连接自己的账户，可将应用保持为开发模式。
{% endhint %}

1. 从左侧菜单选择 **App settings > Basic**（应用设置 > 基本）。
2. 输入 **Privacy Policy URL**（隐私政策 URL），这是将应用切换为 Live（正式）模式前的必填项。
3. 选择 **Save changes**（保存更改）。
4. 如果需要没有应用角色的用户进行身份验证，将 **App Mode**（应用模式）从 **Development**（开发）切换为 **Live**（正式）。

应用模式和切换为 **Live**（正式）模式的更多信息，请参阅[应用模式](https://developers.facebook.com/docs/development/build-and-test/app-modes)和[发布 | 应用类型](https://developers.facebook.com/docs/development/release#app-types)。

### 生成应用访问令牌 <a href="#generate-an-app-access-token" id="generate-an-app-access-token"></a>

然后创建应用访问令牌，供 n8n 凭据和 Webhooks 产品使用：

1. 在单独的选项卡或窗口中打开 [Graph API explorer（Graph API 浏览器）](https://developers.facebook.com/tools/explorer/)。
2. 在 **Access Token**（访问令牌）部分，选择刚创建的 **Meta App**（Meta 应用）。
3. 在 **User or Page**（用户或公共主页）中，选择 **Get App Token**（获取应用令牌）。
4. 选择 **Generate Access Token**（生成访问令牌）。
5. 页面提示你登录并授予访问权限，请按照屏幕提示操作。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>应用不可用</strong></p><p>可能收到应用不可用的警告。将应用上线后，可能需要等待几分钟才能生成访问令牌。</p></div>
6. 复制令牌，填入 n8n 凭据的 **Access Token**（访问令牌）。还需将令牌另存一份，后续配置 Webhooks 时会用到。
7. 保存 n8n 凭据。

生成令牌的更多信息，请参阅 Meta 的[首次请求](https://developers.facebook.com/docs/graph-api/get-started#get-started)说明。

### 配置 Facebook Trigger <a href="#configure-the-facebook-trigger" id="configure-the-facebook-trigger"></a>

取得令牌后，即可配置 Facebook Trigger 节点：

1. 在 Meta 应用中，从顶部导航栏复制 **App ID**（应用 ID）。
2. 在 n8n 中打开 Facebook Trigger 节点。
3. 将 **App ID**（应用 ID）粘贴到 **APP ID** 字段。
4. 选择 **Execute step**（执行步骤），使触发器进入监听状态。
5. 返回打开 Meta 应用 **Webhooks** 产品配置的选项卡或窗口。
6. **Subscribe**（订阅）希望通过 Facebook Trigger 接收通知的对象。对于每个订阅：
   1. 从 n8n 复制 **Webhook URL**，填入 Meta 应用的 **Callback URL**（回调 URL）。
   2. 将上面复制的 **Access Token**（访问令牌）填入 **Verify token**（验证令牌）。
   3. 选择 **Verify and save**（验证并保存）。如果 n8n 触发器未处于监听状态，此步骤会失败。
   4. 某些 webhook 订阅（例如 **User**）会提示你订阅具体事件，请选择需要的事件。
   5. 可从 Meta 发送一些 **Test**（测试）事件，确认配置正常。发送后，请在 n8n 中确认已收到。

更多信息，请参阅 [Facebook Trigger 节点](../trigger-nodes/n8n-nodes-base.facebooktrigger/README.md)文档。

### 可选：添加 App Secret（应用密钥） <a href="#optional-add-an-app-secret" id="optional-add-an-app-secret"></a>

为增强安全性，Meta 建议添加 **App Secret**（应用密钥），通过 `appsecret_proof` 参数为全部 API 调用签名。应用密钥证明是以应用密钥为键，对访问令牌计算得到的 SHA-256 哈希。

生成 App Secret 的步骤如下：

1. 在 Meta 中查看应用时，从左侧菜单选择 **App settings > Basic**（应用设置 > 基本）。
2. 选择 **App secret**（应用密钥）字段旁的 **Show**（显示）。
3. 页面会提示你重新输入 Facebook 账户凭据。完成后，Meta 会显示 App Secret。
4. 选中并复制该值，粘贴到 n8n 凭据的 **App Secret**（应用密钥）。
5. **Save**（保存）n8n 凭据。

更多信息，请参阅 [App Secret 文档](https://developers.facebook.com/docs/facebook-login/security#appsecret)。

### 应用审核 <a href="#app-review" id="app-review"></a>

应用审核要求完成业务验证。

如果应用将由符合以下情况的人员使用，必须经过应用审核：

* 在应用本身中没有角色。
* 在认领该应用的业务中没有角色。

如果全部应用用户都在应用本身中具有角色，则无需应用审核。

应用审核过程中，可能需要为 webhook 订阅申请高级访问权限。

更多信息，请参阅 Meta 的[应用审核](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)和[高级访问权限](https://developers.facebook.com/docs/graph-api/overview/access-levels#advanced-access)文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### 未验证应用数量限制 <a href="#unverified-apps-limit" id="unverified-apps-limit"></a>

对于尚未关联到 Meta 已验证业务账户的应用，Facebook 最多允许你在 15 个应用中具有开发者或管理员角色。

超过此限制时，请参阅[限制 | 创建应用](https://developers.facebook.com/docs/development/create-an-app#limitations)。
