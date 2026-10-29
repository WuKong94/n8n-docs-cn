---
contentType: tutorial
nodeTitle: 使用 npm 安装
originalFilePath: hosting/installation/npm.md
originalUrl: https://docs.n8n.io/hosting/installation/npm
url: https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


{% hint style="warning" %}
**功能可用范围**

从 n8n 3.0 开始，基于 npm 的安装方式已弃用。
{% endhint %}

{% hint style="info" %}
**不支持 n8n Assistant**

通过 npm 安装时，无法使用 n8n Assistant。
{% endhint %}

npm 是在本地计算机上快速开始使用 n8n 的一种方式。你必须先安装 [Node.js](https://nodejs.org/en/)。n8n 要求 Node.js 版本介于 20.19 和 24.x 之间，包含这两个版本。

## 使用 npx 试用 n8n <a href="#try-n8n-with-npx" id="try-n8n-with-npx"></a>

使用 npx 可以免安装试用 n8n。


在终端中运行：

```bash
npx n8n
```

该命令会下载启动 n8n 所需的全部内容。然后打开 [http://localhost:5678](http://localhost:5678)，即可访问 n8n 并开始构建工作流。

## 使用 npm 全局安装 <a href="#install-globally-with-npm" id="install-globally-with-npm"></a>

要全局安装 n8n，请使用 npm：

```bash
npm install n8n -g
```

要安装或更新到特定 n8n 版本，请使用 `@` 语法指定版本。例如：

```bash
npm install -g n8n@0.126.1
```

安装 `next`：

```bash
npm install -g n8n@next
```

安装后，运行以下命令启动 n8n：

```bash
n8n
# or <a href="#or" id="or"></a>
n8n start
```


### 后续步骤 <a href="#next-steps" id="next-steps"></a>

按照[快速入门](../../../get-started/build-your-first-workflow.md)试用 n8n。

## 更新 <a href="#updating" id="updating"></a>

要将 n8n 实例更新为 `latest` 版本，请运行：

```bash
npm update -g n8n
```

安装 `next` 版本：

```bash
npm install -g n8n@next
```

{% include "../../../reusable-content/.gitbook/includes/self-hosting/installation/tunnel.md" %}

{% hint style="info" %}
**需要 Docker**

隧道使用 cloudflared，并将其作为 Docker 容器运行。即使通过 npm 运行 n8n，也请确保计算机上已安装 [Docker](https://docs.docker.com/get-docker/)。
{% endhint %}

对于 npm 安装，请使用**仅服务**方式。先将 cloudflared 作为独立服务启动，再在本地运行 n8n：

```bash
# Terminal 1: Start the cloudflared tunnel service <a href="#terminal-1-start-the-cloudflared-tunnel-service" id="terminal-1-start-the-cloudflared-tunnel-service"></a>
pnpm --filter n8n-containers services --services cloudflared

# Terminal 2: Start n8n locally <a href="#terminal-2-start-n8n-locally" id="terminal-2-start-n8n-locally"></a>
pnpm dev
```

`services` 命令会启动 cloudflared、获取公共隧道 URL，并将 `.env` 文件写入 `packages/cli/bin/.env`，其中包含 `WEBHOOK_URL` 和 `N8N_PROXY_HOPS=1`。n8n 会在启动时自动读取此 `.env`。

完成后清理：

```bash
pnpm --filter n8n-containers services:clean
```

如果希望使用完整堆栈方式（n8n 和 cloudflared 均在容器中运行），请参阅 [Docker 隧道配置](install-with-docker.md#n8n-with-tunnel)。

## 回退升级 <a href="#reverting-an-upgrade" id="reverting-an-upgrade"></a>

安装希望回退到的旧版本。

如果升级涉及数据库迁移：

1. 检查功能文档和更新记录，确认是否需要手动修改。
1. 在当前版本上运行 `n8n db:revert`，回滚数据库。如果需要撤销多次数据库迁移，必须重复此过程。

## Windows 故障排查 <a href="#windows-troubleshooting" id="windows-troubleshooting"></a>

如果在 Windows 上运行 n8n 时遇到问题，请检查 Node.js 环境设置。按照 Microsoft 的[在 Windows 上安装 NodeJS](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)指南操作。

## 相关资源 <a id="related-resources"></a>

* [安装方式](./)
* [一行命令安装](one-line-setup.md)
* [使用 Docker Compose 安装](install-using-docker-compose.md)
* [使用 Docker 安装](install-with-docker.md)
* [使用云服务商](use-a-cloud-provider/README.md)
