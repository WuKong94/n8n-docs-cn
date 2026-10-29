---
contentType: reference
nodeTitle: 查找 IP 地址
originalFilePath: manage-cloud/cloud-ip.md
originalUrl: 'https://docs.n8n.io/manage-cloud/cloud-ip'
url: >-
  https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Cloud IP 地址 <a href="#cloud-ip-addresses" id="cloud-ip-addresses"></a>

n8n Cloud 上的工作流向外发送请求时，例如通过 **HTTP Request** 节点或应用节点发送请求，来源 IP 会是本页列出的地址之一。你可以在防火墙或按 IP 限制访问的服务中，将这些地址加入允许列表。发送到实例的入站 Webhook 流量不使用这些地址。

## n8n Cloud 出站 IP 地址的工作方式 <a id="how-n8n-cloud-outbound-ip-addresses-work"></a>

n8n Cloud 运行在共享基础设施上。多个实例共享每个地址，因此没有你实例专属的地址。实例通常保持使用同一个地址；只有在 n8n 必须将实例迁移到其他集群等少数情况下，地址才会变化。n8n 不会提前通知这些变化。

由于这些地址由多个实例共享，仅凭 IP 允许列表无法证明请求来自你的实例。对提供给 n8n Cloud 访问的服务，应始终要求身份验证。

## n8n Cloud 出站 IP 地址列表 <a id="n8n-cloud-outbound-ip-address-list"></a>

n8n 建议将列表中的所有地址加入允许列表。实际上，这些地址很少变化。要可靠地确认实例当前使用哪个地址，可以[通过工作流检查](#find-the-address-your-instance-currently-uses)。n8n 可能逐步增加新地址，因此如果允许列表开始拦截 n8n Cloud 的请求，请检查本页是否新增了地址。以 `/28` 结尾的条目表示包含 16 个地址的地址块，以 `/32` 结尾的条目表示单个地址。

```text
4.165.103.112/28
4.182.64.64/28
4.184.78.240/28
9.223.34.48/28
20.52.126.0/28
20.79.32.32/28
20.218.174.0/28
20.218.238.112/28
20.240.52.208/28
20.240.204.176/28
51.107.180.112/28
51.116.119.64/28
4.182.88.118/32
4.182.111.50/32
4.182.128.108/32
4.182.129.20/32
4.182.190.144/32
4.182.191.184/32
4.182.212.136/32
72.144.69.38/32
72.144.83.147/32
72.144.111.50/32
72.144.128.145/32
98.67.233.91/32
98.67.233.200/32
98.67.244.108/32
```

## 查找实例当前使用的地址 <a id="find-the-address-your-instance-currently-uses"></a>

如果希望只允许较小范围的地址，请检查实例当前使用的地址：

1. 创建一个包含 **Manual Trigger（手动触发器）** 节点和 **HTTP Request** 节点的工作流。
2. 在 **HTTP Request** 节点中，将 **Method（方法）** 设为 `GET`，将 **URL** 设为一个返回请求来源 IP 的服务，例如 `https://api.ipify.org?format=json`。这个示例服务由第三方运营，并非 n8n 提供。
3. 选择 **Execute workflow（执行工作流）**。**HTTP Request** 节点输出的 `ip` 字段会显示实例当前的出站地址。

如果希望持续确认地址是否变化，请添加 **Schedule Trigger（定时触发器）** 节点，将其连接到 **HTTP Request** 节点，然后发布工作流。

{% hint style="warning" %}
**不保证始终使用同一个地址**

该工作流只是方便你查询，并不提供地址固定不变的保证。实例地址可能在不通知的情况下变化。如果只将这个地址加入允许列表，地址变化时，工作流可能停止正常运行。
{% endhint %}

## 相关资源 <a id="related-resources"></a>

* [配置 Cloud](./)
* [设置时区](set-your-timezone.md)
* [管理数据](manage-your-data.md)
* [更改实例所有者或用户名](change-instance-ownership-or-username.md)
