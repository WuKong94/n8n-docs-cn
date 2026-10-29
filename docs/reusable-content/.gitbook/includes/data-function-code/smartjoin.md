---
title: smartjoin
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

```js
// Input
{{ [{"type":"fruit", "name":"apple"},{"type":"vegetable", "name":"carrot"} ].smartJoin("type","name") }}
// Output
[Object: {"fruit":"apple","vegetable":"carrot"}]
```
