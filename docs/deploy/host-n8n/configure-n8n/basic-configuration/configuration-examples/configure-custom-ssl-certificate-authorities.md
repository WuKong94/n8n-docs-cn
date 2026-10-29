---
title: 配置 n8n 使用自己的证书颁发机构
description: 自定义 n8n 容器，使其在连接服务时支持自签名证书。
contentType: howto
nodeTitle: 配置自定义 SSL 证书颁发机构
originalFilePath: hosting/configuration/configuration-examples/custom-certificate-authority.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-examples/custom-certificate-authority
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 配置 n8n 使用自己的证书颁发机构或自签名证书 <a href="#configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate" id="configure-n8n-to-use-your-own-certificate-authority-or-self-signed-certificate"></a>

可以向 n8n 添加自己的证书颁发机构（CA）或自签名证书。这样可以只信任指定的 SSL 证书，避免信任所有无效证书带来的潜在安全风险。

{% hint style="info" %}
**功能可用范围**

自 n8n 1.42.0 起，支持使用自己的证书颁发机构或自签名证书。
{% endhint %}

要使用此功能，请将证书放入一个文件夹，并将其挂载到容器中的 `/opt/custom-certificates`。映射到 `/opt/custom-certificates` 的外部路径必须允许容器写入。

## Docker <a href="#docker" id="docker"></a>

以下示例假设名为 `pki` 的文件夹包含证书，并位于执行命令的目录中，或与 Docker Compose 文件位于同一目录。

### Docker CLI <a href="#docker-cli" id="docker-cli"></a>
使用 CLI 时，可以在命令行中使用 `-v` 参数：

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -v ./pki:/opt/custom-certificates \
 n8nio/n8n
```

### Docker Compose <a href="#docker-compose" id="docker-compose"></a>

```yaml
name: n8n
services:
    n8n:
        volumes:
            - ./pki:/opt/custom-certificates
        container_name: n8n
        ports:
            - 5678:5678
        image: n8nio/n8n
```

还需要为导入的证书设置正确权限。容器运行后，可以执行以下操作，假设容器名称为 n8n：

```bash
docker exec --user 0 n8n chown -R 1000:1000 /opt/custom-certificates
```

## 自定义信任存储的证书要求 <a href="#certificate-requirements-for-custom-trust-store" id="certificate-requirements-for-custom-trust-store"></a>

支持的证书类型：

- 根 CA 证书：由用于签发其他证书的证书颁发机构提供。信任根 CA 证书后，会接受该 CA 签发的所有证书。
- 自签名证书：由服务器自行创建和签名。信任该证书后，仅接受与此特定服务器的连接。

必须使用 PEM 格式：

- 基于文本，带有 BEGIN/END 标记。
- 支持的文件扩展名：`.pem`、`.crt`、`.cer`。
- 包含公有证书，无需私钥。

例如：

```
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKoK/heBjcOuMA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV
[base64 encoded data]
-----END CERTIFICATE-----
```

系统不接受以下格式：

- DER/二进制格式文件。
- PKCS#7（.p7b）文件。
- PKCS#12（.pfx、.p12）文件。
- 私钥文件。
- 使用前，请将这些格式转换为 PEM。

## 相关资源 <a id="related-resources"></a>

* [配置示例](./)
