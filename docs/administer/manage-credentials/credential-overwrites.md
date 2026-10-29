---
title: 凭据覆盖
description: 在自托管 n8n 实例上全局设置凭据数据，让用户无需查看或输入客户端密钥即可完成身份验证。
contentType: howto
nodeTitle: 凭据覆盖
originalFilePath: hosting/configuration/credential-overwrites.md
originalUrl: https://docs.n8n.io/hosting/configuration/credential-overwrites
url: https://docs.n8n.io/administer/manage-credentials/credential-overwrites
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 凭据覆盖 <a href="#credential-overwrites" id="credential-overwrites"></a>

凭据覆盖允许全局设置凭据数据。用户看不到这些数据，n8n 会在后台自动使用，例如通过 Connect（连接）按钮启用 OAuth 登录，而不暴露客户端密钥。

编辑器界面默认隐藏所有被覆盖的字段，用户可通过凭据上的 Connect（连接）按钮完成 OAuth 身份验证。

配置凭据覆盖所需的环境变量，请参阅[凭据环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials.md)。

观看凭据覆盖教程，包含如何[使用 REST API](#using-the-rest-api)，配合[现成工作流模板](https://n8n.io/workflows/17052-register-credential-overwrites-on-startup-with-the-n8n-api/)完成设置：

{% embed url="https://www.youtube.com/embed/VtCbCdKrqAE" %}

## 使用环境变量 <a href="#using-environment-variables" id="using-environment-variables"></a>

将 `CREDENTIALS_OVERWRITE_DATA` 设为 `{ CREDENTIAL_NAME: { PARAMETER: VALUE }}`。

{% hint style="warning" %}
不建议使用此方式。n8n 不保护环境变量，因此数据可能泄露给用户。
{% endhint %}

## 使用 REST API <a href="#using-the-rest-api" id="using-the-rest-api"></a>

建议通过自定义 REST 端点加载数据。

1. 将 `CREDENTIALS_OVERWRITE_ENDPOINT` 设为端点应提供服务的路径：<br>

    ```sh
    export CREDENTIALS_OVERWRITE_ENDPOINT=send-credentials
    ```

    可选：设置 `CREDENTIALS_OVERWRITE_ENDPOINT_AUTH_TOKEN`，要求访问端点时提供 Bearer 令牌。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>未设置身份验证令牌时，出于安全原因，端点只能调用一次。</p></div>

2. 准备包含待覆盖凭据的 JSON 文件。例如，用于 Asana 和 GitHub 的 `oauth-credentials.json`：

    ```json
    {
        "asanaOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        },
        "githubOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        }
    }
    ```

3. 将文件发送到 n8n 实例：

    ```sh
    curl -H "Content-Type: application/json" --data @oauth-credentials.json http://localhost:5678/send-credentials
    ```

    如果 `CREDENTIALS_OVERWRITE_ENDPOINT_AUTH_TOKEN` 设为 `secure-token`：

    ```sh
    curl -H "Content-Type: application/json" -H "Authorization: Bearer secure-token" --data @oauth-credentials.json http://localhost:5678/send-credentials
    ```

{% hint style="info" %}
凭据可以扩展其他凭据。例如，`googleSheetsOAuth2Api` 扩展 `googleOAuth2Api`。可以在父级（`googleOAuth2Api`）上设置参数，所有子凭据都会使用。
{% endhint %}

## 显示 OAuth 权限范围字段 <a id="show-oauth-scope-fields"></a>

存在托管 OAuth 时，n8n 默认隐藏权限范围字段。要让用户为指定托管 OAuth 凭据类型配置范围，请将 `N8N_MANAGED_OAUTH_SHOW_SCOPES` 设为以逗号分隔的列表：

```sh
export N8N_MANAGED_OAUTH_SHOW_SCOPES=googleOAuth2Api
```

此设置仅作用于列出的凭据类型，不作用于扩展这些类型的其他凭据类型。

{% hint style="warning" %}
允许用户自行设置权限范围，可能影响已验证的 OAuth 应用。Google 等许多提供商要求在应用验证时，声明并说明应用请求的每个范围。如果用户添加未声明的范围，提供商可能暂停或封禁应用。只有用户添加范围不会影响应用验证状态的凭据类型，才应启用此设置。
{% endhint %}

## 持久化 <a href="#persistence" id="persistence"></a>

要将凭据覆盖保存在数据库，并在多实例或队列模式下传播到全部工作进程，请启用：

```sh
export CREDENTIALS_OVERWRITE_PERSISTENCE=true
```

启用后，n8n 将加密的覆盖数据存入 `settings` 表，并广播 `reload-overwrite-credentials` 事件，让工作进程重新加载最新值。禁用时，覆盖数据仅留在加载它的进程内存中，不会传播给工作进程，也不会在重启后保留。

## 相关资源 <a id="related-resources"></a>

* [管理凭据](./)
* [安全共享凭据](share-credentials-securely.md)
* [最终用户凭据](end-user-credentials.md)
* [使用外部密钥存储](use-external-secret-stores.md)
