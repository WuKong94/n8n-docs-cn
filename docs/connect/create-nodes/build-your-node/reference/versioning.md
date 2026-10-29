---
contentType: howto
nodeTitle: 版本控制
originalFilePath: integrations/creating-nodes/build/reference/node-versioning.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/node-versioning
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 节点版本控制 <a href="#node-versioning" id="node-versioning"></a>

n8n 支持节点版本控制。通过引入新版本，可以修改已有节点，同时保留原有行为。

请注意 n8n 如何决定加载哪个节点版本：

* 如果用户使用节点版本 1 构建并保存了工作流，即使你创建并发布节点版本 2，n8n 仍会在该工作流中使用版本 1。
* 用户创建新工作流并浏览节点时，n8n 始终加载节点的最新版本。

{% hint style="info" %}
**版本控制类型受节点构建方式限制**

使用声明式构建的节点不能采用完整版本控制。
{% endhint %}

## 轻量版本控制 <a href="#light-versioning" id="light-versioning"></a>

适用于所有节点类型。

同一个节点可以包含多个版本，允许进行小幅版本更新而无需重复代码。使用方法如下：

1. 将主 `version` 参数改为数组，添加所有版本号，包括已有版本。
2. 然后可以在任意对象中通过 `@version` 访问版本参数，将其用于 `displayOptions`，控制 n8n 在哪些版本中显示该对象。也可以在函数中使用 `const nodeVersion = this.getNode().typeVersion;` 查询版本。

例如，要为[声明式节点教程](../tutorial-build-a-declarative-style-node.md)中的 NasaPics 节点添加版本控制，并将某个资源配置为仅在节点版本 2 中显示，请在节点基础 `NasaPics.node.ts` 文件中设置：

```js
{
    displayName: 'NASA Pics',
    name: 'NasaPics',
    icon: 'file:nasapics.svg',
    // List the available versions
    version: [1,2,3],
    // More basic parameters here
    properties: [
        // Add a resource that's only displayed for version2
        {
            displayName: 'Resource name',
            // More resource parameters
            displayOptions: {
                show: {
                    '@version': 2,
                },
            },
        },
    ],
}
```

## 基于功能的版本控制 <a href="#feature-based-versioning" id="feature-based-versioning"></a>

功能标志将具名功能与节点版本关联，可根据这些功能控制参数是否显示以及执行逻辑。

### 定义功能 <a href="#defining-features" id="defining-features"></a>

在节点类型描述中添加 `features` 对象。每项功能通过 `@version` 条件指定启用该功能的版本：

```js
{
    version: [2, 2.1, 2.2, 2.3, 2.4],
    features: {
        useNewApi: { '@version': [{ _cnd: { gte: 2.2 } }] },
        useLegacyAuth: { '@version': [{ _cnd: { lte: 2.1 } }] },
        useSpecialMode: { '@version': [2] },
    },
    // More basic parameters here
}
```

可用条件：`gte`、`lte`、`gt`、`lt`。传入普通版本号可以匹配指定版本。

### 使用 `@feature`（在 `displayOptions` 中） <a href="#using-feature-in-displayoptions" id="using-feature-in-displayoptions"></a>

使用 `@feature` 在 `displayOptions` 中根据功能标志控制参数是否显示：

```js
{
    displayName: 'New API Field',
    name: 'newApiField',
    type: 'string',
    displayOptions: {
        show: {
            '@feature': ['useNewApi'],
        },
    },
}
```

要在某项功能**未**启用时显示参数，请使用以下条件语法：

```js
displayOptions: {
    show: {
        '@feature': [{ _cnd: { not: 'useNewApi' } }],
    },
}
```

可以将 `@feature` 与其他显示条件组合：

```js
displayOptions: {
    show: {
        resource: ['myResource'],
        '@feature': [{ _cnd: { eq: 'useNewApi' } }],
    },
}
```

### 在代码中检查功能 <a href="#checking-features-in-code" id="checking-features-in-code"></a>

在执行上下文中使用 `this.isNodeFeatureEnabled()`，例如 `IExecuteFunctions` 或 `IWebhookFunctions`：

```js
if (this.isNodeFeatureEnabled('useNewApi')) {
    // Process with new API
} else {
    // Process with legacy API
}
```

## 完整版本控制 <a href="#full-versioning" id="full-versioning"></a>

不适用于声明式节点。

示例请参阅 [Mattermost 节点](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost)。

完整版本控制要点：

- 节点基础文件应继承 `NodeVersionedType`，而非 `INodeType`。
- 节点基础文件应包含描述信息，其中包括 `defaultVersion`（通常为最新版本）、名称等基本节点元数据，以及版本列表。此文件不应包含任何节点功能实现。
- n8n 建议使用 `v1`、`v2` 等作为版本文件夹的名称。



## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
