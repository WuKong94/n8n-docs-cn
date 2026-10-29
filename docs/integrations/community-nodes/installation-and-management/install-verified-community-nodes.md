---
contentType: howto
nodeTitle: 安装经过验证的社区节点
originalFilePath: integrations/community-nodes/installation/verified-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/verified-install
url: https://docs.n8n.io/integrations/community-nodes/installation-and-management/install-verified-community-nodes
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
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安装经过验证的社区节点 <a id="install-verified-community-nodes"></a>

{% hint style="info" %}
**仅限 n8n 实例所有者和管理员**

n8n 实例的所有者和管理员账户可以安装和管理经过验证的社区节点。实例所有者是设置和管理用户管理功能的人。实例中的所有成员都可以在自己的工作流中使用已安装的社区节点。
{% endhint %}

## 安装社区节点 <a href="#install-a-community-node" id="install-a-community-node"></a>

安装[经过验证的社区节点](../../../connect/create-nodes/deploy-your-node/submit-community-nodes.md#submit-your-node-for-verification-by-n8n)：

1. 进入 **Canvas**（画布），通过选择“+”或按 ++n++ 打开**节点面板**。
2. **搜索**所需节点。如果有匹配的、经过验证的社区节点，节点面板底部会显示 **More from the community**（更多社区节点）区域。
3. 选择要安装的节点，进入节点详情视图，查看其支持的全部操作。
4. 选择 **install**（安装），将节点安装到实例中，所有成员都能在工作流中使用该节点。
5. 现在可以将节点添加到工作流。

{% hint style="info" %}
**启用经过验证的社区节点安装功能**

如果不希望节点面板显示经过验证的社区节点，请在 [n8n Cloud 控制台](../../../deploy/use-n8n-cloud/use-the-cloud-console.md)的 **Instance settings**（实例设置）中关闭 **Verified community nodes**（经过验证的社区节点）。自行托管时，可以通过[环境变量](../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)控制此功能是否可用。
{% endhint %}

## 卸载社区节点 <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

卸载社区节点：

1. 进入 **Settings**（设置）> **Community nodes**（社区节点）。
2. 在要卸载的节点上，选择 **Options**（选项）<img src="../../.gitbook/assets/three-dot-options-menu (2).png" alt="三点选项菜单" data-size="line">。
3. 选择 **Uninstall package**（卸载软件包）。
4. 在确认弹窗中选择 **Uninstall Package**（卸载软件包）。
