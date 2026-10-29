---
title: 执行数据脱敏
contentType: howto
nodeTitle: 执行数据脱敏
originalFilePath: workflows/executions/execution-data-redaction.md
originalUrl: https://docs.n8n.io/workflows/executions/execution-data-redaction
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data
description: 控制工作流中执行数据的可见性，保护敏感信息并满足合规要求。
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
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 执行数据脱敏 <a id="redact-execution-data"></a>

{% hint style="info" %}
**功能可用范围**

数据脱敏可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。

自 n8n 2.16.0 起提供按工作流设置的执行数据脱敏；自 n8n 2.26.0 起提供实例级强制执行数据脱敏。
{% endhint %}

执行数据脱敏允许你隐藏工作流执行的输入和输出数据。这有助于保护个人数据、身份验证令牌、财务记录等敏感信息，避免有权查看工作流但无需查看底层数据的用户读取。

启用脱敏后，执行元数据，包括状态、时间信息和节点名称，仍然可见，但 n8n 会将各节点实际处理的数据内容替换为脱敏标记。

你可以为每个工作流配置脱敏，也可以[在整个实例强制脱敏](redact-execution-data.md#instance-level-enforcement)，使所有工作流的执行数据都进行脱敏。

## 为什么使用执行数据脱敏 <a href="#why-use-execution-data-redaction" id="why-use-execution-data-redaction"></a>

工作流经常处理构建者或查看者不应在 n8n 之外访问的数据。常见场景包括：

* **个人身份信息（PII）与合规**：处理客户个人数据，例如邮箱、地址和财务记录的工作流，需要满足 GDPR、SOC 2 或内部安全标准。
* **跨部门工作流**：一个团队构建的工作流处理另一个团队的敏感数据，而构建者原本无权访问这些数据。
* **最小权限原则**：仅允许有需要的人员查看数据，而非所有具有工作流查看权限的用户。

在执行数据脱敏出现之前，唯一选择是在工作流级别完全禁用执行历史，这也会使工作流成功或失败的状态完全不可见。执行数据脱敏在隐藏敏感数据内容的同时，保留执行监控能力。

## 配置脱敏设置 <a href="#configure-redaction-settings" id="configure-redaction-settings"></a>

在工作流设置中为每个工作流配置脱敏。更改这些设置需要 `workflow:enableRedaction` 或 `workflow:disableRedaction` 权限范围，也可以同时拥有两者。

要配置脱敏：

1. 打开工作流。
2. 选择右上角的 **Workflow menu**（工作流菜单）<img src="../../../.gitbook/assets/three-dots-horizontal (1).png" alt="工作流菜单图标" data-size="line">。
3. 选择 **Settings**（设置）。
4. 找到 **Redact production execution data**（生产执行数据脱敏）和 **Redact manual execution data**（手动执行数据脱敏）设置。
5. 分别选择 **Default - Do not redact**（默认，不脱敏）或 **Redact**（脱敏）。
6. 选择 **Save**（保存）。

{% hint style="info" %}
**实例级强制策略锁定的设置**

启用[实例级强制脱敏](redact-execution-data.md#instance-level-enforcement)后，n8n 会将强制范围内的设置锁定为 **Redact**（脱敏），无法在工作流级别关闭。
{% endhint %}

### 脱敏设置说明 <a href="#redaction-settings-explained" id="redaction-settings-explained"></a>

有两个独立开关控制脱敏：

| 设置 | 控制内容 |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Redact production execution data**（生产执行数据脱敏） | 控制 n8n 是否对生产执行，即非手动触发的执行数据脱敏。生产执行包括工作流保持活动状态时，由 webhook、计划或其他触发器触发的执行。 |
| **Redact manual execution data**（手动执行数据脱敏） | 控制 n8n 是否对手动触发的执行数据脱敏。手动执行包括在编辑器中选择 **Execute Workflow**（执行工作流）启动的执行。 |

## 实例级强制脱敏 <a href="#instance-level-enforcement" id="instance-level-enforcement"></a>

实例所有者和管理员可以为实例上的所有工作流强制脱敏，无需依赖各工作流的独立设置。强制策略设定适用于整个实例的最低脱敏要求。

要启用强制脱敏，请前往 **Settings**（设置）> **Security**（安全），配置 **Data redaction**（数据脱敏）区域。详细步骤请参阅[安全设置](manage-security-policies.md#enforce-execution-data-redaction)。

### 强制范围 <a href="#enforcement-scope" id="enforcement-scope"></a>

强制范围控制 n8n 在整个实例中对哪些执行脱敏：

| 范围 | 强制要求 |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Production executions**（生产执行） | n8n 对每个工作流的生产执行数据脱敏，手动执行遵循各工作流自身的设置。这是推荐设置：既保护实际业务数据，又保留手动测试运行的数据可见性，便于调试。 |
| **Manual and production executions**（手动执行和生产执行） | n8n 对每个工作流的所有执行数据脱敏。测试数据也敏感时，请使用此设置。 |

### 强制策略如何与工作流设置配合 <a href="#how-enforcement-interacts-with-workflow-settings" id="how-enforcement-interacts-with-workflow-settings"></a>

* **读取执行数据时应用强制策略。**任何人查看执行时，n8n 都会对强制范围内的数据脱敏，包括自身设置未启用脱敏的工作流的执行。
* **工作流设置不能比强制范围更宽松。**工作流设置界面会锁定受影响的脱敏开关，[公共 API](../../../../connect/n8n-api/README.md) 也会拒绝以低于最低要求的脱敏策略创建或更新工作流。工作流仍可采用更严格的脱敏策略。
* **新工作流默认采用最低要求。**启用强制脱敏后创建工作流，其脱敏策略默认采用强制范围。通过公共 API 创建工作流时，如果未指定脱敏策略，n8n 会将其设为最低要求。
* **现有工作流设置保持原样。**启用强制策略不会更改现有工作流已存储的设置，但执行数据仍会按强制范围脱敏。如果以后关闭强制策略，各工作流将恢复采用自身设置。

## 哪些内容会脱敏 <a href="#what-gets-redacted" id="what-gets-redacted"></a>

n8n 对执行脱敏时，会处理：

* **条目的 JSON 数据**：将每个节点的全部输入和输出数据（`item.json`）替换为空对象。
* **二进制数据**：移除文件、图片等二进制数据（`item.binary`）。
* **声明为敏感的字段**：始终对节点作者通过 `sensitiveOutputFields` 标记的敏感字段脱敏，并禁止查看其原始内容，即使用户拥有查看原始数据的权限。
* **错误元数据**：对错误消息脱敏，仅保留错误类型和 HTTP 状态码（针对 API 错误），以辅助故障排查。

脱敏后的执行中：

* 执行查看器显示带碎纸机图标的 **Data redacted**（数据已脱敏）标记，替代通常的数据表格。
* 执行元数据仍然可见：节点名称、执行状态（成功或失败）、时间信息和工作流结构。

{% hint style="info" %}
**错误信息**

n8n 对执行数据脱敏时，也会对错误详情脱敏，防止敏感信息通过错误消息泄露。仅保留错误类型，例如 `NodeApiError`，以及 HTTP 状态码。这些信息足以识别故障类别，同时不暴露数据。
{% endhint %}

## 查看脱敏前的原始数据 <a href="#reveal-redacted-data" id="reveal-redacted-data"></a>

拥有 **Reveal execution data**（查看原始执行数据，`execution:reveal`）权限范围的用户，可以临时查看某次执行的原始数据。实例所有者和管理员默认拥有此权限范围。

要查看原始数据：

1. 在执行查看器中打开执行。
2. 选择脱敏数据区域显示的 **Reveal data**（查看原始数据）按钮。
3. 阅读确认对话框，其中会说明：
   * 系统会在审计记录中记录此操作。
   * 仅应在有正当理由时查看原始数据。
   * 不必要的访问可能违反组织策略。
4. 选择 **Reveal data**（查看原始数据）确认。

当前会话中，这次执行的数据将变为可见。

{% hint style="info" %}
**使用动态凭据的执行**

对于使用了动态凭据的执行，无论用户权限或生效的脱敏策略如何，n8n 都会拒绝查看原始数据的请求，以免暴露执行在运行时解析出的凭据。
{% endhint %}

## 审计日志 <a href="#audit-logging" id="audit-logging"></a>

[日志流](../../../../administer/observe-and-log/stream-logs-to-external-systems.md) 会跟踪查看原始数据的操作和强制策略的更改，提供以下审计事件：

| 事件 | 说明 |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `n8n.audit.execution.data.revealed` | 用户查看脱敏前的执行数据时，n8n 发出此事件。包含用户、执行 ID、工作流 ID、时间戳、IP 地址和生效的脱敏策略。 |
| `n8n.audit.execution.data.reveal_failure` | n8n 拒绝查看原始数据的尝试时，例如权限不足，发出此事件。包含上述相同字段及拒绝原因。 |
| `n8n.audit.redaction-enforcement.updated` | 用户更改实例级强制策略时，n8n 发出此事件。包含用户以及更改前后的策略值。 |

这些事件可以集成到现有日志流目标，包括 syslog、webhook 和 Sentry，支持合规报告和访问审计。

## 权限范围 <a href="#permission-scopes" id="permission-scopes"></a>

执行数据脱敏引入以下权限范围，可以通过[自定义项目角色](../../../../administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md)分配：

| 权限范围 | 用途 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `workflow:enableRedaction` | 允许在工作流设置中启用脱敏，在角色配置界面中显示为 **Enable data redaction**（启用数据脱敏）。 |
| `workflow:disableRedaction` | 允许在工作流设置中关闭脱敏，在角色配置界面中显示为 **Disable data redaction**（禁用数据脱敏）。 |

默认情况下，实例所有者、管理员和项目管理员有权启用或禁用脱敏，以及查看脱敏前的原始数据。你可以创建自定义角色，分别向更多用户，例如工作流构建者，授予其中一个或两个权限范围。

## 脱敏不涵盖的范围 <a href="#what-redaction-doesnt-cover" id="what-redaction-doesnt-cover"></a>

脱敏控制用户查看执行时，执行数据的可见性。它并非后端访问控制，有些数据路径不在其范围内。评估脱敏是否满足合规要求时，请考虑以下限制：

* **Code 节点的 `console.log` 输出**：Code 节点通过 `console.log` 记录的数据不会脱敏。手动执行时，输出显示在编辑器的 Logs（日志）面板中；生产执行时，输出写入服务器标准输出（stdout）以及与其连接的日志基础设施。
* **节点间流动的数据**：脱敏不限制下游节点收到的内容。执行期间，数据在节点间不受限制地流动，因此工作流中的任何节点都可以将执行数据发送到外部系统。脱敏控制执行查看器中用户能看到的内容，不控制工作流本身如何使用数据。
* **Webhook 响应**：工作流返回给调用方的响应体，例如通过 Respond to Webhook 节点或节点的响应选项返回的内容，仍为原始数据，不是脱敏版本。
* **出站请求中的身份验证标头**：脱敏不会修改工作流向外部服务发出的请求，包括其中包含的身份验证标头。
* **不支持字段级脱敏**：脱敏作用于节点的完整数据内容，无法为数据中的单个字段配置脱敏。节点作者声明为敏感的字段除外，n8n 始终对这些字段脱敏。
* **存储的数据保持原样**：脱敏不加密或更改数据库中的执行数据。n8n 通过 API 提供数据时才应用脱敏。任何能直接访问数据库的人都可以读取底层数据。
* **强制策略不会通过源代码管理传播**：实例级强制策略属于实例策略，使用[源代码管理](../../../../administer/use-source-control-and-environments/README.md)推送工作流时不会包含此策略。从启用强制策略的实例推送到未启用的实例时，工作流在目标实例上不会因此脱敏。这与强制双因素身份验证等其他实例级策略的行为一致。

## 最佳实践 <a href="#best-practices" id="best-practices"></a>

### 选择合适的脱敏策略 <a href="#choosing-the-right-redaction-policy" id="choosing-the-right-redaction-policy"></a>

| 场景 | 推荐设置 |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| 在生产环境处理 PII、财务数据或身份验证令牌的工作流 | 对生产执行数据脱敏 |
| 连测试数据也敏感的工作流，例如使用生产数据副本 | 对生产执行和手动执行数据都脱敏 |
| 处理非敏感数据的工作流，或处于初始开发阶段 | 不脱敏 |

### 一般建议 <a href="#general-recommendations" id="general-recommendations"></a>

* **从生产执行脱敏开始**：对于大多数处理敏感数据的工作流，对生产执行脱敏，同时保留手动执行数据可见性，能兼顾安全性和调试便利。
* **按需对手动数据脱敏**：测试环境使用真实数据或类似生产环境的数据时，也请启用手动执行脱敏。
* **使用日志流**：启用[日志流](../../../../administer/observe-and-log/stream-logs-to-external-systems.md)，记录查看原始数据的审计事件，为合规提供审计记录，并监控谁访问了敏感执行数据。
* **在工作流审核中检查脱敏设置**：将脱敏策略纳入工作流审核或批准流程，尤其是处理跨部门或面向客户数据的工作流。

## 安全注意事项 <a href="#security-considerations" id="security-considerations"></a>

* n8n 在 API 层应用脱敏，从不将已隐藏的原始数据发送到浏览器。
* [创建自定义节点](../../../../connect/create-nodes/overview.md)时，你可以在节点类型定义中使用 `sensitiveOutputFields`，将特定输出字段声明为敏感。n8n 始终对这些字段脱敏，并禁止查看其原始内容，即使用户拥有查看原始数据的权限。
* 如果脱敏服务无法解析节点的类型定义，例如社区节点已卸载，n8n 会对该节点的所有输出数据完全脱敏。这种无法确定时默认拒绝的方式，可防止未知节点泄露敏感字段。
* 启用脱敏后，[日志流](../../../../administer/observe-and-log/stream-logs-to-external-systems.md)和日志输出中的执行数据也会自动脱敏。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
