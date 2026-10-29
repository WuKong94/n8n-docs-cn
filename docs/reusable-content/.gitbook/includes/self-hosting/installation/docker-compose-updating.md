---
title: 更新 Docker Compose 安装
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

如果通过 Docker Compose 文件运行 n8n，请按照以下步骤更新：

```sh
# Navigate to the directory containing your docker compose file <a href="#navigate-to-the-directory-containing-your-docker-compose-file" id="navigate-to-the-directory-containing-your-docker-compose-file"></a>
cd </path/to/your/compose/file/directory>

# Pull latest version <a href="#pull-latest-version" id="pull-latest-version"></a>
docker compose pull

# Stop and remove older version <a href="#stop-and-remove-older-version" id="stop-and-remove-older-version"></a>
docker compose down

# Start the container <a href="#start-the-container" id="start-the-container"></a>
docker compose up -d
```
