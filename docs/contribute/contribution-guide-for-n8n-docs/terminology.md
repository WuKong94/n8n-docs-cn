---
description: 文档中应使用的 n8n 官方术语，以及应避免的非官方用词。
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 术语与命名 <a id="terminology-and-naming"></a>

本文是[风格指南](style-guide-for-n8n-docs.md)的配套文档。风格指南介绍写作风格、格式和结构，本文则是产品术语的权威依据。

n8n 文档力求在每个页面中，对同一概念使用同一个术语，并优先使用官方产品术语，而非看似合适的近义词。统一术语既能帮助读者，也能直接改善 AI 工具（搜索、文档助手和编程智能体）查找和使用文档的效果。

## 大小写 <a id="casing"></a>

* **正文使用句首式大小写：**例如 Add a trigger node、create a sub-workflow。
* **直接引用界面标签或节点名称时，加粗并严格使用产品中的大小写：**例如 Select **Add trigger**、the **HTTP Request** node，与界面显示保持一致。
* **产品名称写作 `n8n`，**始终使用小写，即使位于句首也不例外。

## 核心概念 <a id="core-concepts"></a>

| 应使用 | 避免使用 |
| --- | --- |
| workflow（工作流） | flow、automation（作为整个工作流的名词）、scenario、pipeline、zap |
| node（节点） | step、block、action、module |
| execution（工作流的一次执行） | run（作为名词）、job、invocation |

## 工作流生命周期 <a id="workflow-lifecycle"></a>

| 应使用 | 避免使用 |
| --- | --- |
| publish、unpublish a workflow（发布、取消发布工作流）；published workflow（已发布工作流） | activate、deactivate、enable、disable、turn on、go live、deploy |
| run、execute a workflow（作为动词，运行或执行工作流） | kick off、fire |
| pin data（固定数据）；pinned data（固定的数据） | mock data、freeze data、lock data、sample data |

## 节点 <a id="nodes"></a>

| 应使用 | 避免使用 |
| --- | --- |
| app node（应用节点） | integration node、service node |
| core node（核心节点） | system node |
| cluster node（集群节点）；root node（根节点）；sub-node（子节点） | parent node、child node、super node |
| community node（可安装、由社区发布的社区节点） | custom node、third-party node、plugin、add-on |
| Execute Sub-workflow Trigger 节点；Execute Sub-workflow 节点 | Execute Workflow Trigger 节点、Execute Workflow 节点（已弃用名称） |
| AI Agent 节点 | 单独使用 Agent 节点 |

## 凭据与连接 <a id="credentials-and-connections"></a>

| 应使用 | 避免使用 |
| --- | --- |
| credential（凭据，用于存储服务的身份验证信息） | connection（用作凭据的同义词） |
| connection（连接，指画布上两个节点间的连线） | wire、link |

n8n 界面有时也将凭据的身份验证关联称为 connection，例如私有凭据的共享消息。文档中应区分两者：**credential** 用于向服务进行身份验证，**connection** 用于连接画布上的节点。

## 画布与编辑器 <a id="canvas-and-editor"></a>

两条格式规则：只有术语是选择、单击或打开操作的直接目标时才**加粗**；仅用于说明位置时不加粗。已定义界面元素的名称只将首个单词**首字母大写**，例如 Workflow menu，不使用 Workflow Menu。

| 应使用 | 避免使用 |
| --- | --- |
| canvas（画布） | editor board、diagram、workspace、graph |
| sticky note（便笺） | comment、annotation、label、memo |
| sub-workflow（子工作流） | subworkflow、sub workflow、subflow、child workflow、nested workflow |
| left menu（左侧菜单，即包含 Overview、Projects、Favorites 等的应用级左侧导航） | sidebar、left sidebar、navigation menu、main menu |
| Canvas header（画布顶部栏，包含项目或工作流名称、Workflow menu、编辑器/执行/评估切换项以及 Publish） | top navigation bar、top menu |
| Workflow menu（位于 Canvas header 中，图标为横向 ⋯） | three dots icon、the three dots、Options（此名称保留给竖向图标） |
| Options menu（图标为竖向 ⋮，属于每行或每个条目的菜单，而非画布元素） | three-dot menu（方向不明确）、three dots menu |
| Nodes panel（节点面板，通过画布上的 **+** 按钮打开） | Node Panel（大写单数形式）、add node menu、What happens next? panel |
| Node details view（节点详情视图，双击节点打开） | node editor view、NDV（未预先定义缩写） |
| input panel、output panel（输入面板、输出面板，即节点详情视图的两侧面板） | Input panel/Output panel（首字母大写）、INPUT/OUTPUT pane |
| Logs panel（日志面板，位于画布底部） | bottom panel、bottom menu、canvas footer |

