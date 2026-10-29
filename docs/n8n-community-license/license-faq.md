---
description: n8n 社区许可证的常见问题。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# n8n 社区许可证常见问题 <a id="n8n-community-license-faq"></a>

你可能想知道自己的项目能否使用 n8n 的可持续使用许可证。本页提供进一步说明。如有疑问，请通过 [license@n8n.io](mailto:license@n8n.io) 联系我们。

**如果工作流仅由你本人或组织内部人员创建或修改，你可以依据社区许可证免费使用 n8n。**


## 社区许可证何时适用？ <a id="when-does-the-community-license-apply"></a>

社区许可证的正式名称为[可持续使用许可证](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)（**SUL**），免费且仅适用于 n8n 自托管版本。n8n Cloud 是付费订阅服务，使用其自身条款；本页不适用于 n8n Cloud。

**可持续使用许可证中的“内部业务目的”，指在组织内部或自己的产品中使用 n8n，而企业外部人员可以接收或查看工作流的产出。**

## 社区许可证允许的用途 <a id="what-you-can-do-under-the-community-license"></a>

- 使用 n8n 社区版辅助运营自己的业务。
- 将 n8n 社区版用于个人项目、学习或研究。
- 在自己的实例上为客户构建自动化，前提是客户无法自行创建或编辑这些自动化。
- 向客户收取工作流创建、设置和维护服务费用。
- 向客户收取培训和咨询服务费用。
- 在自己的产品幕后使用 n8n，让用户使用和触发你构建的自动化，甚至连接他们自己的账户。
- 运行多个 n8n 社区版实例。

## 社区许可证不允许的用途 <a id="what-you-cannot-do-under-the-community-license"></a>

- 将 n8n 作为服务托管，并允许客户构建工作流。
- 允许外部最终用户通过你的产品构建或配置自己的工作流，无论使用自定义 UI、我们的 API、MCP，还是代表用户操作的 AI 智能体。
- 复刻 n8n 代码，以推出自己的自动化产品。
- 移除 n8n 品牌标识，以白标形式原样提供 n8n。
- 没有企业许可证，却使用要求许可证密钥的企业功能。

## 仍不确定？ <a id="still-unsure"></a>

如果上述示例没有明确涵盖你的使用场景：

- 许可问题，请联系 [license@n8n.io](mailto:license@n8n.io)。
- 商业许可洽谈，请联系 [sales@n8n.io](mailto:sales@n8n.io)。

## 更多示例 <a id="more-examples"></a>

<details>
<summary>在自己的产品中将 n8n 用作后端引擎</summary>

#### 社区许可证下的使用 <a id="under-the-community-license"></a>

依据社区许可证，你可以在自己的产品中将 n8n 用作后端处理引擎，前提是只有你的后端与 n8n 通信，且最终用户不访问 n8n 界面，也不配置 n8n 工作流。

#### 示例：使用 n8n 处理后台数据的 SaaS 应用 <a id="example-saas-application-using-n8n-for-background-data-processing"></a>

一个项目管理 SaaS 使用 n8n 自动为收到的支持工单评分。用户提交工单后，应用通过内部 API 调用将数据发送到 n8n。n8n 处理数据并返回优先级分数。用户只看到结果，整个过程中都看不到 n8n。

这是允许的，因为 n8n 仅作为内部处理层，不涉及用户凭据，产品价值来自应用本身，而非 n8n。

#### 示例：使用 n8n 实现后台营销自动化的 Next.js 平台 <a id="example-nextjs-platform-using-n8n-for-background-marketing-automation"></a>

一个 Next.js 网站在公司运营的服务器上使用 n8n，自动执行后台营销工作流，包括生成内容创意、安排发布和管理集成。最终用户只与网站交互，看不到 n8n。n8n 不是该平台提供给用户的功能，也没有用户访问或配置它。

这是允许的，因为 n8n 支持的是运营方自己的业务活动，全程使用运营方自己的 API 密钥，平台的商业价值来自网站及其内容，而非 n8n。

#### 示例：嵌入工作流构建器的 SaaS 平台 <a id="example-saas-platform-with-embedded-workflow-builder"></a>

