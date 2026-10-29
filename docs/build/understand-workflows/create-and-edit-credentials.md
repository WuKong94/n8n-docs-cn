---
contentType: howto
nodeTitle: 创建和编辑凭据
originalFilePath: credentials/add-edit-credentials.md
originalUrl: https://docs.n8n.io/credentials/add-edit-credentials
url: https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials
description: 创建和编辑凭据的方法。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 创建和编辑凭据 <a id="create-and-edit-credentials"></a>

凭据是安全存储的身份验证信息，用于将 n8n 工作流连接到 API、数据库等外部服务。

{% hint style="info" %}
在 n8n Cloud 上，支持的 AI 模型和服务甚至无需配置凭据：在节点上选择 **Use Gateway credits（使用 Gateway 额度）**，即可使用 [Gateway 额度](use-gateway-credits.md)运行，而无需使用自己的 API 密钥。
{% endhint %}

## 创建凭据 <a href="#create-a-credential" id="create-a-credential"></a>

1. 选择侧边菜单左上角的 <img src="../.gitbook/assets/universal-resource-button (1).png" alt="通用资源创建图标" data-size="line"> **Create（创建）** 按钮，再选择凭据。
2. 如果 n8n 实例支持项目[^1]，还需要选择是在个人空间中创建凭据，还是在你有权访问的某个项目中创建。使用社区版时，凭据会在个人空间中创建。
3. 选择要连接的应用或服务。

或者：

1. 在 **Overview（概览）** 页面或某个项目中，选择右上角的 <img src="../.gitbook/assets/universal-resource-button (1).png" alt="通用资源创建图标" data-size="line"> **Create（创建）** 按钮，再选择 Credential（凭据）。
2. 如果从 **Overview（概览）** 页面操作，凭据会创建在个人空间中；如果从项目中操作，则会创建在该项目中。
3. 选择要连接的应用或服务。

在工作流编辑器中编辑节点时，也可以通过凭据下拉菜单创建新凭据。

打开凭据弹窗后，输入该服务要求的信息。配置指南请参阅[凭据库](../../integrations/builtin/credentials/README.md)中对应服务的页面。

保存凭据时，n8n 会进行测试，确认其可以正常工作。

{% hint style="info" %}
**凭据命名**

n8n 默认将新凭据命名为“_节点名称_ account”。与重命名节点类似，可以点击名称来重命名凭据。建议使用能够标识应用或服务、类型和用途的名称。统一的命名规则有助于跟踪和识别凭据。
{% endhint %}

## 选择凭据类型 <a href="#choose-a-credential-type" id="choose-a-credential-type"></a>

创建或编辑 OAuth 凭据时，可以选择 **Credential type（凭据类型）**：

* **Fixed credential（固定凭据）**：无论谁运行工作流，都使用相同凭据。这是默认行为。
* **End-user credential（最终用户凭据）**：运行时使用各个用户自己的凭据，且只有该用户能够查看和使用它。

最终用户凭据让工作流使用触发者的凭据运行，并确保每个用户的数据仅对其本人可见。n8n Cloud Enterprise 和自托管 Enterprise 的 OAuth 凭据提供 **Fixed credential（固定凭据）** 与 **End-user credential（最终用户凭据）** 类型选择。设置方法请参阅[最终用户凭据](../../administer/manage-credentials/end-user-credentials.md)。

## 允许的 HTTP 请求域名 <a href="#allowed-http-request-domains" id="allowed-http-request-domains"></a>

许多面向 Web API 和服务的 n8n 凭据都包含 **Allowed HTTP Request Domains（允许的 HTTP 请求域名）** 字段。在 **HTTP Request** 节点中选择该凭据时，此字段控制允许将凭据用于哪些域名。凭据用于其专属节点时，此字段不生效。

此字段有三个选项：

* **All（全部）**：凭据可用于任意 URL。
* **Specific Domains（指定域名）**：限制为特定域名，填写以逗号分隔的列表，例如 `httpbin.org, api.github.com`。
* **None（无）**：完全禁止在 **HTTP Request** 节点中使用此凭据。

此字段用于防止凭据被误用，例如将凭据发送到预期域名之外的 URL。

## 在凭据中使用表达式 <a href="#expressions-in-credentials" id="expressions-in-credentials"></a>

可以使用表达式[^2]，在工作流运行时动态设置凭据：

1. 在工作流中找到包含凭据的数据路径。具体路径取决于数据中的参数名称。确保运行到需要凭据的节点时，包含凭据的数据在工作流中可用。
2. 创建凭据时，将鼠标悬停在要使用表达式的字段上。
3. 开启 **Expression（表达式）**。
4. 输入表达式。

