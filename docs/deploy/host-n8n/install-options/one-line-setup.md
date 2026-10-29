---
description: 使用一条命令，从命令行安装 n8n。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 一行命令安装 <a href="#one-line-setup" id="one-line-setup"></a>

## 适用人群 <a id="who-this-is-for"></a>

本指南通过一条命令配置全新的 n8n 实例，替代旧的 `npm install n8n`／`npx n8n` 方式，后者从 n8n 3.0 开始不再可用。无论你是否使用过 Docker，这都是快速运行 n8n 的方式。

此方法用于全新安装，不用于修改现有配置：

- **已经通过自己的 Docker Compose 文件自行托管？** 无需切换到此脚本，但可以参考 [Docker Compose 配置流程](./install-using-docker-compose.md)。
- **目前通过 npm 安装 n8n？** 从 n8n 3.0 开始，n8n 仅通过 Docker 分发。现有 npm 安装暂时仍可运行，但新安装和后续升级应改用此方式。

## 开始之前需要准备什么 <a id="what-you-need-before-you-start"></a>

此方法使用 Docker，将 n8n 运行在独立的软件包中，无需自行安装或配置其他内容。如果尚未安装：

- 安装 [Docker](https://docs.docker.com/get-docker/)。它包含安装命令同样需要的 Docker Compose。

按照本指南操作不需要掌握 Docker，只需确保它已安装并在后台运行。

{% hint style="info" %}
一行安装命令明确要求使用 `docker compose` v2 插件，而不是旧的独立 `docker-compose` 可执行程序，并会检查 Docker 守护进程是否运行。如果使用 Podman、Colima 或其他兼容 Docker 的引擎，请安装带 Compose 插件的 `docker` CLI，并将 `DOCKER_HOST` 指向对应引擎的套接字。
{% endhint %}

观看视频指南，了解从安装 Docker 到[启用 n8n Assistant](#optional-turn-on-n8n-assistant)的完整配置过程：

{% embed url="https://www.youtube.com/embed/t5RBVTby9EU" %}

## 运行命令 <a id="run-the-command"></a>

打开终端并运行：

```bash
curl -fsSL https://get.n8n.io | sh
```

该命令会完成以下工作：

1. 检查 Docker 是否已安装且正在运行；如果没有，会说明如何修复。
2. 在当前目录创建名为 `n8n` 的新文件夹，存放全部内容。
3. 写入 n8n 运行所需的配置文件。
4. 下载并启动 n8n。

该命令可以安全地重复运行。如果目标文件夹已配置 n8n，命令只会提示已有安装，不会修改任何内容。

成功运行后的输出示例如下：

```
$ curl -fsSL https://get.n8n.io | sh

✓ Docker found (24.0.6)
✓ Docker Compose found (v2.24.0)
✓ Created ./n8n/compose.yml
✓ Created ./n8n/searxng-settings.yml
✓ Created ./n8n/.env (unique secrets generated)
Pulling images and starting (this can take a few minutes on first run)...
✓ Started n8n 2.32.0 and sandbox services

n8n is running at: http://localhost:5678
Data stored in:    ./n8n (Docker volume: n8n-data)
Config files:      ./n8n/compose.yml, ./n8n/.env

To stop:      docker compose -f ./n8n/compose.yml down
To upgrade:   curl -fsSL https://get.n8n.io | sh -s -- --upgrade
To uninstall: docker compose -f ./n8n/compose.yml down -v   # -v DELETES all n8n data
              rm -rf ./n8n
```

{% hint style="warning" %}
n8n 首次启动需要一些时间。命令会等待服务就绪后再输出 URL。如果页面未立即打开，请稍等片刻后刷新。
{% endhint %}

## 默认包含哪些内容 <a id="whats-included-by-default"></a>

运行命令后，下列内容会自动配置，无需额外安装：

| 组件 | 用途 |
|---|---|
| **n8n** | 工作流编辑器本身，运行地址为 `http://localhost:5678`。 |
| **内置数据库** | 保存工作流、凭据和执行历史。它使用 [SQLite](https://www.sqlite.org/)，这是一种以文件形式存储的轻量数据库。无需另外安装或管理数据库服务器。 |
| **n8n Assistant 支持服务** | 包括安全执行 n8n Assistant 生成代码的沙箱，以及供其查询网络信息的内置搜索工具。这些服务会随 n8n 自动启动，但在你添加 AI 服务商密钥之前，Assistant 本身保持关闭。请参阅[启用 n8n Assistant](#optional-turn-on-n8n-assistant)。 |

如果面向团队或生产环境部署，建议考虑 Postgres 等更稳健的数据库，而不是默认内置数据库。相应配置请参阅[使用 Docker Compose 安装](./install-using-docker-compose.md)。

沙箱同样如此：此配置使用 n8n 自带的沙箱，适合试用；对于生产环境，n8n 当前建议改用 Daytona。配置方法请参阅[设置 n8n Assistant](../configure-n8n/set-up-n8n-assistant.md)。

## 可选：启用 n8n Assistant <a id="optional-turn-on-n8n-assistant"></a>

n8n Assistant 是可选功能，不启用也不影响 n8n 的完整运行。n8n 启动后，最简单的启用方式是在实例的 AI 设置界面中添加模型 API 密钥。如果希望首次登录前就完成配置，可以编辑 `.env`：

1. 打开命令创建的 `.env` 文件，默认位置是 `./n8n/.env`。
2. 在 `N8N_INSTANCE_AI_MODEL_API_KEY` 行中添加 AI 服务商密钥。
3. 重启 n8n：`docker compose -f ./n8n/compose.yml up -d`

完整配置步骤和受支持服务商，请参阅[设置 n8n Assistant](../configure-n8n/set-up-n8n-assistant.md)。

默认情况下，n8n Assistant 使用内置搜索工具进行网络搜索，无需配置。如果希望改用 Brave Search，请将 Brave API 密钥填入 `INSTANCE_AI_BRAVE_SEARCH_API_KEY`，该配置位于同一个 `.env` 文件中。设置后会自动使用。

{% hint style="info" %}
这些服务无需额外开放端口或进行配置。只有 n8n 本身的端口 `5678` 可以从计算机外部访问；其余服务默认保持私有。
{% endhint %}

## 日常命令 <a id="everyday-commands"></a>

| 操作 | 运行命令 |
|---|---|
| 停止 n8n | `docker compose -f ./n8n/compose.yml down` |
| 再次启动 | `docker compose -f ./n8n/compose.yml up -d` |
| 升级到最新版本 | `curl -fsSL https://get.n8n.io \| sh -s -- --upgrade` |
| 移除 n8n 并删除其数据 | 先运行 `docker compose -f ./n8n/compose.yml down -v`，再运行 `rm -rf ./n8n` |

### 升级会修改哪些内容 <a id="what-an-upgrade-changes"></a>

升级命令会将 n8n 和内置沙箱服务都更新到较新版本，并修改 `.env` 中的两行：`N8N_VERSION` 和 `N8N_SANDBOX_VERSION`。数据、密钥和其他设置保持原样。

如果安装时沙箱版本尚未移入 `.env`，你的 `compose.yml` 中仍会指定固定的沙箱镜像标签。首次升级会将这些镜像配置行改为使用 `N8N_SANDBOX_VERSION`，将沙箱运行器地址（`SANDBOX_RUNNER_HTTP_BASE_URL`）从 `http://` 改为 `https://`，并输出提示。`compose.yml` 中的其他内容不会变化，因此你做过的修改会保留。

## 参数：进一步控制安装 <a id="flags-for-more-control"></a>

将这些参数添加到安装命令末尾，可以改变其行为：

| 参数 | 作用 |
|---|---|
| `--version` | 单独使用时，显示脚本版本及将安装的最新 n8n 版本。后面跟版本号时，例如 `--version 2.31.4`，则安装或升级到指定版本。 |
| `--no-start` | 仅准备配置文件，暂不启动 n8n。 |
| `--upgrade` | 将现有安装升级到较新的 n8n 版本及匹配的沙箱服务版本。只更新 `.env` 中的版本配置行；对于旧安装，还会更新 `compose.yml` 中的沙箱镜像配置和运行器地址。请参阅[升级会修改哪些内容](#what-an-upgrade-changes)。数据、设置和其他自定义内容保持原样。 |
| `--help` | 显示全部可用选项。 |

## 不想直接运行互联网上的脚本？ <a id="prefer-not-to-run-a-script-from-the-internet"></a>

可以先下载并阅读脚本，再自行运行：

```bash
curl -fsSL https://get.n8n.io -o get-n8n.sh
less get-n8n.sh   # review it
sh get-n8n.sh
```

## Windows 用户 <a id="windows-users"></a>

一行安装命令需要能够理解 Shell 脚本的终端，标准 Windows 命令提示符和 PowerShell 不具备这一能力。请改用：

- **WSL（适用于 Linux 的 Windows 子系统）**，并启用 Docker Desktop 的 WSL2 集成。
- **Git Bash**（随 [Git for Windows](https://git-scm.com/downloads/win) 安装）在 Docker Desktop 运行时也能执行 POSIX Shell 脚本，但 n8n 尚未对一行安装命令在该环境下进行端到端验证。除非已经确认 Git Bash 适用于你的环境，否则请使用 WSL。

## 相关资源 <a id="related-resources"></a>

* [安装方式](./)
* [使用 Docker Compose 安装](install-using-docker-compose.md)
* [使用 npm 安装](install-with-npm.md)
* [使用 Docker 安装](install-with-docker.md)
* [使用云服务商](use-a-cloud-provider/README.md)



