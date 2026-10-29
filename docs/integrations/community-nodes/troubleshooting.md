---
contentType: howto
nodeTitle: 故障排查
originalFilePath: integrations/community-nodes/troubleshooting.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/troubleshooting
url: https://docs.n8n.io/integrations/community-nodes/troubleshooting
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 故障排查与错误 <a href="#troubleshooting-and-errors" id="troubleshooting-and-errors"></a>

## 错误：缺少软件包 <a href="#error-missing-packages" id="error-missing-packages"></a>

n8n 将社区节点直接安装到硬盘中，启动时必须能够访问这些文件才能加载节点。如果启动时软件包不可用，就会出现缺少软件包的错误提示。

使用 Docker 运行 n8n 时，根据 Docker 配置的不同，重新创建容器或升级 n8n 可能导致软件包丢失。必须采取以下一种措施：

* 持久化 `~/.n8n/nodes` 目录的内容。这是最佳选择。[Docker 安装](../../deploy/host-n8n/install-options/install-with-docker.md)指南的配置步骤中已包含该目录的持久化设置。
* 将 `N8N_REINSTALL_MISSING_PACKAGES` 环境变量设为 `true`。

第二种方式可能延长启动时间，并导致健康检查失败。

## 阻止 n8n Cloud 加载社区节点 <a href="#prevent-loading-community-nodes-on-n8n-cloud" id="prevent-loading-community-nodes-on-n8n-cloud"></a>

如果 n8n Cloud 实例崩溃且无法启动，可以阻止实例在启动时加载已安装的社区节点。在 [n8n Cloud 控制台](../../deploy/use-n8n-cloud/use-the-cloud-console.md)中，进入 **Instance settings**（实例设置），开启 **Disable all community nodes**（禁用所有社区节点），然后选择 **Save and restart**（保存并重启）。此设置仅在 **Verified community nodes**（经过验证的社区节点）开启时显示。即使实例离线，仍可[通过免密登录链接登录 Cloud 控制台](../../deploy/use-n8n-cloud/use-the-cloud-console.md#open-the-cloud-console-with-a-magic-link)。
