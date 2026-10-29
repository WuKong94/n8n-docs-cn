---
contentType: reference
nodeTitle: 代码标准
originalFilePath: integrations/creating-nodes/build/reference/code-standards.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/build/reference/code-standards
url: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/code-standards
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 代码标准 <a href="#code-standards" id="code-standards"></a>

构建节点时遵循明确的代码标准，可以提高代码的可读性和可维护性，并帮助避免错误。本文介绍节点开发中的良好编码实践，侧重代码细节。界面标准和用户体验指南，请参阅[节点界面设计](../../plan-your-node/node-ui-design.md)。

## 使用 linter <a href="#use-the-linter" id="use-the-linter"></a>

n8n 节点 linter 可以自动检查多项节点构建标准。发布节点前，应确保节点通过 linter 检查。更多信息请参阅 [n8n 节点 linter](../../test-your-node/node-linter.md) 文档。

## 使用 n8n-node 工具 <a href="#use-the-n8n-node-tool" id="use-the-n8n-node-tool"></a>

n8n 建议使用 [`n8n-node` 命令行工具](../using-the-n8n-node-tool.md)构建和测试节点，尤其是计划[提交节点接受验证](../../deploy-your-node/submit-community-nodes.md#submit-your-node-for-verification-by-n8n)时。该工具可确保节点结构正确、符合社区节点要求，并简化代码检查和测试。

## 使用声明式 <a id="use-the-declarative-style"></a>

使用声明式构建节点。这是默认方式，通过在 `routing` 键中描述请求来替代 `execute()` 方法，使节点代码更简短、更易于维护。

只有节点确实需要时才使用编程式，例如触发器节点、非 REST API、转换传入数据的节点，或需要基于功能进行版本控制的节点。声明式节点仍可使用轻量版本控制。完整适用场景及两种方式的对比，请参阅[选择节点构建方式](../../plan-your-node/choose-a-node-building-style.md)。

## 使用 TypeScript 编写 <a href="#write-in-typescript" id="write-in-typescript"></a>

n8n 的代码全部使用 TypeScript。使用 TypeScript 编写节点可以加快开发并减少错误。

## 节点编写详细指南 <a href="#detailed-guidelines-for-writing-a-node" id="detailed-guidelines-for-writing-a-node"></a>

以下指南适用于你构建的所有节点。

### 资源与操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

如果节点可执行多种操作，请将选择操作的参数命名为 `Operation`。如果节点可对多种资源执行这些操作，请创建 `Resource` 参数。以下代码展示了资源和操作的基本设置：

```js
export const ExampleNode implements INodeType {
    description: {
        displayName: 'Example Node',
        ...
        properties: [
            {
                displayName: 'Resource',
                name: 'resource',
                type: 'options',
                options: [
                    {
                        name: 'Resource One',
                        value: 'resourceOne'
                    },
                    {
                        name: 'Resource Two',
                        value: 'resourceTwo'
                    }
                ],
                default: 'resourceOne'
            },
            {
                displayName: 'Operation',
                name: 'operation',
                type: 'options',
                // Only show these operations for Resource One
                displayOptions: {
                    show: {
                        resource: [
                            'resourceOne'
                        ]
                    }
                },
                options: [
                    {
                        name: 'Create',
                        value: 'create',
                        description: 'Create an instance of Resource One'
                    }
                ]
            }
        ]
    }
}
```

### 复用参数内部名称 <a href="#reuse-internal-parameter-names" id="reuse-internal-parameter-names"></a>

n8n 节点中的所有资源字段和操作字段都有两个设置：通过 `name` 参数设置的显示名称，以及通过 `value` 参数设置的内部名称。复用字段的内部名称，可以让 n8n 在用户切换操作时保留已输入的数据。

> 译注：此段原文使用 name/value 描述显示名称和内部名称。需区分字段对象与 options 选项对象：同页示例中的字段对象使用 displayName/name，而选项对象使用 name/value；“节点界面元素”的字符串字段示例也使用 displayName/name。此处保留原文并标注这一区别，避免把选项对象的命名规则套用于所有输入字段。

例如，你正在构建一个包含 Order（订单）资源的节点。该资源支持 Get（获取）、Edit（编辑）和 Delete（删除）等操作，每项操作都通过订单 ID 指定要处理的订单，因此需要向用户显示 ID 字段。此字段有显示标签和内部名称。如果各项操作的 ID 字段使用相同的内部名称（在 `value` 中设置），用户选择 Get 操作并输入 ID 后，即使切换到 Edit，也不会丢失该 ID。

复用内部名称时，必须确保用户在同一时刻只能看到一个同名字段。可以通过 `displayOptions` 控制显示。

## 编程式节点编写详细指南 <a href="#detailed-guidelines-for-writing-a-programmatic-style-node" id="detailed-guidelines-for-writing-a-programmatic-style-node"></a>

以下指南适用于使用编程式构建的节点，不适用于声明式节点。不同节点构建方式的更多信息，请参阅[选择节点构建方式](../../plan-your-node/choose-a-node-building-style.md)。

### 不要修改传入数据 <a href="#dont-change-incoming-data" id="dont-change-incoming-data"></a>

切勿修改节点接收到的传入数据（通过 `this.getInputData()` 访问的数据），因为所有节点共享这些数据。如果需要添加、修改或删除数据，请先克隆传入数据，再返回新数据。否则，在当前节点之后执行的同级节点将使用被修改的数据，导致处理错误。

无需每次都克隆全部数据。例如，节点只修改二进制数据、不修改 JSON 数据时，可以创建一个新数据项，并复用对原 JSON 数据项的引用。


### 使用内置请求库 <a href="#use-the-built-in-request-library" id="use-the-built-in-request-library"></a>

某些第三方服务在 npm 上提供自己的库，可简化集成开发。但使用这些软件包会增加一项依赖，以及它的全部间接依赖。这会不断增加需要加载的代码，也可能引入安全漏洞和错误。因此，应使用内置模块：

```typescript
// If no auth needed
const response = await this.helpers.httpRequest(options);

// If auth needed
const response = await this.helpers.httpRequestWithAuthentication.call(
	this, 
	'credentialTypeName', // For example: pipedriveApi
	options,
);
```

此模块使用 npm 软件包 [Axios](https://www.npmjs.com/package/axios)。

更多信息以及已移除的 `this.helpers.request` 的迁移说明，请参阅 [HTTP 辅助方法](http-request-helpers.md)。

## 相关资源 <a id="related-resources"></a>

* [节点构建参考](./)
