---
contentType: reference
nodeTitle: 使用命令行
originalFilePath: hosting/cli-commands.md
originalUrl: https://docs.n8n.io/hosting/cli-commands
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line
description: Server CLI，即 n8n 内置命令行界面中可用的命令。
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


# 使用命令行 <a id="use-the-command-line"></a>

**Server CLI** 是内置命令行界面，与 n8n 安装在同一台机器上运行。它直接访问数据库以完成管理任务，即使 n8n 未运行，也能执行大多数命令。

{% hint style="info" %}
**n8n CLI**

希望从远程机器以编程方式与 n8n 交互，或与 AI 智能体集成？请查看 [n8n CLI](https://app.gitbook.com/o/gkeAaBEvbwHB2NmepVHG/s/r7wKI4I1BgdBCuq5Cvcx/)。
{% endhint %}

## 何时使用 Server CLI 或 n8n CLI <a href="#when-to-use-server-cli-vs-n8n-cli" id="when-to-use-server-cli-vs-n8n-cli"></a>

| 功能 | Server CLI | n8n CLI |
| ------------------------ | ------------------------------------------------------------- | -------------------------------------------------------- |
| **运行位置** | 与 n8n 相同的机器 | 任何可访问网络的机器 |
| **身份验证** | 直接访问数据库 | API 密钥 |
| **是否要求 n8n 正在运行** | 否，大多数命令不需要 | 是 |
| **适合用途** | 实例运维、备份、迁移 | 编程、AI 智能体、远程管理 |
| **安全模型** | 绕过访问控制 | 遵循用户权限和 API 密钥的权限范围 |
| **使用场景示例** | 备份恢复、许可证管理、紧急密码重置 | 工作流自动化、通过代码管理凭据 |

## 运行 CLI 命令 <a href="#running-cli-commands" id="running-cli-commands"></a>

自托管 n8n 可以使用 CLI 命令。根据 n8n 安装方式不同，运行命令的方式也不同：

* npm：可以直接使用 `n8n` 命令，下文示例采用此方式。
*   Docker：`n8n` 命令可在 Docker 容器内使用：

    ```sh
    docker exec -u node -it <n8n-container-name> <n8n-cli-command>
    ```

## 启动工作流 <a href="#start-a-workflow" id="start-a-workflow"></a>

可以通过 CLI 直接启动工作流。

按 ID 执行已保存的工作流：

```bash
n8n execute --id <ID>
```

## 发布或取消发布工作流 <a href="#publish-or-unpublish-a-workflow" id="publish-or-unpublish-a-workflow"></a>

可以通过 CLI 发布或取消发布工作流。在 n8n 2.0 中，[原先的激活与停用开关](../../../changelog/v20-breaking-changes.md)被发布与取消发布模型取代。使用 `publish:workflow` 和 `unpublish:workflow`，可通过 CLI 更改工作流的发布状态。

{% hint style="info" %}
**需要重启**

这些命令操作 n8n 数据库。如果在 n8n 运行时执行，必须重启 n8n 后更改才会生效。
{% endhint %}

### 发布工作流 <a href="#publish-a-workflow" id="publish-a-workflow"></a>

使用 `publish:workflow` 按 ID 发布工作流。也可以传入 `versionId`，发布指定历史版本。

命令标志：

| 标志 | 说明 |
| ----------- | --------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --id | 要发布的工作流 ID，必填。 |
| --versionId | 可选的待发布版本 ID，省略时发布当前草稿。 |

{% hint style="info" %}
**没有 `--all` 标志**

与已弃用的 `update:workflow` 命令不同，`publish:workflow` 不支持 `--all`。这是有意设计，防止在生产环境中意外批量发布工作流。请按 ID 逐个发布。
{% endhint %}

按 ID 发布工作流的当前草稿：

```bash
n8n publish:workflow --id=<ID>
```

发布工作流的指定历史版本：

```bash
n8n publish:workflow --id=<ID> --versionId=<VERSION_ID>
```

### 取消发布工作流 <a href="#unpublish-a-workflow" id="unpublish-a-workflow"></a>

使用 `unpublish:workflow` 按 ID 取消发布某个工作流，或一次取消发布所有工作流。

命令标志：

| 标志 | 说明 |
| ------ | ---------------------------------------------------------------- |
| --help | 帮助提示。 |
| --id | 要取消发布的工作流 ID，不能与 `--all` 同时使用。 |
| --all | 取消发布所有工作流，不能与 `--id` 同时使用。 |

按 ID 取消发布工作流：

```bash
n8n unpublish:workflow --id=<ID>
```

取消发布所有工作流：

```bash
n8n unpublish:workflow --all
```

### update:workflow，已弃用 <a href="#updateworkflow-deprecated" id="updateworkflow-deprecated"></a>

{% hint style="warning" %}
**功能可用范围**

`update:workflow` 命令自 n8n 2.0 起已弃用，后续会移除。请改用 [`publish:workflow`](use-the-command-line.md#publish-a-workflow) 和 [`unpublish:workflow`](use-the-command-line.md#unpublish-a-workflow)，详情请参阅 [n8n 2.0 破坏性变更](../../../changelog/v20-breaking-changes.md)。
{% endhint %}

按 ID 将某个工作流的活动状态设为 false：

```bash
n8n update:workflow --id=<ID> --active=false
```

按 ID 将某个工作流的活动状态设为 true：

```bash
n8n update:workflow --id=<ID> --active=true
```

将所有工作流的活动状态设为 false：

```bash
n8n update:workflow --all --active=false
```

将所有工作流的活动状态设为 true：

```bash
n8n update:workflow --all --active=true
```

## 导出实体 <a href="#export-entities" id="export-entities"></a>

可以通过 CLI 从 n8n 导出数据库实体。此工具可以从一种数据库类型，例如 SQLite，导出所有实体类型，再导入另一种数据库类型，例如 Postgres。

命令标志：

| 标志 | 说明 |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --outputDir | 输出目录路径。 |
| --includeExecutionHistoryDataTables | 包含执行历史数据表。这些表可能非常大，因此默认排除。 |

```bash
n8n export:entities --outputDir=./outputs --includeExecutionHistoryDataTables=true
```

## 导出工作流和凭据 <a href="#export-workflows-and-credentials" id="export-workflows-and-credentials"></a>

可以通过 CLI 从 n8n 导出工作流和凭据。

{% hint style="info" %}
**规划完整备份**

`--backup` 标志仅导出工作流和凭据。自托管实例完整备份的内容及恢复方式，请参阅[备份与恢复](../keep-n8n-running/backup-and-restore.md)。
{% endhint %}

命令标志：

| 标志 | 说明 |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --all | 导出所有工作流或凭据。 |
| --backup | 为备份设置 --all --pretty --separate，可以另外设置 --output。 |
| --id | 要导出的工作流 ID。 |
| --output, -o | 输出文件名；使用独立文件时，为输出目录。 |
| --pretty | 将输出格式化为更便于阅读的形式。 |
| --separate | 每个工作流导出一个文件，便于版本管理。必须使用 --output 指定目录。 |
| --decrypted | 以明文格式导出凭据，仅适用于凭据。 |
| --version | 要导出的指定历史版本的版本 ID。仅适用于工作流，不能与 `--all` 或 `--published` 同时使用。 |
| --published | 导出工作流已发布或活动的版本，而非当前草稿。与 `--all` 结合时，跳过未发布的工作流。仅适用于工作流，不能与 `--version` 同时使用。 |

### 工作流 <a href="#workflows" id="workflows"></a>

将所有工作流导出到标准输出，即终端：

```bash
n8n export:workflow --all
```

按 ID 导出某个工作流，并指定输出文件名：

```bash
n8n export:workflow --id=<ID> --output=file.json
```

将所有工作流导出为单个文件，保存到指定目录：

```bash
n8n export:workflow --all --output=backups/latest/file.json
```

使用 `--backup` 标志，将所有工作流导出到指定目录，详情见上文：

```bash
n8n export:workflow --backup --output=backups/latest/
```

#### 导出指定工作流版本 <a href="#export-a-specific-workflow-version" id="export-a-specific-workflow-version"></a>

可以传入工作流的 `versionId`，搭配 `--version`，导出指定历史版本：

```bash
n8n export:workflow --id=<ID> --version=<VERSION_ID> --output=workflow-v1.json
```

#### 导出工作流的已发布版本 <a href="#export-the-published-version-of-a-workflow" id="export-the-published-version-of-a-workflow"></a>

使用 `--published`，导出工作流当前已发布或活动的版本，而非当前草稿：

```bash
n8n export:workflow --id=<ID> --published --output=published.json
```

可以将 `--published` 与 `--all` 结合，导出每个工作流的已发布版本。没有已发布版本的工作流会被跳过：

```bash
n8n export:workflow --all --published --output=workflows.json
```

{% hint style="info" %}
**版本元数据**

导出工作流时，n8n 包含 `versionMetadata` 属性，记录该版本的历史名称和描述。导入命令会将此数据保留在工作流历史表中，不覆盖当前工作流的名称和描述。
{% endhint %}

### 凭据 <a href="#credentials" id="credentials"></a>

将所有凭据导出到标准输出，即终端：

```bash
n8n export:credentials --all
```

按 ID 导出凭据，并指定输出文件名：

```bash
n8n export:credentials --id=<ID> --output=file.json
```

将所有凭据导出为单个文件，保存到指定目录：

```bash
n8n export:credentials --all --output=backups/latest/file.json
```

使用 `--backup` 标志，将所有凭据导出到指定目录，详情见上文：

```bash
n8n export:credentials --backup --output=backups/latest/
```

以明文格式导出所有凭据。可用于从一个安装环境迁移到配置文件中使用不同密钥的另一个安装环境。

{% hint style="warning" %}
**敏感信息**

文件中可以看到所有敏感信息。
{% endhint %}

```bash
n8n export:credentials --all --decrypted --output=backups/decrypted.json
```

## 导入实体 <a href="#import-entities" id="import-entities"></a>

此命令可导入先前通过 `export:entities` 命令导出的实体，支持导入到与导出时不同的数据库类型。目前支持的数据库类型包括 SQLite、Postgres。

导入前数据库应为空，可通过 `--truncateTables` 参数强制清空。

命令标志：

| 标志 | 说明 |
| ---------------- | -------------------------------------------------- |
| --help | 帮助提示。 |
| --inputDir | 存放待导入输出文件的输入目录。 |
| --truncateTables | 导入前清空表。 |

```bash
n8n import:entities --inputDir ./outputs --truncateTables true
```

## 导入工作流和凭据 <a href="#import-workflows-and-credentials" id="import-workflows-and-credentials"></a>

可以通过 CLI 导入从 n8n 导出的工作流和凭据。

{% hint style="warning" %}
**更新 ID**

导出工作流和凭据时，n8n 也会导出其 ID。如果现有数据库中存在相同 ID 的工作流和凭据，它们会被覆盖。为避免此情况，请在导入前删除或更改 ID。
{% endhint %}

可用标志：

| 标志 | 说明 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --input | 输入文件名；使用 --separate 时，为输入目录。 |
| --projectId | 将工作流或凭据导入指定项目，不能与 `--userId` 同时使用。 |
| --separate | 从 --input 指定目录导入 `*.json` 文件。 |
| --userId | 将工作流或凭据导入指定用户，不能与 `--projectId` 同时使用。 |
| --skipMigrationChecks | 跳过迁移验证检查。 |
| --activeState | 控制导入工作流的活动状态。接受 `false`，默认值，会停用所有导入的工作流；或 `fromJson`，使用各工作流 JSON 中的 `active` 字段，仅限多主实例模式。 |

{% hint style="info" %}
**迁移到 SQLite**

n8n 将工作流和凭据名称限制为 128 个字符，但 SQLite 不强制执行长度限制。

这可能导致导入过程中出现 **Data too long for column name**（名称列数据过长）等错误。

此时，可以在 n8n 界面中编辑名称后重新导出，或在导入前直接编辑 JSON 文件。
{% endhint %}

### 工作流 <a href="#workflows" id="workflows"></a>

{% hint style="warning" %}
**已知问题：导入后 cron 触发器继续运行**

导入此前处于活动状态的工作流时，行为因运行模式而异。这是已知缺陷。

在多主实例和队列模式实例上，此前活动工作流的 cron 触发器会在导入时停用。

在非多主实例上，此前活动工作流的 cron 触发器会继续运行，直到重启 n8n 实例。
{% endhint %}

从指定文件导入工作流：

```bash
n8n import:workflow --input=file.json
```

从指定目录导入所有 JSON 格式的工作流文件：

```bash
n8n import:workflow --separate --input=backups/latest/
```

{% hint style="info" %}
**导入时的版本元数据**

如果导入文件包含 `versionMetadata` 属性，由针对指定版本或已发布版本的导出添加，n8n 会将该历史名称和描述保留在工作流历史表中。当前工作流实体的名称和描述保持原样。
{% endhint %}

默认情况下，`import:workflow` 会停用每个导入的工作流。要保留各 JSON 文件中的 `active` 字段，请传入 `--activeState=fromJson`，仅支持多主实例和队列模式：

译注：原文的 --activeState 表格将 fromJson 标为“仅限多主实例模式”，但同页示例说明及同版本备份恢复指南均写“多主实例和队列模式”。此处保留原文差异，不据此判断实际版本兼容性。

```bash
n8n import:workflow --separate --input=backups/latest/ --activeState=fromJson
```

### 凭据 <a href="#credentials" id="credentials"></a>

从指定文件导入凭据：

```bash
n8n import:credentials --input=file.json
```

从指定目录导入所有 JSON 格式的凭据文件：

```bash
n8n import:credentials --separate --input=backups/latest/
```

## 许可证 <a href="#license" id="license"></a>

### 清除 <a href="#clear" id="clear"></a>

从 n8n 数据库清除现有许可证，并将 n8n 重置为默认功能：

```sh
n8n license:clear
```

如果许可证包含[浮动权益](#user-content-fn-1)[^1]，运行此命令也会尝试将其释放回池中，供其他实例使用。

### 信息 <a href="#info" id="info"></a>

显示现有许可证信息：

```sh
n8n license:info
```

## 用户管理 <a href="#user-management" id="user-management"></a>

可以使用 n8n CLI 重置用户管理，将其恢复到初始设置之前的状态，并移除所有用户账号。

忘记密码，且未配置 SMTP、无法通过邮件重置密码时，可使用此命令。

```sh
n8n user-management:reset
```

### 为用户禁用 MFA <a href="#disable-mfa-for-a-user" id="disable-mfa-for-a-user"></a>

用户丢失恢复代码时，可以使用此命令为其禁用 MFA。用户随后即可重新登录，再次设置 MFA。

```sh
n8n mfa:disable --email=johndoe@example.com
```

### 禁用 LDAP <a href="#disable-ldap" id="disable-ldap"></a>

可以通过以下命令重置 LDAP 设置。

```sh
n8n ldap:reset
```

## 卸载社区节点和凭据 <a href="#uninstall-community-nodes-and-credentials" id="uninstall-community-nodes-and-credentials"></a>

可以使用 n8n CLI 管理[社区节点](../../../integrations/community-nodes/installation-and-management/README.md)。目前仅支持卸载社区节点和凭据，适合处理社区节点导致实例不稳定的情况。

命令标志：

| 标志 | 说明 |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| --help | 显示 CLI 帮助。 |
| --credential | 凭据类型。请查看节点的 `<NODE>.credential.ts` 文件，获取 `name` 的值。 |
| --package | 社区节点的包名称。 |
| --uninstall | 卸载节点。 |
| --userId | 凭据所有者的用户 ID。自托管部署可查询数据库，Cloud 可使用 API 密钥查询 API。 |

### 节点 <a href="#nodes" id="nodes"></a>

按包名称卸载社区节点：

```sh
n8n community-node --uninstall --package <COMMUNITY_NODE_NAME>
```

例如，要卸载 [Evolution API 社区节点](https://www.npmjs.com/package/n8n-nodes-evolution-api)，请输入：

```sh
n8n community-node --uninstall --package n8n-nodes-evolution-api
```

### 凭据 <a href="#credentials" id="credentials"></a>

卸载社区节点凭据：

```sh
n8n community-node --uninstall --credential <CREDENTIAL_TYPE> --userId <ID>
```

例如，要卸载 [Evolution API 社区节点凭据](https://www.npmjs.com/package/n8n-nodes-evolution-api)，请访问[仓库](https://github.com/oriondesign2015/n8n-nodes-evolution-api)，找到 [`credentials.ts` 文件](https://github.com/oriondesign2015/n8n-nodes-evolution-api/blob/main/credentials/EvolutionApi.credentials.ts)，查看 `name`：

```sh
n8n community-node --uninstall --credential evolutionApi --userId 1234
```

## 安全审计 <a href="#security-audit" id="security-audit"></a>

可以在 n8n 实例上运行[安全审计](security/run-security-audits.md)，检测常见安全问题。

```sh
n8n audit
```

<a id="user-content-fn-1"></a>
[^1]: 在 n8n 中，权益（entitlements）授予 n8n 实例在特定时间段内使用套餐限制功能的权限。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