一个面向自由职业者的 SaaS 平台包含工作流自动化功能，用户通过自定义 UI 构建自己的自动化。n8n 在运营方服务器上充当后端，用户从不直接看到 n8n。

这是不允许的。自定义 UI 层不会改变使用方式的性质。最终用户仍在配置由 n8n 驱动的自动化逻辑，而工作流构建是产品的核心商业价值。SUL 判断的关键在于谁控制工作流逻辑，以及服务于谁的商业利益；不能仅以 n8n 界面是否可见来判断。

**处理方式：**请联系 [sales@n8n.io](mailto:sales@n8n.io)，洽谈适用于此架构的企业许可证。

</details>

<details>
<summary>社区或教育工作坊</summary>

大使、社区组织者或其他组织，可以在聚会或工作坊等免费教育活动中，使用自托管 n8n 实例开展实践练习，让参与者在活动期间临时构建、复用或测试工作流。

当访问是临时的、仅限活动期间且以教育为目的时，这是允许的。活动结束后，参与者不应继续访问组织者的实例，也不应使用该实例提供托管 n8n 访问服务。

如果参与者希望在活动后继续使用 n8n，应创建自己的 n8n Cloud 试用账户，或自行托管实例。

活动结束后，组织者应及时移除参与者的访问权限及其提供的任何凭据。如果意外保留了访问权限，应在发现后尽快移除。
</details>

<details>
<summary>产品价值来自 n8n 的情况</summary>

可持续使用许可证限制产品商业价值全部或主要来自 n8n 功能的用途。实际判断时，需要看销售的是 n8n 本身，还是将它用作支持另一种产品销售的工具。

#### 示例：技术培训公司使用 n8n 进行工作坊现场演示 <a id="example-technology-training-company-using-n8n-for-live-workshop-demonstrations"></a>

一家技术教育企业自行托管 n8n，在有关数据、AI 和自动化的付费工作坊中进行现场演示。学员在课程期间直接操作 n8n 实例，但工作坊结束后不提供账户或持续访问权限。

这是允许的，因为销售的商业产品是培训本身。n8n 用于演示，类似烹饪学校使用专业厨房设备而不销售设备。学员访问仅限于工作坊的时间和目的，收取的是培训费用，而非 n8n 访问费用。

使这种方式符合 SUL 范围的条件包括：

- 不将 n8n 作为交付物提供给参与者。
- 课程结束后不提供持续访问权限。
- 仅连接运营方拥有或控制的系统。
- 不使用企业功能。
- 收取培训服务费用，而非 n8n 访问费用。

#### 示例：“自动化即服务” <a id="example-automation-as-a-service"></a>

一家公司销售名为“AutoOps”的订阅产品，让客户能够：

- 连接自己的应用，如 Google Workspace、Slack、HubSpot 等。
- 使用 AutoOps 中的可视化构建器构建自动化。
- 在托管后端运行这些自动化。

#### 为什么其价值全部或主要来自 n8n： <a id="why-the-value-derives-entirely-or-substantially-from-n8n"></a>

- 商业价值就是自动化能力本身，而非自动化仅起辅助作用的其他独立产品，也不是围绕 n8n 提供的服务。
- 客户购买的是创建和运行由 n8n 驱动的工作流的能力，无论他们是否看到 n8n 界面。
</details>

<details>
<summary>工作流构建、凭据与控制权</summary>

围绕在 n8n 社区版中使用第三方凭据的问题一直很多。关键在于谁控制工作流逻辑，而不是凭据属于谁。最终用户可以将自己的账户和凭据连接到你为其构建的自动化，前提是他们不能访问 n8n 工作流构建器，也不能自行配置工作流逻辑。

凭据属于最终用户还是运营方是次要因素，关键是最终用户能否构建或修改工作流。判断也不取决于使用的媒介：无论是 UI、n8n API、MCP，还是代表用户操作的 AI 智能体，都要看最终用户是否决定工作流逻辑。通过 API 或 webhook 触发、执行预先构建的工作流是允许的。

#### 示例：客户自行托管 n8n 并使用自己凭据的文档处理工具 <a id="example-document-processing-tool-with-customer-hosted-n8n-and-customer-credentials"></a>

