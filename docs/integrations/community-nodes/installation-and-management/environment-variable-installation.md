---
contentType: howto
nodeTitle: 通过环境变量安装
originalFilePath: integrations/community-nodes/installation/env-install.md
originalUrl: https://docs.n8n.io/integrations/community-nodes/installation/env-install
url: https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 通过环境变量管理社区软件包 <a href="#manage-community-packages-from-environment-variables" id="manage-community-packages-from-environment-variables"></a>

{% hint style="info" %}
**功能可用范围**

从 n8n 2.21.0 起，可以通过环境变量管理社区软件包。
{% endhint %}

在自托管 n8n 中，可以通过环境变量管理已安装的社区软件包。每次启动时，n8n 都会将已安装软件包与列表进行核对，安装缺失的软件包、调整版本，并卸载不在列表中的软件包。可以用此方式为实例初始化固定的一组软件包，例如通过部署流水线进行配置。

{% hint style="warning" %}
**启用此功能会卸载不在列表中的软件包**

首次使用 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true` 启动 n8n 时，n8n 会卸载当前已安装但未包含在 `N8N_COMMUNITY_PACKAGES` 中的所有社区软件包。如果已经通过界面管理软件包，请先检查 **Community nodes**（社区节点）设置页，并将希望保留的软件包加入 `N8N_COMMUNITY_PACKAGES`，再启用此变量。
{% endhint %}

## 配置 <a href="#configure" id="configure"></a>

在 n8n 实例上设置以下环境变量，然后重启：

{% include "../../../reusable-content/.gitbook/includes/self-hosting/configuration/environment-variables/settings-env-vars/community-packages.md" %}

{% hint style="info" %}
**必须启用社区软件包**

`N8N_COMMUNITY_PACKAGES_ENABLED` 必须为 `true`（默认值）。如果在实例级别禁用了社区软件包，n8n 会忽略 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`，并在启动时记录警告。
{% endhint %}

例如：

```bash
export N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV=true
export N8N_COMMUNITY_PACKAGES='[{"name":"n8n-nodes-foo","version":"1.2.3"}]'
```

当 `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV` 为 `true` 时，**Community nodes**（社区节点）设置页为只读，无法通过界面安装、更新或卸载软件包。

### 每个软件包的字段 <a href="#per-package-fields" id="per-package-fields"></a>

| 字段 | 类型 | 必填 | 说明 |
| :---- | :--- | :------- | :---------- |
| `name` | string | 是 | npm 软件包名称。可以使用 `<package-name>@<version>` 在名称中直接指定版本；此时不要再将 `version` 字段设为其他版本，n8n 会拒绝冲突的版本设置。 |
| `version` | string | 否 | 版本说明符。省略时，n8n 会在审核通过的软件包注册表（vetted-packages registry）中查找并使用对应版本；如果软件包未经审核，则安装 npm 解析出的版本，并且不会在后续重启时核对和调整版本。 |
| `checksum` | string | 否 | 已解析的软件包压缩文件的 SHA-512 校验和（`sha512-...`）。要求设置 `version`。n8n 会在可能时自动从审核通过的注册表中获取校验和。 |

包含全部三个字段的示例：

```json
[
  { "name": "n8n-nodes-foo", "version": "1.2.3" },
  { "name": "n8n-nodes-bar@0.5.0" },
  { "name": "n8n-nodes-baz", "version": "2.0.0", "checksum": "sha512-..." }
]
```

{% hint style="warning" %}
**未经验证的软件包需要校验和**

如果软件包不在审核通过的软件包注册表中，且 `N8N_UNVERIFIED_PACKAGES_ENABLED` 为 `false`，n8n 将无法启动。请为软件包固定一个 `checksum`、设置 `N8N_UNVERIFIED_PACKAGES_ENABLED=true`，或选择已经审核通过的软件包。
{% endhint %}

支持哪些环境变量设置方式，请参阅[配置方式](../../../deploy/host-n8n/configure-n8n/basic-configuration.md)。

## 管理软件包 <a href="#manage-packages" id="manage-packages"></a>

要添加、移除、升级或降级软件包，请编辑 `N8N_COMMUNITY_PACKAGES` 并重启 n8n。n8n 会在下次启动时按新列表调整软件包。

{% hint style="warning" %}
**版本中的不兼容变更**

节点开发者可能在新版本中引入不兼容变更，即破坏原有功能的更新。切换版本时请谨慎。如果新版本导致问题，请将 `version` 设回原值并重启 n8n，以回滚到之前的版本。
{% endhint %}
