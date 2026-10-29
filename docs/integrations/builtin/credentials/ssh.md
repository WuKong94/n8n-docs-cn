---
title: SSH 凭据
description: SSH 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 SSH 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: SSH 凭据
originalFilePath: integrations/builtin/credentials/ssh.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ssh
url: https://docs.n8n.io/integrations/builtin/credentials/ssh
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# SSH 凭据 <a href="#ssh-credentials" id="ssh-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [SSH](../core-nodes/n8n-nodes-base.ssh.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建启用了 SSH 的远程服务器。
- 创建可通过以下任一方式使用 `ssh` 登录服务器的用户账户：
    - 该账户自己的[密码](#using-password)
    - SSH [私钥](#using-private-key)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [Password（密码）](#using-password)：用户账户可使用自己的密码通过 `ssh` 登录服务器时，使用此方式。
- [Private key（私钥）](#using-private-key)：用户账户使用 SSH 密钥访问服务器或服务时，使用此方式。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

安全外壳（SSH）协议是一种通过网络安全发送命令的方法。SSH 设置示例，请参阅[使用 SSH 连接到 GitHub](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)。


## 使用密码 <a href="#using-password" id="using-password"></a>

用户账户可使用自己的密码通过 `ssh` 登录服务器时，使用此方式。

要配置此凭据，需要：

1. 将要连接的服务器 IP 地址填入 **Host**（主机）。
2. 输入连接使用的 **Port**（端口）。SSH 默认使用端口 `22`。
3. 输入在服务器上具有 `ssh` 访问权限的用户账户的 **Username**（用户名）。
4. 输入该用户账户的 **Password**（密码）。

## 使用私钥 <a href="#using-private-key" id="using-private-key"></a>

用户账户使用 SSH 密钥访问服务器或服务时，使用此方式。

要配置此凭据，需要：

1. 将要连接的服务器 IP 地址填入 **Host**（主机）。
2. 输入连接使用的 **Port**（端口）。SSH 默认使用端口 `22`。
3. 输入生成私钥的账户的 **Username**（用户名）。
4. 输入 SSH **Private Key**（私钥）的完整内容。
5. 如果为 **Private Key**（私钥）创建了 **Passphrase**（口令），请填入口令。
    - 如果未为密钥创建口令，将此字段留空。
