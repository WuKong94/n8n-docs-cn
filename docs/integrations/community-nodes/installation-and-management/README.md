---
contentType: overview
nodeTitle: 安装与管理
originalFilePath: integrations/community-nodes/installation/index.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation
url: https://docs.n8n.io/integrations/community-nodes/installation-and-management
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安装和管理社区节点 <a href="#install-and-manage-community-nodes" id="install-and-manage-community-nodes"></a>

社区节点有四种安装方式：

* 在 n8n 中通过[节点面板](install-verified-community-nodes.md)安装，仅适用于经过验证的社区节点。
* 在 n8n 中[通过图形界面](gui-installation.md)安装：从 npm 注册表安装社区节点。
* [通过命令行手动安装](manual-installation.md)：如果 n8n 实例不支持通过应用内图形界面安装，可使用此方式从 npm 安装社区节点。
* [通过环境变量安装](environment-variable-installation.md)：用固定的一组社区软件包初始化实例，例如通过部署流水线进行配置。

{% hint style="info" %}
**仅自托管实例支持从 npm 安装**

n8n Cloud 不支持未经验证的社区节点，必须[自行托管](../../../deploy/host-n8n/README.md) n8n 才能使用。
{% endhint %}
