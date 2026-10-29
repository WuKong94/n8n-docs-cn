---
title: 数据库环境变量
description: 通过环境变量设置和配置自托管 n8n 实例的数据库。
contentType: reference
tags:
- environment variables
hide:
- toc
- tags
nodeTitle: 数据库
originalFilePath: hosting/configuration/environment-variables/database.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/database
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 数据库环境变量 <a href="#database-environment-variables" id="database-environment-variables"></a>

{% include "../../../../../reusable-content/.gitbook/includes/self-hosting/file-based-configuration.md" %}

n8n 默认使用 SQLite，也支持 PostgreSQL。自 n8n 1.0 起，[已弃用对 MySQL 和 MariaDB 的支持](../../../../../changelog/v10-migration-guide.md#mysql-and-mariadb)。

本页介绍用于配置自托管 n8n 实例所选数据库的环境变量。

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `DB_TYPE`<br>/`_FILE` | 枚举字符串：<br> `sqlite`, `postgresdb` | `sqlite` | 要使用的数据库。 |
| `DB_TABLE_PREFIX` | * | - | 表名前缀。 |
| `DB_PING_INTERVAL_SECONDS` | Number | `2` | n8n 向数据库发送 ping、检查连接是否仍然可用的频率，单位为秒。 |
| `DB_PING_TIMEOUT_MS` | Number | `5000` | 单次 ping 的响应等待时长，单位为毫秒，超时计为失败。如果设置了 `N8N_DB_PING_TIMEOUT`，则回退使用该值；此旧变量自 n8n 2.35.0 起已弃用。 |
| `DB_PING_MAX_FAILURES_BEFORE_RECOVERY` | Number | `3` | 连续多少次 ping 失败后，n8n 会判定连接已断开并开始恢复。 |
| `DB_RECOVERY_BACKOFF_MIN_MS` | Number | `1000` | 首次尝试恢复前的等待时长，单位为毫秒。后续每次重试的等待时间按指数退避增长。 |
| `DB_RECOVERY_BACKOFF_MAX_MS` | Number | `30000` | 两次恢复尝试之间的最长等待时长，单位为毫秒，用于限制退避上限。必须大于或等于 `DB_RECOVERY_BACKOFF_MIN_MS`。 |
| `DB_CONNECTION_ACQUISITION_TIMEOUT_MS` | Number | `30000` | 恢复期间，查询在快速报错前的等待时长，单位为毫秒。设为 `0` 表示无限等待。仅适用于 PostgreSQL。 |

## PostgreSQL <a href="#postgresql" id="postgresql"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `DB_POSTGRESDB_DATABASE`<br>/`_FILE` | String | `n8n` | PostgreSQL 数据库名称。 |
| `DB_POSTGRESDB_HOST`<br>/`_FILE` | String | `localhost` | PostgreSQL 主机。 |
| `DB_POSTGRESDB_PORT`<br>/`_FILE` | Number | `5432` | PostgreSQL 端口。 |
| `DB_POSTGRESDB_USER`<br>/`_FILE` | String | `postgres` | PostgreSQL 用户。 |
| `DB_POSTGRESDB_PASSWORD`<br>/`_FILE` | String | - | PostgreSQL 密码。 |
| `DB_POSTGRESDB_POOL_SIZE`<br>/`_FILE` | Number | `2` | 控制 n8n 同时保持打开的 Postgres 连接数量。增加连接数可能改善资源利用，但连接过多也可能降低性能。 |
| `DB_POSTGRESDB_CONNECTION_TIMEOUT`<br>/`_FILE` | Number | `20000` | Postgres 连接超时，单位为毫秒。 |
| `DB_POSTGRESDB_IDLE_CONNECTION_TIMEOUT`<br>/`_FILE` | Number | `30000` | 连接空闲多久后可以因空闲被移除。 |
| `DB_POSTGRESDB_MAX_CONNECTION_LIFETIME_MS`<br>/`_FILE` | Number | `3600000` | n8n 在回收连接池中的连接前保留连接的时长，单位为毫秒。回收旧连接有助于避免数据库或网络已断开、但 n8n 尚未察觉的失效连接。默认为一小时，设为 `0` 可禁用回收。 |
| `DB_POSTGRESDB_KEEP_ALIVE`<br>/`_FILE` | Boolean | `true` | 是否为连接启用 TCP keep-alive。启用后，n8n 无需先执行查询，也能发现失效连接。 |
| `DB_POSTGRESDB_KEEP_ALIVE_INITIAL_DELAY_MS`<br>/`_FILE` | Number | `10000` | 在连接上发送首次 TCP keep-alive 探测前的等待时长，单位为毫秒。 |
| `DB_POSTGRESDB_SCHEMA`<br>/`_FILE` | String | `public` | PostgreSQL schema。 |
| `DB_POSTGRESDB_SSL_ENABLED`<br>/`_FILE` | Boolean | `false` | 是否启用 SSL。当 `DB_POSTGRESDB_SSL_CA`、`DB_POSTGRESDB_SSL_CERT` 或 `DB_POSTGRESDB_SSL_KEY` 设为非空值，或 `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED` 设为 `false` 时，会自动启用。 |
| `DB_POSTGRESDB_SSL_CA`<br>/`_FILE` | String | - | PostgreSQL SSL 证书颁发机构。 |
| `DB_POSTGRESDB_SSL_CERT`<br>/`_FILE` | String | - | PostgreSQL SSL 证书。 |
| `DB_POSTGRESDB_SSL_KEY`<br>/`_FILE` | String | - | PostgreSQL SSL 密钥。 |
| `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`<br>/`_FILE` | Boolean | `true` | 是否拒绝未获授权的 SSL 连接，true 表示拒绝，false 表示不拒绝。 |

## SQLite <a href="#sqlite" id="sqlite"></a>

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :---- | :------- | :---------- |
| `DB_SQLITE_POOL_SIZE` | Number | `0` | 控制以 [WAL 模式](https://www.sqlite.org/wal.html)还是[回滚日志模式](https://www.sqlite.org/lockingv3.html#rollback)打开 SQLite 文件。设为零时使用回滚日志模式；大于零时使用 WAL 模式，该值同时指定并行 SQL 读取连接数。WAL 模式比回滚日志模式性能更好，也更可靠。 |
| `DB_SQLITE_VACUUM_ON_STARTUP` | Boolean | `false` | 启动时运行 [VACUUM](https://www.sqlite.org/lang_vacuum.html) 重建数据库，以减小文件大小并优化索引。这是耗时的阻塞操作，会增加启动时间。 |

## 数据库连接恢复的工作原理 <a href="#how-database-connection-recovery-works" id="how-database-connection-recovery-works"></a>

n8n 会持续检查数据库是否可访问。如果连接中断，例如数据库重启或网络短暂故障，n8n 可以自行修复连接，无需一直等待你重启 n8n。

本页变量控制以下循环：

1. n8n 每隔 `DB_PING_INTERVAL_SECONDS` 发送一次 ping。每次 ping 需在 `DB_PING_TIMEOUT_MS` 内响应。
1. 连续 `DB_PING_MAX_FAILURES_BEFORE_RECOVERY` 次 ping 失败后，n8n 会判定连接已断开。
1. 然后 n8n 会重建连接，重试间隔逐渐增加，从 `DB_RECOVERY_BACKOFF_MIN_MS` 开始，最大不超过 `DB_RECOVERY_BACKOFF_MAX_MS`。
1. 对于 PostgreSQL，恢复期间的新查询最多等待 `DB_CONNECTION_ACQUISITION_TIMEOUT_MS`，等待连接恢复；超时后报错，而不是一直挂起。

{% hint style="info" %}
**适用于所有数据库**

健康检查和恢复循环，即 `DB_PING_*` 和 `DB_RECOVERY_BACKOFF_*` 变量，适用于所有数据库类型。
其余设置，即 `DB_CONNECTION_ACQUISITION_TIMEOUT_MS`、`DB_POSTGRESDB_MAX_CONNECTION_LIFETIME_MS`、`DB_POSTGRESDB_KEEP_ALIVE` 和 `DB_POSTGRESDB_KEEP_ALIVE_INITIAL_DELAY_MS`，仅适用于 PostgreSQL。默认值适合大多数部署，除非遇到连接问题，否则可以保持不变。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [环境变量](./)
