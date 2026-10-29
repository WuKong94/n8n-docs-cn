---
title: Tools AI Agent（工具 AI 智能体） 节点文档
contentType:
- integration
- reference
priority: critical
nodeTitle: Tools AI Agent（工具 AI 智能体） 节点文档
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md
originalUrl: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
url: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
description: 了解如何在 n8n 的 AI Agent 节点中使用 Tools Agent，并按照技术文档将其集成到工作流中。
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


# Tools Agent（工具智能体） <a id="tools-agent"></a>

Tools Agent 通过外部工具[^1]和 API 执行操作、获取信息，可理解不同工具的能力，并根据任务决定使用哪种工具，有助于将 LLM 与各种外部服务和数据库集成。

此智能体增强了工具使用能力，并能够确保标准输出格式。

Tools Agent 实现 [LangChain 工具调用](https://docs.langchain.com/oss/javascript/langchain/tools)接口，用于描述可用工具及其架构。它还将解析器作为格式化工具传给模型，从而增强输出解析能力。

AI Agent 节点本身的更多信息，请参阅 [AI Agent](./README.md)。

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/use-with-chat-trigger.md" %}

此智能体支持以下聊天模型：

* [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/README.md)
* [Groq Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatgroq.md)
* [Mistral Cloud Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Anthropic Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)
* [Microsoft Foundry Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)

<details>

<summary>Tools Agent 可使用以下工具……</summary>

* [Call n8n Workflow（调用 n8n 工作流）](../../sub-nodes/n8n-nodes-langchain.toolworkflow.md)
* [Code（代码）](../../sub-nodes/n8n-nodes-langchain.toolcode.md)
* [HTTP Request（HTTP 请求）](../../../core-nodes/n8n-nodes-base.httprequest/README.md)
* [Action Network](../../../app-nodes/n8n-nodes-base.actionnetwork.md)
* [ActiveCampaign](../../../app-nodes/n8n-nodes-base.activecampaign.md)
* [Affinity](../../../app-nodes/n8n-nodes-base.affinity.md)
* [Agile CRM](../../../app-nodes/n8n-nodes-base.agilecrm.md)
* [Airtable](../../../app-nodes/n8n-nodes-base.airtable/README.md)
* [APITemplate.io](../../../app-nodes/n8n-nodes-base.apitemplateio.md)
* [Asana](../../../app-nodes/n8n-nodes-base.asana.md)
* [AWS Lambda](../../../app-nodes/n8n-nodes-base.awslambda.md)
* [AWS S3](../../../app-nodes/n8n-nodes-base.awss3.md)
* [AWS SES](../../../app-nodes/n8n-nodes-base.awsses.md)
* [AWS Textract](../../../app-nodes/n8n-nodes-base.awstextract.md)
* [AWS Transcribe](../../../app-nodes/n8n-nodes-base.awstranscribe.md)
* [Baserow](../../../app-nodes/n8n-nodes-base.baserow.md)
* [Bubble](../../../app-nodes/n8n-nodes-base.bubble.md)
* [Calculator（计算器）](../../sub-nodes/n8n-nodes-langchain.toolcalculator.md)
* [ClickUp](../../../app-nodes/n8n-nodes-base.clickup.md)
* [CoinGecko](../../../app-nodes/n8n-nodes-base.coingecko.md)
* [Compression（压缩）](../../../core-nodes/n8n-nodes-base.compression.md)
* [Crypto（加密）](../../../core-nodes/n8n-nodes-base.crypto.md)
* [DeepL](../../../app-nodes/n8n-nodes-base.deepl.md)
* [DHL](../../../app-nodes/n8n-nodes-base.dhl.md)
* [Discord](../../../app-nodes/n8n-nodes-base.discord/README.md)
* [Dropbox](../../../app-nodes/n8n-nodes-base.dropbox.md)
* [Elasticsearch](../../../app-nodes/n8n-nodes-base.elasticsearch.md)
* [ERPNext](../../../app-nodes/n8n-nodes-base.erpnext.md)
* [Facebook Graph API](../../../app-nodes/n8n-nodes-base.facebookgraphapi.md)
* [FileMaker](../../../app-nodes/n8n-nodes-base.filemaker.md)
* [Ghost](../../../app-nodes/n8n-nodes-base.ghost.md)
* [Git](../../../core-nodes/n8n-nodes-base.git.md)
* [GitHub](../../../app-nodes/n8n-nodes-base.github.md)
* [GitLab](../../../app-nodes/n8n-nodes-base.gitlab.md)
* [Gmail](../../../app-nodes/n8n-nodes-base.gmail/README.md)
* [Google Analytics](../../../app-nodes/n8n-nodes-base.googleanalytics.md)
* [Google BigQuery](../../../app-nodes/n8n-nodes-base.googlebigquery.md)
* [Google Calendar](../../../app-nodes/n8n-nodes-base.googlecalendar/README.md)
* [Google Chat](../../../app-nodes/n8n-nodes-base.googlechat.md)
* [Google Cloud Firestore](../../../app-nodes/n8n-nodes-base.googlecloudfirestore.md)
* [Google Cloud Realtime Database](../../../app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md)
* [Google Contacts](../../../app-nodes/n8n-nodes-base.googlecontacts.md)
* [Google Docs](../../../app-nodes/n8n-nodes-base.googledocs.md)
* [Google Drive](../../../app-nodes/n8n-nodes-base.googledrive/README.md)
* [Google Sheets](../../../app-nodes/n8n-nodes-base.googlesheets/README.md)
* [Google Slides](../../../app-nodes/n8n-nodes-base.googleslides.md)
* [Google Tasks](../../../app-nodes/n8n-nodes-base.googletasks.md)
* [Google Translate](../../../app-nodes/n8n-nodes-base.googletranslate.md)
* [Google Workspace Admin](../../../app-nodes/n8n-nodes-base.gsuiteadmin.md)
* [Gotify](../../../app-nodes/n8n-nodes-base.gotify.md)
* [Grafana](../../../app-nodes/n8n-nodes-base.grafana.md)
* [GraphQL](../../../core-nodes/n8n-nodes-base.graphql.md)
* [Hacker News](../../../app-nodes/n8n-nodes-base.hackernews.md)
* [Home Assistant](../../../app-nodes/n8n-nodes-base.homeassistant.md)
* [HubSpot](../../../app-nodes/n8n-nodes-base.hubspot.md)
* [Jenkins](../../../app-nodes/n8n-nodes-base.jenkins.md)
* [Jira Software](../../../app-nodes/n8n-nodes-base.jira.md)
* [JWT](../../../core-nodes/n8n-nodes-base.jwt.md)
* [Kafka](../../../app-nodes/n8n-nodes-base.kafka.md)
* [LDAP](../../../core-nodes/n8n-nodes-base.ldap.md)
* [Line](../../../app-nodes/n8n-nodes-base.line.md)
* [LinkedIn](../../../app-nodes/n8n-nodes-base.linkedin.md)
* [Mailcheck](../../../app-nodes/n8n-nodes-base.mailcheck.md)
* [Mailgun](../../../app-nodes/n8n-nodes-base.mailgun.md)
* [Mattermost](../../../app-nodes/n8n-nodes-base.mattermost.md)
* [Mautic](../../../app-nodes/n8n-nodes-base.mautic.md)
* [Medium](../../../app-nodes/n8n-nodes-base.medium.md)
* [Microsoft Excel (OneDrive)](../../../app-nodes/n8n-nodes-base.microsoftexcel.md)
* [Microsoft OneDrive](../../../app-nodes/n8n-nodes-base.microsoftonedrive.md)
* [Microsoft Outlook](../../../app-nodes/n8n-nodes-base.microsoftoutlook.md)
* [Microsoft SQL](../../../app-nodes/n8n-nodes-base.microsoftsql.md)
* [Microsoft Teams](../../../app-nodes/n8n-nodes-base.microsoftteams.md)
* [Microsoft To Do](../../../app-nodes/n8n-nodes-base.microsofttodo.md)
* [Monday.com](../../../app-nodes/n8n-nodes-base.mondaycom.md)
* [MongoDB](../../../app-nodes/n8n-nodes-base.mongodb.md)
* [MQTT](../../../app-nodes/n8n-nodes-base.mqtt.md)
* [MySQL](../../../app-nodes/n8n-nodes-base.mysql/README.md)
* [NASA](../../../app-nodes/n8n-nodes-base.nasa.md)
* [Nextcloud](../../../app-nodes/n8n-nodes-base.nextcloud.md)
* [NocoDB](../../../app-nodes/n8n-nodes-base.nocodb.md)
* [Notion](../../../app-nodes/n8n-nodes-base.notion/README.md)
* [Odoo](../../../app-nodes/n8n-nodes-base.odoo.md)
* [OpenWeatherMap](../../../app-nodes/n8n-nodes-base.openweathermap.md)
* [Pipedrive](../../../app-nodes/n8n-nodes-base.pipedrive.md)
* [Postgres](../../../app-nodes/n8n-nodes-base.postgres/README.md)
* [Pushover](../../../app-nodes/n8n-nodes-base.pushover.md)
* [QuickBooks Online](../../../app-nodes/n8n-nodes-base.quickbooks.md)
* [QuickChart](../../../app-nodes/n8n-nodes-base.quickchart.md)
* [RabbitMQ](../../../app-nodes/n8n-nodes-base.rabbitmq.md)
* [Reddit](../../../app-nodes/n8n-nodes-base.reddit.md)
* [Redis](../../../app-nodes/n8n-nodes-base.redis.md)
* [RocketChat](../../../app-nodes/n8n-nodes-base.rocketchat.md)
* [S3](../../../app-nodes/n8n-nodes-base.s3.md)
* [Salesforce](../../../app-nodes/n8n-nodes-base.salesforce.md)
* [Send Email（发送电子邮件）](../../../core-nodes/n8n-nodes-base.sendemail.md)
* [SendGrid](../../../app-nodes/n8n-nodes-base.sendgrid.md)
* [SerpApi (Google Search)](../../sub-nodes/n8n-nodes-langchain.toolserpapi.md)
* [Shopify](../../../app-nodes/n8n-nodes-base.shopify.md)
* [Slack](../../../app-nodes/n8n-nodes-base.slack/README.md)
* [Spotify](../../../app-nodes/n8n-nodes-base.spotify.md)
* [Stripe](../../../app-nodes/n8n-nodes-base.stripe.md)
* [Supabase](../../../app-nodes/n8n-nodes-base.supabase/README.md)
* [Telegram](../../../app-nodes/n8n-nodes-base.telegram/README.md)
* [Todoist](../../../app-nodes/n8n-nodes-base.todoist.md)
* [TOTP](../../../core-nodes/n8n-nodes-base.totp.md)
* [Trello](../../../app-nodes/n8n-nodes-base.trello.md)
* [Twilio](../../../app-nodes/n8n-nodes-base.twilio.md)
* [urlscan.io](../../../app-nodes/n8n-nodes-base.urlscanio.md)
* [Vector Store（向量存储）](../../sub-nodes/n8n-nodes-langchain.toolvectorstore.md)
* [Webflow](../../../app-nodes/n8n-nodes-base.webflow.md)
* [Wikipedia（维基百科）](../../sub-nodes/n8n-nodes-langchain.toolwikipedia.md)
* [Wolfram|Alpha](../../sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)
* [WooCommerce](../../../app-nodes/n8n-nodes-base.woocommerce.md)
* [Wordpress](../../../app-nodes/n8n-nodes-base.wordpress.md)
* [X (Formerly Twitter)（X，原 Twitter）](../../../app-nodes/n8n-nodes-base.twitter.md)
* [YouTube](../../../app-nodes/n8n-nodes-base.youtube.md)
* [Zendesk](../../../app-nodes/n8n-nodes-base.zendesk.md)
* [Zoho CRM](../../../app-nodes/n8n-nodes-base.zohocrm.md)
* [Zoom](../../../app-nodes/n8n-nodes-base.zoom.md)

</details>

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Tools Agent。

### Prompt（提示词） <a href="#prompt" id="prompt"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md" %}

### Require Specific Output Format（要求指定输出格式） <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md" %}

## 节点选项 <a href="#node-options" id="node-options"></a>

使用以下选项调整 Tools Agent 节点的行为：

### System Message（系统消息） <a href="#system-message" id="system-message"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/system-message.md" %}

### Max Iterations（最大迭代次数） <a href="#max-iterations" id="max-iterations"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/max-iterations.md" %}

### Return Intermediate Steps（返回中间步骤） <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md" %}

### Tracing Metadata（追踪元数据） <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/tracing-metadata.md" %}

### Automatically Passthrough Binary Images（自动传递二进制图像） <a href="#automatically-passthrough-binary-images" id="automatically-passthrough-binary-images"></a>

{% include "../../../../../reusable-content/.gitbook/includes/integrations/builtin/cluster-nodes/langchain-root-nodes/binary-images.md" %}

### Enable Streaming（启用流式输出） <a href="#enable-streaming" id="enable-streaming"></a>

开启后，AI Agent 在生成答案时实时向用户返回数据，适用于耗时较长的生成，默认开启。

{% hint style="info" %}
**流式输出要求**

要使用流式输出，工作流必须采用支持流式响应的触发器，例如 [Chat Trigger](../../../core-nodes/n8n-nodes-langchain.chattrigger/README.md) 或 [Webhook](../../../core-nodes/n8n-nodes-base.webhook/README.md) 节点，并将 **Response Mode**（响应模式）设为 **Streaming**（流式）。
{% endhint %}

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅 AI Agent 主节点的[模板与示例](./README.md#templates-and-examples)部分。

## 使用 `$fromAI()` 动态设置工具参数 <a href="#dynamic-parameters-for-tools-with-dollarfromai" id="dynamic-parameters-for-tools-with-dollarfromai"></a>

动态填充应用节点工具参数的方法，请参阅[让 AI 使用 `$fromAI()` 指定工具参数](../../../../../build/integrate-ai/ai-examples/use-ai-for-parameters.md)。

## 工具调用的人工审核 <a href="#human-review-for-tool-calls" id="human-review-for-tool-calls"></a>

可要求 AI Agent 在执行特定工具前获得人工批准，适用于发送消息、修改记录或删除数据等执行敏感操作的工具。

添加人工审核步骤：

1. 点击 AI Agent 节点的工具连接器。
2. 在工具面板中找到 **Human review**（人工审核）部分。
3. 选择并配置所需审批渠道，例如 Chat、Slack、Telegram 等。
4. 将需要审批的工具连接到人工审核步骤。

AI 希望使用受审核工具时，工作流会暂停，并通过所选渠道发送审批请求。接收人可批准（执行工具）或拒绝（取消操作）。

详细配置和最佳实践，请参阅 [AI 工具调用中的人工审核](../../../../../build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

常见问题及建议的解决办法，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 场景中，工具是附加资源，AI 可在响应请求时调用它获取特定信息或功能。AI 模型可以通过工具与外部系统交互，或完成具体、专门的任务。
