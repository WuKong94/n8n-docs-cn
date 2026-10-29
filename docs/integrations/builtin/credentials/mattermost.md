---
title: Mattermost 凭据
description: Mattermost 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 Mattermost 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: Mattermost 凭据
originalFilePath: integrations/builtin/credentials/mattermost.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/mattermost
url: https://docs.n8n.io/integrations/builtin/credentials/mattermost
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Mattermost 凭据 <a href="#mattermost-credentials" id="mattermost-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [Mattermost](../app-nodes/n8n-nodes-base.mattermost.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token（API 访问令牌）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Mattermost API 文档](https://api.mattermost.com/)。

## 使用 API 访问令牌 <a href="#using-api-access-token" id="using-api-access-token"></a>

配置此凭据需要一个 [Mattermost](https://www.mattermost.com/) 账号，以及：

- 个人 **Access Token**（访问令牌）
- Mattermost 的 **Base URL**（基础 URL）。

设置步骤如下：

1. 在 Mattermost 中进入 **Profile > Security > Personal Access Tokens**（个人资料 > 安全 > 个人访问令牌）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>没有 Personal Access Tokens 选项</strong></p><p>如果未看到 Personal Access Tokens（个人访问令牌）选项，请参阅下方<a href="#enable-personal-access-tokens">启用个人访问令牌</a>中的排查步骤。</p></div>

2. 选择 **Create Token**（创建令牌）。
3. 输入 **Token description**（令牌描述），例如 `n8n integration`。
4. 选择 **Save**（保存）。
5. 复制 **Token ID**（令牌 ID），填入 n8n 凭据的 **Access Token**（访问令牌）。
6. 将 Mattermost 的 URL 填入 **Base URL**（基础 URL）。
7. 默认情况下，n8n 仅在 SSL 证书验证成功时连接。如需在验证失败时仍连接，请开启 **Ignore SSL Issues**（忽略 SSL 问题）。

更多信息，请参阅 Mattermost 的[个人访问令牌文档](https://developers.mattermost.com/integrate/reference/personal-access-token/)。

## 启用个人访问令牌 <a href="#enable-personal-access-tokens" id="enable-personal-access-tokens"></a>

看不到 **Personal Access Tokens**（个人访问令牌）选项，可能有以下两个原因：

- Mattermost 尚未启用个人访问令牌集成。
- 你正尝试以非管理员用户身份生成个人访问令牌，而该用户没有相应权限。

确定根本原因并解决问题的步骤如下：

1. 以管理员身份登录 Mattermost。
2. 进入 **System Console > Integrations > Integration Management**（系统控制台 > 集成 > 集成管理）。
3. 确认 **Enable personal access tokens**（启用个人访问令牌）设为 **true**。如果不是，请修改。
4. 进入 **System Console > User Management > Users**（系统控制台 > 用户管理 > 用户）。
5. 搜索要允许其生成个人访问令牌的用户账户。
6. 选择该用户的 **Actions**（操作）下拉列表，再选择 **Manage roles**（管理角色）。
7. 勾选 **Allow this account to generate personal access tokens**（允许此账户生成个人访问令牌），再选择 **Save**（保存）。

更多信息，请参阅 Mattermost 的[个人访问令牌文档](https://developers.mattermost.com/integrate/reference/personal-access-token/)。
