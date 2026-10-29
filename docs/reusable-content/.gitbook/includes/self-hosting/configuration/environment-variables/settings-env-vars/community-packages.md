---
title: 社区节点包
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

| 变量 | 类型 | 默认值 | 说明 |
| :------- | :--- | :------ | :---------- |
| `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` | Boolean | `false` | 设为 `true`，通过环境变量管理已安装的社区节点包。当值为 `true` 时，n8n 会在每次启动时根据 `N8N_COMMUNITY_PACKAGES` 校正已安装的包：安装缺失的包、纠正版本，并**卸载当前已安装但不在列表中的所有包**。**Community nodes（社区节点）**设置页会变为只读，启用期间无法通过界面安装、更新或卸载包。 |
| `N8N_COMMUNITY_PACKAGES` | JSON 字符串 | - | 要安装的社区节点包的 JSON 数组。每项是一个对象，包含必需的 `name` 字段，以及可选的 `version` 和 `checksum` 字段。也可以通过 `<package-name>@<version>` 形式，将版本写在名称中。完整字段参考请参阅[通过环境变量安装](../../../../../../../integrations/community-nodes/installation-and-management/environment-variable-installation.md)。 |
