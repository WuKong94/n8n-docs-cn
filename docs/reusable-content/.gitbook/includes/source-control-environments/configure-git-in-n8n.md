---
title: 在 n8n 中配置 Git
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

1. 前往 **Settings**（设置）> **Environments**（环境）。
1. 选择连接方式：
	- **SSH**：在 **Git repository URL**（Git 仓库 URL）中填写仓库的 SSH URL（例如 `git@github.com:username/repo.git`）。
	- **HTTPS**：在 **Git repository URL**（Git 仓库 URL）中填写仓库的 HTTPS URL（例如 `https://github.com/username/repo.git`）。
1. 根据连接方式配置身份验证：
	- **SSH**：n8n 支持 ED25519 和 RSA 公钥算法，默认为 ED25519。如果 Git 主机要求 RSA，请在 **SSH Key**（SSH 密钥）下选择 **RSA**。复制 SSH 密钥。
	- **HTTPS**：填写凭据：
		- **Username**（用户名）：Git 托管平台的用户名。
		- **Token**（令牌）：Git 托管平台的个人访问令牌（PAT）。
