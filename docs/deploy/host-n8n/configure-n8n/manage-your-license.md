---
title: 许可证密钥
description: 如何激活许可证密钥。
contentType: howto
nodeTitle: 管理许可证
originalFilePath: license-key.md
originalUrl: https://docs.n8n.io/license-key
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 许可证密钥 <a href="#license-key" id="license-key"></a>

要启用某些需要许可的功能，必须先激活许可证。可以通过界面或环境变量进行激活。

## 通过界面添加许可证密钥 <a href="#add-a-license-key-using-the-ui" id="add-a-license-key-using-the-ui"></a>

在 n8n 实例中：

1. 以 **Admin（管理员）**或 **Owner（所有者）**身份登录。
1. 选择 **Settings（设置）** > **Usage and plan（使用情况与套餐）**。
1. 选择 **Enter activation key（输入激活密钥）**。
1. 粘贴许可证密钥。
1. 选择 **Activate（激活）**。

## 通过环境变量添加许可证密钥 <a href="#add-a-license-key-using-an-environment-variables" id="add-a-license-key-using-an-environment-variables"></a>

在 n8n 配置中，将 `N8N_LICENSE_ACTIVATION_KEY` 设置为许可证密钥。如果实例已经激活许可证，此变量不会生效。

更多 n8n 配置说明请参阅[环境变量](basic-configuration.md)。

### 将许可证服务器 IP 地址加入允许列表 <a href="#allowlist-the-license-server-ip-addresses" id="allowlist-the-license-server-ip-addresses"></a>

n8n 使用 Cloudflare 托管许可证服务器。具体 IP 地址可能变化，因此需要将 [Cloudflare 的完整 IP 地址范围](https://www.cloudflare.com/ips/)加入允许列表，确保 n8n 始终能够访问许可证服务器。

## 通过环境变量添加许可证证书 <a id="add-a-license-certificate-using-an-environment-variable"></a>

对于隔离网络等特定使用场景，n8n 可以提供许可证证书，而非许可证密钥。许可证证书是由 n8n 提供的 base64 编码字符串。

在 n8n 配置中，将 `N8N_LICENSE_CERT` 设为从 n8n 收到的字符串：

```bash
N8N_LICENSE_CERT=<base64-encoded-license-string>
```

设置 `N8N_LICENSE_CERT` 或 `N8N_LICENSE_ACTIVATION_KEY` 中的一个，不要同时设置。



## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
