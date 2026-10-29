---
title: 加固任务运行器
description: 加固任务运行器，提高自托管 n8n 实例的隔离性。
contentType: howto
nodeTitle: 加固任务运行器
originalFilePath: hosting/securing/hardening-task-runners.md
originalUrl: https://docs.n8n.io/hosting/securing/hardening-task-runners
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 加固任务运行器 <a href="#hardening-task-runners" id="hardening-task-runners"></a>

[任务运行器](../set-up-task-runners.md)负责执行 [Code 节点](../../../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)中的代码。Code 节点执行本身具有安全保护，也可以通过以下建议进一步加固运行器。

## 在外部模式下以边车容器运行 <a href="#run-task-runners-as-sidecars-in-external-mode" id="run-task-runners-as-sidecars-in-external-mode"></a>

要加强 n8n 核心进程与 Code 节点代码之间的隔离，请使用[外部模式](../set-up-task-runners.md#setting-up-external-mode)运行任务运行器。外部运行器在独立容器中启动，为 Code 节点定义的 JavaScript 提供完全隔离的执行环境。

## 使用 distroless 镜像 <a href="#use-the-distroless-image" id="use-the-distroless-image"></a>

为缩小攻击面，可以使用 distroless Docker 镜像变体。它只包含应用及运行时依赖，不包含运行时不需要的包管理器、Shell 或其他工具。

使用此镜像时，在 Docker 标签后添加 `-distroless` 后缀，例如 `2.4.6-distroless`。

## 以 nobody 用户运行 <a href="#run-as-the-nobody-user" id="run-as-the-nobody-user"></a>

为提高安全性，将任务运行器配置为使用无特权的 `nobody` 用户，其用户和组 ID 均为 65532。这样可以避免容器进程以 root 权限运行，限制安全漏洞可能造成的损害。

## 配置只读根文件系统 <a href="#configure-read-only-root-filesystem" id="configure-read-only-root-filesystem"></a>

配置[只读根文件系统](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)，禁止运行时修改容器文件系统，防止恶意代码试图改写系统文件。

任务运行器仍需要少量临时存储。因此，将最小规模的 `emptyDir` 卷挂载到 `/tmp`。工作流需要更多临时空间时，相应增加卷大小。

## 配置 AppArmor 策略 <a href="#configure-an-apparmor-profile" id="configure-an-apparmor-profile"></a>

作为纵深防御措施，可应用 [AppArmor](https://apparmor.net/) 策略，禁止任务运行器容器读取敏感的 `/proc` 文件，例如 `environ` 和 `mounts`。这些文件可能向容器内代码暴露环境变量，包括密钥和凭据。如何将策略应用到 Pod，请参阅 [Kubernetes AppArmor 文档](https://kubernetes.io/docs/tutorials/security/apparmor/)。

将以下规则添加到 AppArmor 策略：

```
audit deny @{PROC}/[0-9]*/{environ,mounts} rwl,
```

此规则拒绝并记录任何读取、写入或链接各进程 `environ` 和 `mounts` 文件的尝试。

## 相关资源 <a id="related-resources"></a>

* [安全](../security.md)
