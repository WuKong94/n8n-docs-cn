---
contentType: reference
nodeTitle: 验证指南
originalFilePath: integrations/creating-nodes/build/reference/verification-guidelines.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/verification-guidelines
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/verification-guidelines
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 社区节点验证指南 <a href="#community-node-verification-guidelines" id="community-node-verification-guidelines"></a>

{% hint style="info" %}
**希望 n8n 验证你的节点吗？**

如果计划将节点提交给 n8n 验证，请在构建节点时遵循以下指南。无论使用自托管部署还是 n8n Cloud，只要启用了经过验证的社区节点，用户就可以在 n8n 节点面板中发现并安装这些节点。
{% endhint %}


{% hint style="info" %}
**即将发生的变更**

从 2026 年 5 月 1 日起，**所有**社区节点都必须通过 GitHub Action 发布，并包含[来源证明声明](https://docs.npmjs.com/generating-provenance-statements)。
{% endhint %}

## 使用 n8n-node 工具 <a href="#use-the-n8n-node-tool" id="use-the-n8n-node-tool"></a>

所有经过验证的社区节点作者都应使用 [`n8n-node` 工具](../using-the-n8n-node-tool.md)创建和检查软件包。此工具通过以下方式帮助 n8n 确保质量和一致性：

* 生成符合要求的软件包文件结构。
* 在 `package.json` 文件中添加所需的元数据和配置。
* 简化按 n8n 标准执行的代码检查。
* 允许在本地 n8n 实例中加载节点进行测试。

## 节点类型 <a href="#node-types" id="node-types"></a>

* 节点**不得**与已有节点重复。如果只是迭代已有节点，请改为提交拉取请求。
* n8n 目前不接受逻辑节点或流程控制节点。
* 每个软件包应集成一个第三方服务。封装多个不相关 API，或作为多个服务代理层的软件包，通常不符合验证要求。请为每个服务提交独立软件包。
* 可以在主节点之外，为同一服务添加触发器节点。触发器必须使用编程式构建，因为[声明式](../../plan-your-node/choose-a-node-building-style.md)不支持触发器。一个软件包可以混用两种方式，因此声明式操作节点和编程式触发器节点可以放在同一个软件包中。

## 软件包来源验证 <a href="#package-source-verification" id="package-source-verification"></a>

* 检查 npm 软件包的仓库 URL 是否指向预期的 GitHub 仓库。
* 确认 npm 与仓库中的软件包作者或维护者信息一致。
* 确认 npm 中的 Git 链接有效，且仓库为公开仓库。
* 确保软件包包含完善的文档，例如 README 和使用示例。
* 确保软件包使用 MIT 许可证。
* 软件包应通过 GitHub Action 发布，并包含[来源证明](https://docs.npmjs.com/generating-provenance-statements)。

## 不使用外部依赖 <a href="#no-external-dependencies" id="no-external-dependencies"></a>

* 确保软件包**不包含**任何外部依赖，使其保持轻量且易于维护。

## 提供完善文档 <a href="#proper-documentation" id="proper-documentation"></a>

* 提供清晰的文档，可以是 GitHub 上的 **README**，或指向相关 **API 文档**的链接。
* 包含使用说明、示例工作流，以及必要的身份验证信息。

## 不访问环境变量或文件系统 <a href="#no-access-to-environment-variables-or-file-system" id="no-access-to-environment-variables-or-file-system"></a>

* 代码**不得**访问环境变量，也不得尝试读写文件。
* 所有必要数据都通过节点参数传入。

## 遵循 n8n 最佳实践 <a href="#follow-n8n-best-practices" id="follow-n8n-best-practices"></a>

* 保持清晰、一致的编码风格。
* 使用 **TypeScript**，并遵循 n8n 的[**节点开发指南**](../../overview.md)。
* 妥善处理错误并进行验证。
* 确保通过 linter 检查，即运行 `npx @n8n/scan-community-package n8n-nodes-PACKAGE` 必须通过。

## 仅使用英语 <a href="#use-english-language-only" id="use-english-language-only"></a>

* 节点界面和所有文档都必须仅使用**英语**。
* 此要求涵盖参数名称、描述、帮助文字、错误消息和 **README** 内容。

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
