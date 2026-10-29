---
description: 将自托管 n8n 部署到云提供商，包括 DigitalOcean、AWS、Azure 和 Google Cloud。
contentType: overview
nodeTitle: 使用云提供商
originalFilePath: hosting/installation/server-setups/index.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用云提供商 <a href="#server-setups" id="server-setups"></a>

## 本节内容 <a id="in-this-section"></a>

使用 Docker Compose 自托管：

* [DigitalOcean](deploy-to-digital-ocean.md)：在 DigitalOcean Droplet 上自托管 n8n，使用真实域名和自动 HTTPS。
* [Heroku](deploy-to-heroku.md)：在 Heroku 上自托管 n8n。
* [Hetzner Cloud](deploy-to-hetzner.md)：在 Hetzner Cloud 服务器上自托管 n8n。

使用 Google Cloud Run 自托管，并让 n8n 工作流工具访问 Gmail、Drive 等 Google Workspace 服务：

* [Google Cloud Run](deploy-to-google-cloud-run.md)：在无服务器容器运行时 Google Cloud Run 上自托管 n8n。

Kubernetes 部署入门方案：

* [AWS](deploy-to-aws.md)：在 Amazon Web Services 上使用 Postgres 和 Kubernetes 自托管 n8n。
* [Azure](deploy-to-azure.md)：在 Azure 上使用 Postgres 和 Kubernetes 自托管 n8n。
* [Google Kubernetes Engine（GKE）](deploy-to-google-kubernetes.md)：在 Google Kubernetes Engine 上自托管 n8n。
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)：在本地 OpenShift 集群中部署 n8n 以供测试，无需云服务费用。

帮助你开始在其他平台上部署的配置指南：

* [Docker Compose](use-docker-compose.md)：使用 Docker Compose 安装并运行 n8n。

## 相关资源 <a id="related-resources"></a>

* [安装方式](../)
* [一行命令安装](../one-line-setup.md)
* [使用 Docker Compose 安装](../install-using-docker-compose.md)
* [使用 npm 安装](../install-with-npm.md)
* [使用 Docker 安装](../install-with-docker.md)
