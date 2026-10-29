---
title: 加密密钥轮换
description: 启用并轮换用于保护自托管 n8n 实例中凭据和其他敏感数据的数据加密密钥。
contentType: howto
nodeTitle: 轮换加密密钥
originalFilePath: hosting/securing/encryption-key-rotation.md
originalUrl: https://docs.n8n.io/hosting/securing/encryption-key-rotation
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 加密密钥轮换 <a href="#encryption-key-rotation" id="encryption-key-rotation"></a>

{% hint style="info" %}
**功能可用范围**

加密密钥轮换可用于：

- **自托管：**所有版本。

n8n Cloud 不提供此功能。

自 n8n 3.0 起，默认启用加密密钥轮换。更早版本需通过环境变量启用。

只有实例所有者才能启用或禁用此功能，以及轮换密钥。
{% endhint %}

加密密钥轮换允许你定期更换用于加密 n8n 数据的密钥，例如凭据、OAuth 令牌及其他敏感内容，而无需更改实例的主加密密钥。

## 加密密钥轮换的工作原理 <a href="#how-encryption-key-rotation-works" id="how-encryption-key-rotation-works"></a>

n8n 使用两层密钥模型：

* **实例加密密钥**（`N8N_ENCRYPTION_KEY`）：部署时设置的主密钥，始终保持不变。n8n 仅用它保护数据加密密钥。
* **数据加密密钥**：直接加密凭据数据的密钥，也是轮换的对象。n8n 将其加密后存储在数据库中，由实例密钥保护。

轮换时，n8n 会生成新的数据加密密钥，用于此后的所有写入。使用旧密钥加密的现有数据仍然可读。下次更新每条记录时，n8n 会自动使用新密钥重新加密。

## 开始之前 <a href="#before-you-begin" id="before-you-begin"></a>

{% hint style="warning" %}
**请先完整备份数据库**

一旦 n8n 使用数据加密密钥写入数据，旧版 n8n 就无法读取。启用此功能前，以及升级到会自动启用此功能的 n8n 3.0 前，请备份数据库。详情请参阅[向后兼容与回滚](#backwards-compatibility-and-rollback)。
{% endhint %}

你还需要确保：

* 所有 n8n 实例，包括主实例和所有工作进程，都使用相同的 `N8N_ENCRYPTION_KEY` 值。
* 你可以直接控制环境变量和 n8n 数据库。只有自托管部署满足此条件。

## 启用加密密钥轮换 <a href="#enable-encryption-key-rotation" id="enable-encryption-key-rotation"></a>

自 n8n 3.0 起，默认启用加密密钥轮换，无需额外设置。升级后首次启动时，n8n 会生成初始数据加密密钥，并加密存储在数据库中。

在 n8n 2.x 中，请手动启用此功能：

1. 在**所有** n8n 实例上设置以下环境变量，包括主实例和工作进程：

    ```sh
    N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=true
    ```

2. 重启所有实例。n8n 会在启动时自动生成初始数据加密密钥，并加密存储在数据库中。

要确认功能已生效，请前往 **Settings**（设置）> **Data Encryption Keys**（数据加密密钥），应能看到列出的当前活动密钥。

## 轮换当前活动密钥 <a href="#rotate-the-active-key" id="rotate-the-active-key"></a>

启用此功能后，你可以随时轮换为新的数据加密密钥。

### 使用界面 <a href="#using-the-ui" id="using-the-ui"></a>

前往 **Settings**（设置）> **Data Encryption Keys**（数据加密密钥），选择 **Rotate key**（轮换密钥）。

### 使用 API <a href="#using-the-api" id="using-the-api"></a>

发送 `POST` 请求到 `/encryption/keys` 端点。请求需要 `encryptionKey:manage` 全局权限范围。n8n 的 API 响应不会返回密钥内容，只返回 ID、算法、状态和时间戳等元数据。

轮换后，所有新写入都使用新的活动密钥。使用旧密钥加密的记录仍然可读。下次更新每条记录时，n8n 会使用新密钥重新加密。

## 关闭加密密钥轮换 <a id="turn-off-encryption-key-rotation"></a>

自 n8n 2.40.3 起，可以再次关闭加密密钥轮换。在**所有** n8n 实例上设置以下环境变量，包括主实例和工作进程，然后重启：

```sh
N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION=false
```

在早于 n8n 2.40.3 的版本中，如果 n8n 已用新格式写入数据，再关闭此功能会导致这些数据永久无法访问。请先升级到 n8n 2.40.3。

## 向后兼容与回滚 <a href="#backwards-compatibility-and-rollback" id="backwards-compatibility-and-rollback"></a>

{% hint style="danger" %}
**加密密钥轮换写入数据后，请勿降级 n8n**

启用此功能前，以及升级到会自动启用此功能的 n8n 3.0 前，请阅读本节。
{% endhint %}

启用加密密钥轮换后，n8n 会使用包含密钥标识符的新格式写入凭据和其他敏感数据。旧版 n8n 无法读取此格式。

* n8n 使用新格式写入数据后，**请勿降级 n8n 版本**。旧版无法解密这些数据。
* **自 n8n 2.40.3 起，可以安全关闭此功能。**在更早版本中，将 `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` 设为 `false`，会使启用此功能后加密的所有数据永久无法访问。

目前没有自动化工具将新格式加密的数据转换回旧格式。如果最终使用的 n8n 版本无法读取数据，唯一恢复方式是还原数据库备份。

## 建议步骤 <a href="#recommended-steps" id="recommended-steps"></a>

1. **备份数据库**。任何更改之前都先创建完整快照，包括升级到 n8n 3.0 之前。
2. **先在预发布环境尝试**。在非生产环境启用此功能或升级到 n8n 3.0，重启后验证凭据仍能正确解密。
3. **再应用到生产环境**。仅在验证预发布环境行为后进行。
4. **不要降级**。一旦生产数据使用新格式写入，就保持当前 n8n 版本或使用更新版本。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

* [安全](../security.md)：审计、加固并限制自托管实例。
* [设置自定义加密密钥](../basic-configuration/configuration-examples/set-a-custom-encryption-key.md)：设置实例级 `N8N_ENCRYPTION_KEY` 值。
* [部署环境变量](../basic-configuration/use-environment-variables/deployment.md)：`N8N_ENCRYPTION_KEY` 和 `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION` 的参考。
* [配置队列模式](../scaling/enable-queue-mode.md)：确保所有工作进程使用相同的实例加密密钥。
* [n8n 3.0 破坏性变更](../../../../changelog/v30-breaking-changes.md)：升级带来的变化，包括加密密钥轮换。