一家软件供应商销售文档处理工具，用于获取邮件附件、通过 OCR 从 PDF 中提取数据，再将结果写入客户的 SQL 数据库。n8n 自托管在客户本地，客户向实例输入自己的凭据，例如 OpenAI 凭据。供应商按月收取文档处理平台费用。

这是可行的，但可能处于灰色地带。将 n8n 作为付费产品的一部分交付客户，须遵守许可证中的额外条件；客户拥有本地访问权限后，也很难保证其无法构建工作流。上线前，请通过 [license@n8n.io](mailto:license@n8n.io) 确认架构。

#### 示例：自由职业顾问在共享 n8n 实例中使用客户自有凭据 <a id="example-freelance-consultant-using-client-owned-credentials-in-shared-n8n-instance"></a>

一名自由职业自动化顾问运行单个自托管 n8n 实例，为客户构建自定义工作流。每位客户生成自己的 OAuth 凭据或 API 密钥，并打开 n8n，通过 OAuth 对服务进行身份验证。

这是允许的。客户无权访问 n8n 界面或工作流逻辑。允许这种方式的原因是客户不能构建或修改工作流，而不是由顾问代为输入凭据。
</details>

<details>
<summary>咨询与代理服务用途</summary>

如果希望跨多个客户环境管理 n8n，请联系 [license@n8n.io](mailto:license@n8n.io)；涵盖多实例管理的**合作伙伴计划**仍在开发中。

可持续使用许可证明确允许咨询和自动化服务。关键条件是 n8n 始终作为你的内部工具，客户接收产出，而不获得访问权限。

#### 能否以托管服务的形式，为多个客户交付自动化解决方案？ <a id="can-i-use-n8n-to-deliver-automation-solutions-to-multiple-clients-as-a-managed-service"></a>

可以，前提是客户不直接访问你的 n8n 实例。

允许在自己的 n8n 实例上代客户构建、运行和维护工作流，也允许收取咨询或开发费用。单个实例可服务的客户数量没有限制。决定因素是客户访问权限，而非客户数量或收入规模。

#### 示例：自动化代理服务商 <a id="example-automation-agency"></a>

一位自动化顾问在代理服务商托管的单个 n8n 实例上，为小企业客户构建自定义工作流。客户支付咨询费用，只接收自动化消息、同步数据、聊天机器人回复等产出。客户均无权访问 n8n、其界面或底层工作流。

- 由顾问全权运营单个 n8n 实例。
- 客户为结果付费，而非为访问 n8n 付费。
- 客户只接收产出。
- 客户无权访问 n8n 界面或工作流逻辑。

#### 能否在客户自己的服务器上安装和管理 n8n？ <a id="can-i-install-and-manage-n8n-on-a-clients-own-server"></a>

可以，前提是你没有*同时*为其提供托管。客户在自己的基础设施上运行 n8n，并需要咨询或实施服务时，你可以就代其安装、配置、构建工作流和维护 n8n 收费。只要不同时提供托管服务，就是允许的，因为托管服务会与 n8n 自己的 Cloud 服务竞争。

<details>
<summary>更多禁止用途</summary>

无论使用场景如何组织，可持续使用许可证都明确禁止以下用途。

#### 构建竞争性自动化产品 <a id="building-a-competing-automation-product"></a>

可持续使用许可证将使用范围限制在内部业务目的，或非商业、个人用途。利用 n8n 源代码构建与 n8n 竞争的产品，例如工作流自动化平台、iPaaS 工具，或以自动化编排为核心价值的产品，不属于允许的用途。无论是否为竞争产品收费、是否修改源代码，都适用此限制。

#### 复刻 n8n，创建衍生自动化平台 <a id="forking-n8n-to-create-a-derivative-automation-platform"></a>

仅允许出于个人、非商业或内部用途创建复刻和衍生作品。专门为提供自动化即服务或推出竞争产品而创建复刻，不符合 SUL。

#### 没有企业许可证却使用企业专属功能 <a id="using-enterprise-only-features-without-an-enterprise-license"></a>

可通过源文件名中的 `.ee.` 字符串识别企业专属功能。无论自行托管还是使用 n8n Cloud，没有有效企业许可证却使用这些功能，都违反许可条款。如果不确定所用功能是否为企业专属，请联系 [license@n8n.io](mailto:license@n8n.io)。
</details>
