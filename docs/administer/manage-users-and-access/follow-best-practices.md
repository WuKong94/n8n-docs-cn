---
description: 用户管理最佳实践。
contentType: explanation
nodeTitle: 遵循最佳实践
originalFilePath: user-management/best-practices.md
originalUrl: https://docs.n8n.io/user-management/best-practices
url: https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 用户管理最佳实践 <a href="#best-practices-for-user-management" id="best-practices-for-user-management"></a>

本页提供 n8n 用户管理的最佳实践建议。

## 所有平台 <a href="#all-platforms" id="all-platforms"></a>

* n8n 建议所有者为自己创建成员级账号。所有者能查看全部工作流，但无法查看特定工作流的创建者，因此以所有者身份构建和编辑工作流，可能覆盖其他人的工作。
* 用户应避免同时编辑同一工作流。虽然可以这样操作，但会相互覆盖更改。
* 要在账号间迁移工作流，请导出为 JSON，再导入新账号。此操作会丢失工作流历史。
* Webhook 路径必须在整个实例中唯一，即所有用户的所有工作流都不能使用重复路径。n8n 默认生成较长的随机路径值，但用户可改为自定义路径。如果两个用户设置相同路径：
    * 路径对最先运行或发布的工作流有效。
    * 其他工作流尝试使用相同路径运行时会报错。

## 自托管 <a href="#self-hosted" id="self-hosted"></a>

如果 n8n 位于反向代理之后，请设置以下环境变量，确保生成的邮件包含正确 URL：

* `N8N_HOST`
* `N8N_PORT`
* `N8N_PROTOCOL`
* `N8N_EDITOR_BASE_URL`  

这些变量的更多信息请参阅[环境变量](../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)。

## 相关资源 <a id="related-resources"></a>

* [管理用户与访问](./)
* [设置 Cloud 用户管理](set-up-for-cloud.md)
* [添加和移除用户](add-and-remove-users.md)
* [理解实例角色](understand-instance-roles.md)
* [设置权限与角色（RBAC）](set-permissions-and-roles-rbac/README.md)
* [验证用户身份](verify-user-identity/README.md)

