---
title: Data Table 节点的行操作
description: Data Table 节点行操作的参考文档，包括删除、获取、插入、更新和 upsert。
contentType:
- integration
- reference
priority: critical
nodeTitle: Data Table 节点的行操作
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


使用行操作删除、获取、插入、更新、upsert 或筛选数据表中的行。有关节点本身的更多信息，请参阅 [Data Table 节点](README.md)文档。

## 删除数据行 <a href="#delete-row" id="delete-row"></a>

使用此操作，根据指定条件从数据表中删除一行或多行。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **Delete**（删除）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择删除符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）的行。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。

### 删除数据行的选项 <a href="#delete-row-options" id="delete-row-options"></a>

使用以下选项进一步配置操作行为：

- **Dry Run:**（试运行）开启后模拟删除，不修改数据表。节点返回将被删除的行，包括操作前后的状态。

## 获取数据行 <a href="#get-row" id="get-row"></a>

使用此操作，根据指定条件从数据表中检索一行或多行。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **Get**（获取）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择获取符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）的行。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。
- **Return All:**（返回全部）开启时返回所有匹配的行；关闭时，在 **Limit**（数量上限）中输入要返回的行数量，例如 `50`。
- **Order By:**（排序）开启时，指定排序列及方向（升序或降序）；关闭时，不对结果排序。

### 获取过程中数据表发生变化 <a id="reading-rows-while-the-table-changes"></a>

一次请求大量结果时，n8n 会按较小批次（“页”）依次获取，而不是一次性获取全部数据。

获取需要一定时间。如果此时有人修改底层数据，例如添加、编辑或删除记录，返回结果可能不完全准确：某些记录可能遗漏，某些记录可能重复出现，不同部分的结果也可能反映略有差异的时间点的数据状态。

* **要获得完全准确的结果：** 确保在获取全部完成前，没有人添加、编辑或删除记录。
* **使用“Return All”时：** 如果获取期间持续新增匹配记录，由于总有更多数据需要获取，**Return All**（返回全部）可能永远无法完成。发生这种情况时，可以取消操作，操作会在当前批次完成后停止。

## 如果行存在 <a href="#if-row-exists" id="if-row-exists"></a>

使用此操作，检查数据表中是否存在符合指定条件的行。如果找到匹配行，节点原样输出收到的输入数据项；如果不存在匹配行，则不输出任何内容。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **If Row Exists**（如果行存在）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择行必须符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。

## 如果行不存在 <a href="#if-row-does-not-exist" id="if-row-does-not-exist"></a>

使用此操作，检查数据表中是否不存在符合指定条件的行。如果没有找到匹配行，节点原样输出收到的输入数据项；如果存在匹配行，则不输出任何内容。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **If Row Does Not Exist**（如果行不存在）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择行必须符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。

## 插入数据行 <a href="#insert-row" id="insert-row"></a>

使用此操作向数据表插入新行。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **Insert**（插入）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Mapping Column Mode:**（列映射模式）选择：
    - **Map Each Column Manually:**（逐列手动映射）明确选择传入数据的字段与列之间的映射关系。即使传入字段名称与数据表列名不同，也可映射；还可以从映射中删除某些值。
    - **Map Automatically:**（自动映射）让节点按名称自动匹配字段与列。要成功映射，传入数据的字段名称必须与数据表列名完全一致，所有字段都会被映射。

### 插入数据行的选项 <a href="#insert-row-options" id="insert-row-options"></a>

使用以下选项进一步配置操作行为：

- **Optimize Bulk:**（优化批量插入）开启后不返回插入的数据，可使批量插入性能最高提升至 5 倍。

## 更新数据行 <a href="#update-row" id="update-row"></a>

使用此操作，根据指定条件更新数据表中的一行或多行。

配置以下参数：

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **Update**（更新）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择更新符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）的行。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。
- **Mapping Column Mode:**（列映射模式）选择：
    - **Map Each Column Manually:**（逐列手动映射）明确选择传入数据的字段与列之间的映射关系。即使传入字段名称与数据表列名不同，也可映射；还可以从映射中删除某些值。
    - **Map Automatically:**（自动映射）让节点按名称自动匹配字段与列。要成功映射，传入数据的字段名称必须与数据表列名完全一致，所有字段都会被映射。

### 更新数据行的选项 <a href="#update-row-options" id="update-row-options"></a>

使用以下选项进一步配置操作行为：

- **Dry Run:**（试运行）开启后模拟更新，不修改数据表。节点返回将被更新的行，包括操作前后的状态。

## Upsert 数据行 <a href="#upsert-row" id="upsert-row"></a>

使用此操作在数据表中执行 upsert。如果存在符合指定条件的行，就使用提供的值更新该行；如果不存在匹配行，则创建新行。

- **Resource:**（资源）选择 **Row**（数据行）。
- **Operation:**（操作）选择 **Upsert**（存在则更新，否则插入）。
- **Data table:**（数据表）选择如何指定要操作的数据表：
    - **From list:**（从列表选择）从所有数据表的下拉列表中选择。
    - **By Name:**（按名称）输入数据表名称。
    - **By ID:**（按 ID）输入数据表 ID。
- **Must Match:**（匹配要求）选择对符合下一步所定义的 **Any Condition**（任一条件）或 **All Conditions**（所有条件）的行执行 upsert。
- **Conditions:**（条件）点击 **Add Condition**（添加条件），定义要操作的数据表行。可以添加多个条件，每个条件配置如下：
    - **Column:**（列）选择要比较的列。
    - **Condition:**（比较条件）选择如何比较列值：**Equals**（等于）、**Not Equals**（不等于）、**Greater Than**（大于）、**Greater Than or Equal**（大于或等于）、**Less Than**（小于）、**Less Than or Equal**（小于或等于）、**Is Empty**（为空）或 **Is Not Empty**（非空）。
    - **Value:**（值）输入用于和列值比较的值。可以使用固定值，或引用前置节点数据的表达式。条件为 **Is Empty**（为空）或 **Is Not Empty**（非空）时，没有此字段。
- **Mapping Column Mode:**（列映射模式）选择：
    - **Map Each Column Manually:**（逐列手动映射）明确选择传入数据的字段与列之间的映射关系。即使传入字段名称与数据表列名不同，也可映射；还可以从映射中删除某些值。
    - **Map Automatically:**（自动映射）让节点按名称自动匹配字段与列。要成功映射，传入数据的字段名称必须与数据表列名完全一致，所有字段都会被映射。

### Upsert 数据行的选项 <a href="#upsert-row-options" id="upsert-row-options"></a>

使用以下选项进一步配置操作行为：

- **Dry Run:**（试运行）开启后模拟 upsert，不修改数据表。节点返回将受影响的行，包括操作前后的状态。
