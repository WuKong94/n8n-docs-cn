---
contentType: howto
nodeTitle: 手动安装
originalFilePath: integrations/community-nodes/installation/manual-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/manual-install
url: https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 从 npm 手动安装社区节点 <a href="#manually-install-community-nodes-from-npm" id="manually-install-community-nodes-from-npm"></a>

在自托管 n8n 中，可以从 npm 注册表手动安装社区节点。

以下情况需要手动安装社区节点：

* n8n 实例以队列模式运行。
* 希望安装[私有软件包](https://docs.npmjs.com/creating-and-publishing-private-packages)。

## 安装社区节点 <a href="#install-a-community-node" id="install-a-community-node"></a>

进入 Docker 容器的 shell：

```sh
docker exec -it n8n sh
```

如果 `~/.n8n/nodes` 不存在，请创建该目录，然后进入其中：

```sh
mkdir ~/.n8n/nodes
cd ~/.n8n/nodes
```

安装节点：

```sh
npm i n8n-nodes-nodeName
```

然后重启 n8n。

## 卸载社区节点 <a href="#uninstall-a-community-node" id="uninstall-a-community-node"></a>

进入 Docker 容器的 shell：

```sh
docker exec -it n8n sh
```

运行 npm uninstall：

```sh
npm uninstall n8n-nodes-nodeName
```

## 升级社区节点 <a href="#upgrade-a-community-node" id="upgrade-a-community-node"></a>

{% hint style="warning" %}
**版本中的不兼容变更**

节点开发者可能在新版本中引入不兼容变更，即破坏原有功能的更新。根据开发者采用的节点版本控制方式，升级到含有不兼容变更的版本，可能导致所有使用该节点的工作流无法正常运行。升级时请谨慎；如果升级后出现问题，可以[降级](#upgrade-or-downgrade-to-a-specific-version)。
{% endhint %}

### 升级到最新版本 <a href="#upgrade-to-the-latest-version" id="upgrade-to-the-latest-version"></a>

进入 Docker 容器的 shell：

```sh
docker exec -it n8n sh
```

运行 npm update：

```sh
npm update n8n-nodes-nodeName
```

### 升级或降级到指定版本 <a href="#upgrade-or-downgrade-to-a-specific-version" id="upgrade-or-downgrade-to-a-specific-version"></a>

进入 Docker 容器的 shell：

```sh
docker exec -it n8n sh
```

运行 npm uninstall，移除当前版本：

```sh
npm uninstall n8n-nodes-nodeName
```

运行 npm install，并指定版本：

```sh
# Replace 2.1.0 with your version number <a href="#replace-210-with-your-version-number" id="replace-210-with-your-version-number"></a>
npm install n8n-nodes-nodeName@2.1.0
```
