---
title: NVIDIA Nemotron 凭据
description: NVIDIA Nemotron 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 NVIDIA Nemotron 的身份验证。
contentType:
- integration
- reference
priority: critical
nodeTitle: NVIDIA Nemotron 凭据
originalFilePath: integrations/builtin/credentials/nvidia.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/nvidia
url: https://docs.n8n.io/integrations/builtin/credentials/nvidia
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# NVIDIA Nemotron 凭据 <a href="#nvidia-nemotron-credentials" id="nvidia-nemotron-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [NVIDIA Nemotron Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md)

同一凭据适用于两种部署模式：

- **Cloud**（云）：[build.nvidia.com](https://build.nvidia.com/) 上由 NVIDIA 托管的 Nemotron 模型。
- **Self-hosted NIM**（自托管 NIM）：在你自己的基础设施上运行的 [NVIDIA Inference Microservice](https://docs.nvidia.com/nim/) 容器。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

如需访问云服务，请创建 [NVIDIA build](https://build.nvidia.com/) 账户。

如需访问自托管服务，请运行提供兼容 OpenAI 规范端点的 NIM 容器。设置指南，请参阅 [NVIDIA NIM 文档](https://docs.nvidia.com/nim/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key（API 密钥；连接未强制身份验证的自托管 NIM 时可选）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

可用的 Nemotron 模型列表，请参阅 NVIDIA 的 [build 目录](https://build.nvidia.com/models)；自托管指南，请参阅 [NIM 文档](https://docs.nvidia.com/nim/)。

## 使用 API 密钥 <a href="#using-api-key" id="using-api-key"></a>

配置此凭据需要：

- **Base URL**（基础 URL）：要调用的兼容 OpenAI 规范的端点。使用 build.nvidia.com 云服务时，使用默认值 `https://integrate.api.nvidia.com/v1`；自托管时，替换为 NIM URL（例如 `http://localhost:8000/v1`）。
- **API Key**（API 密钥）：build.nvidia.com 云服务必填。自托管 NIM 不要求身份验证时，可留空。

为 build.nvidia.com 生成 API 密钥的步骤如下：

1. 登录 [NVIDIA build](https://build.nvidia.com/) 账户。
2. 在目录中打开一个 Nemotron 模型，选择 **Get API Key**（获取 API 密钥）。
3. 复制密钥，填入 n8n 的 **API Key**（API 密钥）。

连接自托管 NIM 的步骤如下：

1. 将 **Base URL**（基础 URL）设为 NIM 端点，包含 `/v1` 路径（例如 `http://localhost:8000/v1`）。
2. 如果 NIM 要求身份验证，将令牌粘贴到 **API Key**（API 密钥）；否则将该字段留空。