+Workflow menu 的图标为 `three-dots-horizontal.png`，Options menu 的图标为 `three-dot-options-menu.png`。提及这些菜单时，应在行内使用对应图标。行内图标的格式请参阅[风格指南](style-guide-for-n8n-docs.md#images)。

## AI 与智能体 <a id="ai-and-agents"></a>

| 应使用 | 避免使用 |
| --- | --- |
| sub-agent（子智能体） | subagent、child agent |

n8n 有多项不同的 AI 工作流构建功能。每项都是具体的 n8n 产品名称，而非泛指描述，因此不能互换使用：

| 应使用 | 避免使用 |
| --- | --- |
| n8n Assistant（基于对话的智能体，可创建、编辑、测试和发布工作流及智能体） | assistant、the AI、chatbot、AI Assistant |
| AI Workflow Builder（旧版功能，根据提示生成和改进单个工作流） | workflow builder、builder |
| Ask n8n AI（旧版帮助助手，已停止积极开发，应将读者引导至 AI Assistant） | AI assistant（用作此功能的同义词）、help assistant |

## 功能成熟度 <a id="feature-maturity"></a>

| 应使用 | 避免使用 |
| --- | --- |
| Preview（功能成熟度标签，首字母大写） | beta、alpha、early access |

## 平台与部署 <a id="platform-and-deployment"></a>

| 应使用 | 避免使用 |
| --- | --- |
| self-hosted（自托管） | self hosted、on-premise、on-premises、on-prem |
| n8n Cloud | Cloud、hosted version、SaaS、the cloud、managed n8n |
| instance（实例，即运行中的 n8n 系统） | server、box、deployment（用作运行中系统的名词） |
| Enterprise（方案） | enterprise edition、premium、paid tier |
| Cloud console（n8n Cloud 控制台，位于 app.n8n.cloud，实例所有者在其中管理实例、方案、账单和额度） | admin dashboard、admin panel、Cloud dashboard、Cloud admin dashboard |

并非完全禁止使用 deployment：描述部署行为时，例如 deployment methods、the deployment finishes，或指 Kubernetes 的 `Deployment` 资源时，此用法正确。只有将其用作运行中的 n8n 系统的名词时，才应改用 instance。

每页首次提及时，写作 n8n Cloud console，以区别于 Google Cloud Console 等其他供应商的控制台，之后可以简写为 Cloud console。所有者在其中管理的 n8n Cloud 系统应称为 instance，不使用 workspace。n8n 编辑器的左侧菜单将 Cloud 控制台入口标为 **Admin Panel**；只有在指示读者选择该入口的步骤中，才使用这一确切标签。

### 方案与层级 <a id="plans-and-tiers"></a>

使用以下确切方案名称，保持指定大小写，顺序从低到高。不要自行创造其他名称，例如 professional plan 或 team tier：

* **n8n Cloud：**Starter、Pro、Enterprise
* **自托管：**Community、Registered Community、Business、Enterprise

同时指代全部层级时，使用 All plans 或 All editions，不要逐项列举。

## 功能 <a id="features"></a>

| 应使用 | 避免使用 |
| --- | --- |
| project（项目） | workspace、team space |
| folder（文件夹） | directory（应用内）、group |
| environment variable（环境变量） | env（作为名词）、config var |
| data table（数据表） | database table、datatable、the table feature |

## 产品与品牌名称 <a id="product-and-brand-names"></a>

| 应使用 | 避免使用 |
| --- | --- |
| n8n（始终小写） | N8n、N8N、n8N |
| GitHub、npm、JavaScript、OAuth2 | Github、NPM、Javascript、oAuth |

## 相关资源 <a id="related-resources"></a>

* [n8n 文档贡献指南](./)
* [n8n 文档风格指南](style-guide-for-n8n-docs.md)
* [面向智能体的友好文档](agent-friendly-docs.md)
