---
title: 更改实例所有者或用户名
Description: 更改实例所有者或用户名。
contentType: howto
nodeTitle: 更改实例所有者或用户名
originalFilePath: manage-cloud/change-ownership-or-username.md
originalUrl: 'https://docs.n8n.io/manage-cloud/change-ownership-or-username'
url: >-
  https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


## 更改实例所有者 <a href="#change-instance-ownership" id="change-instance-ownership"></a>

要更改实例所有者，请登录所有者账号，进入 **Settings > Personal（设置 > 个人）** 页面，并编辑 **Email（邮箱）** 字段。修改后，向下滚动并点击 **Save（保存）**。
注意，新邮箱地址必须未关联任何其他 n8n 账号，修改才会生效，因为每个实例只能有一个**唯一的所有者邮箱**。如果目标邮箱已关联某个现有用户，请先修改或删除该用户，以释放该邮箱。

更改邮箱会同时更改实例所有者、登录邮箱，以及用于接收发票和一般通信的邮箱。

如果实例已停用，将无法进入 **Settings（设置）** 页面，也无法更改邮箱地址或所有者信息。

## 更改实例用户名 <a href="#change-instance-username" id="change-instance-username"></a>

目前无法更改用户名。

如果希望实例使用不同的名称，需要创建一个新账号，并将已有工作迁移过去。[导入／导出文档](../../../build/manage-workflows/export-and-import.md)说明了如何将已有工作迁移到新的 n8n 实例。

## 相关资源 <a id="related-resources"></a>

* [配置 Cloud](./)
* [设置时区](set-your-timezone.md)
* [查找 IP 地址](find-your-ip-addresses.md)
* [管理数据](manage-your-data.md)