### 示例工作流 <a href="#example-workflow" id="example-workflow"></a>

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22name%22%3A%20%22Dynamic%20credentials%20using%20expressions%22%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22path%22%3A%20%22da4071f2-7550-4dae-aa48-8bced4291643%22%2C%0A%20%20%20%20%20%20%20%20%22formTitle%22%3A%20%22Test%20dynamic%20credentials%22%2C%0A%20%20%20%20%20%20%20%20%22formDescription%22%3A%20%22This%20form%20is%20for%20testing%20an%20n8n%20workflow%20that%20demonstrates%20setting%20credentials%20with%20expressions.%22%2C%0A%20%20%20%20%20%20%20%20%22formFields%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22values%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22fieldLabel%22%3A%20%22Enter%20your%20NASA%20API%20key%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22requiredField%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%22responseMode%22%3A%20%22responseNode%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22cc6f2b1e-0ed0-4d22-8a44-d7223ba283b4%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22n8n%20Form%20Trigger%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.formTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20560%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22webhookId%22%3A%20%22da4071f2-7550-4dae-aa48-8bced4291643%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22additionalFields%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22ef336bae-3d4f-419c-ab5c-b9f0de89f170%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.nasa%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20900%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22credentials%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22nasaApi%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22id%22%3A%20%22QDDBOZOD6k3ijL5t%22%2C%0A%20%20%20%20%20%20%20%20%20%20%22name%22%3A%20%22NASA%20account%22%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22respondWith%22%3A%20%22redirect%22%2C%0A%20%20%20%20%20%20%20%20%22redirectURL%22%3A%20%22%3D%7B%7B%20%24json.url%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22143bcdb6-aca0-4dd8-9204-9777271cd230%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Respond%20to%20Webhook%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.respondToWebhook%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201220%2C%0A%20%20%20%20%20%20%20%20520%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22This%20workflow%20shows%20how%20to%20set%20credentials%20dynamically%20using%20expressions.%5Cn%5Cn%5CnFirst%2C%20set%20up%20your%20NASA%20credential%3A%20%5Cn%5Cn1.%20Create%20a%20new%20NASA%20credential.%5Cn1.%20Hover%20over%20%2A%2AAPI%20Key%2A%2A.%5Cn1.%20Toggle%20%2A%2AExpression%2A%2A%20on.%5Cn1.%20In%20the%20%2A%2AAPI%20Key%2A%2A%20field%2C%20enter%20%60%7B%7B%20%24json%5B%5C%22Enter%20your%20NASA%20API%20key%5C%22%5D%20%7D%7D%60.%5Cn%5Cn%5CnThen%2C%20test%20the%20workflow%3A%5Cn%5Cn1.%20Get%20an%20%5BAPI%20key%20from%20NASA%5D%28https%3A%2F%2Fapi.nasa.gov%2F%29%5Cn2.%20Select%20%2A%2AExecute%20workflow%2A%2A%5Cn3.%20Enter%20your%20key%20using%20the%20form.%5Cn4.%20The%20workflow%20runs%20and%20sends%20you%20to%20the%20NASA%20picture%20of%20the%20day.%5Cn%5Cn%5CnFor%20more%20information%20on%20expressions%2C%20refer%20to%20%5Bn8n%20documentation%20%7C%20Expressions%5D%28https%3A%2F%2Fdocs.n8n.io%2Fcode%2Fexpressions%2F%29.%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20564%2C%0A%20%20%20%20%20%20%20%20%22width%22%3A%20322%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%204%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%220a0dee23-fa16-4f09-b5e0-856f47fb53d0%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20120%2C%0A%20%20%20%20%20%20%20%20140%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22User%20submits%20an%20API%20key%20using%20the%20form%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22dd766e32-334d-4e46-9daa-7800b134a3a5%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note1%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20500%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22The%20workflow%20passes%20the%20key%20to%20the%20NASA%20node.%20You%20can%20reference%20the%20value%20using%20the%20expression%20%60%24json%5B%5C%22Enter%20your%20NASA%20API%20key%5C%22%5D%60.%20This%20is%20also%20available%20to%20the%20node%20credential.%20%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%2C%0A%20%20%20%20%20%20%20%20%22color%22%3A%205%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%223d8f02e6-e029-41dc-89ad-0f5cffe09348%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note2%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20820%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22content%22%3A%20%22The%20Respond%20to%20Webhook%20node%20controls%20the%20form%20response%20%28in%20this%20example%2C%20redirecting%20the%20user%20to%20an%20image%29%22%2C%0A%20%20%20%20%20%20%20%20%22height%22%3A%20319%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22096eb6ab-c276-4687-9dc0-50e16a8f709a%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Sticky%20Note3%22%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.stickyNote%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%201140%2C%0A%20%20%20%20%20%20%20%20380%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22n8n%20Form%20Trigger%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22NASA%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22NASA%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Respond%20to%20Webhook%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/credentials/dynamic_credentials_using_expressions.json" %}

#### 使用示例 <a href="#using-the-example" id="using-the-example"></a>

{% include "../../reusable-content/.gitbook/includes/examples-color-key.md" %}

[^1]: n8n 项目可以将工作流、变量和凭据分为不同组，便于管理。通过共享相关资源并将其分类隔离，项目可以帮助团队协作。
[^2]: 在 n8n 中，表达式通过执行 JavaScript 代码动态填充节点参数。你可以使用 n8n 表达式语法，根据前面节点、其他工作流或 n8n 环境中的数据定义值，而不是提供静态值。

## 相关资源 <a id="related-resources"></a>

* [理解工作流](./)
* [创建和运行工作流](create-and-run-workflows.md)
* [保存和发布工作流](save-and-publish-workflows.md)
* [使用 Gateway 额度](use-gateway-credits.md)
* [工作流组件](workflow-components/README.md)
* [理解执行](understand-executions/README.md)
