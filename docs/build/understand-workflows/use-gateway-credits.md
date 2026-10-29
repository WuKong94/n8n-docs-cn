---
description: 在 n8n 工作流中使用 Gateway 额度运行 AI 模型和第三方服务，无需设置自己的凭据。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 使用 Gateway 额度 <a id="use-gateway-credits"></a>

Gateway 额度可以让你在工作流中运行支持的 AI 模型和第三方服务，无需创建服务提供商账号或设置[凭据](create-and-edit-credentials.md)。n8n 通过自己的网关转发请求，并从实例的预付额度余额中扣除使用费用。计费方式请参阅 [Gateway 额度](../../deploy/use-n8n-cloud/gateway-credits/README.md)。

Gateway 额度不能用于 [n8n Assistant](../ways-of-building-workflows/n8n-assistant.md)，后者使用独立的 [Assistant 额度](../../deploy/use-n8n-cloud/assistant-credits/README.md)。

{% hint style="info" %}
**功能可用范围**

以下套餐提供 Gateway 额度：

- **n8n Cloud：** Starter、Pro

n8n Cloud Enterprise 和自托管 n8n 不提供 Gateway 额度。此功能从 n8n 2.36.0 起可用。免费试用包含 Gateway 额度，但升级到付费套餐后才能充值。
{% endhint %}

## 在节点上使用 Gateway 额度 <a id="use-gateway-credits-on-a-node"></a>

在支持此功能的节点中，凭据字段会同时提供 Gateway 额度和你自己的凭据选项：

1. 打开节点设置。
1. 在凭据字段中选择 **Use Gateway credits（使用 Gateway 额度）**。该选项会显示剩余余额。
1. 照常配置节点的其余部分，然后运行。

设置到此完成，无需注册服务提供商账号，也无需 API 密钥。n8n 会按照[服务价格页面](https://app.n8n.cloud/service-pricing)上的费率，从余额中扣除每次请求的费用。

如果要改用自己的账号，选择 **Use my own credential（使用我自己的凭据）**，再选择或创建凭据。每个节点都可以单独选择，因此同一个工作流可以在某个节点使用 Gateway 额度，在其他节点使用自己的凭据。

## 查找支持的节点 <a id="find-supported-nodes"></a>

节点面板会突出显示可使用 Gateway 额度运行的节点：

- AI 模型和工具列表顶部的 **Included in n8n（n8n 已包含）** 部分显示支持的节点，该部分标题中会显示剩余余额。
- 搜索结果中，支持的节点会带有额度标签。

根据你是否已经充值，标签和分区标题会显示 **Gateway credits（Gateway 额度）** 或 **Free credits（免费额度）**。

支持的服务和模型会逐渐增加。最新列表请查看[服务价格页面](https://app.n8n.cloud/service-pricing)。

## 不支持的操作 <a id="unsupported-operations"></a>

部分节点仅有一部分操作支持 Gateway 额度。在这类节点上使用 Gateway 额度时，n8n 会隐藏不支持的操作。如果切换到 Gateway 额度时，节点已选中不支持的操作，n8n 会保留该操作并显示警告。如果需要使用不支持的操作，请将该节点切换为 **Use my own credential（使用我自己的凭据）**。

## 余额用尽时 <a id="when-your-balance-runs-out"></a>

当实例余额降至零时，使用 Gateway 额度的节点会失败。实例所有者可以[充值余额](../../deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits.md)或设置自动充值，也可以在 n8n Cloud 控制台中[按模型或工作流跟踪支出](../../deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md)。你也可以随时将受影响节点切换为自己的凭据。

## Gateway 额度与自己的 API 密钥 <a id="gateway-credits-versus-your-own-api-keys"></a>

两种方式运行的节点相同，区别在于设置、计费和覆盖范围：

| | Gateway 额度 | 自己的 API 密钥 |
|---|---|---|
| 设置 | 无需额外设置，选择后即可运行 | 创建服务提供商账号、生成密钥并添加凭据 |
| 计费 | 所有支持的服务共用一个预付余额，由 n8n 计费 | 各服务提供商单独计费，适用各自账号的费率和条款 |
| 覆盖范围 | 仅支持列表中的服务和模型 | n8n 集成的任意服务或模型，适用你所订阅套餐的速率限制和功能 |
| 支出可见性 | 在 n8n 中通过一个[支出视图](../../deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md)，按模型和工作流查看 | 各服务提供商自己的控制台 |

可以随时在两种方式之间切换节点，无需重新构建工作流。

## 控制实例上的 Gateway 额度功能 <a id="control-gateway-credits-on-your-instance"></a>

实例所有者可以为实例上的所有人关闭 Gateway 额度功能：

1. 打开 [Cloud 控制台](../../deploy/use-n8n-cloud/use-the-cloud-console.md)，选择 **Instance settings（实例设置）**。
1. 在 **Runtime（运行时）** 部分，关闭 **Gateway credits（Gateway 额度）**。
1. 在页面底部栏中选择 **Save and restart（保存并重启）**。实例会重启以应用更改，重启完成前处于离线状态。

关闭后，实例上的所有人都不会在节点中看到 Gateway 额度选项。

## 相关资源 <a id="related-resources"></a>

* [理解工作流](./)
* [创建和运行工作流](create-and-run-workflows.md)
* [保存和发布工作流](save-and-publish-workflows.md)
* [创建和编辑凭据](create-and-edit-credentials.md)
* [工作流组件](workflow-components/README.md)
* [理解执行](understand-executions/README.md)
