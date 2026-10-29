---
description: 备份与恢复自托管 n8n 实例，了解 CLI 备份包含和遗漏的内容，以及如何恢复完整实例。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 备份与恢复 <a id="back-up-and-restore"></a>

备份自托管 n8n 实例，以便在数据丢失后恢复、回滚失败的更新，或迁移到新服务器。完整备份所需的内容多于单独使用 CLI 导出命令产生的文件。本页说明完整备份包含哪些内容、CLI 的 `--backup` 标志会导出什么，以及如何恢复各类备份。

## 完整备份包含哪些内容 <a id="what-a-complete-backup-includes"></a>

自托管 n8n 实例的完整备份由两部分组成：

* `.n8n` 用户文件夹，默认为 `~/.n8n`。其中的 `config` 文件保存凭据加密密钥。使用默认 SQLite 数据库时，该文件夹也包含数据库文件。如果二进制数据或执行数据采用 `filesystem` 存储模式，也包含这些数据。

可以通过 `N8N_USER_FOLDER` 环境变量更改文件夹位置：n8n 使用所设路径下的 `.n8n` 子文件夹。
* 如果使用 PostgreSQL 而非默认 SQLite，还需要备份外部数据库。请使用数据库自身的工具备份。`.n8n` 文件夹仍属于备份的一部分，因为数据库中的凭据由其中保存的密钥加密。

如果为二进制数据或执行数据配置了 S3、Azure Blob Storage 等外部存储，也请备份这些存储。如果二进制数据或执行数据存储在自定义文件系统路径，请将该位置纳入备份。如果通过 `N8N_CUSTOM_EXTENSIONS` 环境变量指定目录来加载自定义节点，也请备份这些目录，否则恢复后的实例会缺少工作流引用的节点。

使用默认 SQLite 数据库时，复制 `.n8n` 文件夹之前请先停止 n8n。在 n8n 写入数据库时复制数据库文件，可能生成不一致的备份。如果无法停止 n8n，请使用能为 SQLite 文件创建一致性快照的工具。

在 Docker 中运行 n8n 时，`.n8n` 文件夹位于 `n8n_data` 卷中，挂载到 `/home/node/.n8n`。Docker 持久化数据的更多信息，请参阅[使用 Docker 安装](../install-options/install-with-docker.md)。

{% hint style="info" %}
**恢复凭据需要加密密钥**

n8n 将凭据以加密形式保存在数据库中。没有 `config` 文件中的加密密钥，或自定义的 `N8N_ENCRYPTION_KEY`，就无法解密恢复后的数据库或加密的凭据导出文件。更多信息请参阅[设置自定义加密密钥](../configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key.md)。
{% endhint %}

n8n 建议在更新前进行完整备份。更新步骤请参阅[更新 n8n](update-n8n.md)。

## 使用 CLI 备份工作流和凭据 <a id="back-up-workflows-and-credentials-with-the-cli"></a>

可以使用[服务器 CLI](../configure-n8n/use-the-command-line.md)，将工作流和凭据导出到 JSON 文件：

```bash
n8n export:workflow --backup --output=backups/workflows/
n8n export:credentials --backup --output=backups/credentials/
```

`--backup` 标志会设置 `--all --pretty --separate`，将每个工作流和凭据分别写入独立、便于阅读的 JSON 文件。

