---
description: 阻止用户通过界面修改生产等仅应用变更的实例。
status: preview
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 保护生产实例 <a id="protect-a-production-instance"></a>

在生产等仅应用变更的实例上，进入 **Settings（设置）** > **Environments（环境）**，开启 **Protected instance（受保护实例）**。

{% hint style="info" %}
**预览状态**

环境管理处于预览阶段，未来版本可能更改。在为生产实例设置此功能前，请先在测试实例上试用。
{% endhint %}

**Protected instance（受保护实例）**会阻止用户在界面中执行以下操作：

- 编辑工作流，或创建工作流、凭据、项目、文件夹、变量和数据表。
- 手动运行工作流。已发布的工作流仍会通过触发器运行。
- 修改数据表列。

用户仍然可以：

- 编辑已有凭据、变量值和数据表行。
- 在解决应用阻碍问题时创建缺失的凭据和变量。
- 从应用变更的来源环境添加缺失项目。
- 发布和取消发布工作流。
- 晋级和应用变更。

公共 API 仍允许大多数其他修改。

经典环境使用同一设置。开启或关闭此设置会同时影响两者。

## 相关资源 <a id="related-resources"></a>

- [环境管理](./)
- [规划环境](plan-your-environments.md)
- [首次晋级](first-promotion.md)
- [晋级变更](promote-changes.md)
- [应用变更](apply-changes.md)
- [晋级审核](promotion-reviews.md)
- [基于 Git 的晋级](git-based-promotion/README.md)
- [已知限制](known-limitations.md)
- [从经典环境升级](upgrade-from-environments-classic.md)
