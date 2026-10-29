---
title: KoboToolbox 节点文档
description: 了解如何在 n8n 中使用 KoboToolbox 节点，并按照技术文档将 KoboToolbox 节点集成到工作流中。
contentType:
- integration
- reference
nodeTitle: KoboToolbox 节点文档
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# KoboToolbox 节点 <a href="#kobotoolbox-node" id="kobotoolbox-node"></a>

使用 KoboToolbox 节点自动处理 KoboToolbox 中的工作，并将其与其他应用集成。n8n 内置支持多种 KoboToolbox 功能，包括创建、更新、删除和获取文件、表单、钩子及提交记录。

本页列出了 KoboToolbox 节点支持的操作，并提供更多资源的链接。

{% hint style="info" %}
**凭据**

有关身份验证设置，请参阅 [KoboToolbox 凭据](../credentials/kobotoolbox.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* File（文件）
    * Create（创建）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
* Form（表单）
    * Get（获取）
    * Get Many（获取多条）
        * Redeploy（重新部署）
* Hook（钩子）
    * Get（获取）
    * Get Many（获取多条）
    * Logs（日志）
    * Retry All（重试全部）
    * Retry One（重试单条）
* Submission（提交记录）
    * Delete（删除）
    * Get（获取）
    * Get Many（获取多条）
    * Get Validation Status（获取验证状态）
    * Update Validation Status（更新验证状态）

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 KoboToolbox 集成模板](https://n8n.io/integrations/kobotoolbox)，或[搜索所有模板](https://n8n.io/workflows/)

## 选项 <a href="#options" id="options"></a>

### 查询选项 <a href="#query-options" id="query-options"></a>

Query Submission（查询提交记录）操作支持查询选项：

* 在 **Parameters**（参数）面板的主要部分：
    * **Start**（起始位置）控制查询开始的索引偏移量，用于 API 分页逻辑。
    * **Limit**（数量限制）设置最多返回的记录数。请注意，无论填写什么值，API 始终最多返回 30,000 条记录。
* 在 **Query Options**（查询选项）部分，可启用以下参数：
    * **Query**（查询）允许使用 MongoDB 的 JSON 查询格式指定筛选条件。例如，`{"status": "success", "_submission_time": {"$lt": "2021-11-01T01:02:03"}}` 会查询所有将 `success` 作为 `status` 字段值，且在 2021 年 11 月 1 日 01:02:03 之前提交的记录。
    * **Fields**（字段）允许指定要获取的字段列表，减小响应体积。
    * **Sort**（排序）允许提供 MongoDB JSON 格式的排序条件列表。例如，`{"status": 1, "_submission_time": -1}` 指定先按状态升序排列，再按提交时间降序排列。

这些选项的更多详情，请参阅 [Formhub API 文档](https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters)。

### 提交记录选项 <a href="#submission-options" id="submission-options"></a>

所有返回表单提交数据的操作都提供调整响应的选项，包括：

- 下载选项允许下载每条表单提交记录关联的附件，例如图片和视频，还可选择命名模式和下载文件大小（如果可用，通常用于图片）。
- 格式化选项按[关于重新格式化](#about-reformatting)中的说明重新格式化数据。

#### 关于重新格式化 <a href="#about-reformatting" id="about-reformatting"></a>

KoboToolbox 提交数据的默认 JSON 格式有时难以处理，因为它不了解架构，所有字段都会以字符串返回。

此节点提供轻量、按预设规则重新格式化的逻辑，通过 **Reformat?**（重新格式化？）参数启用。所有返回表单提交记录的操作均提供此参数，包括提交记录查询、获取和附件下载操作。

启用后，重新格式化会执行以下处理：

- 按表单分组，将 JSON 重组为多层结构。默认情况下，问题的分组层级通过字段名中的 `/` 字符表示，例如 `Group1/Question1`。启用重新格式化后，n8n 会将其重组为 `Group1.Question1`，即嵌套 JSON 对象。
- 重命名字段，去掉许多下游系统不支持的 `_`。
- 将所有地理空间字段，即 Point（点）、Line（线）和 Area（区域）题型，解析为对应的标准 GeoJSON 格式。
- 将匹配任一 **Multiselect Mask**（多选掩码）通配模式的字段拆分为数组。多选字段以空格分隔的字符串形式出现，无法通过算法猜测，因此必须提供字段命名掩码。多个掩码以逗号分隔，列表支持 `*` 通配符。
- 将匹配任一 **Number Mask**（数字掩码）通配模式的字段转换为 JSON 浮点数。

以下为详细的 JSON 示例：

```json
{
  "_id": 471987,
  "formhub/uuid": "189436bb09a54957bfcc798e338b54d6",
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details/Field_Name": "Test Fields",
  "Field_Details/Field_Location": "-1.932914 30.078211 1421 165",
  "Field_Details/Field_Shape": "-1.932914 30.078211 1421 165;-1.933011 30.078085 0 0;-1.933257 30.078004 0 0;-1.933338 30.078197 0 0;-1.933107 30.078299 0 0;-1.932914 30.078211 1421 165",
  "Field_Details/Crops_Grown": "maize beans avocado",
  "Field_Details/Field_Size_sqm": "2300",
  "__version__": "veGcULpqP6JNFKRJbbMvMs",
  "meta/instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "_uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_attachments": [],
  "_status": "submitted_via_web",
  "_geolocation": [
    -1.932914,
    30.078211
  ],
  "_submission_time": "2021-12-05T14:15:44",
  "_tags": [],
  "_notes": [],
  "_validation_status": {},
  "_submitted_by": null
}
```

启用重新格式化，并为多选和数字格式设置适当的掩码，例如分别使用 `Crops_*` 和 `*_sqm` 后，n8n 将其解析为：

```json
{
  "id": 471987,
  "formhub": {
    "uuid": "189436bb09a54957bfcc798e338b54d6"
  },
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details": {
    "Field_Name": "Test Fields",
    "Field_Location": {
      "lat": -1.932914,
      "lon": 30.078211
    },
    "Field_Shape": {
      "type": "polygon",
      "coordinates": [
        {
          "lat": -1.932914,
          "lon": 30.078211
        },
        {
          "lat": -1.933011,
          "lon": 30.078085
        },
        {
          "lat": -1.933257,
          "lon": 30.078004
        },
        {
          "lat": -1.933338,
          "lon": 30.078197
        },
        {
          "lat": -1.933107,
          "lon": 30.078299
        },
        {
          "lat": -1.932914,
          "lon": 30.078211
        }
      ]
    },
    "Crops_Grown": [
      "maize",
      "beans",
      "avocado"
    ],
    "Field_Size_sqm": 2300
  },
  "version": "veGcULpqP6JNFKRJbbMvMs",
  "meta": {
    "instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a"
  },
  "xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "attachments": [],
  "status": "submitted_via_web",
  "geolocation": {
    "lat": -1.932914,
    "lon": 30.078211
  },
  "submission_time": "2021-12-05T14:15:44",
  "tags": [],
  "notes": [],
  "validation_status": {},
  "submitted_by": null
}
```


{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/operation-not-supported.md" %}
