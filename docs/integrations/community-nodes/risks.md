---
contentType: explanation
nodeTitle: 风险
originalFilePath: integrations/community-nodes/risks.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/risks
url: https://docs.n8n.io/integrations/community-nodes/risks
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用社区节点的风险 <a href="#risks-when-using-community-nodes" id="risks-when-using-community-nodes"></a>

从 npm 安装社区节点，意味着向 n8n 实例中安装来自公共来源、未经验证的代码，存在一定风险。

风险包括：

* 系统安全：社区节点可以完全访问运行 n8n 的机器，能够执行任何操作，包括恶意操作。
* 数据安全：你使用的任何社区节点都能够访问工作流中的数据。
* 不兼容变更：节点开发者可能在新版本中引入不兼容变更，即破坏原有功能的更新。根据开发者采用的节点版本控制方式，升级到含有不兼容变更的版本，可能导致所有使用该节点的工作流无法正常运行。升级节点时请谨慎。

{% hint style="info" %}
**n8n 会审核经过验证的社区节点**

除 npm 上公开提供的社区节点外，n8n 还会检查部分节点，并将其作为[经过验证的社区节点提供在节点面板中](installation-and-management/install-verified-community-nodes.md)。这些节点必须符合一组数据安全和系统安全要求才能获得批准。
{% endhint %}

## 举报有问题的社区节点 <a href="#report-bad-community-nodes" id="report-bad-community-nodes"></a>



可以向 [security@n8n.io](mailto: security@n8n.io) 举报有问题的社区节点。



## 禁用社区节点 <a href="#disable-community-nodes" id="disable-community-nodes"></a>

自行托管 n8n 时，可以将 `N8N_COMMUNITY_PACKAGES_ENABLED` 设为 `false` 来禁用社区节点。在 n8n Cloud 中，实例所有者可以在 [n8n Cloud 控制台](../../deploy/use-n8n-cloud/use-the-cloud-console.md)的 **Instance settings**（实例设置）中关闭 **Verified community nodes**（经过验证的社区节点）。更多信息请参阅[故障排查](troubleshooting.md)。
