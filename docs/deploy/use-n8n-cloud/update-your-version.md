---
contentType: howto
nodeTitle: 更新版本
originalFilePath: manage-cloud/update-cloud-version.md
originalUrl: https://docs.n8n.io/manage-cloud/update-cloud-version
url: https://docs.n8n.io/deploy/use-n8n-cloud/update-your-version
description: 如何更新 Cloud 上的 n8n 版本。
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


# 更新版本 <a id="update-your-version"></a>

n8n 建议及时更新 Cloud 版本。在 n8n Cloud 控制台的 **Instance settings（实例设置）> Updates（更新）** 部分，你可以选择实例运行的 n8n 版本，并控制自动更新的时间和方式。查看[更新记录](../../changelog/README.md)了解各版本的变化。

{% hint style="info" %}
只有实例所有者可以修改这些设置。如果你没有更新 n8n Cloud 的权限，请联系实例所有者。
{% endhint %}

打开设置的步骤如下：

1. 打开 [Cloud 控制台](use-the-cloud-console.md)。
2. 在侧边栏选择 **Instance settings（实例设置）**。**Updates（更新）** 部分位于页面顶部。

修改设置后，页面底部会出现操作栏，显示尚未保存的修改数量：

* 如果修改了 n8n 版本，请选择 **Save and restart（保存并重启）**。实例会重启，期间有一到两分钟无法使用。
* 如果只修改了发布通道、更新频率或维护窗口，请选择 **Save（保存）**。这些设置无需重启即可生效。

选择 **Discard all（放弃全部）**，可撤销尚未保存的修改。

## n8n 版本 <a id="n8n-version"></a>

**n8n version（n8n 版本）** 下拉列表用于设置实例运行的版本。如果希望在修改前比较版本，请选择 **Open changelog（打开更新记录）**。

要更改版本：

1. 从 **n8n version（n8n 版本）** 下拉列表中选择版本。
2. 选择 **Save and restart（保存并重启）**。
3. 如果新版本属于大版本更新或需要迁移数据库，n8n 会要求确认。阅读警告后，选择 **Update and restart（更新并重启）**。这类更新无法回滚到先前版本。

## 发布通道 <a id="release-track"></a>

发布通道决定实例跟随哪条 n8n 发布线。n8n 会测试这两个通道。两者的区别在于实例获得新版本的时间，以及该版本在此之前已经历的生产运行时间：

* **Beta（测试通道）**：新版本准备好后立即提供。如果希望率先体验最新功能，可以选择 Beta。
* **Stable（稳定通道）**：版本在 Beta 通道运行一段时间后，再提供经过更多验证的后续补丁版本。n8n 建议所有关键业务负载使用 Stable。

你可以随时切换发布通道。

## 更新频率 <a id="update-cadence"></a>

更新频率决定 n8n 多久将实例升级到较新的构建版本。无论选择哪种频率，n8n 都至少每两周升级一次实例，以确保所有用户都能获得安全修复：

* **Every 2 weeks（每两周）**：n8n 大约每两周升级一次实例。推荐大多数实例选择此项。
* **Every new release（每个新版本）**：每个新版本发布时都会升级，平均每天一次。适合体验新功能。

## 维护窗口 <a id="maintenance-window"></a>

维护窗口决定 n8n 可在哪些时段进行升级，以减少影响。每次升级会导致一到两分钟停机。时间使用实例的时区，具体时区显示在该设置的说明中。

* **Anytime（任意时间）**：升级可用后，n8n 会立即应用。
* **Pick a window（选择时段）**：n8n 仅在你设置的 **Start time（开始时间）** 与 **End time（结束时间）** 之间进行升级。

## 相关资源 <a id="related-resources"></a>

* [使用 n8n Cloud](./)
* [免费试用并选择套餐](start-your-free-trial.md)
* [使用 Cloud 控制台](use-the-cloud-console.md)
* [配置 Cloud](configure-cloud/README.md)
* [Gateway 额度](gateway-credits/README.md)
* [Assistant 额度](assistant-credits/README.md)
* [理解并发](understand-concurrency.md)
* [下载工作流](download-workflows.md)
