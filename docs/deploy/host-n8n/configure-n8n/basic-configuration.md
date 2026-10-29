---
title: 配置方式
description: 如何设置 n8n 的环境变量。
contentType: howto
nodeTitle: 基础配置
originalFilePath: hosting/configuration/configuration-methods.md
originalUrl: https://docs.n8n.io/hosting/configuration/configuration-methods
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 配置 <a href="#configuration" id="configuration"></a>

可以通过环境变量更改 n8n 设置。所有可用配置请参阅[环境变量](basic-configuration/use-environment-variables/README.md)。

## 通过命令行设置环境变量 <a href="#set-environment-variables-by-command-line" id="set-environment-variables-by-command-line"></a>

### npm <a href="#npm" id="npm"></a>

使用 npm 时，在终端中设置所需的环境变量。命令取决于使用的命令行环境。

Bash 命令行：

```bash
export <variable>=<value>
```

在 cmd.exe 中：

```bash
set <variable>=<value>
```

在 PowerShell 中：

```powershell
$env:<variable>=<value>
```

### Docker <a href="#docker" id="docker"></a>

使用 Docker 时，可以通过命令行中的 `-e` 参数设置：

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e N8N_TEMPLATES_ENABLED="false" \
 n8nio/n8n
```


## Docker Compose 文件 <a href="#docker-compose-file" id="docker-compose-file"></a>

在 Docker 中，可以通过 `n8n: environment:` 元素设置环境变量，该元素位于 `docker-compose.yaml` 文件中。

例如：

```yaml
n8n:
    environment:
      - N8N_TEMPLATES_ENABLED=false
```

## 将敏感数据保存在单独的文件中 <a href="#keeping-sensitive-data-in-separate-files" id="keeping-sensitive-data-in-separate-files"></a>

可以为单个环境变量添加 `_FILE` 后缀，改为从单独的文件提供配置，避免通过环境变量直接传递敏感信息。n8n 会从指定文件中加载数据，因此可使用 [Docker secrets](https://docs.docker.com/engine/swarm/secrets/) 和 [Kubernetes secrets](https://kubernetes.io/docs/concepts/configuration/secret/)。

各变量的详情请参阅[环境变量](basic-configuration/use-environment-variables/README.md)。

虽然大多数环境变量都可以使用 `_FILE` 后缀，但对于凭据[^1]和数据库配置等敏感数据更有帮助。以下是一些示例：

```yaml
CREDENTIALS_OVERWRITE_DATA_FILE=/path/to/credentials_data
DB_TYPE_FILE=/path/to/db_type
DB_POSTGRESDB_DATABASE_FILE=/path/to/database_name
DB_POSTGRESDB_HOST_FILE=/path/to/database_host
DB_POSTGRESDB_PORT_FILE=/path/to/database_port
DB_POSTGRESDB_USER_FILE=/path/to/database_user
DB_POSTGRESDB_PASSWORD_FILE=/path/to/database_password
DB_POSTGRESDB_SCHEMA_FILE=/path/to/database_schema
DB_POSTGRESDB_SSL_CA_FILE=/path/to/ssl_ca
DB_POSTGRESDB_SSL_CERT_FILE=/path/to/ssl_cert
DB_POSTGRESDB_SSL_KEY_FILE=/path/to/ssl_key
DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED_FILE=/path/to/ssl_reject_unauth
```

[^1]: 在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，就可以通过相应应用节点与服务交互。

## 本节内容 <a id="in-this-section"></a>

* [环境变量](basic-configuration/use-environment-variables/README.md)：n8n 支持的所有环境变量参考。
* [配置示例](basic-configuration/configuration-examples/README.md)：针对特定使用场景配置 n8n 的示例。

## 相关资源 <a id="related-resources"></a>

* [配置 n8n](./)
