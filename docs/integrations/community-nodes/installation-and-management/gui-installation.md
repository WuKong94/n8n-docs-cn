---
contentType: howto
nodeTitle: 通过图形界面安装
originalFilePath: integrations/community-nodes/installation/gui-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/gui-install
url: https://docs.n8n.io/integrations/community-nodes/installation-and-management/gui-installation
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


# 通过图形界面安装 <a id="gui-installation"></a>

{% hint style="info" %}
**仅限所有者和管理员用户**

在自托管 n8n 实例中，只有 Owner（所有者）或 Admin（管理员）角色的用户，才能从 npm 安装和管理社区节点。实例所有者是设置和管理用户管理功能的人。
{% endhint %}

## 安装社区节点 <a href="#install-a-community-node" id="install-a-community-node"></a>

从 npm 安装社区节点：

1. 进入 **Settings**（设置）> **Community Nodes**（社区节点）。
2. 选择 **Install**（安装）。
3. 查找要安装的节点：
   1. 选择 **Browse**（浏览）。n8n 会打开 npm 搜索结果页，显示所有带有 `n8n-community-node-package` 关键字的软件包。
   2. 浏览搜索结果，可以筛选结果或添加更多关键字。
   3. 找到所需软件包后，记下软件包名称。如果要安装指定版本，还需记下版本号。
   4. 返回 n8n。
4. 输入 npm 软件包名称，也可以指定版本号或 dist-tag（分发标签）。例如，有一个社区节点用于访问名为 Storms 的天气 API，软件包名为 n8n-node-storms，并且有三个主版本。<br>

    * 要安装名为 n8n-node-weather 的软件包的最新版本：在 **Enter npm package name**（输入 npm 软件包名称）中输入 `n8n-nodes-storms`。

    > 译注：此示例段落将包名分别写作 n8n-node-storms、n8n-node-weather 和 n8n-nodes-storms，彼此不一致。此处保留原始示例，请使用实际要安装的软件包名称，不要假定这三个名称指向同一软件包。
    * 要安装版本 2.3：在 **Enter npm package name**（输入 npm 软件包名称）中输入 `n8n-node-storms@2.3`。
    * 要通过 `beta` 等 dist-tag 安装：在 **Enter npm package name**（输入 npm 软件包名称）中输入 `n8n-node-storms@beta`。可以使用软件包作者发布的任何 [npm dist-tag](https://docs.npmjs.com/cli/commands/npm-dist-tag)，例如 `beta`、`next` 或 `latest`。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>dist-tag 仅在安装时解析一次</strong></p><p>通过 dist-tag 安装软件包时，n8n 会将标签解析为当时对应的版本，后续更新不会继续跟随该标签。例如，安装 <code>n8n-node-storms@beta</code> 时，如果 <code>beta</code> 指向版本 <code>2.0.0-beta.1</code>，n8n 就会安装该具体版本。之后更新时会与已安装的 semver 版本比较，而非跟随 <code>beta</code> 标签。</p></div>
5. 确认接受使用社区节点的[风险](../risks.md)：勾选 **I understand the risks of installing unverified code from a public source.**（我了解从公共来源安装未经验证代码的风险）。
6. 选择 **Install**（安装）。n8n 会安装节点，并返回 **Settings**（设置）中的 **Community Nodes**（社区节点）列表。

{% hint style="info" %}
**屏蔽名单中的节点**

n8n 维护社区节点屏蔽名单，并禁止安装名单中的节点。更多信息请参阅 [n8n 社区节点屏蔽名单](../blocklist.md)。
{% endhint %}

## 卸载社区节点 <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

卸载社区节点：

1. 进入 **Settings**（设置）> **Community nodes**（社区节点）。
2. 在要卸载的节点上，选择 **Options**（选项）<img src="../../.gitbook/assets/three-dot-options-menu (2).png" alt="三点选项菜单" data-size="line">。
3. 选择 **Uninstall package**（卸载软件包）。
4. 在确认弹窗中选择 **Uninstall Package**（卸载软件包）。

## 升级社区节点 <a href="#upgrade-a-community-node" id="upgrade-a-community-node"></a>

{% hint style="warning" %}
**版本中的不兼容变更**

节点开发者可能在新版本中引入不兼容变更，即破坏原有功能的更新。根据开发者采用的节点版本控制方式，升级到含有不兼容变更的版本，可能导致所有使用该节点的工作流无法正常运行。升级时请谨慎；如果升级后出现问题，可以[降级](gui-installation.md#downgrade-a-community-node)。
{% endhint %}

\### 升级到最新版本

可以在 **Settings**（设置）> **community nodes**（社区节点）的节点列表中，将社区节点升级到最新版本。

社区节点有新版本可用时，n8n 会在该节点上显示 **Update**（更新）按钮。单击按钮即可升级到最新版本。

### 升级到指定版本 <a href="#upgrade-to-a-specific-version" id="upgrade-to-a-specific-version"></a>

要升级到指定版本（而非最新版本），先卸载节点，再重新安装，并指定目标版本。更多说明请参阅[安装](gui-installation.md#install-a-community-node)指南。

## 降级社区节点 <a href="#downgrade-a-community-node" id="downgrade-a-community-node"></a>

如果某个版本的社区节点出现问题，可以回滚到之前的版本。

先卸载社区节点，再重新安装并指定所需版本。更多说明请参阅[安装](gui-installation.md#install-a-community-node)指南。
