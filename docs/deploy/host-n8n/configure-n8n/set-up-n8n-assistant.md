---
description: 使用环境变量，在自托管 n8n 上设置 n8n Assistant。
status: preview
tags:
- tag: preview
  primary: true
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
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
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 设置 n8n Assistant <a id="set-up-n8n-assistant"></a>

{% hint style="info" %}
**功能可用范围**

n8n Assistant 可用于：

- **n8n Cloud：**Starter、Pro。
- **自托管：**Community、Registered Community、Business。

目前尚未适配 n8n Cloud Enterprise 或自托管 Enterprise。Enterprise 客户可联系客户成功经理，了解预览访问权限。
{% endhint %}

{% hint style="info" %}
**预览状态**

n8n Assistant 处于预览阶段，可能出错，开发期间行为也可能更改。用于生产环境之前，请始终审核生成的工作流。
{% endhint %}

## n8n Assistant 需要哪些组件 <a id="what-n8n-assistant-needs"></a>

每个自托管 n8n Assistant 配置都需要考虑三个部分：

* **模型提供商：**Anthropic、OpenAI 或 OpenRouter 的 API 密钥。
* **沙箱，必需：**n8n Assistant 运行代码的隔离环境。
* **搜索提供商，可选：**让 n8n Assistant 能在网上查找信息。

沙箱的提供方式是主要决策。n8n 自带的沙箱（`n8n-sandbox`）适合本地开发和测试，[一行命令安装](../install-options/one-line-setup.md)和 [Docker Compose 指南](../install-options/install-using-docker-compose.md)会自动设置它。生产环境请改用 Daytona。

