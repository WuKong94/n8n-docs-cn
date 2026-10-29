---
title: 数据模拟与固定
description: 开发期间在 n8n 工作流中模拟和固定数据的方法。
contentType: howto
nodeTitle: 固定和模拟数据
originalFilePath: data/data-pinning.md
originalUrl: https://docs.n8n.io/data/data-pinning
url: https://docs.n8n.io/build/work-with-data/pin-and-mock-data
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 固定和模拟数据 <a href="#pinning-and-mocking-data" id="pinning-and-mocking-data"></a>

开发工作流时，可能希望测试逻辑，而不反复调用外部系统或处理实时数据。n8n 提供两项相关功能：

* **数据模拟**：无需连接真实数据源，即可创建或模拟测试数据
* **数据固定**：保存模拟或真实测试数据，在后续工作流执行中复用，代替获取新数据

这两种方式都能节省开发时间和资源，让测试使用一致的数据集，并避免对线上系统重复发起测试调用。

{% hint style="info" %}
**仅用于开发**

数据固定和模拟用于开发期间测试工作流。生产工作流执行不支持数据固定。
{% endhint %}

## 数据模拟方式 <a href="#data-mocking-approaches" id="data-mocking-approaches"></a>

可以通过多种方式创建开发期间使用的测试数据：

### 使用 Code 或 Edit Fields 节点生成自定义数据 <a href="#generate-custom-data-using-the-code-or-edit-fields-nodes" id="generate-custom-data-using-the-code-or-edit-fields-nodes"></a>

可以通过 [Code 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.code/README.md)或 [Edit Fields (Set) 节点](../../integrations/builtin/core-nodes/n8n-nodes-base.set.md)在工作流中创建自定义数据集。

在 Code 节点中，可以创建任意数据集并作为节点输出返回。在 Edit Fields 节点中，选择 **Add fields（添加字段）** 加入自定义数据。

小规模测试适合使用 Edit Fields 节点，复杂数据集则使用 Code 节点。

**适用场景**：需要完全控制测试数据的结构和值，或希望用特定数据模式测试边界情况。

### 通过 Customer Datastore 节点输出示例数据集 <a href="#output-a-sample-data-set-from-the-customer-datastore-node" id="output-a-sample-data-set-from-the-customer-datastore-node"></a>

Customer Datastore 节点提供虚构数据集。添加并执行节点，即可查看数据。

**适用场景**：探索 n8n 时需要测试数据，但还没有真实使用场景。

创建或获取希望在多次工作流执行中复用的测试数据后，使用[数据固定](#data-pinning)保存，以保持测试一致。

## 数据固定 <a href="#data-pinning" id="data-pinning"></a>

开发工作流时可以“固定”数据，即保存节点输出，并在后续执行中使用保存的数据，代替获取新数据。

处理外部数据源时，可以借此避免反复请求外部系统，节省时间和资源：

* 工作流依赖外部系统触发时，例如 Webhook 调用，固定数据可以避免每次测试都再次操作外部系统。
* 外部资源有数据量或使用量限制时，固定测试数据可以避免消耗配额。
* 获取并固定所需测试数据，确保各次工作流测试的数据一致。
* 通过上述方式模拟测试数据，再固定以便多次执行复用。

只能为具有单个主输出的节点固定数据，此处不计“error”错误输出。

### 固定数据 <a href="#pin-data" id="pin-data"></a>

{% include "../../reusable-content/.gitbook/includes/data/how-to-pin-data.md" %}

### 取消固定 <a href="#unpin-data" id="unpin-data"></a>

数据固定后，节点输出面板顶部会出现提示横幅。要取消固定，并在下次执行时获取新数据，选择横幅中的 **Unpin（取消固定）** 链接。

### 编辑固定数据 <a href="#edit-pinned-data" id="edit-pinned-data"></a>

n8n 支持编辑固定数据。无需在外部系统中逐一搭建场景并发送对应数据，就能检查不同情况，更方便测试边界条件。

{% hint style="info" %}
**仅用于开发**

生产工作流执行不支持数据编辑，此功能用于开发期间测试工作流。
{% endhint %}

#### 编辑输出数据 <a href="#edit-output-data" id="edit-output-data"></a>

编辑输出数据的步骤如下：

1. 运行节点，加载数据。
2. 在 **OUTPUT（输出）** 视图中选择 **JSON**，切换到 JSON 视图。
3. 选择 **Edit（编辑）** <img src="../.gitbook/assets/edit-data.png" alt="编辑数据图标" data-size="line">。
4. 编辑数据。
5. 选择 **Save（保存）**。n8n 会保存更改并固定数据。

#### 使用以往执行的数据 <a href="#use-data-from-previous-executions" id="use-data-from-previous-executions"></a>

可以复制以往工作流执行中的节点数据：

1. 打开左侧菜单。
2. 选择 **Executions（执行）**。
3. 浏览工作流执行列表，找到包含所需数据的执行。
4. 选择 **Open Past Execution（打开以往执行）** <img src="../.gitbook/assets/open-execution.png" alt="打开以往执行图标" data-size="line">。
5. 双击要复制数据的节点。
6. 如果当前是表格布局，选择 **JSON** 切换视图。
7. 有两种复制 JSON 的方式：
  1. 像选择文本一样，高亮选中所需 JSON，再按 `ctrl` + `c` 复制。
  2. 点击参数，选中要复制的 JSON，然后：
    1. 将鼠标悬停在 JSON 上，n8n 会显示 **Copy（复制）** <img src="../.gitbook/assets/copy-data.png" alt="复制数据图标" data-size="line"> 按钮。
    2. 选择 **Copy（复制）** <img src="../.gitbook/assets/copy-data.png" alt="复制数据图标" data-size="line">。
    3. 选择复制内容：
        * **Copy Item Path（复制数据项路径）** 和 **Copy Parameter Path（复制参数路径）** 会生成访问部分 JSON 的表达式。
        * **Copy Value（复制值）**：复制所选 JSON 的完整内容。
8. 返回正在编辑的工作流：
    1. 打开左侧菜单。
    2. 选择 **Workflows（工作流）**。
    3. 选择 **Open（打开）**。
    4. 选择要打开的工作流。
9. 打开需要使用复制数据的节点。
10. 如果没有数据，运行节点以加载数据。
11. 在 **OUTPUT（输出）** 视图中选择 **JSON**，切换视图。
12. 选择 **Edit（编辑）** <img src="../.gitbook/assets/edit-data.png" alt="编辑数据图标" data-size="line">。
15. 粘贴以往执行的数据。
16. 选择 **Save（保存）**，n8n 会保存更改并固定数据。

### 结合模拟与固定 <a href="#combine-mocking-with-pinning" id="combine-mocking-with-pinning"></a>

要获得更贴近实际的测试体验，可以结合两种方式：

1. 通过 Code、Edit Fields 或 Customer Datastore 节点创建测试数据
2. 编辑测试数据，构建特定场景或边界情况
3. 固定编辑后的数据，供多次工作流执行复用
4. 使用这份编辑并固定的数据集继续开发

这样既能完全控制测试数据，又能确保多次运行中的测试一致。

## 相关资源 <a id="related-resources"></a>

* [处理数据](./)
* [理解 n8n 的数据结构](understand-n8ns-data-structure.md)
* [表达式与数据节点](expressions-versus-data-nodes.md)
* [引用数据](reference-data/README.md)
* [转换数据](transform-data/README.md)
* [过滤不需要的数据](filter-out-unwanted-data.md)
* [处理特殊数据类型](handle-special-data-types/README.md)
* [数据表](data-tables.md)
