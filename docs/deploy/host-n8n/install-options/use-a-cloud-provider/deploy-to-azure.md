---
contentType: tutorial
nodeTitle: 部署到 Azure
originalFilePath: hosting/installation/server-setups/azure.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/azure
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 Azure 上托管 n8n <a href="#hosting-n8n-on-azure" id="hosting-n8n-on-azure"></a>

本指南介绍如何在 Azure 上自托管 n8n，使用 Postgres 作为数据库后端，并通过 Kubernetes 管理所需资源和反向代理。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

需要 [Azure 命令行工具](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)。

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/warning.md" %}

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/latest-next-version.md" %}

## 托管选项 <a href="#hosting-options" id="hosting-options"></a>

Azure 提供多种适合托管 n8n 的方式，包括 Azure Container Instances（针对运行容器优化）、Linux 虚拟机和 Azure Kubernetes Service（使用 Kubernetes 运行的容器）。

本指南使用 Azure Kubernetes Service（AKS）托管。Kubernetes 会增加一些复杂性和配置，但最适合随需求变化扩展 n8n。

本指南结合使用 Azure 界面和命令行工具，但大多数任务可任选一种方式完成。

## 打开 Azure Kubernetes Service <a href="#open-the-azure-kubernetes-service" id="open-the-azure-kubernetes-service"></a>

