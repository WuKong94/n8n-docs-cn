---
contentType: tutorial
nodeTitle: 部署到 Hetzner
originalFilePath: hosting/installation/server-setups/hetzner.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/hetzner
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Hetzner Cloud 上托管 n8n <a href="#hosting-n8n-on-hetzner-cloud" id="hosting-n8n-on-hetzner-cloud"></a>

本指南介绍如何在 Hetzner Cloud 服务器上自托管 n8n，采用以下组件：

* [Caddy](https://caddyserver.com)，反向代理，让服务器可以从互联网访问。
* [Docker Compose](https://docs.docker.com/compose/)，创建并定义应用组件及其协作方式。

n8n 启动运行后，最后的可选章节介绍如何添加 n8n Assistant。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/warning.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/latest-next-version.md" %}

## 创建服务器 <a href="#create-a-server" id="create-a-server"></a>

1. [登录](https://console.hetzner.cloud/) Hetzner Cloud 控制台。
2. 选择托管服务器的项目，或点击 **+ NEW PROJECT**（新建项目）创建项目。
3. 在希望添加服务器的项目卡片上，选择 **+ CREATE SERVER**（创建服务器）。

大多数设置可按需更改，但本指南使用 Docker 运行应用，因此请在 **Image**（镜像）区域的 **APPS**（应用）选项卡中，选择 Docker CE。

{% hint style="info" %}
**类型**

创建服务器时，Hetzner 会要求选择套餐。对于大多数使用量，CPX11 类型就足够。如果计划添加 n8n Assistant，请改选至少具有 4 GB RAM 和 2 vCPU 的套餐。添加沙箱后，CPX11 的资源余量不足。
{% endhint %}
{% hint style="info" %}
**SSH 密钥**

Hetzner 支持选择 SSH 或密码身份验证，SSH 更安全。后续步骤假定使用 SSH。
{% endhint %}

## 登录服务器 <a href="#log-in-to-your-server" id="log-in-to-your-server"></a>

后续步骤需要在终端中通过 SSH 登录服务器。更多信息请参阅[通过 SSH、rsync 或 BorgBackup 访问](https://docs.hetzner.com/robot/storage-box/access/access-ssh-rsync-borg)。可在项目的服务器列表中找到公网 IP。

## 安装 Docker Compose <a href="#install-docker-compose" id="install-docker-compose"></a>

Hetzner Docker 应用镜像未安装 Docker Compose。请运行以下命令安装：

```shell
apt update && apt -y upgrade
apt install docker-compose-plugin
```

## 克隆配置仓库 <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Docker Compose、n8n 和 Caddy 需要一系列文件夹和配置文件。可以从[此仓库](https://github.com/n8n-io/n8n-docker-caddy)克隆到服务器 root 用户的主目录。以下步骤说明要更改哪些文件，以及具体修改内容。

使用以下命令克隆仓库：

```shell
git clone https://github.com/n8n-io/n8n-docker-caddy.git
```

然后切换到所克隆仓库的根目录：

```shell
cd n8n-docker-caddy
```

## 默认文件夹和文件 <a href="#default-folders-and-files" id="default-folders-and-files"></a>

主机操作系统，即服务器，将创建的两个文件夹复制到 Docker 容器中，供 Docker 使用。这两个文件夹是：

- `caddy_config`：保存 Caddy 配置文件。
- `local_files`：保存通过 n8n 上传或添加的文件。

### 创建 Docker 卷 <a href="#create-docker-volume" id="create-docker-volume"></a>

要在重启间保留 Caddy 缓存并加快启动，请创建一个可在重启后复用的 [Docker 卷](https://docs.docker.com/storage/volumes/)：

```shell
docker volume create caddy_data
```

为 n8n 数据创建 Docker 卷：

```shell
sudo docker volume create n8n_data
```

## 设置 DNS <a href="#set-up-dns" id="set-up-dns"></a>

n8n 通常运行在子域名上。请在 DNS 提供商处为子域名创建记录，指向服务器 IP 地址。具体步骤取决于 DNS 提供商，通常需要为 n8n 子域名创建 A 记录。DigitalOcean 提供了 [DNS 术语、组件和概念介绍](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts)。

## 开放端口 <a href="#open-ports" id="open-ports"></a>

n8n 作为 Web 应用运行，因此服务器需要允许端口 80 的非加密入站流量，以及端口 443 的加密入站流量。

运行以下两条命令，在服务器防火墙中开放端口：

```shell
sudo ufw allow 80
sudo ufw allow 443
```

{% hint style="info" %} If you add n8n Assistant later, its sandbox services stay internal to the Compose network. You don't need to open any additional ports for them. {% endhint %}

## 配置 n8n <a href="#configure-n8n" id="configure-n8n"></a>

需要为 n8n 设置一些环境变量，并传递给 Docker 容器中的应用。示例 `.env` 文件包含占位符，请替换为你自己的值。

使用以下命令打开文件：

```shell
nano .env
```

文件内包含行内注释，说明需要更改哪些内容。

n8n 环境变量详情请参阅[环境变量](../../configure-n8n/basic-configuration/use-environment-variables/README.md)。

## Docker Compose 文件 <a href="#the-docker-compose-file" id="the-docker-compose-file"></a>

Docker Compose 文件（`docker-compose.yml`）定义应用所需的服务，此处为 Caddy 和 n8n。没有独立数据库服务，n8n 默认使用内置 SQLite 数据库。

- Caddy 服务定义使用的端口，以及要复制到容器中的本地卷。
- n8n 服务定义使用的端口、运行所需的环境变量，其中部分在 `.env` 文件中定义，以及要复制到容器中的卷。

Docker Compose 文件使用 `.env` 文件中设置的环境变量，因此通常无需修改。要查看其内容，请运行：

```shell
nano docker-compose.yml
```

## 配置 Caddy <a href="#configure-caddy" id="configure-caddy"></a>

Caddy 需要知道应提供服务的域名，以及向外暴露的端口。请编辑 `Caddyfile` 文件，它位于 `caddy_config` 文件夹中。

```shell
nano caddy_config/Caddyfile
```

将占位子域名改为你的子域名。如果按照上述步骤将子域名命名为 n8n，完整域名会类似 `n8n.example.com`。`n8n` 位于 `reverse_proxy` 设置中，指示 Caddy 使用 `docker-compose.yml` 文件中定义的服务：

```text
n8n.<domain>.<suffix> {
    reverse_proxy n8n:5678 {
      flush_interval -1
    }
}
```

## 启动 Docker Compose <a href="#start-docker-compose" id="start-docker-compose"></a>

使用以下命令启动 n8n 和 Caddy：

```shell
docker compose up -d
```

这可能需要几分钟。

## 测试配置 <a href="#test-your-setup" id="test-your-setup"></a>

在浏览器中打开前面定义的子域名和域名组成的 URL。输入前面定义的用户名和密码，应能访问 n8n。

## 停止 n8n 和 Caddy <a href="#stop-n8n-and-caddy" id="stop-n8n-and-caddy"></a>

使用以下命令停止 n8n 和 Caddy：

```shell
sudo docker compose stop
```

## 可选：添加 n8n Assistant <a href="#optional-add-n8n-assistant" id="optional-add-n8n-assistant"></a>

n8n Assistant 需要沙箱来运行代码。可以向此部署添加 [Docker Compose 指南](../install-using-docker-compose.md)使用的相同沙箱组件栈。开始前请了解：

* 此沙箱适合本地开发和测试。以下组件栈使用 n8n 自带的沙箱（`n8n-sandbox`）。具有公开域名的 Hetzner Cloud 服务器通常是真实部署，如果要用于生产，请考虑改用 Daytona。
* **按需调整规格。**沙箱运行器使用 Docker-in-Docker，需要比单独运行 n8n 更多的资源余量。请至少提供 4 GB RAM 和 2 vCPU。
* **无需更改网络。**Caddy 仅代理 n8n 本身，沙箱服务保留在 Compose 内部网络，无需更改 DNS、防火墙或 Caddyfile。

1. 将沙箱密钥添加到 `.env`，与现有变量放在一起：

   ```
   # Sandbox service secrets — pick your own values
   SANDBOX_API_KEYS=change-me-api-key
   SANDBOX_API_RUNNER_REGISTRATION_TOKEN=change-me-registration-token
   SANDBOX_API_RUNNER_API_KEY=change-me-runner-key

   # Web search: secret for the bundled SearXNG instance — pick your own value
   SEARXNG_SECRET=change-me-searxng-secret
   ```

2. 在其他配置文件旁创建 `searxng-settings.yml` 文件。默认 SearXNG 镜像仅提供 HTML，此配置启用 n8n 网页搜索需要的 JSON API：

   ``` yaml
   use_default_settings: true
   search:
     formats:
       - html
       - json
   ```

3. 打开 `docker-compose.yml`，在现有 `caddy` 和 `n8n` 服务旁添加沙箱和搜索服务：

   ```yaml
   volumes:
     sandbox-tls:

   services:
     sandbox-certs:
       image: ghcr.io/n8n-io/n8n-sandbox-service-api:latest
       user: '0:0'
       entrypoint: ['sh', '-c']
       command:
         - >
           bootstrap-mtls.sh --out-dir /tls --api-san sandbox-api
           --control-san-prefix sandbox-runner &&
           chown -R sandbox-api:sandbox-api /tls/api
       environment:
         NUM_RUNNERS: '1'
       volumes:
         - sandbox-tls:/tls

     sandbox-api:
       image: ghcr.io/n8n-io/n8n-sandbox-service-api:latest
       depends_on:
         sandbox-certs:
           condition: service_completed_successfully
       environment:
         SANDBOX_API_KEYS: ${SANDBOX_API_KEYS}
         SANDBOX_API_RUNNER_REGISTRATION_TOKEN: ${SANDBOX_API_RUNNER_REGISTRATION_TOKEN}
         SANDBOX_API_RUNNER_API_KEY: ${SANDBOX_API_RUNNER_API_KEY}
         SANDBOX_API_GRPC_TLS_CERT_FILE: /tls/api/grpc-server.crt
         SANDBOX_API_GRPC_TLS_KEY_FILE: /tls/api/grpc-server.key
         SANDBOX_API_GRPC_TLS_CLIENT_CA_FILE: /tls/api/ca.crt
         SANDBOX_API_RUNNER_CONTROL_GRPC_TLS_CA_FILE: /tls/api/ca.crt
         SANDBOX_API_RUNNER_CONTROL_GRPC_TLS_CERT_FILE: /tls/api/control-grpc-api-client.crt
         SANDBOX_API_RUNNER_CONTROL_GRPC_TLS_KEY_FILE: /tls/api/control-grpc-api-client.key
         SANDBOX_API_RUNNER_CONTROL_GRPC_TLS_SERVER_NAME: sandbox-runner-1
       volumes:
         - sandbox-tls:/tls:ro
       healthcheck:
         test: ["CMD", "wget", "-qO-", "http://localhost:8080/healthz"]
         interval: 5s
         timeout: 3s
         retries: 5
         start_period: 10s
       # Never publish 8080/9090 — Caddy never routes to this service, and it shouldn't.

     sandbox-runner-1:
       image: ghcr.io/n8n-io/n8n-sandbox-service-runner-dind:latest
       privileged: true
       depends_on:
         sandbox-api:
           condition: service_healthy
       environment:
         SANDBOX_RUNNER_API_KEYS: ${SANDBOX_API_RUNNER_API_KEY}
         SANDBOX_RUNNER_REGISTRATION_TOKEN: ${SANDBOX_API_RUNNER_REGISTRATION_TOKEN}
         SANDBOX_RUNNER_API_GRPC_ADDR: sandbox-api:9090
         SANDBOX_RUNNER_HTTP_BASE_URL: http://sandbox-runner-1:8080
         SANDBOX_RUNNER_CONTROL_GRPC_LISTEN_ADDR: ':9091'
         SANDBOX_RUNNER_CONTROL_GRPC_ADVERTISE_ADDR: sandbox-runner-1:9091
         SANDBOX_RUNNER_ID: runner-1
         SANDBOX_RUNNER_DOCKER_SANDBOX_IMAGE: ghcr.io/n8n-io/n8n-sandbox-service-sandbox:latest
         SANDBOX_RUNNER_REGISTRATION_GRPC_CA_FILE: /tls/runner/ca.crt
         SANDBOX_RUNNER_REGISTRATION_GRPC_CERT_FILE: /tls/runner/grpc-client.crt
         SANDBOX_RUNNER_REGISTRATION_GRPC_KEY_FILE: /tls/runner/grpc-client.key
         SANDBOX_RUNNER_REGISTRATION_GRPC_SERVER_NAME: sandbox-api
         SANDBOX_RUNNER_CONTROL_GRPC_TLS_CERT_FILE: /tls/runner/control-grpc-server.crt
         SANDBOX_RUNNER_CONTROL_GRPC_TLS_KEY_FILE: /tls/runner/control-grpc-server.key
         SANDBOX_RUNNER_CONTROL_GRPC_TLS_CLIENT_CA_FILE: /tls/runner/ca.crt
       volumes:
         - sandbox-tls:/tls:ro
       # Never expose this container's ports publicly — it runs privileged Docker-in-Docker.

     searxng:
       image: ghcr.io/searxng/searxng:latest
       environment:
         SEARXNG_SECRET: ${SEARXNG_SECRET}
       volumes:
         - ./searxng-settings.yml:/etc/searxng/settings.yml:ro
       # Internal-only: n8n reaches it by service name. Never publish its port, and don't route Caddy to it.
   ```

4. 在现有 `n8n` 服务的 `environment` 块中添加匹配的沙箱变量：

   ```yaml
   environment:
    # ...your existing N8N_HOST, N8N_PORT, etc. stay as they are
    - N8N_ENABLED_MODULES=instance-ai
    - N8N_INSTANCE_AI_SANDBOX_ENABLED=true
    - N8N_INSTANCE_AI_SANDBOX_PROVIDER=n8n-sandbox
    - N8N_SANDBOX_SERVICE_URL=http://sandbox-api:8080
    - N8N_SANDBOX_SERVICE_API_KEY=${SANDBOX_API_KEYS}
    - N8N_INSTANCE_AI_SEARXNG_URL=http://searxng:8080
   depends_on:
    sandbox-api:
      condition: service_healthy
   ```

5. 重启全部服务，让新服务加载更改：

   ```bash
   sudo docker compose up -d
   ```

6. 添加模型 API 密钥。完整参考及模型提供商选择，请参阅[设置 n8n Assistant](../../configure-n8n/set-up-n8n-assistant.md)。网页搜索可直接使用上方内置的 SearXNG 服务；如果更喜欢 Brave Search，可改为添加其密钥。

{% hint style="warning" %}
将服务器暴露到互联网之前，请将 `change-me-...` 占位符替换为你自己的唯一密钥，占位符位于 `.env` 中。`sandbox-runner-1` 以特权模式运行 Docker-in-Docker。不要公开其端口，也不要让 Caddy 路由到它。
{% endhint %}

## 更新 <a href="#updating" id="updating"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/docker-compose-updating.md" %}

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/server-setups-next-steps.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Heroku](deploy-to-heroku.md)
* [AWS](deploy-to-aws.md)
* [Azure](deploy-to-azure.md)
* [Google Cloud Run](deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)
* [使用 Docker Compose](use-docker-compose.md)
