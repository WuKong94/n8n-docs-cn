---
contentType: howto
nodeTitle: 管理执行数据
originalFilePath: hosting/scaling/execution-data.md
originalUrl: https://docs.n8n.io/hosting/scaling/execution-data
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 执行数据 <a href="#execution-data" id="execution-data"></a>

根据执行设置和执行量的不同，n8n 数据库可能不断增大，耗尽存储空间。

为避免此问题，n8n 建议不保存不必要的数据，并启用旧执行数据清理。

请配置相应的[环境变量](../basic-configuration/use-environment-variables/executions.md)。

## 减少保存的数据 <a href="#reduce-saved-data" id="reduce-saved-data"></a>

{% hint style="info" %}
**工作流级配置**

也可以通过[工作流设置](../../../../build/manage-workflows/configure-workflow-settings.md)，为各个工作流单独配置这些选项。
{% endhint %}
可以选择 n8n 保存哪些执行数据。例如，只保存以 `Error` 结束的执行。

```sh
# npm <a href="#npm" id="npm"></a>
# Save executions ending in errors <a href="#save-executions-ending-in-errors" id="save-executions-ending-in-errors"></a>
export EXECUTIONS_DATA_SAVE_ON_ERROR=all

# Don't save successful executions <a href="#dont-save-successful-executions" id="dont-save-successful-executions"></a>
export EXECUTIONS_DATA_SAVE_ON_SUCCESS=none

# Don't save node progress for each execution <a href="#dont-save-node-progress-for-each-execution" id="dont-save-node-progress-for-each-execution"></a>
export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false

# Don't save manually launched executions <a href="#dont-save-manually-launched-executions" id="dont-save-manually-launched-executions"></a>
export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false

```

```sh
# Docker <a href="#docker" id="docker"></a>
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_SAVE_ON_ERROR=all \
 -e EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \
 -e EXECUTIONS_DATA_SAVE_ON_PROGRESS=true \
 -e EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \
 n8nio/n8n
```

```yaml
# Docker Compose <a href="#docker-compose" id="docker-compose"></a>
n8n:
    environment:
      - EXECUTIONS_DATA_SAVE_ON_ERROR=all
      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=none
      - EXECUTIONS_DATA_SAVE_ON_PROGRESS=true
      - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
```

## 启用执行清理 <a href="#enable-executions-pruning" id="enable-executions-pruning"></a>

执行清理会定期删除已完成的执行及其执行数据和二进制数据。n8n 默认启用清理。出于性能考虑，清理会先将目标标记为待删除，之后再永久移除。

满足以下**任一**条件时，n8n 会清理执行：

- **时间**：执行已结束超过 `EXECUTIONS_DATA_MAX_AGE` 小时，默认 336 小时，即 14 天。
- **数量**：执行总数超过 `EXECUTIONS_DATA_PRUNE_MAX_COUNT`，默认为 10,000。此时 n8n 按从旧到新的顺序删除执行。

请注意：

- 状态为 `new`、`running` 或 `waiting` 的执行不符合清理条件。
- 带注释的执行，例如带有标签或评分的执行，永远不会被清理。
- 清理会遵循 `EXECUTIONS_DATA_HARD_DELETE_BUFFER` 小时的安全缓冲期，默认为 1 小时，确保用户构建或调试工作流时仍可访问近期数据。

```sh
# Enable executions pruning <a href="#enable-executions-pruning" id="enable-executions-pruning"></a>
export EXECUTIONS_DATA_PRUNE=true

# How old (hours) a finished execution must be to qualify for soft-deletion <a href="#how-old-hours-a-finished-execution-must-be-to-qualify-for-soft-deletion" id="how-old-hours-a-finished-execution-must-be-to-qualify-for-soft-deletion"></a>
export EXECUTIONS_DATA_MAX_AGE=168

# Max number of finished executions to keep. May not strictly prune back down to the exact max count. Set to `0` for unlimited. <a href="#max-number-of-finished-executions-to-keep-may-not-strictly-prune-back-down-to-the-exact-max-count-set-to-0-for-unlimited" id="max-number-of-finished-executions-to-keep-may-not-strictly-prune-back-down-to-the-exact-max-count-set-to-0-for-unlimited"></a>
export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

```sh
# Docker <a href="#docker" id="docker"></a>
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_PRUNE=true \
 -e EXECUTIONS_DATA_MAX_AGE=168 \
 n8nio/n8n
```

```yaml
# Docker Compose <a href="#docker-compose" id="docker-compose"></a>
n8n:
    environment:
      - EXECUTIONS_DATA_PRUNE=true
      - EXECUTIONS_DATA_MAX_AGE=168
      - EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

{% hint style="info" %}
**SQLite**

如果使用默认的 SQLite 数据库运行 n8n，已清理数据所占的磁盘空间不会自动释放，而是留给未来的执行数据复用。要释放空间，请配置 `DB_SQLITE_VACUUM_ON_STARTUP` [环境变量](../basic-configuration/use-environment-variables/database.md#sqlite)，或手动执行 [VACUUM](https://www.sqlite.org/lang_vacuum.html) 操作。
{% endhint %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/scaling/binary-data-pruning.md" %}

## 相关资源 <a id="related-resources"></a>

* [扩展](../scaling.md)
* [衡量性能](measure-performance.md)
* [启用队列模式](enable-queue-mode.md)
* [控制并发](control-concurrency.md)
* [处理二进制数据](handle-binary-data.md)
* [使用外部存储](use-external-storage.md)
* [解决内存问题](fix-memory-issues.md)
