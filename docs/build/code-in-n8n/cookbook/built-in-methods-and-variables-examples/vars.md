---
description: 访问环境的自定义变量。
contentType: reference
nodeTitle: vars
originalFilePath: code/cookbook/builtin/vars.md
originalUrl: https://docs.n8n.io/code/cookbook/builtin/vars
url: https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# `vars` <a href="#vars" id="vars"></a>

{% hint style="info" %}
**功能可用范围**

以下套餐提供 `vars`：

- **n8n Cloud：** Pro、Enterprise
- **自托管：** Business、Enterprise

需要 n8n 实例所有者账号的访问权限，才能创建变量。
{% endhint %}

`vars` 包含当前环境的所有[变量](../../define-custom-variables.md)，它是只读的：可以使用 `vars` 访问变量，但必须通过界面设置。

{% tabs %}
{% tab title="JavaScript" %}
```js
// Access a variable
$vars.<variable-name>
```
{% endtab %}

{% tab title="Python" %}
```python
# Access a variable
_vars.<variable-name>
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**`vars` 与 `env`**

`vars` 用于访问用户创建的变量，属于[环境](../../../../administer/use-source-control-and-environments/README.md)功能。`env` 用于访问 n8n 实例的[配置环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [内置方法和变量示例](./)
