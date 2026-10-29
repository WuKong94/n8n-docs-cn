---
contentType: howto
nodeTitle: 获取二进制数据缓冲区
originalFilePath: code/cookbook/code-node/get-binary-data-buffer.md
originalUrl: https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer
url: https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 获取二进制数据缓冲区 <a href="#get-the-binary-data-buffer" id="get-the-binary-data-buffer"></a>

二进制数据缓冲区包含工作流处理的全部二进制文件数据。执行以下操作时，需要访问缓冲区：

* 操作数据，例如为 CSV 文件添加列标题。
* 使用数据计算，例如根据内容计算哈希值。
* 发起复杂 HTTP 请求，例如上传文件时同时发送其他格式的数据。

{% hint style="info" %}
**Python 不支持**

使用 Python 时，不支持 `getBinaryDataBuffer()`。
{% endhint %}
可以通过 n8n 的 `getBinaryDataBuffer()` 函数访问缓冲区：


```js
/* 
* itemIndex: number. The index of the item in the input data.
* binaryPropertyName: string. The name of the binary property. 
* The default in the Read/Write File From Disk node is 'data'. 
*/
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(itemIndex, binaryPropertyName);
```

例如：

```js
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(0, 'data');
// Returns the data in the binary buffer for the first input item
```


应始终使用 `getBinaryDataBuffer()` 函数，避免采用直接访问缓冲区的旧方法，例如使用 `items[0].binary.data.data` 之类的表达式。

## 相关资源 <a id="related-resources"></a>

* [Code 节点实用示例](./)
* [获取前一节点返回的数据项数量](get-number-of-items-returned-by-last-node.md)
* [输出到浏览器控制台](output-to-the-browser-console.md)