请根据 n8n 安装方式和运行环境，在下文[选择配置方案](#pick-your-setup)。

### 开始之前 <a id="before-you-start"></a>

请确保具备：

* 配置 n8n 实例环境变量的权限。
* 较新的 n8n 版本。运行最新稳定版或更新版本；较旧版本可能有效，但越新越好。
* 受支持 LLM 提供商的 API 密钥：Anthropic、OpenAI 或 OpenRouter。

## 选择配置方案 <a id="pick-your-setup"></a>

| 方案 | 使用场景 | 沙箱托管方 | 最适合 |
| --- | --- | --- | --- |
| [1. 沙箱已在运行](#setup-1-already-running-the-sandbox-recommended-for-local-development) | 已通过一行命令或 Docker Compose 指南安装。 | 你自己，已完成 | 本地开发和测试 |
| [2. 手动自托管沙箱](#setup-2-self-host-the-sandbox-manually-advanced) | 以其他方式运行 n8n，希望自托管沙箱，而非使用 Daytona。 | 你自己 | 本地开发和测试 |
| [3. Daytona，托管沙箱](#setup-3-daytona-managed-sandbox-recommended-for-production) | 部署到生产环境，或不想自己运行沙箱容器。 | Daytona | 生产环境 |

### 方案 1：沙箱已在运行，本地开发推荐 <a id="setup-1-already-running-the-sandbox-recommended-for-local-development"></a>

如果通过[一行命令](../install-options/one-line-setup.md)安装 n8n，或按 [Docker Compose 指南](../install-options/install-using-docker-compose.md)手动部署，沙箱及使用内置 SearXNG 的搜索服务都已经运行，只需补充模型密钥。

**所需内容：**仅需 LLM API 密钥。

**步骤：**

最快的方法是打开编辑器，前往实例 AI 设置，在其中添加模型密钥。如果更喜欢使用 `.env`，请按以下步骤操作。

1. 在 `.env` 中添加模型密钥：

   ```bash
   N8N_INSTANCE_AI_MODEL_API_KEY=sk-ant-xxx
   ```

2. 重启 n8n。
3. 打开编辑器，确认 n8n Assistant 显示并能响应。

`N8N_INSTANCE_AI_MODEL` 默认为 `anthropic/claude-opus-4-8`。只有希望使用其他模型时，才需要显式设置，参阅[选择模型提供商](#choose-a-model-provider)。

更喜欢看视频？此[视频指南](https://go.n8n.io/RZZWq1)涵盖从一行命令安装，到在编辑器中选择提供商和模型的完整过程。

### 方案 2：手动自托管沙箱，进阶 <a id="setup-2-self-host-the-sandbox-manually-advanced"></a>

如果没有采用一行命令或 Docker Compose 指南配置 n8n，并希望自己运行沙箱，而非交给 Daytona，请使用此方案。

{% hint style="warning" %}
这意味着需要自行托管两个额外容器：沙箱 API 和具有特权的 Docker-in-Docker 运行器，并在两者之间配置双向 TLS。与方案 1 一样，此方案使用 `n8n-sandbox`，最适合本地开发和测试。生产环境请改用 [Daytona](#setup-3-daytona-managed-sandbox-recommended-for-production)。
{% endhint %}

**所需内容：**

* n8n Sandbox Service 正在运行，且 n8n 可以访问。完整组件栈（`sandbox-certs`、`sandbox-api`、`sandbox-runner-1`）及其密钥，请参阅 [Docker Compose 指南](../install-options/install-using-docker-compose.md)。
* LLM API 密钥。

**步骤：**

1. 部署沙箱组件栈，参阅上方链接的 Docker Compose 指南。
2. 让 n8n 指向该沙箱：

   ```bash
   N8N_INSTANCE_AI_SANDBOX_ENABLED=true
   N8N_INSTANCE_AI_SANDBOX_PROVIDER=n8n-sandbox
   N8N_SANDBOX_SERVICE_URL=http://sandbox-api:8080
   N8N_SANDBOX_SERVICE_API_KEY=my-sandbox-api-key
   ```

   | 变量 | 说明 |
   | --- | --- |
   | `N8N_INSTANCE_AI_SANDBOX_ENABLED` | 设为 `true`。 |
   | `N8N_INSTANCE_AI_SANDBOX_PROVIDER` | 设为 `n8n-sandbox`。 |
   | `N8N_SANDBOX_SERVICE_URL` | n8n 可访问的沙箱 API URL。 |
   | `N8N_SANDBOX_SERVICE_API_KEY` | 必须与 API 容器上的 `SANDBOX_API_KEYS` 一致。 |

3. 添加模型密钥，参阅[选择模型提供商](#choose-a-model-provider)，然后重启 n8n。

**验证：**

```bash
curl http://<sandbox-api-host>:8080/healthz
```

预期响应：`{"status":"ok"}`

**说明：**

* 将 `my-sandbox-api-key` 替换为你自己的密钥，并在 API 和运行器容器上设置相互匹配的注册令牌和运行器密钥。完整变量列表及其关联方式，请参阅 [Docker Compose 指南](../install-options/install-using-docker-compose.md)。
* `N8N_SANDBOX_SERVICE_API_KEY` 必须与沙箱 API 容器上 `SANDBOX_API_KEYS` 中的某个值一致。
* 运行器会在首次使用时拉取沙箱镜像。对于隔离网络环境，请预先将该镜像加载到运行器内部的 Docker。
* 主机名很重要。证书签发给 `sandbox-api` 和 `sandbox-runner-<n>`，因此请保留这些服务名称，或重新生成具有匹配 SAN 的证书。

### 方案 3：Daytona，托管沙箱，生产环境推荐 <a id="setup-3-daytona-managed-sandbox-recommended-for-production"></a>

Daytona 按需创建沙箱，无需自行托管容器。这是 n8n 推荐用于生产环境的沙箱提供商。

**所需内容：**Daytona 账号和 API 密钥，以及 LLM API 密钥。

**步骤：**

1. 在 n8n 实例上设置以下环境变量：

   ```bash
   # Enable the module and choose a model
   N8N_ENABLED_MODULES=instance-ai
   N8N_INSTANCE_AI_MODEL=anthropic/claude-opus-4-8
   N8N_INSTANCE_AI_MODEL_API_KEY=sk-ant-xxx

   # Sandbox, required
   N8N_INSTANCE_AI_SANDBOX_ENABLED=true
   N8N_INSTANCE_AI_SANDBOX_PROVIDER=daytona
   N8N_INSTANCE_AI_SANDBOX_IMAGE=daytonaio/sandbox:0.5.3-slim

   # Daytona
   DAYTONA_API_URL=https://app.daytona.io/api
   DAYTONA_API_KEY=dtn_xxx

   # Web search, recommended
   INSTANCE_AI_BRAVE_SEARCH_API_KEY=BSA-xxx
   ```

   | 变量 | 说明 |
   | --- | --- |
   | `N8N_ENABLED_MODULES` | 必须包含 `instance-ai` 才能启用模块。 |
   | `N8N_INSTANCE_AI_MODEL` | 以 `provider/model` 格式选择 LLM。已有默认值（`anthropic/claude-opus-4-8`），仅在希望使用其他模型时显式设置。 |
   | `N8N_INSTANCE_AI_MODEL_API_KEY` | 所选提供商的 API 密钥。 |
   | `N8N_INSTANCE_AI_SANDBOX_ENABLED` | 设为 `true`，n8n Assistant 必须使用沙箱。 |
   | `N8N_INSTANCE_AI_SANDBOX_PROVIDER` | 设为 `daytona`。 |
   | `N8N_INSTANCE_AI_SANDBOX_IMAGE` | Daytona 沙箱的基础容器镜像。 |
   | `DAYTONA_API_URL` | Daytona API 端点。 |
   | `DAYTONA_API_KEY` | 你的 Daytona API 密钥。 |
   | `INSTANCE_AI_BRAVE_SEARCH_API_KEY` | 用于网页搜索的 Brave Search API 密钥。此变量有意不使用 `N8N_` 前缀。 |

   Docker Compose 示例：

   ```yaml
   services:
     n8n:
       image: n8nio/n8n
       environment:
         N8N_ENABLED_MODULES: instance-ai
         N8N_INSTANCE_AI_MODEL: anthropic/claude-opus-4-8
         N8N_INSTANCE_AI_MODEL_API_KEY: sk-ant-xxx
         N8N_INSTANCE_AI_SANDBOX_ENABLED: 'true'
         N8N_INSTANCE_AI_SANDBOX_PROVIDER: daytona
         N8N_INSTANCE_AI_SANDBOX_IMAGE: daytonaio/sandbox:0.5.3-slim
         DAYTONA_API_URL: https://app.daytona.io/api
         DAYTONA_API_KEY: dtn_xxx
         INSTANCE_AI_BRAVE_SEARCH_API_KEY: BSA-xxx
   ```

2. 重启 n8n，打开编辑器，确认 n8n Assistant 显示并能响应。

**可选：调整沙箱生命周期**

```bash
N8N_INSTANCE_AI_SANDBOX_AUTO_STOP_MINUTES=15
N8N_INSTANCE_AI_SANDBOX_AUTO_ARCHIVE_MINUTES=60
N8N_INSTANCE_AI_SANDBOX_AUTO_DELETE_MINUTES=10080
```

{% hint style="info" %}
默认情况下，Daytona 在沙箱空闲 15 分钟后停止它，停止一小时后归档，七天后删除。可以通过上述变量更改。
{% endhint %}

## 选择模型提供商 <a id="choose-a-model-provider"></a>

`N8N_INSTANCE_AI_MODEL` 使用以下格式：

```
provider/model
```

支持的提供商：

* `anthropic`
* `openai`
* `openrouter`

对于托管提供商，可以从 `anthropic/claude-opus-4-8` 或 `openai/gpt-5.5` 开始。

示例：

```bash
# Anthropic
N8N_INSTANCE_AI_MODEL=anthropic/claude-opus-4-8

# OpenAI
N8N_INSTANCE_AI_MODEL=openai/gpt-5.5

# OpenRouter
N8N_INSTANCE_AI_MODEL=openrouter/deepseek/deepseek-v4-pro
```

将 `N8N_INSTANCE_AI_MODEL_API_KEY` 设为所选提供商的 API 密钥。

如果未设置 `N8N_INSTANCE_AI_MODEL_API_KEY`，n8n 会回退使用提供商的标准环境变量：

* `ANTHROPIC_API_KEY`
* `OPENAI_API_KEY`
* `OPENROUTER_API_KEY`

### 使用本地或自定义的 OpenAI 兼容端点 <a id="use-a-local-or-custom-openai-compatible-endpoint"></a>

要使用本地或自定义的 OpenAI 兼容端点，请设置 `N8N_INSTANCE_AI_MODEL_URL`。

```bash
N8N_INSTANCE_AI_MODEL_URL=http://localhost:1234/v1
N8N_INSTANCE_AI_MODEL_API_KEY=optional-key
```

部分本地服务器不要求 API 密钥。

## 启用网页搜索 <a id="enable-web-search"></a>

网页搜索让 n8n Assistant 能在网上查找信息。这是可选功能，未启用也不影响 n8n Assistant 的其他功能。

如果使用[一行命令安装](../install-options/one-line-setup.md)或 [Docker Compose 指南](../install-options/install-using-docker-compose.md)，SearXNG 已包含在组件中并运行，无需额外设置，除非希望改用 Brave Search。

```bash
# Brave Search
INSTANCE_AI_BRAVE_SEARCH_API_KEY=BSA-xxx

# SearXNG
N8N_INSTANCE_AI_SEARXNG_URL=http://searxng:8080
```

{% hint style="info" %}
`INSTANCE_AI_BRAVE_SEARCH_API_KEY` 有意不使用 `N8N_` 前缀，请严格按所示变量名使用。
{% endhint %}

如果两者都配置，Brave Search 优先于 SearXNG。免费或无需身份验证的提供商，包括 SearXNG，可能遇到速率限制，使用 Brave Search 可获得更可靠的配置。

如果实例管理员在 AI 设置界面中选择了 Brave Search 或 SearXNG 凭据，n8n 会使用该凭据，而非这些环境变量。

## 启用实例上下文 <a id="enable-instance-context"></a>

{% hint style="info" %}
**功能可用范围**

本文介绍的共享实例上下文开关和活动日志保留设置，自 n8n 2.41.0 起提供。
{% endhint %}

{% hint style="info" %}
**预览状态**

实例上下文处于预览阶段，未来版本可能更改。n8n 尚未为所有实例启用实例上下文，请避免在生产工作中依赖此功能。
{% endhint %}

实例上下文为 n8n Assistant 提供发起对话所在项目的简短摘要，包括工作流、近期更改和执行结果。这是可选功能，未启用也不影响 n8n Assistant 的其他功能。参阅 [n8n Assistant 了解实例的哪些信息](../../../build/ways-of-building-workflows/n8n-assistant.md#what-n8n-assistant-knows-about-your-instance)。

由 `114_instance_activity_context` PostHog 开关控制。n8n 按实例评估此开关，而非按用户。同一开关控制活动记录、n8n Assistant 中的实例上下文，以及 [n8n MCP 服务器](../../../connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md#instance-context)上的实例上下文工具。

在自托管实例上，设置 `N8N_FEATURE_FLAG_OVERRIDES` 可覆盖 PostHog 的值。例如，将以下值添加到 `.env` 文件，保留 JSON 对象中的其他条目。

```bash
N8N_FEATURE_FLAG_OVERRIDES='{"114_instance_activity_context":true}'
```

重启 n8n，使更改生效。

| `N8N_FEATURE_FLAG_OVERRIDES` 值 | 结果 |
| --- | --- |
| `{"114_instance_activity_context":true}` | 启用，不受 PostHog 值影响。 |
| `{"114_instance_activity_context":false}` | 关闭，即使 PostHog 返回 `true`。 |
| 未覆盖此开关 | 仅在 PostHog 返回 `true` 时启用，否则关闭。 |
| JSON 无效或覆盖数据无效 | n8n 忽略覆盖设置，使用 PostHog 的值。 |

如果 PostHog 开关评估失败，除非有有效覆盖明确启用，否则功能关闭。

同一开关同时控制记录和读取。关闭后，n8n 不写入活动条目，n8n Assistant 也不读取实例上下文。

活动日志记录发生了更改，以及其中新增或移除的节点类型，从不记录参数值。它报告某次保存更改了什么，而非项目当前使用什么。节点类型计数报告当前使用情况，需要独立开关。

关闭开关会停止记录新活动和读取新实例上下文，活动日志工具也不可用。先前记录的条目仍遵循以下保留设置：

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `N8N_ACTIVITY_LOG_RETENTION_DAYS` | `0` | 活动条目保留天数。`0` 禁用按时间清理。 |
| `N8N_ACTIVITY_LOG_MAX_ENTRIES` | `1000` | 所有项目合计的最大活动条目数。`0` 禁用按数量清理。 |

默认情况下，n8n 保留整个实例最新的 1,000 条活动记录，不根据时间移除。如果日志始终低于此上限，条目可能永久保留。

清理每小时运行一次，开关关闭后仍继续。更改这些环境变量后，请重启 n8n。

## 启用节点类型计数 <a id="enable-node-type-counting"></a>

{% hint style="info" %}
**功能可用范围**

节点类型计数自 n8n 2.39.0 起提供。通过以下功能开关或环境变量启用。
{% endhint %}

节点类型计数让 n8n Assistant 能查询项目中有多少工作流使用各节点类型，无需读取每个工作流，就能遵循你的惯例。它独立于实例上下文，具有自己的开关。

由 `109_instance_ai_node_usage` PostHog 开关控制。在自托管实例上，`N8N_INSTANCE_AI_NODE_USAGE_ENABLED` 可强制启用：

```bash
N8N_INSTANCE_AI_NODE_USAGE_ENABLED=true
```

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `N8N_INSTANCE_AI_NODE_USAGE_ENABLED` | `false` | 设为 `true` 后，无论 PostHog 开关返回什么，都会启用节点类型计数。 |

此变量只能启用节点类型计数。设为 `false` 或省略，会将决定权交还给 PostHog 开关，不能用于强制关闭功能。

节点类型计数报告节点类型数量，从不报告参数值。

## 启用智能体 <a id="enable-agents"></a>

无论是否使用 n8n Assistant，都可以[在实例上构建和运行智能体](../../../build/build-and-manage-agents/README.md)。智能体处于预览阶段，自 n8n 2.32.3 起提供。

{% hint style="info" %}
**功能可用范围**

所有自托管套餐默认启用智能体，包括 Enterprise。
{% endhint %}

只使用 `agents` 模块即可手动构建智能体：自行选择模型、编写指令、附加工具和技能。n8n Assistant（`instance-ai`）是可选项，可增加 AI 辅助构建能力，让你描述智能体，由 n8n 生成初始结构。

要更改实例设置：

1. 以实例所有者或管理员身份登录。
2. 打开 **Settings > Agents**（设置 > 智能体）。
3. 打开或关闭 **Enable Agents**（启用智能体）。

n8n 会在重启和许可证变更后保留此选择。此设置独立于 **Settings > Assistant**（设置 > Assistant）。关闭智能体会阻止新运行，并取消为后续运行排队的消息，已开始的运行可以完成。详情请参阅[启用或禁用智能体](../../../build/build-and-manage-agents/README.md#enable-or-disable-agents)。

`agents` 模块默认加载。如果已通过 `N8N_DISABLED_MODULES` 禁用，请从列表中移除 `agents` 并重启 n8n，以恢复设置页面。模块环境变量不会覆盖已保存的智能体设置。

### 共享沙箱与可选功能 <a id="shared-sandbox-and-optional-features"></a>

通过 **Settings > Agents > Shared sandbox**（设置 > 智能体 > 共享沙箱）[配置沙箱连接](../../../build/build-and-manage-agents/README.md#configure-the-shared-sandbox)。智能体和 n8n Assistant 使用同一连接，更改会同时影响两者。任一功能关闭时，也可以配置。

共享沙箱编辑器需要 `instance-ai` 模块，该模块也默认加载。如果通过 `N8N_DISABLED_MODULES` 排除了它，请从列表中移除并重启 n8n。可以在 **Settings > Assistant** 中保持 n8n Assistant 关闭，也可以使用环境变量配置沙箱。

启用共享沙箱也会启用智能体知识库。通过环境变量配置时，可使用以下可选设置：

```bash
# Enable the agent knowledge base with your existing Daytona connection
N8N_AGENTS_AI_SANDBOX_ENABLED=true
N8N_INSTANCE_AI_SANDBOX_PROVIDER=daytona

# Let channels reach your instance
N8N_WEBHOOK_URL=https://<your-public-hostname>
```

| 变量 | 说明 |
| --- | --- |
| `N8N_AGENTS_AI_SANDBOX_ENABLED` | 共享沙箱尚未启用时，设为 `true` 可启用知识库。需要已配置的沙箱，默认为 `false`。 |
| `N8N_INSTANCE_AI_SANDBOX_PROVIDER` | 智能体和 n8n Assistant 的共享沙箱提供商。使用 `n8n-sandbox` 或 `daytona`，默认为 `n8n-sandbox`。 |
| `N8N_WEBHOOK_URL` | 实例公开、安全的 URL。连接智能体到 Slack、Telegram、Linear 等渠道时必需。自 n8n 2.30.0 起提供，更早版本请使用 `WEBHOOK_URL`。 |

{% hint style="info" %}
**功能可用范围**

自托管 n8n 的知识库需要已配置的沙箱。没有沙箱时，智能体的其他功能仍可使用。沙箱选项请参阅[选择配置方案](#pick-your-setup)。
{% endhint %}

{% hint style="info" %}
**预览状态**

自托管部署中的知识库处于预览阶段。
{% endhint %}

完整部署示例请参阅[安装选项](../install-options/README.md)。创建第一个智能体，请参阅[构建和管理智能体](../../../build/build-and-manage-agents/README.md)。

## 禁用 n8n Assistant <a id="disable-n8n-assistant"></a>

要关闭 n8n Assistant，请使用 **Settings > Assistant**（设置 > Assistant）。要卸载其模块，请将 `instance-ai` 添加到 `N8N_DISABLED_MODULES` 并重启 n8n：

```bash
N8N_DISABLED_MODULES=instance-ai
```

卸载 `instance-ai` 也会从 **Settings > Agents** 中移除共享沙箱编辑器，但仍可以通过环境变量配置沙箱。

## 故障排查 <a id="troubleshooting"></a>

如果 n8n Assistant 未显示或无法使用，请检查以下问题。

**常规检查**

* `N8N_DISABLED_MODULES` 不包含 `instance-ai`。
* 模型值采用 `provider/model` 格式，如果设置了 `N8N_INSTANCE_AI_MODEL`。
* API 密钥对所选提供商有效。
* `N8N_INSTANCE_AI_SANDBOX_ENABLED` 已设为 `true`。

**自托管沙箱，方案 2**

* `N8N_SANDBOX_SERVICE_API_KEY` 与 API 容器上的 `SANDBOX_API_KEYS` 一致。
* 沙箱健康检查返回 `{"status":"ok"}`。
* n8n 容器能访问 `N8N_SANDBOX_SERVICE_URL`。

**Daytona，方案 3**

* 已设置 `DAYTONA_API_URL` 和 `DAYTONA_API_KEY`。
* Daytona 账号有容量创建新沙箱。

**网页搜索**

* 已设置 `INSTANCE_AI_BRAVE_SEARCH_API_KEY`，或已设置 `N8N_INSTANCE_AI_SEARXNG_URL`。
* 如果都未设置，属于预期情况。网页搜索是可选功能，n8n Assistant 的其他功能仍可使用。

**实例上下文**

* 实例已启用 `114_instance_activity_context` 开关。将 `N8N_FEATURE_FLAG_OVERRIDES` 设为 `{"114_instance_activity_context":true}` 可强制启用。
* 项目尚未发生更改。活动日志仅记录启用开关后发生的更改。
* 项目为空，且未在其中运行任何内容。n8n Assistant 会不报告内容，而非提供空摘要。

**节点类型计数**

* 已启用 `109_instance_ai_node_usage` 开关，或 `N8N_INSTANCE_AI_NODE_USAGE_ENABLED` 的值为 `true`。
* 将变量设为 `false` 不能强制关闭功能，而是将决定权交还给开关。
* 它独立于实例上下文，启用实例上下文不会启用节点类型计数。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
