---
title: OEM 部署
description: OEM 部署概览：根据 OEM 协议，在你自己的产品界面中嵌入并展示 n8n 界面。
contentType: overview
nodeTitle: 作为 OEM 集成部署
originalFilePath: hosting/oem-deployment/index.md
originalUrl: https://docs.n8n.io/hosting/oem-deployment
url: https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# OEM 部署 <a href="#oem-deployment" id="oem-deployment"></a>

{% include "../../../reusable-content/.gitbook/includes/self-hosting/oem-agreement.md" %}

n8n 的 OEM 部署选项允许在你自己的产品界面中嵌入并展示 n8n 界面，让用户无需离开产品，就能构建工作流、配置连接并运行工作流自动化。OEM 集成必须保留 n8n 品牌标识。

这与[将 n8n 用作后端](../README.md)不同：后者在后台执行工作流，最终用户不会看到 n8n。在该模式中，产品通过 webhook 或 [API](../../../connect/n8n-api/README.md) 调用 n8n 触发工作流，n8n 像基础设施中的其他自托管服务一样运行，用户不会看到任何 n8n 界面。所有付费套餐均可根据标准许可证使用此模式，无需单独协议。只有希望用户直接与 n8n 编辑器交互时，才需要 OEM 部署。

## 涵盖内容 <a href="#whats-covered" id="whats-covered"></a>

- [前提条件](prerequisites.md)：规划部署时所需的 CPU、内存和数据库要求。
- [管理工作流](manage-workflows.md)：嵌入部署中，跨多个用户或组织管理工作流的模式。
- [令牌交换](set-up-token-exchange.md)：通过 iframe SSO，使用你自己的身份提供商验证用户，并代表用户调用 n8n API。
- [工作流模板](../configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library.md)：为用户配置自定义工作流模板库。
- [凭据覆盖](../../../administer/manage-credentials/credential-overwrites.md)：全局设置 OAuth 凭据，让用户无需查看或输入客户端密钥即可完成身份验证。


## 支持 <a href="#support" id="support"></a>

请使用签署 OEM 协议时提供的邮箱联系 [n8n 支持团队](mailto:support@n8n.io)。一般问题也可在[社区论坛](https://community.n8n.io/)咨询。

## 相关资源 <a id="related-resources"></a>

* [自托管 n8n](../)
* [安装方式](../install-options/README.md)
* [配置 n8n](../configure-n8n/README.md)
* [保持 n8n 运行](../keep-n8n-running/README.md)
* [理解架构](../understand-the-architecture/README.md)
* [使用 AI 入门套件部署](../deploy-with-the-ai-starter-kit.md)
* [比较版本](../community-edition-features.md)
