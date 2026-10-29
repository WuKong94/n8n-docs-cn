---
description: 在 n8n Cloud 上部署或自行托管 n8n，并查阅实例安装、配置和维护指南。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 部署 <a id="deploy"></a>

n8n 提供两种部署方式。[n8n Cloud](use-n8n-cloud/README.md) 提供由 n8n 运营的托管实例，可以快速开始使用。[自托管 n8n](host-n8n/README.md) 则允许你在自己的计算机或基础设施上运行 n8n。

**部署**文档将帮助你在这两种模式下部署、配置、保护和维护 n8n。

<table data-view="cards"><thead><tr><th>部署方式</th><th data-card-target data-type="content-ref">进入章节</th></tr></thead><tbody><tr><td><strong>使用 n8n Cloud</strong><br>由 n8n 托管。快速开始使用，减少运维工作。</td><td><a href="use-n8n-cloud/">使用 n8n Cloud</a></td></tr><tr><td><strong>自托管 n8n</strong><br>通过 Docker、npm、Docker Compose 或受支持的平台自行运行 n8n。</td><td><a href="host-n8n/">托管 n8n</a></td></tr></tbody></table>

### 比较部署方式 <a id="compare-deployment-options"></a>

下面简要介绍两种方式。如果尚未决定，请参阅[选择适合你的 n8n](../get-started/choose-how-to-use-n8n.md)获取更多建议。

#### 使用 n8n Cloud <a id="use-n8n-cloud"></a>

n8n Cloud 是托管方式，由 n8n 为你运行实例。

如果你希望做到以下几点，可以选择 n8n Cloud：

* 以最少的配置快速开始使用
* 减少基础设施和维护工作
* 使用 Cloud 专属的管理和配置工具

{% content-ref url="use-n8n-cloud/" %}
[使用 n8n Cloud](use-n8n-cloud/README.md)
{% endcontent-ref %}

#### 自托管 n8n <a id="self-host-n8n"></a>

自托管让你能够控制 n8n 的运行方式和环境管理方式。

如果你希望做到以下几点，可以选择自托管：

* 在自己的基础设施上运行 n8n
* 精细控制升级、配置和安全设置
* 根据定制的扩展或平台需求设计部署架构

{% hint style="success" %}
**想立即尝试自托管？**

```bash
curl -fsSL https://get.n8n.io | sh
```

需要在 Linux 或 macOS 上安装 Docker（Windows 则使用 WSL）。一条命令即可在本地配置 n8n。详情请参阅[一行命令安装指南](host-n8n/install-options/one-line-setup.md)。
{% endhint %}

<table data-view="cards"><thead><tr><th>自托管主题</th><th data-card-target data-type="content-ref">打开</th></tr></thead><tbody><tr><td><strong>托管 n8n 概览</strong><br>从自托管主页开始。</td><td><a href="host-n8n/">托管 n8n</a></td></tr><tr><td><strong>安装方式</strong><br>使用 Docker、npm、Docker Compose 或云服务商配置 n8n。</td><td><a href="host-n8n/install-options/">安装方式</a></td></tr><tr><td><strong>配置 n8n</strong><br>管理数据库、环境变量、用户、许可和安全设置。</td><td><a href="host-n8n/configure-n8n/">配置 n8n</a></td></tr><tr><td><strong>维护 n8n 运行</strong><br>监控实例，记录日志和追踪信息，并更新实例。</td><td><a href="host-n8n/keep-n8n-running/">维护 n8n 运行</a></td></tr><tr><td><strong>理解架构</strong><br>了解 n8n 的工作原理和数据库结构。</td><td><a href="host-n8n/understand-the-architecture/">理解架构</a></td></tr></tbody></table>

{% content-ref url="host-n8n/" %}
[托管 n8n](host-n8n/README.md)
{% endcontent-ref %}
