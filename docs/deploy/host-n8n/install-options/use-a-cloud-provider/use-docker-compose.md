---
contentType: tutorial
description: 使用 Docker Compose 安装并运行 n8n。
nodeTitle: 使用 Docker Compose
originalFilePath: hosting/installation/server-setups/docker-compose.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/docker-compose
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Docker Compose <a href="#docker-compose" id="docker-compose"></a>

以下说明介绍如何在 Linux 服务器上使用 Docker Compose 运行 n8n。

如果已安装 Docker 和 Docker Compose，可以从[第 3 步](#3-dns-setup)开始。

不同架构的 Docker Compose 配置，可在 [n8n-hosting 仓库](https://github.com/n8n-io/n8n-hosting)找到。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/warning.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/latest-next-version.md" %}

## 1. 安装 Docker 和 Docker Compose <a href="#1-install-docker-and-docker-compose" id="1-install-docker-and-docker-compose"></a>

Docker 和 Docker Compose 的安装方式取决于 Linux 发行版。各组件的具体安装步骤见以下链接：

* [Docker Engine](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/linux/)

按说明安装后，输入以下命令验证 Docker 和 Docker Compose 是否可用：

```shell
docker --version
docker compose version
```

## 2. 可选：非 root 用户访问 <a href="#2-optional-non-root-user-access" id="2-optional-non-root-user-access"></a>

可以按需授予无需 `sudo` 命令即可运行 Docker 的权限。

要为当前登录用户授予访问权限，假定该用户拥有 `sudo` 权限，请运行：

```shell
sudo usermod -aG docker ${USER}
# Register the `docker` group membership with current session without changing your primary group <a href="#register-the-docker-group-membership-with-current-session-without-changing-your-primary-group" id="register-the-docker-group-membership-with-current-session-without-changing-your-primary-group"></a>
exec sg docker newgrp
```

要为其他用户授予访问权限，请输入以下命令，将 `<USER_TO_RUN_DOCKER>` 替换为对应用户名：

```shell
sudo usermod -aG docker <USER_TO_RUN_DOCKER>
```

对于该用户已打开的会话，需要运行 `exec sg docker newgrp`，才能使用新的用户组权限。

输入以下命令，确认当前会话识别 `docker` 用户组：

```shell
groups
```

## 3. 设置 DNS <a href="#3-dns-setup" id="3-dns-setup"></a>

要在互联网或网络中托管 n8n，请创建指向服务器的专用子域名。

添加 A 记录，将子域名路由到对应地址：

| 记录类型 | 名称 | 目标 |
|-------------|-----------------------------------|----------------------------|
| A | `n8n`，或你希望使用的子域名 | `<your_server_IP_address>` |

## 4. 创建 `.env` 文件 <a href="#4-create-an-env-file" id="4-create-an-env-file"></a>

创建项目目录，用于保存 n8n 环境配置和 Docker Compose 文件，并进入目录：

```shell
mkdir n8n-compose
cd n8n-compose
```

在 `n8n-compose` 目录中创建 `.env` 文件，定制 n8n 实例详情。请更改为你自己的信息：

```shell title=".env 文件"
# DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from <a href="#domainname-and-subdomain-together-determine-where-n8n-will-be-reachable-from" id="domainname-and-subdomain-together-determine-where-n8n-will-be-reachable-from"></a>
# The top level domain to serve from <a href="#the-top-level-domain-to-serve-from" id="the-top-level-domain-to-serve-from"></a>
DOMAIN_NAME=example.com

# The subdomain to serve from <a href="#the-subdomain-to-serve-from" id="the-subdomain-to-serve-from"></a>
SUBDOMAIN=n8n

# The above example serve n8n at: https://n8n.example.com <a href="#the-above-example-serve-n8n-at-httpsn8nexamplecom" id="the-above-example-serve-n8n-at-httpsn8nexamplecom"></a>

# Optional timezone to set which gets used by Cron and other scheduling nodes <a href="#optional-timezone-to-set-which-gets-used-by-cron-and-other-scheduling-nodes" id="optional-timezone-to-set-which-gets-used-by-cron-and-other-scheduling-nodes"></a>
# New York is the default value if not set <a href="#new-york-is-the-default-value-if-not-set" id="new-york-is-the-default-value-if-not-set"></a>
GENERIC_TIMEZONE=Europe/Berlin

# The email address to use for the TLS/SSL certificate creation <a href="#the-email-address-to-use-for-the-tlsssl-certificate-creation" id="the-email-address-to-use-for-the-tlsssl-certificate-creation"></a>
SSL_EMAIL=user@example.com
```

## 5. 创建本地文件目录 <a href="#5-create-local-files-directory" id="5-create-local-files-directory"></a>

在项目目录中创建名为 `local-files` 的目录，用于在 n8n 实例和主机系统间共享文件，例如通过 [Read/Write Files from Disk 节点](../../../../integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)：

```shell
mkdir local-files
```

下方 Docker Compose 文件可以自动创建此目录，但手动创建可确保所有权和权限正确。

## 6. 创建 Docker Compose 文件 <a href="#6-create-docker-compose-file" id="6-create-docker-compose-file"></a>

创建 `compose.yaml` 文件，粘贴以下内容：

```yaml title="compose.yaml 文件"
services:
  traefik:
    image: "traefik"
    restart: always
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.web.http.redirections.entryPoint.to=websecure"
      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.mytlschallenge.acme.tlschallenge=true"
      - "--certificatesresolvers.mytlschallenge.acme.email=${SSL_EMAIL}"
      - "--certificatesresolvers.mytlschallenge.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - traefik_data:/letsencrypt
      - /var/run/docker.sock:/var/run/docker.sock:ro

  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "127.0.0.1:5678:5678"
    labels:
      - traefik.enable=true
      - traefik.http.routers.n8n.rule=Host(`${SUBDOMAIN}.${DOMAIN_NAME}`)
      - traefik.http.routers.n8n.tls=true
      - traefik.http.routers.n8n.entrypoints=web,websecure
      - traefik.http.routers.n8n.tls.certresolver=mytlschallenge
      - traefik.http.middlewares.n8n.headers.SSLRedirect=true
      - traefik.http.middlewares.n8n.headers.STSSeconds=315360000
      - traefik.http.middlewares.n8n.headers.browserXSSFilter=true
      - traefik.http.middlewares.n8n.headers.contentTypeNosniff=true
      - traefik.http.middlewares.n8n.headers.forceSTSHeader=true
      - traefik.http.middlewares.n8n.headers.SSLHost=${DOMAIN_NAME}
      - traefik.http.middlewares.n8n.headers.STSIncludeSubdomains=true
      - traefik.http.middlewares.n8n.headers.STSPreload=true
      - traefik.http.routers.n8n.middlewares=n8n@docker
    environment:
      - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
      - N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https  
      - NODE_ENV=production
      - N8N_WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - TZ=${GENERIC_TIMEZONE}
      - N8N_RESTRICT_FILE_ACCESS_TO=/files
    volumes:
      - n8n_data:/home/node/.n8n
      - ./local-files:/files

volumes:
  n8n_data:
  traefik_data:
```

自 n8n 2.30.0 起可使用 `N8N_WEBHOOK_URL`，更早版本请使用 `WEBHOOK_URL`。

上述 Docker Compose 文件配置两个容器：一个运行 n8n，另一个运行应用代理 [Traefik](https://github.com/traefik/traefik)，管理 TLS/SSL 证书和路由。

它还创建并挂载两个 [Docker 卷](https://docs.docker.com/engine/storage/volumes/)，以及前面创建的 `local-files` 目录：

| 名称 | 类型 | 容器挂载位置 | 说明 |
|-----------------|-------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `n8n_data` | [卷](https://docs.docker.com/engine/storage/volumes/) | `/home/node/.n8n` | n8n 保存 SQLite 数据库文件和加密密钥的位置。 |
| `traefik_data` | [卷](https://docs.docker.com/engine/storage/volumes/) | `/letsencrypt` | Traefik 保存 TLS/SSL 证书数据的位置。 |
| `./local-files` | [绑定挂载](https://docs.docker.com/engine/storage/bind-mounts/) | `/files` | n8n 实例与主机共享的本地目录。在 n8n 中，使用 `/files` 路径读写此目录。 |

## 7. 启动 Docker Compose <a href="#7-start-docker-compose" id="7-start-docker-compose"></a>

输入以下命令启动 n8n：

```shell
sudo docker compose up -d
```

要停止容器，请输入：

```shell
sudo docker compose stop
```

## 8. 完成 <a href="#8-done" id="8-done"></a>

现在可以使用 `.env` 文件中配置的子域名和域名组合访问 n8n。上述示例的地址为 `https://n8n.example.com`。

只能通过安全的 HTTPS 访问 n8n，不支持普通 HTTP。

如果无法访问实例，请检查服务器防火墙设置和 DNS 配置。

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/server-setups-next-steps.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Heroku](deploy-to-heroku.md)
* [Hetzner Cloud](deploy-to-hetzner.md)
* [AWS](deploy-to-aws.md)
* [Azure](deploy-to-azure.md)
* [Google Cloud Run](deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)
