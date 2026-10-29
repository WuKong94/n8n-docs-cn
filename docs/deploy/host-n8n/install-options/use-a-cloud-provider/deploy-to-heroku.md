---
contentType: tutorial
nodeTitle: 部署到 Heroku
originalFilePath: hosting/installation/server-setups/heroku.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/heroku
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Heroku 上托管 n8n <a href="#hosting-n8n-on-heroku" id="hosting-n8n-on-heroku"></a>

本指南介绍如何在 Heroku 上自托管 n8n，采用以下组件：


- [Docker Compose](https://docs.docker.com/compose/)，创建并定义应用组件及其协作方式。
- [Heroku PostgreSQL 服务](https://devcenter.heroku.com/categories/heroku-postgres)，托管 n8n 的数据存储。
- **Deploy to Heroku**（部署到 Heroku）按钮，稍作配置即可一键部署。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/warning.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/latest-next-version.md" %}


## 使用部署模板创建 Heroku 项目 <a href="#use-the-deployment-template-to-create-a-heroku-project" id="use-the-deployment-template-to-create-a-heroku-project"></a>

在 Heroku 部署 n8n，最快的入门方式是使用 **Deploy to Heroku** 按钮：

[![部署](../../../.gitbook/assets/heroku-deploy-button.svg)](https://dashboard.heroku.com/new?template=https://github.com/n8n-io/n8n-heroku/tree/main)

点击后会打开 Heroku 的 **Create New App**（创建新应用）页面。请设置项目名称，并选择部署区域。

### 配置环境变量 <a href="#configure-environment-variables" id="configure-environment-variables"></a>

Heroku 会预填 `env` 部分定义的配置选项，该部分位于 `app.json` 文件中，该文件也为 n8n 使用的环境变量设置默认值。

可按需更改这些值，但必须更改以下选项：

- **N8N_ENCRYPTION_KEY**，n8n 将用户账号详情保存到数据库前，用此密钥[加密](../../configure-n8n/basic-configuration/use-environment-variables/deployment.md)。
- **WEBHOOK_URL**，应与所创建的应用名称匹配，确保 webhook URL 正确。

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

选择 **Deploy app**（部署应用）。

Heroku 构建并部署应用后，会提供 **Manage App**（管理应用）和 **View**（查看应用）链接。

{% hint style="info" %}
**Heroku 与 DNS**

如何将域名连接到 Heroku 应用，请参阅 [Heroku 文档](https://devcenter.heroku.com/categories/networking-dns)。
{% endhint %}

## 更改部署模板 <a href="#changing-the-deployment-template" id="changing-the-deployment-template"></a>

可以派生此[仓库](https://github.com/n8n-io/n8n-heroku)并从派生仓库部署，以修改部署模板。

### Dockerfile <a href="#the-dockerfile" id="the-dockerfile"></a>

Dockerfile 默认拉取最新 n8n 镜像。如果希望使用其他或固定版本，请更新 `Dockerfile` 首行的镜像标签。

### Heroku 与端口暴露 <a href="#heroku-and-exposing-ports" id="heroku-and-exposing-ports"></a>

Heroku 不允许基于 Docker 的应用通过 `EXPOSE` 命令定义暴露端口，而是提供在应用运行时动态填充的 `PORT` 环境变量。`entrypoint.sh` 文件覆盖默认 Docker 镜像命令，改为设置 Heroku 提供的端口变量。随后可在浏览器通过端口 80 访问 n8n。

{% hint style="info" %}
**Heroku 的 Docker 限制**

在 Heroku 使用 Docker 的限制，请[阅读此指南](https://devcenter.heroku.com/articles/container-registry-and-runtime#unsupported-dockerfile-commands)。
{% endhint %}

### 配置 Heroku <a href="#configuring-heroku" id="configuring-heroku"></a>

`heroku.yml` 文件定义要在 Heroku 创建的应用，由两个部分组成：

* `setup` > `addons` 定义要使用的 Heroku 附加组件，此处为 PostgreSQL 数据库附加组件。
* `build` 部分定义 Heroku 如何构建应用。此处使用 Docker buildpack 构建 `web` 服务，依据是提供的 `Dockerfile`。

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/server-setups-next-steps.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Hetzner Cloud](deploy-to-hetzner.md)
* [AWS](deploy-to-aws.md)
* [Azure](deploy-to-azure.md)
* [Google Cloud Run](deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)
* [使用 Docker Compose](use-docker-compose.md)
