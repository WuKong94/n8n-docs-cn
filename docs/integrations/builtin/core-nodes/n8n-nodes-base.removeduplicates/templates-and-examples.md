---
title: Remove Duplicates 节点模板与示例
description: 通过连续示例了解 Remove Duplicates 节点的当前输入去重、跨执行去重及数值和日期比较，并查找相关模板。
contentType:
- integration
- reference
priority: medium
nodeTitle: Remove Duplicates 节点模板与示例
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

以下是 [Remove Duplicates 节点](README.md)的模板和示例。

{% hint style="info" %}
**连续示例**

本节示例前后衔接，请按顺序操作，避免出现意外结果。
{% endhint %}

## 模板 <a href="#templates" id="templates"></a>


[浏览 Remove Duplicates 节点集成模板](https://n8n.io/integrations/remove-duplicates)，或[搜索所有模板](https://n8n.io/workflows/)

## 使用 Code 节点准备示例数据 <a href="#set-up-sample-data-using-the-code-node" id="set-up-sample-data-using-the-code-node"></a>

创建一个带示例输入数据的工作流，尝试使用 Remove Duplicates 节点。

1. 向画布添加 Code 节点，并将其连接到 Manual Trigger 节点。
2. 在 Code 节点中，将 **Mode**（模式）设为 **Run Once for Each Item**（对每个数据项运行一次），将 **Language**（语言）设为 **JavaScript**。
3. 将以下 JavaScript 代码片段粘贴到 **JavaScript** 字段：
```js
let data =[];

return {
  data: [
    { id: 1, name: 'Taylor Swift', job: 'Pop star', last_updated: '2024-09-20T10:12:43.493Z' },
    { id: 2, name: 'Ed Sheeran', job: 'Singer-songwriter', last_updated: '2024-10-05T08:30:59.493Z' },
    { id: 3, name: 'Adele', job: 'Singer-songwriter', last_updated: '2024-10-07T14:15:59.493Z' },
    { id: 4, name: 'Bruno Mars', job: 'Singer-songwriter', last_updated: '2024-08-25T17:45:12.493Z' },
    { id: 1, name: 'Taylor Swift', job: 'Pop star', last_updated: '2024-09-20T10:12:43.493Z' },  // duplicate
    { id: 5, name: 'Billie Eilish', job: 'Singer-songwriter', last_updated: '2024-09-10T09:30:12.493Z' },
    { id: 6, name: 'Katy Perry', job: 'Pop star', last_updated: '2024-10-08T12:30:45.493Z' },
    { id: 2, name: 'Ed Sheeran', job: 'Singer-songwriter', last_updated: '2024-10-05T08:30:59.493Z' },  // duplicate
    { id: 7, name: 'Lady Gaga', job: 'Pop star', last_updated: '2024-09-15T14:45:30.493Z' },
    { id: 8, name: 'Rihanna', job: 'Pop star', last_updated: '2024-10-01T11:50:22.493Z' },
    { id: 3, name: 'Adele', job: 'Singer-songwriter', last_updated: '2024-10-07T14:15:59.493Z' },  // duplicate
    //{ id: 9, name: 'Tom Hanks', job: 'Actor', last_updated: '2024-10-17T13:58:31.493Z' },
    //{ id: 0, name: 'Madonna', job: 'Pop star', last_updated: '2024-10-17T17:11:38.493Z' },
    //{ id: 15, name: 'Bob Dylan', job: 'Folk singer', last_updated: '2024-09-24T08:03:16.493Z'},
    //{ id: 10, name: 'Harry Nilsson', job: 'Singer-songwriter', last_updated: '2020-10-17T17:11:38.493Z' },
    //{ id: 11, name: 'Kylie Minogue', job: 'Pop star', last_updated: '2024-10-24T08:03:16.493Z'},
  ]
}
```
4. 向画布添加 Split Out 节点，并将其连接到 Code 节点。
5. 在 Split Out 节点的 **Fields To Split Out**（要拆分的字段）中输入 `data`。

## 移除当前输入中的重复项 <a href="#removing-duplicates-from-the-current-input" id="removing-duplicates-from-the-current-input"></a>

1. 向画布添加 Remove Duplicates 节点，并将其连接到 Split Out 节点。先将 **Action**（动作）选为 **Remove items repeated within current input**（移除当前输入内的重复项）。
2. 打开 Remove Duplicates 节点，确保 **Operation**（操作）为 **Remove Items Repeated Within Current Input**。
3. 在 **Compare**（比较）字段中选择 **All fields**（所有字段）。
4. 选择 **Execute step**（执行步骤），运行 Remove Duplicates 节点，移除当前输入中的重复数据。

n8n 会移除所有字段数据均相同的重复项。表格视图中的输出应如下所示：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |


5. 再次打开 Remove Duplicates 节点，将 **Compare** 参数改为 **Selected Fields**（选定字段）。
6. 在 **Fields To Compare**（要比较的字段）中输入 `job`。
7. 选择 **Execute step**（执行步骤），运行 Remove Duplicates 节点，移除当前输入中的重复数据。

n8n 会移除当前输入中 `job` 数据相同的重复项。表格视图中的输出应如下所示：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |


## 保留值是新的数据项 <a href="#keep-items-where-the-value-is-new" id="keep-items-where-the-value-is-new"></a>

1. 打开 Remove Duplicates 节点，将 **Operation**（操作）设为 **Remove Items Processed in Previous Executions**（移除先前执行已处理的数据项）。
2. 将 **Keep Items Where**（保留条件）设为 **Value Is New**（值是新的）。
3. 将 **Value to Dedupe On**（去重依据值）设为 `{{ $json.name }}`。
4. 在画布上选择 **Execute workflow**（执行工作流）运行工作流，再打开 Remove Duplicates 节点查看结果。

n8n 将当前输入与先前执行存储的数据项比较。由于这是首次以此操作运行 Remove Duplicates 节点，n8n 会处理所有数据项，并将其放入 **Kept**（保留）输出标签页。数据项的顺序可能与输入顺序不同：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |


{% hint style="info" %}
**仅与先前执行比较数据项**

当前输入项只与先前执行存储的数据项比较。因此，此操作模式不会移除当前输入内部的重复项。如果需要同时移除当前输入内部的重复项和跨执行的重复项，请依次连接两个 Remove Duplicates 节点：第一个使用 **Remove Items Repeated Within Current Input**，第二个使用 **Remove Items Processed in Previous Executions**。
{% endhint %}

5. 打开 Code 节点，取消“Tom Hanks”对应行的注释（移除 `//`）。
6. 在画布上再次选择 **Execute workflow**，再打开 Remove Duplicates 节点查看结果。

n8n 将当前输入与先前执行存储的数据项比较。这次 **Kept**（保留）标签页只包含 Code 节点中新增的一条记录：


| **id** | **name**  | **job** | **last_updated**         |
|--------|-----------|---------|--------------------------|
| 9      | Tom Hanks | Actor   | 2024-10-17T13:58:31.493Z |


**Discarded**（丢弃）标签页包含上一次执行已处理的数据项：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |


继续之前，先清除去重历史，为下一个示例做好准备：

7. 打开 Remove Duplicates 节点，将 **Operation**（操作）设为 **Clear Deduplication History**（清除去重历史）。
8. 选择 **Execute step**（执行步骤），清除当前去重历史。

## 保留值高于所有先前值的数据项 <a href="#keep-items-where-the-value-is-higher-than-any-previous-value" id="keep-items-where-the-value-is-higher-than-any-previous-value"></a>

1. 打开 Remove Duplicates 节点，将 **Operation**（操作）设为 **Remove Items Processed in Previous Executions**（移除先前执行已处理的数据项）。
2. 将 **Keep Items Where**（保留条件）设为 **Value Is Higher than Any Previous Value**（值高于所有先前值）。
3. 将 **Value to Dedupe On**（去重依据值）设为 `{{ $json.id }}`。
4. 在画布上选择 **Execute workflow**（执行工作流）运行工作流，再打开 Remove Duplicates 节点查看结果。

n8n 将当前输入与先前执行存储的数据项比较。由于这是清除历史后首次运行 Remove Duplicates 节点，n8n 会处理所有数据项，并将其放入 **Kept**（保留）输出标签页。数据项的顺序可能与输入顺序不同：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |


5. 打开 Code 节点，取消“Madonna”和“Bob Dylan”对应行的注释（移除 `//`）。
6. 在画布上再次选择 **Execute workflow**，再打开 Remove Duplicates 节点查看结果。

n8n 将当前输入与先前执行存储的数据项比较。这次 **Kept**（保留）标签页只有“Bob Dylan”一条记录，因为其 `id` 列的值（15）高于先前的所有值（先前最大值为 9）：


| **id** | **name**  | **job**     | **last_updated**         |
|--------|-----------|-------------|--------------------------|
| 15     | Bob Dylan | Folk singer | 2024-09-24T08:03:16.493Z |


**Discarded**（丢弃）标签页包含 `id` 列的值小于或等于先前最大值（9）的 13 个数据项。“Madonna”虽然是新记录，也在此表中，因为其 `id` 值未超过先前最大值：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |


继续之前，先清除去重历史，为下一个示例做好准备：

7. 打开 Remove Duplicates 节点，将 **Operation**（操作）设为 **Clear Deduplication History**（清除去重历史）。
8. 选择 **Execute step**（执行步骤），清除当前去重历史。

## 保留日期晚于所有先前日期的数据项 <a href="#keep-items-where-the-value-is-a-date-later-than-any-previous-date" id="keep-items-where-the-value-is-a-date-later-than-any-previous-date"></a>

1. 打开 Remove Duplicates 节点，将 **Operation**（操作）设为 **Remove Items Processed in Previous Executions**（移除先前执行已处理的数据项）。
2. 将 **Keep Items Where**（保留条件）设为 **Value Is a Date Later than Any Previous Date**（日期晚于所有先前日期）。
3. 将 **Value to Dedupe On**（去重依据值）设为 `{{ $json.last_updated }}`。
4. 在画布上选择 **Execute workflow**（执行工作流）运行工作流，再打开 Remove Duplicates 节点查看结果。

n8n 将当前输入与先前执行存储的数据项比较。由于这是清除历史后首次运行 Remove Duplicates 节点，n8n 会处理所有数据项，并将其放入 **Kept**（保留）输出标签页。数据项的顺序可能与输入顺序不同：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
| 15     | Bob Dylan     | Folk singer       | 2024-09-24T08:03:16.493Z |



5. 打开 Code 节点，取消“Harry Nilsson”和“Kylie Minogue”对应行的注释（移除 `//`）。

6. 在画布上再次选择 **Execute workflow**，再打开 Remove Duplicates 节点查看结果。


n8n 将当前输入与先前执行存储的数据项比较。这次 **Kept**（保留）标签页只有“Kylie Minogue”一条记录，因为其 `last_updated` 列的值（`2024-10-24T08:03:16.493Z`）晚于先前的所有日期（先前最晚日期为 `2024-10-17T17:11:38.493Z`）：



| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 11     | Kylie Minogue | Pop star          | 2024-10-24T08:03:16.493Z |


**Discarded**（丢弃）标签页包含 `last_updated` 列的值早于或等于先前最晚日期（`2024-10-17T17:11:38.493Z`）的 15 个数据项。“Harry Nilsson”虽然是新记录，也在此表中，因为其 `last_updated` 值未晚于先前最大值：


| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 10     | Harry Nilsson | Singer-songwriter | 2020-10-17T17:11:38.493Z |
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
| 15     | Bob Dylan     | Folk singer       | 2024-09-24T08:03:16.493Z |

