---
contentType: tutorial
nodeTitle: 部署到 Google Cloud Run
originalFilePath: hosting/installation/server-setups/google-cloud-run.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/google-cloud-run
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Google Cloud Run 上托管 n8n <a href="#hosting-n8n-on-google-cloud-run" id="hosting-n8n-on-google-cloud-run"></a>

本指南介绍如何在无服务器容器运行时 Google Cloud Run 上自托管 n8n。如果刚开始使用 n8n，且不需要生产级部署，可以采用下方的“简易模式”。如果计划大规模使用此部署，请参阅后面的“持久模式”。

还可以通过 OAuth 允许访问 Gmail、Drive 等 Google Workspace 服务，将其用作 n8n 工作流工具。授权方式见文档末尾。

如果希望改为部署到 Google Kubernetes Engine（GKE），请参阅[此指南](deploy-to-google-kubernetes.md)。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/warning.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/latest-next-version.md" %}

## 开始之前：准备 Google Cloud 项目 <a href="#before-you-begin-get-a-google-cloud-project" id="before-you-begin-get-a-google-cloud-project"></a>

如果尚未创建 Google Cloud 项目，请[先创建](https://developers.google.com/workspace/guides/create-project)，并确保已启用结算。即使 Cloud Run 服务免费运行，部署时也必须启用结算。已有项目时，请前往希望部署 n8n 的项目。

## 简易模式 <a href="#easy-mode" id="easy-mode"></a>

这是在 Cloud Run 上部署 n8n 的最快方式。此部署中的 n8n 数据位于内存中，因此仅建议用于演示。**每当 Cloud Run 服务缩容到零或重新部署时，n8n 数据都会丢失。**需要生产级部署时，请参阅下方持久模式。

如果尚未创建 Google Cloud 项目，请[先创建](https://developers.google.com/workspace/guides/create-project)，并确保已启用结算。即使 Cloud Run 服务免费运行，部署时也必须启用结算。已有项目时，请前往希望部署 n8n 的项目。

打开 Cloud Shell 终端：在 Google Cloud 控制台依次按 G、S，或点击右上角终端图标。

会话打开后，可能需要先运行以下命令登录，并按提示完成操作：

```sh
gcloud auth login
```

也可以显式启用 Cloud Run API。即使未提前启用，部署时也会询问是否启用：

```sh
gcloud services enable run.googleapis.com
```

{% hint style="warning" %}
**必需：自定义健康检查端点**

Google Cloud Run 将 `/healthz` 保留给自身的健康检查。n8n 默认也使用此路径，可能发生冲突并导致工作流画布连接问题。请将 `N8N_ENDPOINT_HEALTH` 环境变量设为自定义路径，下方部署命令已包含此设置。
{% endhint %}

部署 n8n：

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n \
    --region=us-west1 \
    --allow-unauthenticated \
    --port=5678 \
    --no-cpu-throttling \
    --memory=2Gi \
    --set-env-vars="N8N_ENDPOINT_HEALTH=health"
```

可以将 us-west1 替换为你希望使用的其他区域。

部署完成后，在另一个标签页打开 Service URL（服务 URL）。n8n 可能仍在加载，显示“n8n is starting up. Please wait”（n8n 正在启动，请稍候），稍后应出现 n8n 登录页面。

可选：如果希望让 n8n 服务尽量长时间运行以避免数据丢失，也可以将手动扩缩容设为 1，防止自动缩容到 0。

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n \
    --region=us-west1 \
    --allow-unauthenticated \
    --port=5678 \
    --no-cpu-throttling \
    --memory=2Gi \
    --scaling=1 \
    --set-env-vars="N8N_ENDPOINT_HEALTH=health"
```

这不能完全避免数据丢失，例如 Cloud Run 服务重新部署或更新时仍会丢失。要真正持久化数据，请按下方说明连接数据库。

## 持久模式 <a href="#durable-mode" id="durable-mode"></a>

以下步骤用于在 Cloud Run 上建立更持久的生产级 n8n 部署，包括持久化数据库，以及保存敏感数据的 Secret Manager 等资源。

如果希望通过 Terraform 部署相同配置，请参阅[此示例](https://github.com/ryanpei/n8n-hosting/tree/main/google-cloud-run)。它与下方设置一致，但不包含 Google Workspace 工具的 OAuth 配置。

## 启用 API 并设置环境变量 <a href="#enable-apis-and-set-env-vars" id="enable-apis-and-set-env-vars"></a>

打开 Cloud Shell 终端：在 Google Cloud 控制台依次按 G、S，或点击右上角终端图标，然后在终端会话中运行：

```sh
## You may need to login first <a href="#you-may-need-to-login-first" id="you-may-need-to-login-first"></a>
gcloud auth login

gcloud services enable run.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

为后续步骤设置一些环境变量：

```sh
export PROJECT_ID=your-project
export REGION=region-where-you-want-this-deployed
```

## 设置 Postgres 数据库 <a href="#setup-your-postgres-database" id="setup-your-postgres-database"></a>

运行以下命令创建 Postgres 数据库实例。完成可能需要几分钟，请将 root-password 字段替换为你自己的密码：

```sh
gcloud sql instances create n8n-db \
    --database-version=POSTGRES_17 \
    --tier=db-f1-micro \
    --region=$REGION \
    --root-password="change-this-password" \
    --storage-size=10GB \
    --availability-type=ZONAL \
    --no-backup \
    --storage-type=HDD
```

完成后，添加 n8n 要使用的数据库：

```sh
gcloud sql databases create n8n --instance=n8n-db
```

创建 n8n 数据库用户，并更改密码值：

```sh
gcloud sql users create n8n-user \
    --instance=n8n-db \
    --password="change-this-password"
```

可以将 n8n-user 密码保存到文件，供下一步写入 Secret Manager 使用。之后务必删除此文件。

## 在 Secret Manager 中保存敏感数据 <a href="#store-sensitive-data-in-secret-manager" id="store-sensitive-data-in-secret-manager"></a>

虽然不是必需，但强烈建议将敏感数据保存在 Secret Manager 中。

为数据库密码创建 Secret，将 /your/password/file 替换为上文创建的 n8n-user 密码文件：

```sh
gcloud secrets create n8n-db-password \
    --data-file=/your/password/file \
    --replication-policy="automatic"
```

创建加密密钥。可以使用你自己的密钥，此示例生成随机密钥：

```sh
openssl rand -base64 -out my-encryption-key 42
```

为此加密密钥创建 Secret。如果使用自己的密钥，请替换 my-encryption-key：

```sh
gcloud secrets create n8n-encryption-key \
    --data-file=my-encryption-key \
    --replication-policy="automatic"
```

现在可以删除创建的 my-encryption-key 和数据库密码文件，这些值已安全保存在 Secret Manager 中。

## 为 Cloud Run 创建服务账号 <a href="#create-a-service-account-for-cloud-run" id="create-a-service-account-for-cloud-run"></a>

应限制 Cloud Run 服务仅访问所需资源。以下命令创建服务账号，并授予访问 Secret 和数据库所需的权限：

```sh
gcloud iam service-accounts create n8n-service-account \
    --display-name="n8n Service Account"

gcloud secrets add-iam-policy-binding n8n-db-password \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"

gcloud secrets add-iam-policy-binding n8n-encryption-key \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"
```

## 部署 Cloud Run 服务 <a href="#deploy-the-cloud-run-service" id="deploy-the-cloud-run-service"></a>

现在可以部署 n8n 服务：

```sh
gcloud run deploy n8n \
    --image=n8nio/n8n:latest \
    --command="/bin/sh" \
    --args="-c,sleep 5;n8n start" \
    --region=$REGION \
    --allow-unauthenticated \
    --port=5678 \
    --memory=2Gi \
    --no-cpu-throttling \
    --set-env-vars="N8N_PORT=5678,N8N_PROTOCOL=https,N8N_ENDPOINT_HEALTH=health,DB_TYPE=postgresdb,DB_POSTGRESDB_DATABASE=n8n,DB_POSTGRESDB_USER=n8n-user,DB_POSTGRESDB_HOST=/cloudsql/$PROJECT_ID:$REGION:n8n-db,DB_POSTGRESDB_PORT=5432,DB_POSTGRESDB_SCHEMA=public,GENERIC_TIMEZONE=UTC,QUEUE_HEALTH_CHECK_ACTIVE=true" \
    --set-secrets="DB_POSTGRESDB_PASSWORD=n8n-db-password:latest,N8N_ENCRYPTION_KEY=n8n-encryption-key:latest" \
    --add-cloudsql-instances=$PROJECT_ID:$REGION:n8n-db \
    --service-account=n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com
```

部署完成后，在另一个标签页打开 Service URL（服务 URL），应看到 n8n 登录页面。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

如果出现“Cannot GET /”页面，通常表示 n8n 仍在启动。可以刷新页面，稍后应能加载。

## 可选：将 Google Workspace 服务启用为 n8n 工具 <a href="#optional-enabling-google-workspace-services-as-n8n-tools" id="optional-enabling-google-workspace-services-as-n8n-tools"></a>

如果希望将 Gmail、Calendar、Drive 等 Google Workspace 服务用作 n8n 工具，建议设置 OAuth 来访问这些服务。

首先确保已启用所需服务对应的 API：

```sh
## Enable whichever APIs you need <a href="#enable-whichever-apis-you-need" id="enable-whichever-apis-you-need"></a>
## Note: If you want Sheets/Docs, it's not enough to just enable Drive; these services each have their own API <a href="#note-if-you-want-sheetsdocs-its-not-enough-to-just-enable-drive-these-services-each-have-their-own-api" id="note-if-you-want-sheetsdocs-its-not-enough-to-just-enable-drive-these-services-each-have-their-own-api"></a>
gcloud services enable gmail.googleapis.com
gcloud services enable drive.googleapis.com
gcloud services enable sheets.googleapis.com
gcloud services enable docs.googleapis.com
gcloud services enable calendar-json.googleapis.com
```

在 Cloud Run 上重新部署 n8n，将必需的 OAuth 回调 URL 设为环境变量：

```sh
export SERVICE_URL="your-n8n-service-URL"
## e.g. https://n8n-12345678.us-west1.run.app <a href="#eg-httpsn8n-12345678us-west1runapp" id="eg-httpsn8n-12345678us-west1runapp"></a>

gcloud run services update n8n \
    --region=$REGION \
    --update-env-vars="N8N_HOST=$(echo $SERVICE_URL | sed 's/https:\/\///'),N8N_WEBHOOK_URL=$SERVICE_URL,N8N_EDITOR_BASE_URL=$SERVICE_URL"
```

自 n8n 2.30.0 起可使用 `N8N_WEBHOOK_URL`，更早版本请使用 `WEBHOOK_URL`。

最后，必须为这些服务设置 OAuth。访问 `https://console.cloud.google.com/auth` 并按以下步骤操作：

1. 如果显示 **Get Started**（开始）按钮，说明尚未在此 Cloud 项目设置 OAuth，请点击它。
1. 在 **App Information**（应用信息）中，输入所需的 **App Name**（应用名称）和 **User Support Email**（用户支持邮箱）。
1. 在 **Audience**（受众）中，如果仅向同一 Google Workspace 内的用户开放访问，选择 **Internal**（内部），否则可选择 **External**（外部）。
1. 输入 **Contact Information**（联系信息）。
1. 如果选择 External，请点击 **Audience**，添加需要授予访问权限的测试用户。
1. 点击 **Clients**（客户端）> **Create client**（创建客户端），将 **Application type**（应用类型）设为 **Web application**（Web 应用）。在 **Authorized JavaScript origins**（已获授权的 JavaScript 来源）中输入 n8n 服务 URL，在 **Authorized redirect URIs**（已获授权的重定向 URI）中输入“<YOUR-N8N-URL>/rest/oauth2-credential/callback”。YOUR-N8N-URL 同样是 n8n 服务 URL，例如 `https://n8n-12345678.us-west1.run.app/rest/oauth2-credential/callback`。请务必下载创建的客户端 JSON 文件，其中包含之后无法再从控制台查看的客户端密钥。
1. 点击 **Data Access**（数据访问），添加希望授予 n8n 的权限范围。例如，访问 Google Sheets 需要 `https://googleapis.com/auth/drive.file` 和 `https://googleapis.com/auth/spreadsheets`。
1. 现在应能使用这些 Workspace 服务。可登录 n8n，添加对应服务的工具，并使用第 6 步 OAuth 客户端 JSON 文件中的信息添加凭据，以测试是否有效。


## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Heroku](deploy-to-heroku.md)
* [Hetzner Cloud](deploy-to-hetzner.md)
* [AWS](deploy-to-aws.md)
* [Azure](deploy-to-azure.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)
* [使用 Docker Compose](use-docker-compose.md)
