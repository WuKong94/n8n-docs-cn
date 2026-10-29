---
title: 部署环境变量
contentType: reference
hide:
- toc
- tags
nodeTitle: 部署
originalFilePath: hosting/configuration/environment-variables/deployment.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/deployment
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment
description: 通过环境变量配置自托管 n8n 实例的部署选项和访问方式。
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
tags:
- environment variables
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 部署 <a id="deployment"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

本页列出自托管 n8n 实例的部署配置选项，包括访问 URL、模板启用、自定义加密和服务器信息。

{% hint style="info" %}
**代理变量的优先级**

n8n 使用的 [`proxy-from-env`](https://www.npmjs.com/package/proxy-from-env) 包会为以 `_PROXY` 结尾的代理环境变量规定优先顺序。特别是大小写变量同时存在时，小写形式，例如 `http_proxy`，优先于大写形式，例如 `HTTP_PROXY`。

代理环境变量的更多说明，请参阅[此包说明中的环境变量部分](https://www.npmjs.com/package/proxy-from-env#environment-variables)。
{% endhint %}

| 变量 | 类型 | 默认值 | 说明 |
| -------------------------------------- | ---------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HTTP_PROXY` | String | - | 用于代理未加密 HTTP 请求的 URL。设置后，n8n 会通过此代理转发节点发出的所有未加密 HTTP 流量。 |
| `HTTPS_PROXY` | String | - | 用于代理 TLS/SSL 加密 HTTP 请求的 URL。设置后，n8n 会通过此代理转发节点发出的所有 TLS/SSL 加密 HTTP 流量。 |
| `ALL_PROXY` | String | - | 用于代理未加密和加密 HTTP 请求的 URL。未设置更具体的变量 `HTTP_PROXY` 或 `HTTPS_PROXY` 时，n8n 使用此值。 |
| `NO_PROXY` | String | - | 不经过代理的主机名或 URL 列表，以逗号分隔。使用 `HTTP_PROXY`、`HTTPS_PROXY` 或 `ALL_PROXY` 时，n8n 会直接连接此处列出的 URL 或主机名，不使用代理。 |
| `N8N_ENFORCE_GLOBAL_USER_AGENT` | Boolean | `false` | 设为 `true` 时，n8n 会将所有出站 HTTP 请求中默认仅含 `n8n` 的 User-Agent 字符串，替换为符合 RFC 的值 `Mozilla/5.0 (compatible; n8n/<version>; +https://n8n.io/)`。启用后可避免 Web 应用防火墙阻止 n8n 请求。 |
| `N8N_GLOBAL_USER_AGENT_VALUE` | String | - | 所有出站 HTTP 请求使用的自定义 User-Agent 字符串，覆盖 `N8N_ENFORCE_GLOBAL_USER_AGENT` 设置的符合 RFC 的默认值。不希望向上游服务器透露 n8n 版本时，可使用此设置。 |
| `N8N_EDITOR_BASE_URL` | String | - | 用户访问编辑器的公开 URL，也用于 n8n 发送的邮件及基于 SAML 的身份验证重定向 URL。 |
| `N8N_DISABLE_UI` | Boolean | `false` | 设为 `true` 可禁用用户界面。 |
| `N8N_PREVIEW_MODE` | Boolean | `false` | 设为 `true` 可在预览模式下运行。 |
| `N8N_CANVAS_ONLY` | Boolean | `false` | 设为 `true`，以[仅画布模式](../../deploy-n8n-in-canvas-only-mode.md)运行 n8n，在查看单个工作流时隐藏顶部区域、侧边栏和浮层元素。自 n8n 2.15.0 起提供。 |
| `N8N_TEMPLATES_ENABLED` | Boolean | `true` | 是否启用[工作流模板](#user-content-fn-1)[^1]，true 表示启用，false 表示禁用。 |
| `N8N_TEMPLATES_HOST` | String | `https://api.n8n.io` | 创建自己的工作流模板库时修改此值。自建模板库的 API 必须提供与 n8n 相同的端点及响应结构。更多信息请参阅[工作流模板](../../../../../build/ways-of-building-workflows/use-templates.md)。 |
| `N8N_ENCRYPTION_KEY` | String | n8n 生成的随机密钥 | 提供用于加密 n8n 数据库中凭据的自定义密钥。n8n 默认在首次启动时生成随机密钥。 |
| `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` | Boolean | `false` | 在所有实例，包括主实例和工作进程上设为 `true`，启用[加密密钥轮换](../../security/rotate-encryption-keys.md)。这是单向变更，请先完整备份数据库。 |
| `N8N_ENV_FEAT_OAUTH2_JWE` | Boolean | `false` | 在所有实例，包括主实例和工作进程上设为 `true`，启用 [OAuth 2.0 凭据的 JWE 令牌解密](../../security/decrypt-oauth-20-tokens-with-jwe.md)。此功能处于预览阶段。 |
| `N8N_ENV_FEAT_TOKEN_EXCHANGE` | Boolean | `false` | 设为 `true`，启用[嵌入合作伙伴的令牌交换](../../../deploy-as-an-oem-integration/set-up-token-exchange.md)。此功能处于预览阶段。 |
| `N8N_OAUTH_JWE_JWKS_PER_MINUTE` | Number | `60` | 公开 JWKS 端点 `/rest/.well-known/jwks.json` 的每 IP 速率限制，此端点用于 [OAuth 2.0 凭据的 JWE 令牌解密](../../security/decrypt-oauth-20-tokens-with-jwe.md)。 |
| `N8N_MCP_BASE_URL` | String | - | 当实例级 MCP 服务器的公开基础 URL 与实例基础 URL 不同时，指定 MCP 客户端访问的公开基础 URL。适用于通过独立主机名提供 MCP 服务器的部署，例如在同一实例前使用 `https://n8n-mcp.example.com`。设置后，n8n 会公布此 MCP 地址，并在 OAuth 身份验证时同时接受此 URL 和根据实例基础 URL 推导出的 URL。不影响编辑器或 Webhook URL。自 n8n 2.31.0 起提供。 |
| `N8N_MCP_SERVER_RATE_LIMIT` | Number | `100` | 每个 IP 在每五分钟内对 MCP 服务器端点 `/mcp-server/http` 发出的最大请求数。 |
| `N8N_OAUTH_SERVER_REGISTER_RATE_LIMIT` | Number | `10` | 每个 IP 在每五分钟内对 OAuth 服务器客户端注册端点 `/oauth/register` 和 `/mcp-oauth/register` 发出的最大请求数。 |
| `N8N_OAUTH_SERVER_AUTHORIZE_RATE_LIMIT` | Number | `50` | 每个 IP 在每五分钟内对 OAuth 服务器授权端点 `/oauth/authorize` 和 `/mcp-oauth/authorize` 发出的最大请求数。 |
| `N8N_OAUTH_SERVER_TOKEN_RATE_LIMIT` | Number | `20` | 每个 IP 在每五分钟内对 OAuth 服务器令牌端点 `/oauth/token` 和 `/mcp-oauth/token` 发出的最大请求数。 |
| `N8N_OAUTH_SERVER_REVOKE_RATE_LIMIT` | Number | `30` | 每个 IP 在每五分钟内对 OAuth 服务器令牌撤销端点 `/oauth/revoke` 和 `/mcp-oauth/revoke` 发出的最大请求数。 |
| `N8N_USER_FOLDER` | String | `user-folder` | 指定 n8n 创建 `.n8n` 文件夹的父路径。该目录存储数据库文件、加密密钥等用户专属数据。 |
| `N8N_PATH` | String | `/` | n8n 的部署路径。将 `N8N_PATH` 与反向代理结合可能导致文件夹导航问题。请使用子域名，例如 `n8n.example.com`，或在不使用反向代理时使用 `N8N_PATH`。 |
| `N8N_HOST` | String | `localhost` | 运行 n8n 的主机名。 |
| `N8N_PORT` | Number | `5678` | 运行 n8n 的 HTTP 端口。 |
| `N8N_LISTEN_ADDRESS` | String | `::` | n8n 应监听的 IP 地址。 |
| `N8N_PROTOCOL` | 枚举字符串： `http`, `https` | `http` | 访问 n8n 所用的协议。 |
| `N8N_SSL_KEY` | String | - | HTTPS 协议所用的 SSL 密钥。 |
| `N8N_SSL_CERT` | String | - | HTTPS 协议所用的 SSL 证书。 |
| `N8N_PERSONALIZATION_ENABLED` | Boolean | `true` | 是否向用户提出个性化问题，并据此自定义 n8n。 |
| `N8N_VERSION_NOTIFICATIONS_ENABLED` | Boolean | `true` | 启用后，n8n 会发送新版本和安全更新通知。 |
| `N8N_VERSION_NOTIFICATIONS_ENDPOINT` | String | `https://api.n8n.io/versions/` | 获取版本信息的端点。 |
| `N8N_VERSION_NOTIFICATIONS_INFO_URL` | String | `https://docs.n8n.io/getting-started/installation/updating.html` | 新版本面板中用于查看详细信息的 URL。 |
| `N8N_DIAGNOSTICS_ENABLED` | Boolean | `true` | 是否与 n8n 共享选定的匿名[遥测数据](../../../../../privacy-and-security/README.md)。请注意，设为 `false` 时，无法在 Code 节点中启用 Ask AI。 |
| `N8N_DIAGNOSTICS_CONFIG_FRONTEND` | String | `1zPn9bgWPzlQc0p8Gj1uiK6DOTn;https://telemetry.n8n.io` | 前端遥测配置。 |
| `N8N_DIAGNOSTICS_CONFIG_BACKEND` | String | `1zPn7YoGC3ZXE9zLeTKLuQCB4F6;https://telemetry.n8n.io/v1/batch` | 后端遥测配置。 |
| `N8N_PUSH_BACKEND` | String | `websocket` | 选择 n8n 后端通过服务器发送事件 `sse` 还是 WebSocket `websocket`，将变化推送到界面。 |
| `VUE_APP_URL_BASE_API` | String | `http://localhost:5678/` | 手动构建 `n8n-editor-ui` 包时，用于设置前端访问后端 API 的方式。参阅[配置 Base URL](../configuration-examples/configure-the-base-url.md)。 |
| `N8N_HIRING_BANNER_ENABLED` | Boolean | `true` | 是否在控制台显示 n8n 招聘横幅，true 表示显示，false 表示不显示。 |
| `N8N_PUBLIC_API_SWAGGERUI_DISABLED` | Boolean | `false` | 是否禁用 Swagger UI，即 API 调试界面，true 表示禁用，false 表示不禁用。 |
| `N8N_PUBLIC_API_DISABLED` | Boolean | `false` | 是否禁用公共 API，true 表示禁用，false 表示不禁用。 |
| `N8N_PUBLIC_API_ENDPOINT` | String | `api` | 公共 API 端点路径。 |
| `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` | Number | `30` | n8n 进程退出前等待组件关闭的时长，单位为秒。 |
| `N8N_DEV_RELOAD` | Boolean | `false` | 开发 n8n 源码时，设为 `true`，可在源文件变化时自动重新加载或重启应用。 |
| `N8N_REINSTALL_MISSING_PACKAGES` | Boolean | `false` | 设为 `true` 时，n8n 会自动尝试重新安装缺失的包。 |
| `N8N_TUNNEL_SUBDOMAIN` | String | - | 指定 n8n 隧道的子域名。未设置时，n8n 会生成随机子域名。 |
| `N8N_PROXY_HOPS` | Number | 0 | n8n 前方反向代理的数量。 |

<a id="user-content-fn-1"></a>
[^1]: n8n 模板是 n8n 和社区成员设计的预构建工作流，可以导入到自己的 n8n 实例中。使用模板时，可能需要填写凭据并调整配置，以满足实际需求。

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
