---
description: n8n 的隐私政策。
tags:
- gdpr
- data collection
- pid
- payment processor
hide:
- tags
contentType: explanation
nodeTitle: 隐私
originalFilePath: privacy-security/privacy.md
originalUrl: https://docs.n8n.io/privacy-security/privacy
url: https://docs.n8n.io/privacy-and-security/privacy
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->




# 隐私 <a href="#privacy" id="privacy"></a>

本页介绍 n8n 官方的数据隐私实践。

## GDPR <a href="#gdpr" id="gdpr"></a>

### 数据处理协议 <a href="#data-processing-agreement" id="data-processing-agreement"></a>

对于 n8n Cloud，按照 GDPR 的定义，n8n 同时是控制者和处理者。作为处理者，n8n 实施相应政策和实践，保护发送至平台的个人数据，并将[数据处理协议](https://n8n.io/legal/#data)纳入公司的标准[服务条款](https://n8n.io/legal/#terms)。

n8n 数据处理协议包含[标准合同条款（SCC）](https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)，明确 n8n 如何处理数据，并更新 GDPR 政策，以涵盖欧盟委员会的最新标准。

可以在[此处](https://n8n.io/legal/sub-processors/)查看 n8n 的子处理者列表。

{% hint style="info" %}
**自托管 n8n**

对于自托管版本，n8n 不管理你的数据，因此既不是控制者，也不是处理者。
{% endhint %}

### 提交账号删除请求 <a href="#submitting-an-account-deletion-request" id="submitting-an-account-deletion-request"></a>

在 n8n Cloud 上，实例所有者可以通过 [n8n Cloud 控制台](../deploy/use-n8n-cloud/use-the-cloud-console.md)删除账号：

1. 选择 **Instance settings（实例设置）**。
1. 在 **Danger zone（危险区域）** 中，选择 **Delete account（删除账号）**。
1. 如果账号有生效中的订阅，n8n 会要求先取消订阅。选择 **Cancel subscription（取消订阅）** 并完成取消。
1. 输入账号邮箱地址确认，再选择 **Delete account（删除账号）**。

也可以发送邮件至 [help@n8n.io](mailto:help@n8n.io)，提出账号删除请求。

### 子处理者 <a href="#sub-processors" id="sub-processors"></a>

子处理者列表见 [n8n.io/legal/sub-processors](https://n8n.io/legal/sub-processors/)。

### 自托管用户与 GDPR <a href="#gdpr-for-self-hosted-users" id="gdpr-for-self-hosted-users"></a>

{% include "../reusable-content/.gitbook/includes/privacy-security/gdpr-self-hosted.md" %}


## 遥测 <a id="telemetry"></a>

n8n 会收集有限的产品使用信息，用于保持产品正常运行、修复故障，并决定后续开发方向。本页说明收集的内容、原因，以及可以关闭哪些收集。

概括而言，n8n 收集产品使用方式的信息，不收集工作流中流转的数据，也不收集凭据。

### 如何阅读本页 <a id="how-to-read-this-page"></a>

**自托管**指 n8n 运行在你自己的服务器上，包括免费 Community Edition，以及 Enterprise 等付费许可版本。

**n8n Cloud** 指由 n8n 托管、通过浏览器使用的服务。下文同样适用于 Cloud，差异在[使用 n8n Cloud 时](#if-you-use-n8n-cloud)一节说明。

**假名化**指数据关联到某个代码，而不是姓名或邮箱；如果没有另行保存的信息，就无法追溯到你。在 GDPR 下，这仍属于个人数据，n8n 也按个人数据处理。

### 谁对这些数据负责 <a id="who-is-responsible-for-this-data"></a>

对于自托管实例中工作流流转的数据，n8n 既不是控制者，也不是处理者。这些数据保留在你的基础设施中，n8n 不会收到。

遥测则不同。如果实例向 n8n 发送使用和诊断数据，n8n 是这些数据的控制者，并决定使用方式。

### n8n 为遥测收集哪些内容 <a id="what-n8n-collects-for-telemetry"></a>

n8n 尽可能对遥测数据进行假名化，并避免收集敏感数据。收集类别如下。

| 收集内容 | 示例 | 收集原因 | 能否关闭 |
| --- | --- | --- | --- |
| **实例和配置。** 标识实例的代码、n8n 版本、数据库和部署类型、部分配置设置，以及操作系统、内存和 CPU 等服务器基本信息。还包括部署制品及版本、运行时和基础设施提供商、数据库和缓存提供商、分配的 CPU 和内存资源，以及定期汇总的 n8n 进程数量和资源分配。 | 部署类型 `default`，数据库 postgres，版本 `1.105.0`，通过 `helm-chart/1.14.0` 安装在 Kubernetes 上，两个工作进程各分配一个 CPU | 判断更新是否破坏原本正常的功能、了解实际实例配置，并为发布的部署模板设置合理默认值 | 可以 |
| **标识符。** 结合实例和用户编号的代码，以及截断的 IP 地址。代码不包含姓名或邮箱。 | 用户 `5678`，所在实例为 `abc123`。`12.214.31.144` 保存为 `12.214.31.0` | 区分重复活动与新活动，并保持服务安全稳定 | 可以 |
| **IP 地址。** 截断的 IP 地址。末尾部分被移除，因此存储内容识别的是网络，而非设备。对于自托管实例，这是服务器的地址，而不是浏览器用户的地址。n8n Cloud 的情况见[使用 n8n Cloud 时](#if-you-use-n8n-cloud)。n8n 用它判断实例所在国家。 | `12.214.31.144` 保存为 `12.214.31.0` | 保持服务安全稳定，并了解 n8n 在哪些国家使用 | 可以 |
| **产品中的操作。** 创建、保存、运行和删除工作流；工作流形状，即哪些节点类型相互连接，但不包含流经节点的信息；使用了哪些功能和模板，以及如何在界面中导航。 | “工作流首次在生产环境中成功运行” | 查找用户遇到的困难，并决定后续开发内容 | 可以 |
| **错误和诊断。** 界面及服务器中的错误消息和失败详情、失败执行及系统健康信号。错误消息有时包含来自工作流的文本，例如节点名称或所连接服务返回的错误。 | `ECONNREFUSED` 及失败的节点类型 | 排查问题并保持 n8n 可靠运行 | 可以 |
| **连接的外部服务。** HTTP Request 节点所配置地址的可注册域名，以及 Webhook 调用的域名。自 2026 年 1 月起，不再收集子域名或路径。 | 指向 `api.stripe.com/v1/charges` 的节点被记录为 `stripe.com` | 判断哪些服务值得提供专用的 n8n 集成 | 可以 |
| **许可证和使用量。** 活跃工作流、工作流总数、执行次数及实例用户数。持有付费许可证时，这些数据会与许可证标识符一起上报。 | 活跃工作流：3。生产执行：45678 | 运行许可证服务并正确计费，因为 n8n 按执行次数定价 | 不可以。订阅或许可证运行需要这些数据。 |

### 收集机制 <a id="how-collection-works"></a>

大多数数据会在相应事件发生时发送给 n8n。工作流执行次数和实例心跳每六小时发送一次。

### n8n 不收集哪些内容 <a id="what-n8n-doesnt-collect"></a>

- 工作流中流转的数据，即节点发送和接收的信息
- 凭据内容
- 节点参数，但节点所选的 `resource` 和 `operation` 除外
- 敏感配置，例如端点、端口、数据库连接，以及用户名或密码
- 错误载荷

n8n 不出售遥测数据，也不会为他人的商业目的共享遥测数据。

### 关闭遥测 <a id="turning-telemetry-off"></a>

遥测默认开启。要在自托管实例上关闭，设置以下环境变量。必须由实例管理员操作，n8n 界面内没有开关。

退出遥测事件上报：

```shell
export N8N_DIAGNOSTICS_ENABLED=false
```

停止检查 n8n 新版本：

```shell
export N8N_VERSION_NOTIFICATIONS_ENABLED=false
```

禁用模板功能，避免后台健康检查调用：

```shell
export N8N_TEMPLATES_ENABLED=false
```

设置环境变量的方法，请参阅[配置](../deploy/host-n8n/configure-n8n/basic-configuration.md)。

{% hint style="warning" %} 退出设置不涵盖的内容

如果持有付费许可证，无论是否关闭遥测，实例都会继续上报使用量和许可证标识符。这是运行许可证服务所必需的，无法禁用。

目前无法在 n8n Cloud 上关闭遥测。
{% endhint %}

### 使用 n8n Cloud 时 <a id="if-you-use-n8n-cloud"></a>

以上内容同样适用于 n8n Cloud，但有三点不同。

**无法关闭遥测。** Cloud 没有退出选项，界面中也没有相应设置。

**n8n 看到的 IP 地址不同。** Cloud 实例发送的任何内容，其地址属于 n8n 基础设施，而不是用户。对于浏览器中的 Cloud 控制台，则使用用户网络地址，并按上述方式截断。

**n8n 会录制界面会话。** 仅在 Cloud 上，n8n 会捕获用户使用界面时屏幕发生的情况，以了解产品中令人困惑的地方。凭据值不会被录制。录像会在 21 天后删除。

### AI 功能 <a id="ai-in-n8n"></a> <a id="ai-features"></a>

n8n 集成了使用大语言模型的 AI 功能。为了回答问题，n8n 可能向这些模型发送当前打开工作流的上下文。

**n8n 会发送的内容**

- **工作流基本信息**，包括有哪些节点、包含多少数据项，以及工作流是否活跃
- **节点输入和输出结构**，即数据的形状，而不是实际值
- **节点配置**，即对应节点中选择的操作、选项和设置
- **对应节点中的代码和表达式**，便于模型协助调试

**n8n 不会发送的内容**

- **凭据。** 节点凭据字段中的任何值
- **输出数据。** 工作流实际处理的数据
- 未明确放入节点参数或 [Code 节点](../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)代码中的**敏感信息**

只有工作空间已选择使用助手时，才会向 AI 服务发送数据；n8n Cloud 默认启用助手。节点专属数据只在直接与助手交互时传输。这些数据不会用于训练 AI 服务的模型。

## 文档站遥测 <a id="documentation-telemetry"></a>

n8n 官方文档站使用 Cookie 识别重复访问和偏好，并衡量用户是否找到所需内容。可以通过 Cookie 组件控制同意设置。

## 个人身份识别数据的保留和删除 <a href="#retention-and-deletion-of-personal-identifiable-data" id="retention-and-deletion-of-personal-identifiable-data"></a>

PID（personal identifiable data，个人身份识别数据）指与你本人相关、能够识别你个人身份的数据。

### n8n Cloud <a href="#n8n-cloud" id="n8n-cloud"></a>

#### PID 保留 <a href="#pid-retention" id="pid-retention"></a>

n8n 只会在提供核心服务所需的期限内保留数据。

对于 n8n Cloud，只要账号仍活跃，n8n 就会保存工作流代码、凭据和其他数据，直到你选择删除或关闭账号。平台按账号的保留规则存储执行数据。

n8n 会在 90 天内删除大多数内部应用日志和与子处理者相关的日志。安全调查需要时，部分安全和审计日志会保留更久；计费记录则按税务和会计法律要求的期限保留。

#### PID 删除 <a href="#pid-deletion" id="pid-deletion"></a>

在 Cloud 控制台删除 n8n 账号后，n8n 会在当天删除关联的工作流、凭据、用户和执行数据，并在 90 天内从备份中移除。

如果账号关闭但未提出删除请求，n8n 会在关闭后 100 天内删除客户数据，备份则在 90 天内删除。

### 自托管 <a href="#self-hosted" id="self-hosted"></a>

自托管用户应制定自己的 PID 政策和数据删除流程。更多信息请参阅[可以采取的措施](what-you-can-do.md)。

## 支付处理商 <a href="#payment-processor" id="payment-processor"></a>

n8n 使用 Paddle.com 处理付款。注册付费套餐时，Paddle 会按其安全政策传输和存储支付方式详情。n8n 不保存支付方式信息。