在 [Azure 门户](https://portal.azure.com/)中选择 **Kubernetes services**（Kubernetes 服务）。

## 创建集群 <a href="#create-a-cluster" id="create-a-cluster"></a>

在 Kubernetes 服务页面，选择 **Create**（创建）> **Create a Kubernetes cluster**（创建 Kubernetes 集群）。

选择符合需求的配置选项，完成后选择 **Create**（创建）。

## 设置 kubectl 上下文 <a href="#set-kubectl-context" id="set-kubectl-context"></a>

后续步骤要求将 Azure 实例设为 kubectl 上下文。打开集群实例的详情页，点击 **Connect**（连接），即可找到连接信息。显示的代码片段说明如何在终端中粘贴并运行命令，将本地 Kubernetes 设置切换到新集群。

## 克隆配置仓库 <a href="#clone-configuration-repository" id="clone-configuration-repository"></a>

Kubernetes 和 n8n 需要一系列配置文件，可以从[此仓库](https://github.com/n8n-io/n8n-hosting)克隆。以下步骤说明各文件配置哪些内容，以及需要更改的设置。

使用以下命令克隆仓库：

```shell
git clone https://github.com/n8n-io/n8n-hosting.git
```

然后切换目录：

```shell
cd n8n-hosting/kubernetes
```

## 配置 Postgres <a href="#configure-postgres" id="configure-postgres"></a>

对于较大规模的 n8n 部署，Postgres 比 SQLite 提供更稳健的数据库后端。

### 配置持久存储卷 <a href="#configure-volume-for-persistent-storage" id="configure-volume-for-persistent-storage"></a>

为在 Pod 重启后保留数据，Postgres 部署需要持久卷。默认存储类适合此用途，由 `postgres-claim0-persistentvolumeclaim.yaml` 清单定义。

{% hint style="info" %}
**专用存储类**

如果对存储类有特殊或更高要求，请[阅读 Azure 文档中的可用选项](https://learn.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes)。
{% endhint %}

### Postgres 环境变量 <a href="#postgres-environment-variables" id="postgres-environment-variables"></a>

需要为 Postgres 设置一些环境变量，并传递给容器内运行的应用。

示例 `postgres-secret.yaml` 文件包含占位符，需要替换为你自己的值。Postgres 创建数据库时会使用这些信息。

随后，`postgres-deployment.yaml` 清单使用此文件中的值，将其传递给应用 Pod。

## 配置 n8n <a href="#configure-n8n" id="configure-n8n"></a>

### 创建文件存储卷 <a href="#create-a-volume-for-file-storage" id="create-a-volume-for-file-storage"></a>

虽然运行 n8n 并非必须使用持久卷，但以下情况需要：

* 使用与文件交互的节点，例如二进制数据节点。
* 希望在重启间保留[手动设置的 n8n 加密密钥](../../configure-n8n/basic-configuration/use-environment-variables/deployment.md)。启动时，密钥会写入文件存储中的一个文件。

`n8n-claim0-persistentvolumeclaim.yaml` 清单创建此存储卷声明，n8n Deployment 通过 `volumes` 部分挂载它，该部分位于 `n8n-deployment.yaml` 清单中。

```yaml
…
volumes:
  - name: n8n-claim0
    persistentVolumeClaim:
      claimName: n8n-claim0
…
```

### Pod 资源 <a href="#pod-resources" id="pod-resources"></a>

[Kubernetes 允许](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)按需指定应用容器所需的最小资源和可使用的上限。前文克隆的示例 YAML 文件，其 `resources` 部分包含以下内容，位于 `n8n-deployment.yaml` 文件中：

```yaml
…
resources:
  requests:
    memory: "250Mi"
  limits:
    memory: "500Mi"
…    
```

这为每个容器定义最少 250 MB、最多 500 MB 的内存，并由 Kubernetes 处理 CPU。可以按需更改。以下是 n8n Cloud 套餐的资源值，供参考：

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/suggested-pod-resources.md" %}

### 可选：环境变量 <a href="#optional-environment-variables" id="optional-environment-variables"></a>

可以通过环境变量配置 n8n 设置和行为。

创建 `n8n-secret.yaml` 文件。n8n 环境变量详情请参阅[环境变量](../../configure-n8n/basic-configuration/use-environment-variables/README.md)。

## 部署 <a href="#deployments" id="deployments"></a>

两个部署清单（`n8n-deployment.yaml` 和 `postgres-deployment.yaml`）向 Kubernetes 定义 n8n 和 Postgres 应用。

{% hint style="warning" %}
这些清单运行 PostgreSQL 18，首次设置无需额外操作。

如果已有数据库运行较旧的 PostgreSQL 主版本，请勿直接对其应用这些清单。PostgreSQL 18 无法打开旧主版本写入的数据目录，移动文件夹也无济于事。Pod 会持续处于 `CrashLoopBackOff`，并报错 `database files are incompatible with server`。PostgreSQL 不会改动原数据，可以将镜像重新固定回先前版本。

要迁移现有数据库，请先按照官方 [PostgreSQL 升级指南](https://www.postgresql.org/docs/18/upgrading.html)操作。
{% endhint %}

这些清单定义以下内容：

- 将定义的环境变量传递给各应用 Pod。
- 定义要使用的容器镜像。
- 通过 `resources` 对象设置资源消耗上限。
- 使用前文定义的 `volumes` 和 `volumeMounts`，指定容器中挂载卷的路径。
- 扩展和重启策略。示例清单为每种 Pod 定义一个实例，请按需调整。

## 服务 <a href="#services" id="services"></a>

两个服务清单（`postgres-service.yaml` 和 `n8n-service.yaml`）通过 Kubernetes 负载均衡器向外提供服务，端口分别为 5432 和 5678。

## 发送到 Kubernetes 集群 <a href="#send-to-kubernetes-cluster" id="send-to-kubernetes-cluster"></a>

运行以下命令，将所有清单发送到集群：

```shell
kubectl apply -f .
```

{% hint style="info" %}
**命名空间错误**

资源尚未就绪时，可能出现找不到“n8n”命名空间的错误。可以再次运行相同命令，或先使用以下命令应用命名空间清单：

```shell
kubectl apply -f namespace.yaml
```
{% endhint %}


## 设置 DNS <a href="#set-up-dns" id="set-up-dns"></a>

n8n 通常运行在子域名上。请在 DNS 提供商处为子域名创建记录，指向 n8n 服务的 IP 地址。打开目标集群的 **Services & ingresses**（服务与入口）菜单，在 **External IP**（外部 IP）列查找 n8n 服务地址。URL 中还需添加 n8n 端口 5678。

{% hint style="info" %}
**AKS 静态 IP 地址**

如何为 AKS 使用静态 IP 地址，请[阅读此教程](https://learn.microsoft.com/en-us/azure/aks/static-ip)。
{% endhint %}

## 删除资源 <a href="#delete-resources" id="delete-resources"></a>

使用以下命令移除清单创建的资源：

```shell
kubectl delete -f .
```

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/server-setups-next-steps.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Heroku](deploy-to-heroku.md)
* [Hetzner Cloud](deploy-to-hetzner.md)
* [AWS](deploy-to-aws.md)
* [Google Cloud Run](deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [OpenShift Local（CRC）](deploy-to-openshift-local-crc.md)
* [使用 Docker Compose](use-docker-compose.md)
