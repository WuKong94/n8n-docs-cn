---
title: 前提条件
description: n8n OEM 部署的基础设施规格建议和部署最佳实践。
contentType: explanation
nodeTitle: 前提条件
originalFilePath: hosting/oem-deployment/prerequisites.md
originalUrl: https://docs.n8n.io/hosting/oem-deployment/prerequisites
url: https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/prerequisites
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 前提条件 <a href="#prerequisites" id="prerequisites"></a>

此处要求以 n8n Cloud 为例，仅作说明。实际需求可能因用户、工作流和执行数量而异。更多信息请联系 n8n。

| 组件 | 规格 | 支持 |
| :-------- | :----- | :-------- |
| CPU/vCPU | 至少 10 个 CPU 周期，按需扩展 | 任何公有云或私有云 |
| 数据库 | 512 MB - 4 GB SSD | SQLite 或 PostgreSQL |
| 内存 | 320 MB - 2 GB | |

## CPU 注意事项 <a href="#cpu-considerations" id="cpu-considerations"></a>

n8n 不是 CPU 密集型应用，因此 AWS、GCP 等提供商的小型实例通常足以应对大多数场景。通常内存需求比 CPU 更重要，规划基础设施时应优先将资源投入内存。

## 数据库注意事项 <a href="#database-considerations" id="database-considerations"></a>

n8n 使用数据库存储凭据[^1]、历史执行和工作流。

灵活选择数据库是 n8n 的核心特性。各受支持数据库都有不同优缺点，需要分别评估并选择最符合需求的类型。如果指定位置没有数据库，n8n 默认创建 SQLite 数据库。

n8n 建议为每个实例配置专用数据库，以防止依赖关系和潜在性能下降。如果无法为每个实例提供专用数据库，建议利用 Postgres 的 schema 功能。

使用 Postgres 时，数据库必须已存在于数据库实例上。n8n 进程使用的数据库用户，需要对所有使用或创建的表拥有完整权限。n8n 会创建并维护数据库 schema。

### 最佳实践 <a href="#best-practices" id="best-practices"></a>

* 使用 SSD 存储。
* 在容器化云环境中，确保停止或启动容器时，卷已持久化并挂载，否则所有数据都会丢失。
* 使用 Postgres 时，不要使用 `tablePrefix` 配置选项，它将在不久后弃用。
* 关注新版本更新记录，降级前考虑回退数据库迁移。
* 至少设置基本的数据库安全和稳定性机制，例如 IP 允许列表和备份。

## 内存注意事项 <a href="#memory-considerations" id="memory-considerations"></a>

n8n 实例通常不需要大量可用内存，例如 n8n Cloud 实例在空闲时约需 100 MB。实际内存需求由工作流性质及处理的数据决定。

例如，大多数节点只将数据传给下一个节点，而 [Code 节点](../../../build/code-in-n8n/using-the-code-node.md)会在处理前后创建数据副本。处理大型二进制文件时，这可能耗尽全部可用资源。

## 部署建议 <a href="#deployment-recommendations" id="deployment-recommendations"></a>

详细设置选项请参阅[托管文档](../install-options/use-a-cloud-provider/README.md)。

### 用户数据 <a href="#user-data" id="user-data"></a>

n8n 建议采用与 n8n Cloud 内部相同或类似的做法：使用 [Rook](https://rook.io/) 保存用户数据。n8n 服务器停止运行后，在另一台机器启动使用相同数据的新实例。

因此，通常只在灾难性故障，或用户希望在规定保留期内重新激活账号时，才需要使用备份；n8n Cloud 的该保留期为两周。

### 备份 <a href="#backups" id="backups"></a>

n8n 建议附加另一个容器，每晚将全部数据复制到第二个容器中创建备份。这种方式的 RAM 用量很小，不会影响服务器可承载的用户数量。

### 重启 <a href="#restarting" id="restarting"></a>

如果实例停止运行或重启，此期间错过的执行，例如 Cron 或 Webhook 节点，无法恢复。如果必须保持 100% 可用性，需要在前面增加另一个代理以缓存数据。

译注：本节原文未区分调度器模式。同一版本的“持久调度器”文档说明，Schedule Trigger 的运行记录可以跨重启保留，宽限期内会延迟触发，超过宽限期则遵循错过执行策略；该调度器自 n8n 2.45.0 起默认启用。这里保留原文，不将其“无法恢复”的描述推广到所有定时执行，也不推断 Webhook 请求会自动重放。

[^1]: 在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，就可以通过相应应用节点与服务交互。

## 相关资源 <a id="related-resources"></a>

* [作为 OEM 集成部署](./)
* [管理工作流](manage-workflows.md)
* [设置令牌交换](set-up-token-exchange.md)
