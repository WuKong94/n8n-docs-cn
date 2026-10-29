---
title: GitHub 触发器节点文档
description: 了解如何在 n8n 中使用 GitHub 触发器节点，并按照技术文档将其集成到工作流中。
contentType:
- integration
- reference
priority: medium
nodeTitle: GitHub 触发器节点文档
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md
originalUrl: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger
url: https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# GitHub 触发器节点 <a href="#github-trigger-node" id="github-trigger-node"></a>

[GitHub](https://github.com/) 提供基于 Git 的软件开发和版本控制托管服务。它提供 Git 的分布式版本控制和源代码管理（SCM）功能、访问控制，以及每个项目的缺陷跟踪、功能请求、任务管理和 Wiki 等协作功能。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [GitHub 凭据文档](../credentials/github.md)。
{% endhint %}

{% hint style="info" %}
**示例与模板**

入门用法示例和模板，请参阅 n8n 的 [GitHub Trigger 集成](https://n8n.io/integrations/github-trigger/)页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Check run（检查运行）
* Check suite（检查套件）
* Commit comment（提交评论）
* Create（创建）
* Delete（删除）
* Deploy key（部署密钥）
* Deployment（部署）
* Deployment status（部署状态）
* Fork（派生仓库）
* GitHub app authorization（GitHub 应用授权）
* Gollum（Wiki 页面变更）
* Installation（应用安装）
* Installation repositories（应用安装的仓库）
* Issue comment（议题评论）
* Label（标签）
* Marketplace purchase（Marketplace 购买）
* Member（仓库成员）
* Membership（团队成员资格）
* Meta（Webhook 元信息）
* Milestone（里程碑）
* Org block（组织屏蔽用户）
* Organization（组织）
* Page build（GitHub Pages 构建）
* Project（项目）
* Project card（项目卡片）
* Project column（项目列）
* Public（仓库设为公开）
* Pull request（拉取请求）
* Pull request review（拉取请求审查）
* Pull request review comment（拉取请求审查评论）
* Push（推送）
* Release（发布版本）
* Repository（仓库）
* Repository import（仓库导入）
* Repository vulnerability alert（仓库漏洞警报）
* Security advisory（安全公告）
* Star（加星标）
* Status（状态）
* Team（团队）
* Team add（团队添加到仓库）
* Watch（关注仓库）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 GitHub 提供应用节点。更多信息请参阅 [GitHub 节点文档](../app-nodes/n8n-nodes-base.github.md)。

在 n8n 网站查看[示例工作流和相关内容](https://n8n.io/integrations/github-trigger/)。

API 的详细信息，请参阅 [GitHub 文档](https://docs.github.com/en/rest)。
