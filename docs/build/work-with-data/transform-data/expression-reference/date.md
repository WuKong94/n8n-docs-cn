---
nodeTitle: Date（日期）
originalFilePath: data/expression-reference/date.md
originalUrl: https://docs.n8n.io/data/expression-reference/date
url: https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# Date（日期） <a href="#date" id="date"></a>

## _`Date`_.**`toDateTime()`** <a href="#datetodatetime" id="datetodatetime"></a>

**说明：** 将 JavaScript Date 转换为 Luxon DateTime。DateTime 包含相同的信息，但更易于操作。

**语法：** _`Date`_.toDateTime()

**返回值：** DateTime

**来源：** n8n 自定义功能

**示例：**

  ```javascript
  // date = new Date("2024-03-30T18:49")
  date.toDateTime().plus(5, 'days') //=> 2024-04-04T18:49
  ```


## 相关资源 <a id="related-resources"></a>

* [表达式参考](./)
