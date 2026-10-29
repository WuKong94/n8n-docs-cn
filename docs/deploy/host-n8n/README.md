---
title: n8n 托管文档与指南
description: 查阅 n8n 托管文档与指南，设置和管理自托管 n8n 实例。
contentType: overview
hide:
- toc
- feedback
- kapaButton
nodeTitle: 托管 n8n
originalFilePath: hosting/index.md
originalUrl: https://docs.n8n.io/hosting
url: https://docs.n8n.io/deploy/
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 自托管 n8n <a href="#self-hosting-n8n" id="self-hosting-n8n"></a>

你可以使用 Docker Compose、一行命令安装或其他部署方式，在自己的基础设施、本地机房或私有云中托管 n8n。不确定自托管是否适合你？请参阅[选择 n8n 的使用方式](../../get-started/choose-how-to-use-n8n.md)。

{% hint style="success" %}
**不想阅读文档？运行这条命令：**

```bash
curl -fsSL https://get.n8n.io | sh
```

需要在 Linux 或 macOS 上安装 Docker（Windows 则使用 WSL）。一条命令即可在本地配置 n8n。请参阅[一行命令安装指南](install-options/one-line-setup.md)了解其操作内容，或继续阅读以比较各种安装方式。
{% endhint %}

所有自托管安装都使用相同的核心产品。没有许可证密钥时，n8n 以免费社区版运行。添加 Business 或 Enterprise 许可证密钥后，即可启用相应版本。各自托管版本的区别，请参阅[比较版本](community-edition-features.md)。

## 本节内容 <a id="in-this-section"></a>

* [安装方式](install-options/README.md)：使用 Docker、npm、Docker Compose 或云服务商配置 n8n。
* [配置 n8n](configure-n8n/README.md)：管理数据库、环境变量、用户、许可和安全设置。
* [维护 n8n 运行](keep-n8n-running/README.md)：监控实例，记录日志和追踪信息，并更新实例。
* [理解架构](understand-the-architecture/README.md)：了解 n8n 的工作原理和数据库结构。
* [以 OEM 集成方式部署](deploy-as-an-oem-integration/README.md)：将 n8n 界面嵌入你自己产品的界面。
* [使用 AI 入门套件部署](deploy-with-the-ai-starter-kit.md)：使用 n8n 精选的自托管 AI 入门套件。
* [比较版本](community-edition-features.md)：比较自托管社区版、Business 和 Enterprise 版本。

## 选择安装方式 <a href="#choose-your-installation-method" id="choose-your-installation-method"></a>

选择最符合技术需求和基础设施条件的安装方式：

- __一行命令安装__

	**适合：** 以最少的配置快速部署。
	
	**要求：** 已安装 curl 的 Linux 或 macOS 系统。
	
	自动安装脚本会为你处理全部依赖和配置。

	[一行命令安装指南](install-options/one-line-setup.md)

- __Docker Compose__

	**适合：** 包含数据库和附加服务的生产部署。
	
	**要求：** 系统已安装 Docker 和 Docker Compose。
	
	多容器配置适合需要持久化数据和扩展能力的稳健部署。

	[Docker Compose 指南](install-options/install-using-docker-compose.md)

- __AWS__

	使用 EC2、ECS 或其他 AWS 服务，在 Amazon Web Services 上部署。

	[AWS 配置指南](install-options/use-a-cloud-provider/deploy-to-aws.md)

- __Azure__

	通过容器实例或虚拟机，在 Microsoft Azure 上托管 n8n。

	[Azure 配置指南](install-options/use-a-cloud-provider/deploy-to-azure.md)

- __Google Cloud__

	使用 Cloud Run 或 Kubernetes Engine，在 Google Cloud 上运行 n8n。

	[Google Cloud Run](install-options/use-a-cloud-provider/deploy-to-google-cloud-run.md) | [Kubernetes Engine](install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md)

- __DigitalOcean__

	基于 Droplet 的简单托管方式，适合中小型部署。

	[DigitalOcean 配置指南](install-options/use-a-cloud-provider/deploy-to-digital-ocean.md)

- __Hetzner__

	性价比较高、性能出色的欧洲托管服务。

	[Hetzner 配置指南](install-options/use-a-cloud-provider/deploy-to-hetzner.md)

- __Heroku__

	平台即服务方案，可用最少配置快速部署。

	[Heroku 配置指南](install-options/use-a-cloud-provider/deploy-to-heroku.md)

- __OpenShift__

	面向容器化应用的企业级 Kubernetes 平台。

	[OpenShift 配置指南](install-options/use-a-cloud-provider/deploy-to-openshift-local-crc.md)

- __npm__

	**适合：** 本地开发或测试。
	
	**要求：** 系统已安装 Node.js。
	
	从 n8n 3.0 开始，npm 安装方式已弃用。请考虑改用 Docker Compose 或一行命令安装。
	
	直接使用 Node Package Manager 安装 n8n。配置快速，但需要自行管理 Node.js 版本和依赖。

	[npm 安装指南](install-options/install-with-npm.md)

## 相关资源 <a id="related-resources"></a>

* [部署](../)
* [使用 n8n Cloud](../use-n8n-cloud/README.md)
