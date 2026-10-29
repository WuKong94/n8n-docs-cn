---
contentType: explanation
nodeTitle: 选择节点开发方式
originalFilePath: integrations/creating-nodes/plan/choose-node-method.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/plan/choose-node-method
url: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 选择节点开发方式 <a href="#choose-your-node-building-approach" id="choose-your-node-building-approach"></a>

n8n 有两种节点开发方式：声明式和编程式。新节点默认采用声明式，请优先使用这种方式构建。

声明式：

* 使用基于 JSON 的语法，编写更简单，降低引入错误的风险。
* 更适应未来的演进。
* 支持 REST API 集成。
* 无需 `execute()` 方法，减少需要编写和维护的代码。

如果不确定需要哪种方式，请从声明式开始。[`n8n-node` 工具](../build-your-node/using-the-n8n-node-tool.md)可以生成声明式节点脚手架，[构建声明式节点](../build-your-node/tutorial-build-a-declarative-style-node.md)则提供完整示例。

## 何时需要编程式 <a id="when-you-need-the-programmatic-style"></a>

编程式代码更多，需要用自行维护的代码实现节点行为，应仅在特殊情况下使用。节点属于以下情况时，使用编程式：

* 触发节点。
* 不基于 REST 的节点，包括需要调用 GraphQL API 或使用外部依赖的节点。
* 需要在路由能力之外转换数据的节点。声明式可以通过 `routing.request.preSend` 修改请求、通过 `routing.output.postReceive` 修改 API 响应。如果节点需要独立于单次 API 调用处理输入数据项，请使用编程式。
* 需要基于功能的版本控制，在代码中通过 `this.isNodeFeatureEnabled()` 实现不同行为分支的节点。声明式节点仍可使用轻量版本控制，并通过 `@feature` 在 `displayOptions` 中读取功能标志。版本控制类型的更多说明，请参阅[节点版本控制](../build-your-node/reference/versioning.md)。

如果节点不属于上述情况，请使用声明式。

{% hint style="info" %}
**触发节点必须使用编程式**

声明式不支持触发节点。所有触发节点都必须使用编程式，即使同一服务的操作节点采用声明式。

可以在一个节点软件包中混用两种方式。例如，提交[验证](../build-your-node/reference/verification-guidelines.md)的软件包，可以包含同一服务的声明式操作节点和编程式触发节点。
{% endhint %}

## 数据处理差异 <a href="#data-handling-differences" id="data-handling-differences"></a>

声明式与编程式的主要区别，在于如何处理输入数据和构建 API 请求。编程式需要 `execute()` 方法，读取输入数据和参数后构建请求。声明式通过 `routing` 键处理，该键位于 `operations` 对象中。节点参数及 `execute()` 方法的更多信息，请参阅[节点基础文件](../build-your-node/reference/base-files/README.md)。

## 语法差异 <a href="#syntax-differences" id="syntax-differences"></a>

可比较下面两段代码，理解声明式与编程式的区别。此示例创建了 SendGrid 集成的简化版本，称为“FriendGrid”。代码片段并不完整，只突出两种节点开发方式的差异。

FriendGrid 调用 REST API，且不转换输入，因此适合使用声明式。声明式实现如下：

```js
import { INodeType, INodeTypeDescription } from 'n8n-workflow';

// Create the FriendGrid class
export class FriendGrid implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'FriendGrid',
    name: 'friendGrid',
    . . .
    // Set up the basic request configuration
    requestDefaults: {
      baseURL: 'https://api.sendgrid.com/v3/marketing'
    },
    properties: [
      {
        displayName: 'Resource',
        . . .
      },
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        displayOptions: {
          show: {
            resource: [
              'contact',
            ],
          },
        },
        options: [
          {
            name: 'Create',
            value: 'create',
            description: 'Create a contact',
            // Add the routing object
            routing: {
              request: {
                method: 'POST',
                url: '=/contacts',
                send: {
                  type: 'body',
                  properties: {
                    email: '={{$parameter["email"]}}'
                  }
                }
              },
              // Handle the response to contact creation
              output: {
                postReceive: [
                  {
                    type: 'set',
                    properties: {
                      value: '={{ { "success": $response } }}'
                    }
                  }
                ]
              }
            }
          },
        ],
        default: 'create',
        description: 'The operation to perform.',
      },
      {
        displayName: 'Email',
        . . .
      },
      {
        displayName: 'Additional Fields',
        // Sets up optional fields
      },
    ],
  }
  // No execute method needed
}
```

同一节点采用编程式时，需要一个 `execute()` 方法，手动读取参数并构建请求：

```js
import {
	IExecuteFunctions,
	INodeExecutionData,
	INodeType,
	INodeTypeDescription,
	IRequestOptions,
} from 'n8n-workflow';

// Create the FriendGrid class
export class FriendGrid implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'FriendGrid',
    name: 'friendGrid',
    . . .
    properties: [
      {
        displayName: 'Resource',
        . . .
      },
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        displayOptions: {
          show: {
              resource: [
              'contact',
              ],
          },
        },
        options: [
          {
            name: 'Create',
            value: 'create',
            description: 'Create a contact',
          },
        ],
        default: 'create',
        description: 'The operation to perform.',
      },
      {
        displayName: 'Email',
        name: 'email',
        . . .
      },
      {
        displayName: 'Additional Fields',
        // Sets up optional fields
      },
    ],
};

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    let responseData;
    const resource = this.getNodeParameter('resource', 0) as string;
    const operation = this.getNodeParameter('operation', 0) as string;
    //Get credentials the user provided for this node
    const credentials = await this.getCredentials('friendGridApi') as IDataObject;

    if (resource === 'contact') {
      if (operation === 'create') {
      // Get email input
      const email = this.getNodeParameter('email', 0) as string;
      // Get additional fields input
      const additionalFields = this.getNodeParameter('additionalFields', 0) as IDataObject;
      const data: IDataObject = {
          email,
      };

      Object.assign(data, additionalFields);

      // Make HTTP request as defined in https://sendgrid.com/docs/api-reference/
      const options: IRequestOptions = {
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${credentials.apiKey}`,
        },
        method: 'PUT',
        body: {
            contacts: [
            data,
            ],
        },
        url: `https://api.sendgrid.com/v3/marketing/contacts`,
        json: true,
      };
      responseData = await this.helpers.httpRequest(options);
      }
    }
    // Map data to n8n data
    return [this.helpers.returnJsonArray(responseData)];
  }
}
```

## 相关资源 <a id="related-resources"></a>

* [规划节点](./)
* [选择节点类型](choose-a-node-type.md)
* [节点界面设计](node-ui-design.md)
* [选择节点文件结构](choose-node-file-structure.md)
