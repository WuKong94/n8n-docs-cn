---
description: 如何使用 API 测试台试用 n8n 公共 REST API。
contentType: howto
nodeTitle: 使用 API 测试台
originalFilePath: api/using-api-playground.md
originalUrl: https://docs.n8n.io/api/using-api-playground
url: https://docs.n8n.io/connect/n8n-api/use-an-api-playground
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 API 测试台 <a href="#using-an-api-playground" id="using-an-api-playground"></a>

文档站提供用于测试调用的 API 测试台。自托管用户还可使用随实例提供的内置测试台。

## 文档测试台 <a href="#documentation-playground" id="documentation-playground"></a>

可在文档站的[端点参考](api-reference.md)中测试 API 调用。需要设置服务器的基础 URL 和实例名称，并添加 API 密钥。

n8n 使用 [Scalar](https://github.com/scalar/scalar) 的开源 API 平台提供此功能。

{% hint style="warning" %}
**暴露的 API 密钥和数据**

使用测试台时，请使用作用域受限的测试 API 密钥和测试数据。测试台的所有调用都会经过 Scalar 代理服务器。
{% endhint %}

{% hint style="warning" %}
**真实数据**

你能够访问正式数据，这便于试用请求。请注意，请求可能更改或删除真实数据。
{% endhint %}


## 内置测试台 <a href="#built-in-playground" id="built-in-playground"></a>

{% hint style="info" %}
**功能可用范围**

API 测试台可用于：

- **自托管：**所有版本。

n8n Cloud 不提供此功能。
{% endhint %}

自托管版本的 n8n API 带有内置 Swagger UI 测试台，提供可尝试请求的交互式文档。访问路径取决于托管配置。

n8n 使用环境变量中设置的值构造路径：

```shell
N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/docs
```

API 版本号为 `1`，未来可能同时提供多个版本。

{% hint style="warning" %}
**真实数据**

在 API 测试台选择 **Authorize**（授权）并输入 API 密钥后，就能够访问正式数据。这便于试用请求，但请注意可能更改或删除真实数据。
{% endhint %}
API 还包含凭据格式的内置文档，可通过 `credentials` 端点获取：

```shell
N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/credentials/schema/{credentialTypeName}
```

{% hint style="info" %}
**如何查找 `credentialTypeName`**

要查找类型，请下载工作流 JSON 并查看内容。例如，Google Drive 节点的 `{credentialTypeName}` 为 `googleDriveOAuth2Api`：
```json
{
    ...,
    "credentials": {
        "googleDriveOAuth2Api": {
        "id": "9",
        "name": "Google Drive"
        }
    }
}
```
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [n8n API](./)
* [身份验证](authentication.md)
* [分页](pagination.md)
* [幂等性](idempotency.md)
* [端点参考](api-reference.md)
