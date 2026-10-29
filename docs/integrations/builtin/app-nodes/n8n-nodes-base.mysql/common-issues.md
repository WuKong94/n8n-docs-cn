---
title: MySQL 节点常见问题
description: 了解 n8n 工作流自动化平台中 MySQL 节点的常见错误和问题，包括问题详情及建议的解决方法。
contentType:
- integration
- reference
priority: high
nodeTitle: MySQL 节点常见问题
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# MySQL 节点常见问题 <a href="#mysql-node-common-issues" id="mysql-node-common-issues"></a>

以下介绍 [MySQL 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 按复合键更新行 <a href="#update-rows-by-composite-key" id="update-rows-by-composite-key"></a>

MySQL 节点的 **Update**（更新）操作通过指定 **Column to Match On**（匹配列）及其值来更新表中的行。此方式适用于单列值能唯一标识每一行的表。

对于使用[复合键](https://en.wikipedia.org/wiki/Composite_key)的表，必须通过多列才能唯一标识一行，因此无法使用上述方式。例如，MySQL 的 [`user` 表](https://mariadb.com/kb/en/mysql-user-table/)位于 `mysql` 数据库，需要同时使用 `user` 和 `host` 列才能唯一标识行。

要更新具有复合键的表，请改用 **Execute SQL**（执行 SQL）操作，手动编写查询。这样可以同时匹配多个值，例如以下查询同时匹配 `customer_id` 和 `product_id`：

```sql
UPDATE orders SET quantity = 3 WHERE customer_id = 538 AND product_id = 800;
```

## 使用 Docker 时无法连接本地 MySQL 服务器 <a href="#cant-connect-to-a-local-mysql-server-when-using-docker" id="cant-connect-to-a-local-mysql-server-when-using-docker"></a>

在 Docker 中运行 n8n 或 MySQL 时，需要配置网络，使 n8n 能够连接到 MySQL。

解决方法取决于两个组件的托管方式。

### 仅 MySQL 在 Docker 中运行 <a href="#if-only-mysql-is-in-docker" id="if-only-mysql-is-in-docker"></a>

如果仅 MySQL 在 Docker 中运行，请在容器内将 MySQL 绑定到 `0.0.0.0`，使其监听所有网络接口，官方镜像已这样配置。

运行容器时，使用 `-p` 标志[发布端口](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)。MySQL 默认运行在 3306 端口，因此 Docker 命令应类似于：

```shell
docker run -p 3306:3306 --name my-mysql -d mysql:latest
```

配置 [MySQL 凭据](../../credentials/mysql.md)时，`localhost` 地址应能正常工作，将 **Host**（主机）设为 `localhost` 即可。

### 仅 n8n 在 Docker 中运行 <a href="#if-only-n8n-is-in-docker" id="if-only-n8n-is-in-docker"></a>

如果仅 n8n 在 Docker 中运行，请在宿主机上将 MySQL 绑定到 `0.0.0.0`，使其监听所有网络接口。

如果在 **Linux** 上通过 Docker 运行 n8n，请在启动容器时使用 `--add-host` 标志，将 `host.docker.internal` 映射到 `host-gateway`。例如：

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

如果使用 Docker Desktop，此映射会自动配置。

配置 [MySQL 凭据](../../credentials/mysql.md)时，请将 **Host**（主机）地址设为 `host.docker.internal`，而非 `localhost`。

### MySQL 与 n8n 在不同的 Docker 容器中运行 <a href="#if-mysql-and-n8n-are-running-in-separate-docker-containers" id="if-mysql-and-n8n-are-running-in-separate-docker-containers"></a>

如果 n8n 和 MySQL 均在 Docker 中运行，且位于不同容器，可使用 Docker 网络连接它们。

在容器内将 MySQL 绑定到 `0.0.0.0`，使其监听所有网络接口，官方镜像已这样配置。将 MySQL 和 n8n 容器加入同一个[用户自定义桥接网络](https://docs.docker.com/engine/network/drivers/bridge/)。

配置 [MySQL 凭据](../../credentials/mysql.md)时，请使用 MySQL 容器名称作为主机地址，而非 `localhost`。例如，如果 MySQL 容器名为 `my-mysql`，请将 **Host**（主机）设为 `my-mysql`。

### MySQL 与 n8n 在同一个 Docker 容器中运行 <a href="#if-mysql-and-n8n-are-running-in-the-same-docker-container" id="if-mysql-and-n8n-are-running-in-the-same-docker-container"></a>

如果 MySQL 和 n8n 在同一个 Docker 容器中运行，`localhost` 地址无需特殊配置。可让 MySQL 监听 `localhost`，并将 [n8n 中的 MySQL 凭据](../../credentials/ollama.md)的 **Host**（主机）设为 `localhost`。

## 小数以字符串形式返回 <a href="#decimal-numbers-returned-as-strings" id="decimal-numbers-returned-as-strings"></a>

默认情况下，MySQL 节点将 [`DECIMAL` 值](https://dev.mysql.com/doc/refman/8.4/en/fixed-point-types.html)作为字符串返回。这是为了避免 JavaScript 数字表示方式的限制导致精度损失。有关该设计决定的更多信息，请参阅 n8n 所用 [MySQL 库的文档](https://sidorares.github.io/node-mysql2/docs/api-and-configurations)。

如果希望将小数作为数字而非字符串输出，并接受可能的精度损失，请启用 **Output Decimals as Numbers**（将小数输出为数字）选项。开启后，值将作为数字输出。

也可使用 `toFloat()` 函数结合 [`toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)，或在 MySQL 节点后使用 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md)（编辑字段）节点，手动将字符串转换为小数。请注意，这仍可能需要考虑精度损失。
