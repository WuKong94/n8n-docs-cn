---
title: Ollama Chat Model 节点常见问题
description: 工作流自动化平台 n8n 中 Ollama Chat Model 节点的常见错误和问题，包括问题详情及建议的解决办法。
contentType:
- integration
- reference
priority: high
nodeTitle: Ollama Chat Model 节点常见问题
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Ollama Chat Model 节点常见问题 <a href="#ollama-chat-model-node-common-issues" id="ollama-chat-model-node-common-issues"></a>

以下列出 [Ollama Chat Model 节点](README.md)的常见错误和问题，以及解决或排查步骤。

## 参数处理 <a href="#processing-parameters" id="processing-parameters"></a>

Ollama Chat Model 是子节点[^1]。使用表达式处理多个数据项时，子节点的行为与其他节点不同。

多数节点，包括[根节点](#user-content-fn-2)[^2]，可以接收任意数量的输入数据项，处理后输出结果。你可以用表达式引用输入数据项，节点会依次对每个数据项解析表达式。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 会依次解析为每个名称。

在子节点中，表达式始终解析为第一个数据项。例如，输入包含五个名称值时，表达式 `{{ $json.name }}` 始终解析为第一个名称。

## 无法连接远程 Ollama 实例 <a href="#cant-connect-to-a-remote-ollama-instance" id="cant-connect-to-a-remote-ollama-instance"></a>

Ollama Chat Model 节点支持 Bearer 令牌身份验证，可连接位于身份验证代理（例如 Open WebUI）后的远程 Ollama 实例。

使用经过身份验证的远程连接时，请在 Ollama 凭据中同时配置远程 URL 和 API 密钥。

更多信息请参阅 [Ollama 凭据说明](../../../credentials/ollama.md)。

## 使用 Docker 时无法连接本地 Ollama 实例 <a href="#cant-connect-to-a-local-ollama-instance-when-using-docker" id="cant-connect-to-a-local-ollama-instance-when-using-docker"></a>

Ollama Chat Model 节点通过 [Ollama 凭据](../../../credentials/ollama.md)中定义的基础 URL 连接本地托管的 Ollama 实例。n8n 或 Ollama 任一组件在 Docker 中运行时，都需要配置网络，使 n8n 能连接到 Ollama。

Ollama 通常在本地网络地址 `localhost` 上监听连接。Docker 中，每个容器默认都有自己的 `localhost`，只能从该容器内部访问。n8n 或 Ollama 任一组件在容器中运行时，都无法通过 `localhost` 相互连接。

解决方法取决于两个组件的托管方式。

### 仅 Ollama 在 Docker 中运行 <a href="#if-only-ollama-is-in-docker" id="if-only-ollama-is-in-docker"></a>

如果只有 Ollama 在 Docker 中运行，请在容器内将其绑定到 `0.0.0.0`，以监听所有网络接口；官方镜像已采用此配置。

运行容器时，使用 `-p` 标志[发布端口](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)。Ollama 默认运行在 11434 端口，因此 Docker 命令应如下所示：

```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

配置 [Ollama 凭据](../../../credentials/ollama.md)时，`localhost` 地址应可正常使用，将 **base URL**（基础 URL）设为 `http://localhost:11434`。

### 仅 n8n 在 Docker 中运行 <a href="#if-only-n8n-is-in-docker" id="if-only-n8n-is-in-docker"></a>

如果只有 n8n 在 Docker 中运行，请在宿主机上将 Ollama 绑定到 `0.0.0.0`，以监听所有网络接口。

如果在 **Linux** 上通过 Docker 运行 n8n，请在启动容器时使用 `--add-host` 标志，将 `host.docker.internal` 映射到 `host-gateway`。例如：

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

使用 Docker Desktop 时，会自动完成此配置。

配置 [Ollama 凭据](../../../credentials/ollama.md)时，使用 `host.docker.internal` 作为主机地址，替代 `localhost`。例如，使用默认端口 11434 时，可将基础 URL 设为 `http://host.docker.internal:11434`。

### Ollama 和 n8n 在不同 Docker 容器中运行 <a href="#if-ollama-and-n8n-are-running-in-separate-docker-containers" id="if-ollama-and-n8n-are-running-in-separate-docker-containers"></a>

将两个容器连接到同一个用户自定义桥接网络。更多信息请参阅 Docker 的[桥接网络驱动文档](https://docs.docker.com/engine/network/drivers/bridge/)。默认 Docker 桥接网络无法解析容器名称；在默认桥接网络上使用容器名称，即使 Ollama 正在运行，也可能导致 `ENOTFOUND` 错误。

在容器内将 Ollama 配置为监听 `0.0.0.0`，官方 Ollama 镜像已使用此设置。

连接已有容器的步骤如下。将 `<ollama-container>` 和 `<n8n-container>` 替换为现有容器名称，可运行 `docker ps` 查找名称。

1. 创建共享网络：

	```shell
	docker network create n8n-ollama
	```

2. 连接 Ollama 容器：

	```shell
	docker network connect n8n-ollama <ollama-container>
	```

3. 连接 n8n 容器：

	```shell
	docker network connect n8n-ollama <n8n-container>
	```

4. 在 [Ollama 凭据](../../../credentials/ollama.md)中，将 **Base URL**（基础 URL）设为 `http://<ollama-container>:11434`。将 `<ollama-container>` 替换为 Ollama 容器名称。例如，容器名称为 `ollama` 时，使用 `http://ollama:11434`。

两个容器都必须处于运行状态。同一网络中的容器可直接通信，因此无需将 Ollama 端口发布到宿主机。

### Ollama 和 n8n 在同一 Docker 容器中运行 <a href="#if-ollama-and-n8n-are-running-in-the-same-docker-container" id="if-ollama-and-n8n-are-running-in-the-same-docker-container"></a>

如果 Ollama 和 n8n 在同一个 Docker 容器中运行，`localhost` 地址无需特殊配置。可将 Ollama 配置为监听 localhost，并在 [n8n 的 Ollama 凭据](../../../credentials/ollama.md)中将基础 URL 配置为 localhost：`http://localhost:11434`。


## 错误：connect ECONNREFUSED ::1:11434 <a href="#error-connect-econnrefused-111434" id="error-connect-econnrefused-111434"></a>


计算机启用了 IPv6，而 Ollama 监听 IPv4 地址时，会出现此错误。

解决方法是在 [Ollama 凭据](../../../credentials/ollama.md)中修改基础 URL，连接 IPv4 专用本地地址 `127.0.0.1`，替代可能解析为 IPv4 或 IPv6 的 `localhost` 别名：`http://127.0.0.1:11434`。

## Ollama 与 HTTP/HTTPS 代理 <a href="#ollama-and-httphttps-proxies" id="ollama-and-httphttps-proxies"></a>

Ollama 的配置不支持自定义 HTTP agent，因此难以通过自定义 HTTP/HTTPS 代理使用。根据代理配置的不同，即使设置了 `HTTP_PROXY` 或 `HTTPS_PROXY` 环境变量，也可能完全无法工作。

更多信息请参阅 [Ollama 常见问题](https://docs.ollama.com/faq#how-do-i-use-ollama-behind-a-proxy)。

[^1]: n8n 集群节点由连接到根节点的一个或多个子节点组成。子节点通过访问特定服务或资源，或提供特定类型的专用处理（例如计算器功能），扩展根节点的功能。
<a id="user-content-fn-2"></a>
[^2]: 每个 n8n 集群节点都包含一个根节点，用于定义集群的主要功能。一个或多个子节点连接到根节点，以扩展其功能。
