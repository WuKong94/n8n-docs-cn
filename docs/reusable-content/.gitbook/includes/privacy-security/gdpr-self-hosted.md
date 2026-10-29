---
title: 自托管用户的 GDPR 数据删除责任
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

自托管 n8n 时，你负责删除用户数据。如需代表某位用户删除数据，可以删除相应执行记录。n8n 建议配置为每隔几天自动清理执行数据，尽量减少处理 GDPR 请求的工作量。通过 `EXECUTIONS_DATA_MAX_AGE` 环境变量进行配置。更多信息请参阅[环境变量](../../../../deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/README.md)。
