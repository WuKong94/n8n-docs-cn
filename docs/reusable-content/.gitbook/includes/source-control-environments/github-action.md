---
title: GitHub Action 示例
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

GitHub Action 示例：

译注：原示例仍请求 /version-control/pull，且没有显式指定 POST；同一版本的“在环境间复制工作”和公共 API 指南示例使用 POST /api/v1/source-control/pull。此处保留原始代码以便对照，请以对应实例的 API 端点、方法和鉴权要求核对后再使用。

```yaml
name: CI
on:
  # Trigger the workflow on push or pull request events for the "production" branch
  push:
    branches: [ "production" ]
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
jobs:
  run-pull:
    runs-on: ubuntu-latest
    steps:
      - name: PULL
				# Use GitHub secrets to protect sensitive information
        run: >
          curl --location '${{ secrets.INSTANCE_URL }}/version-control/pull' --header
          'Content-Type: application/json' --header 'X-N8N-API-KEY: ${{ secrets.INSTANCE_API_KEY }}'
```
