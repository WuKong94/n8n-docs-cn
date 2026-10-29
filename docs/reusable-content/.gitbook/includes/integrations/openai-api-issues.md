---
title: OpenAI API 常见问题
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

## The service is receiving too many requests from you（服务收到的请求过多） <a href="#the-service-is-receiving-too-many-requests-from-you" id="the-service-is-receiving-too-many-requests-from-you"></a>

超过 [OpenAI 速率限制](https://platform.openai.com/docs/guides/rate-limits)时，会显示此错误。

可通过以下两种方式处理：

1. 使用 [Loop Over Items](../../../../integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) 节点将数据拆成较小批次，并在末尾添加 [Wait](../../../../integrations/builtin/core-nodes/n8n-nodes-base.wait.md) 节点，设置合适的等待时间。复制下方代码，粘贴到工作流中作为模板使用。
    ```
    {
        "nodes": [
        {
            "parameters": {},
            "id": "35d05920-ad75-402a-be3c-3277bff7cc67",
            "name": "When clicking ‘Execute workflow’",
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [
            880,
            400
            ]
        },
        {
            "parameters": {
            "batchSize": 500,
            "options": {}
            },
            "id": "ae9baa80-4cf9-4848-8953-22e1b7187bf6",
            "name": "Loop Over Items",
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [
            1120,
            420
            ]
        },
        {
            "parameters": {
            "resource": "chat",
            "options": {},
            "requestOptions": {}
            },
            "id": "a519f271-82dc-4f60-8cfd-533dec580acc",
            "name": "OpenAI",
            "type": "n8n-nodes-base.openAi",
            "typeVersion": 1,
            "position": [
            1380,
            440
            ]
        },
        {
            "parameters": {
            "unit": "minutes"
            },
            "id": "562d9da3-2142-49bc-9b8f-71b0af42b449",
            "name": "Wait",
            "type": "n8n-nodes-base.wait",
            "typeVersion": 1,
            "position": [
            1620,
            440
            ],
            "webhookId": "714ab157-96d1-448f-b7f5-677882b92b13"
        }
        ],
        "connections": {
        "When clicking ‘Execute workflow’": {
            "main": [
            [
                {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
                }
            ]
            ]
        },
        "Loop Over Items": {
            "main": [
            null,
            [
                {
                "node": "OpenAI",
                "type": "main",
                "index": 0
                }
            ]
            ]
        },
        "OpenAI": {
            "main": [
            [
                {
                "node": "Wait",
                "type": "main",
                "index": 0
                }
            ]
            ]
        },
        "Wait": {
            "main": [
            [
                {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
                }
            ]
            ]
        }
        },
        "pinData": {}
    }
    ```
2. 使用带有内置批次限制选项的 [HTTP Request](../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md) 节点调用 [OpenAI API](https://platform.openai.com/docs/quickstart)，替代 OpenAI 节点。

## Insufficient quota（配额不足） <a href="#insufficient-quota" id="insufficient-quota"></a>

{% hint style="info" %}
**配额问题**

OpenAI 存在多种与配额相关的问题，包括刚充值后仍失败。为避免这些问题，请确保账户有可用余额，并在 [API 密钥页面](https://platform.openai.com/settings/organization/api-keys)签发新的 API 密钥。
{% endhint %}

OpenAI 账户没有足够余额或容量完成请求时，会显示此错误。可能是试用期已结束、账户需要充值，或超过了使用限额。

排查此错误时，请在 [OpenAI 设置](https://platform.openai.com/settings/organization/billing/overview)页面中：

* 在左上角第一个选择器中，选择 API 密钥对应的正确组织。
* 在左上角第二个选择器中，选择 API 密钥对应的正确项目。
* 检查组织级别的[账单概览](https://platform.openai.com/settings/organization/billing/overview)页面，确保组织余额充足，并再次确认此页面选择的是正确组织。
* 检查组织级别的[使用限额](https://platform.openai.com/settings/organization/limits)页面，再次确认选择的是正确组织，并滚动到 **Usage limits**（使用限额）部分，核对是否超过组织的使用限额。
* 检查 OpenAI 项目的使用限额。再次确认左上角第二个选择器中选择的是正确项目。选择 **Project**（项目）> **Limits**（限额），查看或修改项目限额。
* 检查 [OpenAI API](https://status.openai.com/) 是否正常运行。

{% hint style="info" %}
**余额等待时间**

充值后，OpenAI 账户显示新余额可能存在延迟。
{% endhint %}

在 n8n 中：

* 检查 [OpenAI 凭据](../../../../integrations/builtin/credentials/openai.md)使用的 [OpenAI API 密钥](https://platform.openai.com/api-keys)是否有效，并对应你充值的账户。
* 确保 [OpenAI 节点](../../../../integrations/builtin/app-nodes/n8n-nodes-langchain.openai/README.md)连接到正确的 [OpenAI 凭据](../../../../integrations/builtin/credentials/openai.md)。

如果账户余额经常耗尽，可考虑在 [OpenAI 账单设置](https://platform.openai.com/settings/organization/billing/overview)中开启自动充值，使余额降至 $0 时自动为账户充值。

## Bad request - please check your parameters（请求错误，请检查参数） <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

请求出错，但 n8n 无法解析 OpenAI 返回的错误消息时，会显示此错误。

排查时，可先尝试使用 [HTTP Request](../../../../integrations/builtin/core-nodes/n8n-nodes-base.httprequest/README.md) 节点运行相同操作，通常能获得更详细的错误消息。