请为每条命令使用不同的输出目录。目前，如果输入目录还包含工作流文件，`import:credentials --separate` 就会失败。这是一个[已知问题](https://github.com/n8n-io/n8n/issues/37814)。

在 Docker 中运行 n8n 时，容器内的 `backups/` 目录不会持久化，只有 `.n8n` 文件夹位于卷中。请绑定挂载主机目录来存放备份，或在重新创建容器前，将导出的文件复制到容器外。

### CLI 备份不包含哪些内容 <a id="what-a-cli-backup-doesnt-contain"></a>

`--backup` 导出仅包含工作流和凭据，不包含：

* 用户及其角色。导入到全新实例后，n8n 会再次显示所有者设置页面，首个完成设置的人会成为所有者。
* 执行历史和日志。
* 变量。
* 实例设置，包括加密密钥。

因此，CLI 备份足以在实例间迁移工作流，但无法单独用于恢复完整实例。要恢复完整实例，请按[完整备份包含哪些内容](#what-a-complete-backup-includes)一节备份 `.n8n` 文件夹和外部数据库。

## 恢复 <a id="restore"></a>

### 恢复工作流和凭据 <a id="restore-workflows-and-credentials"></a>

导入 CLI 备份中的文件。全新实例应先完成所有者设置：导入命令需要已有用户，导入的凭据也需要所有者。如果实例包含多个用户或项目，请使用 `--userId` 或 `--projectId` 指定导入凭据的归属。

```bash
n8n import:workflow --separate --input=backups/workflows/
n8n import:credentials --separate --input=backups/credentials/
```

导出内容包含原工作流和凭据 ID。如果目标实例已存在相同 ID 的条目，它们会被覆盖。导入的工作流默认停用。导入后请在界面中激活，或传入 `--activeState=fromJson` 恢复各工作流导出时的活动状态，此选项仅适用于队列或多主实例模式。完整标志列表和注意事项请参阅[使用命令行](../configure-n8n/use-the-command-line.md)。

要恢复凭据，导入实例必须能够解密它们。有两种选择：

* 使用与导出实例相同的加密密钥。将 `config` 文件恢复到 `.n8n` 文件夹，或设置相同的 `N8N_ENCRYPTION_KEY` 环境变量。
* 使用 `--decrypted` 标志导出，以明文形式写入凭据。

{% hint style="warning" %}
**敏感信息**

`--decrypted` 导出包含明文形式的全部凭据数据。请像保护凭据本身一样妥善保存，并在恢复完成后删除。
{% endhint %}

### 恢复完整实例 <a id="restore-the-full-instance"></a>

要恢复完整实例：

1. 停止 n8n。
2. 将 `.n8n` 文件夹恢复到原位置，并恢复通过 `N8N_CUSTOM_EXTENSIONS` 配置的所有自定义节点目录。
3. 如果使用 PostgreSQL，请从备份恢复数据库。
4. 恢复部署配置，包括数据库连接环境变量、使用自定义密钥时的 `N8N_ENCRYPTION_KEY`，以及外部存储设置。缺少这些配置，恢复后的实例将无法访问数据库或解密数据。
5. 启动 n8n。

使用默认 SQLite 数据库时，`.n8n` 文件夹包含恢复实例所需的全部内容：保存用户、设置和执行数据的 SQLite 数据库文件、加密密钥，以及在文件系统存储模式下的二进制数据和执行数据。使用 PostgreSQL 时，`.n8n` 文件夹仍保存加密密钥，数据库备份保存其余内容。

## 相关内容 <a id="related-content"></a>

* [保持 n8n 运行](README.md)：自托管 n8n 实例的运行维护指南。
* [使用命令行](../configure-n8n/use-the-command-line.md)：完整服务器 CLI 参考，包括所有导出和导入标志。
* [设置自定义加密密钥](../configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key.md)：如何显式提供 `N8N_ENCRYPTION_KEY`。
* [选择 n8n 的数据库](../configure-n8n/choose-n8ns-database.md)：SQLite 和 PostgreSQL 配置。
* [更新 n8n](update-n8n.md)：npm 和 Docker 安装的更新步骤。

## 相关资源 <a id="related-resources"></a>

* [保持 n8n 运行](./)
* [设置日志](set-up-logging.md)
* [监控 n8n](monitor-n8n.md)
* [使用 Grafana 可视化指标](visualize-metrics-with-grafana.md)
* [更新 n8n](update-n8n.md)
* [使用 OpenTelemetry 跟踪执行](trace-executions-with-opentelemetry.md)
