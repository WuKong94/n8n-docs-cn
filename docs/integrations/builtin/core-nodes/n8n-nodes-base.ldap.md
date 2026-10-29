---
title: LDAP 节点
description: 了解 n8n 中 LDAP 节点的用法，并查看相关示例。
contentType:
- integration
- reference
nodeTitle: LDAP 节点
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ldap.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# LDAP <a href="#ldap" id="ldap"></a>

此节点用于与 LDAP 服务器交互，创建、查找和更新对象。

{% hint style="info" %}
**凭据**

此节点的身份验证信息，请参阅 [LDAP 凭据文档](../credentials/ldap.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Compare**](#compare)（比较）属性
* [**Create**](#create)（创建）新条目
* [**Delete**](#delete)（删除）条目
* [**Rename**](#rename)（重命名）现有条目的 DN
* [**Search**](#search)（搜索）LDAP
* [**Update**](#update)（更新）属性

各操作的节点配置说明见下文。

{% include "../../../reusable-content/.gitbook/includes/integrations/builtin/app-nodes/ai-tools.md" %}

## Compare（比较） <a href="#compare" id="compare"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **DN**：输入待比较条目的 Distinguished Name（专有名称，DN）。
* **Attribute ID**（属性 ID）：输入要比较的属性 ID。
* **Value**（值）：输入要比较的值。

## Create（创建） <a href="#create" id="create"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **DN**：输入要创建条目的 Distinguished Name（专有名称，DN）。
* **Attributes**（属性）：添加要创建的 **Attribute ID**（属性 ID）/**Value**（值）对。

## Delete（删除） <a href="#delete" id="delete"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **DN**：输入待删除条目的 Distinguished Name（专有名称，DN）。

## Rename（重命名） <a href="#rename" id="rename"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **DN**：输入待重命名条目当前的 Distinguished Name（专有名称，DN）。
* **New DN**（新 DN）：输入此条目新的 Distinguished Name（专有名称，DN）。

## Search（搜索） <a href="#search" id="search"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **Base DN**（基准 DN）：输入要搜索子树的 Distinguished Name（专有名称，DN）。
* **Search For**（搜索对象）：选择要搜索的目录对象类。
* **Attribute**（属性）：选择要搜索的属性。
* **Search Text**（搜索文本）：输入要搜索的文本，使用 `*` 作为通配符。
* **Return All**（返回全部）：开启时返回所有结果，关闭时返回不超过 **Limit**（数量上限）的结果。
* **Limit**（数量上限）：仅在关闭 **Return All**（返回全部）时可用，输入最多返回的结果数。

### Search（搜索）选项 <a href="#search-options" id="search-options"></a>

还可通过以下选项配置此操作：

* **Attribute Names or IDs**（属性名称或 ID）：输入以逗号分隔的待返回属性列表，可从列表中选择，也可使用表达式指定 ID。
* **Page Size**（分页大小）：输入每次请求的最多结果数，设为 0 时禁用分页。
* **Scopes**（范围）：在 **Base DN**（基准 DN）处或其下搜索潜在匹配条目的范围，可选：
    * **Base Tree**（下级子树）：常称为 subordinateSubtree 或 subordinates，搜索 **Base DN**（基准 DN）条目的下级，但不包含 **Base DN** 条目自身。
    * **Single Level**（单层）：常称为 one，仅搜索 **Base DN**（基准 DN）条目的直接子项。
    * **Whole Subtree**（整个子树）：常称为 sub，搜索 **Base DN**（基准 DN）条目自身及任意深度的所有下级。

搜索范围的更多信息，请参阅 [LDAP 搜索操作](https://ldap.com/the-ldap-search-operation/)。

## Update（更新） <a href="#update" id="update"></a>

使用以下参数配置此操作：

* **Credential to connect with**（连接凭据）：选择或创建用于连接的 [LDAP 凭据](../credentials/ldap.md)。
* **DN**：输入待更新条目的 Distinguished Name（专有名称，DN）。
* **Update Attributes**（更新属性）：选择 **Add**（添加）新属性、**Remove**（移除）现有属性，或 **Replace**（替换）现有属性。
* 然后输入要更新的 **Attribute ID**（属性 ID）/**Value**（值）对。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 LDAP 集成模板](https://n8n.io/integrations/ldap)，或[搜索所有模板](https://n8n.io/workflows/)
