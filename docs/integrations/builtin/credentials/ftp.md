---
title: FTP 凭据
description: FTP 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 FTP 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: FTP 凭据
originalFilePath: integrations/builtin/credentials/ftp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ftp
url: https://docs.n8n.io/integrations/builtin/credentials/ftp
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# FTP 凭据 <a href="#ftp-credentials" id="ftp-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [FTP](../core-nodes/n8n-nodes-base.ftp.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在 [JSCAPE](https://mft.jscape.com/lp/ftp-server)、[OpenSSH](https://www.openssh.com/) 或 [FileZilla Server](https://filezilla-project.org/) 等文件传输协议（FTP）服务器上创建账户。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- **FTP account**（FTP 账户）：FTP 服务器不支持 SSH 隧道或加密连接时，使用此方式。
- **SFTP account**（SFTP 账户）：FTP 服务器支持 SSH 隧道和加密连接时，使用此方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

文件传输协议（FTP）和安全外壳文件传输协议（SFTP）用于在 FTP/SFTP 客户端与服务器之间直接传输文件。

## 使用 FTP 账户 <a href="#using-ftp-account" id="using-ftp-account"></a>

FTP 服务器不支持 SSH 隧道或加密连接时，使用此方式。

要配置此凭据，需要：

1. 输入 FTP 服务器 **Host**（主机）的名称或 IP 地址。
2. 输入连接使用的 **Port**（端口）号。
3. 输入此凭据用于连接的 **Username**（用户名）。
4. 输入该用户的 **Password（密码）**。

如何获取所需信息，请参阅 FTP 服务器提供商的文档。

## 使用 SFTP 账户 <a href="#using-sftp-account" id="using-sftp-account"></a>

FTP 服务器支持 SSH 隧道和加密连接时，使用此方式。

要配置此凭据，需要：

1. 输入 FTP 服务器 **Host**（主机）的名称或 IP 地址。
2. 输入连接使用的 **Port**（端口）号。
3. 输入此凭据用于连接的 **Username**（用户名）。
4. 输入该用户的 **Password（密码）**。
5. 在 **Private Key**（私钥）中输入用于基于密钥或基于主机的用户身份验证的字符串。
    - 输入 OpenSSH 格式的私钥，通常使用 ssh-keygen 的 `-o` 参数生成，例如：`ssh-keygen -o -a 100 -t ed25519`。
6. 如果 **Private Key**（私钥）已加密，输入用于解密的 **Passphrase**（口令）。
    - 如果 **Private Key**（私钥）未使用口令，将此字段留空。

如何获取所需信息，请参阅 FTP 服务器提供商的文档。
