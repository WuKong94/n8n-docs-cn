# n8n 中文文档与教程：工作流自动化、AI Agent 和 Docker 部署

**用中文学习 n8n，从第一个工作流开始，把重复操作变成可维护的自动化流程。**

`n8n-docs-cn` 是 n8n 官方文档的简体中文社区翻译项目，涵盖 n8n 入门教程、节点与凭据、数据处理、AI Agent（智能体）、MCP、Docker 自托管部署和 API 开发。适合第一次接触 n8n 的学习者，也适合在搭建工作流时查参数、找示例和排查问题。

**[在线阅读 n8n 中文文档 → docs.n8ndoc.com](https://docs.n8ndoc.com/)**

[n8n 中文站 · n8ndoc.com](https://n8ndoc.com/) · [构建第一个工作流](https://docs.n8ndoc.com/build-your-first-workflow) · [反馈译文问题](https://github.com/WuKong94/n8n-docs-cn/issues)

Simplified Chinese translation of the n8n documentation, covering workflow automation, AI agents, MCP, nodes, self-hosting with Docker, and API development.

> 本项目由社区维护，非 n8n 官方站点。英文原文来自 [n8n-io/n8n-docs](https://github.com/n8n-io/n8n-docs)，对应版本记录在 [upstream.json](upstream.json) 中。

## 这份 n8n 中文文档能帮你做什么？

n8n 通过可视化工作流连接应用、API 和 AI 模型。你可以从现成节点开始，在需要时加入表达式或代码，完成数据同步、定时任务、消息通知和 AI 信息处理等工作。

本项目把教程和参考手册放在同一套中文文档中：

- **入门时有步骤可跟**：选择使用方式，认识触发器、节点和执行数据，完成第一个工作流。
- **搭建时有资料可查**：查找节点配置、凭据认证、HTTP 请求、表达式、条件分支与循环。
- **接入 AI 时有概念可对照**：理解模型、工具、记忆和智能体的关系，学习 AI 工作流与 MCP 集成。
- **部署和维护时有指南可用**：查阅 Docker、Docker Compose、自托管配置、用户管理与错误处理。

译文保留原始图片、附件和代码示例，常用术语遵循统一的[翻译术语表](TERMINOLOGY.md)，方便对照英文界面与原文。

## n8n 中文教程：按目标开始

### 第一次使用 n8n

1. 阅读[学习路线](https://docs.n8ndoc.com/learning-paths)，了解有哪些学习入口。
2. [选择使用方式](https://docs.n8ndoc.com/choose-how-to-use-n8n)，准备一个 n8n 实例。
3. 跟着[第一个工作流教程](https://docs.n8ndoc.com/build-your-first-workflow)，完成“定时获取天气 → 整理消息 → 保存到数据表”的练习。
4. 打开每个节点的输入和输出，观察数据如何变化，再修改一个字段或触发时间，验证自己的理解。

把“能解释每一步的数据从哪里来、要到哪里去”作为第一个学习目标。之后再加入分支、外部 API 和 AI，排错时会更容易定位问题。

### 已经有明确需求

| 你想完成的事情 | 中文文档入口 |
| --- | --- |
| 搭建工作流，处理数据、分支与循环 | [n8n 使用指南](https://docs.n8ndoc.com/build) |
| 查某个节点的参数、操作和认证方式 | [集成节点与凭据参考](https://docs.n8ndoc.com/integrations) |
| 构建 AI Agent，连接模型、工具和记忆 | [AI 工作流指南](https://docs.n8ndoc.com/build/integrate-ai) |
| 通过 MCP 连接 n8n 与 AI 工具 | [n8n MCP 服务器指南](https://docs.n8ndoc.com/build/integrate-ai/mcp-servers) |
| 安装和维护自己的 n8n 实例 | [部署与自托管指南](https://docs.n8ndoc.com/deploy) |
| 管理用户、权限和实例 | [n8n 管理指南](https://docs.n8ndoc.com/administer) |
| 开发自定义节点或调用 n8n API | [开发与 API 文档](https://docs.n8ndoc.com/connect) |
| 了解数据保护和安全设置 | [隐私与安全](https://docs.n8ndoc.com/privacy-and-security) |

## 常用节点、部署教程与排错速查

- **调用外部接口**：[HTTP Request 节点](https://docs.n8ndoc.com/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)，学习请求参数、认证与响应处理。
- **编写自定义逻辑**：[Code 节点](https://docs.n8ndoc.com/integrations/builtin/core-nodes/n8n-nodes-base.code)，处理现成节点无法直接完成的逻辑。
- **读取和转换字段**：[表达式与数据转换](https://docs.n8ndoc.com/build/work-with-data/transform-data/expressions-for-data-transformation)，理解节点间的数据引用。
- **在服务器上运行 n8n**：[Docker 安装](https://docs.n8ndoc.com/deploy/host-n8n/install-options/install-with-docker) / [Docker Compose 部署](https://docs.n8ndoc.com/deploy/host-n8n/install-options/install-using-docker-compose)。
- **处理执行失败**：[工作流错误处理](https://docs.n8ndoc.com/build/flow-logic/handle-errors-gracefully)，为异常情况设计后续流程。

## 在线阅读与源码仓库

日常学习和查询，访问 **[docs.n8ndoc.com](https://docs.n8ndoc.com/)**，可以使用中文搜索和章节导航；了解中文站及部署教程，访问 **[n8ndoc.com](https://n8ndoc.com/)**。修改译文、查看来源版本或提交贡献，则使用本仓库。

```text
n8n-docs-cn/
├── docs/                       # 中文文档、图片与附件
│   ├── get-started/             # 入门与学习路线
│   ├── build/                   # 工作流、数据处理与 AI
│   ├── integrations/            # 节点与凭据参考
│   ├── deploy/                  # Cloud 与自托管部署
│   ├── administer/              # 用户与实例管理
│   ├── connect/                 # 节点开发与 API
│   └── changelog/               # 更新记录，保留英文
├── TERMINOLOGY.md               # 翻译术语约定
├── upstream.json                # 锁定的英文上游版本
├── translation-status.json      # 译文状态与来源校验信息
├── source-corrections.json      # 有依据的原文修正记录
└── LICENSE.md                   # 原始文档许可证
```

本仓库维护文档内容。在线文档站使用独立的网站工程构建，按锁定版本读取译文，审核后发布。因此，仓库中的最新修改与线上内容可能存在发布时间差。

## 翻译范围与版本

中文译文基于明确的上游快照维护。阅读涉及新功能的说明时，请结合自己的 n8n 版本，并按需对照[官方英文文档](https://docs.n8n.io/)。

- **来源版本**：见 [upstream.json](upstream.json)。
- **翻译状态**：见 [translation-status.json](translation-status.json)；登记范围包含正文、目录、复用片段和 API 参考，不能直接当作网页数量。
- **更新记录**：`docs/changelog/` 保留英文，便于核对原始版本变更。
- **API 来源**：额外导出的英文 API 参考快照及哈希记录保存在 [.upstream/generated-api/](.upstream/generated-api/)。

<details>
<summary>维护者说明：翻译与校验约定</summary>

- 文件名和目录尽量与上游一致；跨章节链接使用对应文件的相对路径，保留原英文章节锚点。
- 保留原始图片、动图、附件、程序代码和表达式。
- 代码围栏中的自然语言提示词可以翻译，原文及译文哈希在状态文件的 `prose_fences` 中单独登记。
- OpenAPI JSON 仅翻译经过复核的 `title`、`summary`、`description` 字符串，并通过 `openapi_fences` 逐字段登记；接口路径、参数名、类型、枚举、默认值和示例数据保持原样。
- 有明确文档证据的原文修正记入 `source-corrections.json`，上游英文快照保持原样。
- `translated` 表示译文已写入并登记来源，不等同于已通过网站渲染和线上链接验收。URL 映射、转换与检查脚本在网站工程中维护。

</details>

## 官方文档更新检查

GitHub Actions 在**每月 1 日北京时间 09:23**运行一次上游检查，也可以在 [Actions → Monthly upstream documentation check](https://github.com/WuKong94/n8n-docs-cn/actions/workflows/check-upstream.yml) 中选择 **Run workflow** 随时检查。

检查覆盖官方 Git 仓库的正文、目录、共享片段、资源，以及官网单独生成的 API 参考和公开 URL。结果展示在运行摘要中，并提供 `upstream-documentation-report` 下载，包含 Markdown 报告和 JSON 明细，保留 90 天。检查失败会明确标记，网络错误不会被当成内容删除。

待更新清单以已接受的原文版本和逐文件哈希为基线，未完成的更新会在后续检查中持续出现。完成译文和网站验收后，再更新来源版本及官网快照。

本地检查需要 Python 3.12、Git 和 curl：

```sh
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/check_upstream.py
```

## 参与贡献与反馈

欢迎修正翻译、补充说明和反馈失效链接。

1. 通过 [Issues](https://github.com/WuKong94/n8n-docs-cn/issues) 提供文档地址、问题位置和建议修改；如果与操作有关，请附上 n8n 版本及必要的复现步骤。
2. 修改译文前阅读 [TERMINOLOGY.md](TERMINOLOGY.md)，让节点名、界面名称和术语保持一致。
3. Fork 本仓库，在分支中修改对应文档，然后提交 Pull Request。请保留来源说明、图片路径和可执行示例，说明修改原因。

n8n 产品使用问题也可以到 [n8n 官方社区](https://community.n8n.io/) 交流。查找可参考的自动化流程，可浏览 [n8n 官方工作流模板库](https://n8n.io/workflows/)。

## 来源与许可

感谢 [n8n 文档项目](https://github.com/n8n-io/n8n-docs)及所有贡献者。本仓库保留锁定上游版本的 [LICENSE.md](LICENSE.md) 原文，已翻译文件带有修改说明；使用和再分发请以该文件的实际条款为准。文档许可与网站程序许可分别管理。

如果这份中文文档对你有帮助，欢迎 Star 收藏，或把 [n8n 中文文档](https://docs.n8ndoc.com/) 分享给正在学习工作流自动化的朋友。
