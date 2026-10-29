---
contentType: howto
nodeTitle: 连接节点
originalFilePath: workflows/components/connections.md
originalUrl: https://docs.n8n.io/workflows/components/connections
url: https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together
description: 连接在节点之间建立链接，让数据在工作流中流转。
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


# 连接节点 <a id="connect-nodes-together"></a>

连接在节点之间建立链接，让数据在工作流中流转。两个节点之间的连接会将数据从一个节点的输出传递到另一个节点的输入。

![创建和删除连接的示例](../../.gitbook/assets/example.gif)

## 创建连接 <a href="#create-a-connection" id="create-a-connection"></a>

要连接两个节点，选择节点右侧的灰点或 **Add node（添加节点）** <img src="../../.gitbook/assets/add-node-small (1).png" alt="添加节点图标" data-size="line">，将箭头拖动到下一个节点左侧的灰色矩形上。

## 删除连接 <a href="#delete-a-connection" id="delete-a-connection"></a>

将鼠标悬停在连接上，再选择 **Delete（删除）** <img src="../../.gitbook/assets/delete-connector.png" alt="删除连接图标" data-size="line">。

## 相关资源 <a id="related-resources"></a>

* [工作流组件](./)
* [使用节点](work-with-nodes.md)
* [添加笔记和说明](add-notes-and-documentation.md)
* [画布分组](canvas-groups.md)
* [查找工作流 ID](find-your-workflow-id.md)
