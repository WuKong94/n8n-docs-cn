---
contentType: tutorial
nodeTitle: 部署到 OpenShift Local（CRC）
originalFilePath: hosting/installation/server-setups/openshift-crc.md
originalUrl: https://docs.n8n.io/hosting/installation/server-setups/openshift-crc
url: https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 在 OpenShift Local（CRC）上托管 n8n <a href="#hosting-n8n-on-openshift-local-crc" id="hosting-n8n-on-openshift-local-crc"></a>

本指南介绍如何在 OpenShift Local（CRC）上部署 n8n。CRC 是 Red Hat 提供的本地 OpenShift 集群运行工具。此部署与 AWS/EKS 类似，但完全运行在本机，适合在本地 OpenShift 环境中测试 n8n，无需云服务费用。

OpenShift 本身消耗较多资源，因此需要一台具有充足可用资源的机器。

## OpenShift 与标准 Kubernetes 的概念对照 <a href="#openshift-concepts-vs-standard-kubernetes" id="openshift-concepts-vs-standard-kubernetes"></a>

OpenShift 基于 Kubernetes 构建，但术语有所不同，默认安全限制也更严格。如果熟悉标准 Kubernetes，或参考过 EKS 等托管 Kubernetes 服务指南，下表可帮助理解对应概念。

| 标准 Kubernetes / EKS | OpenShift Local（CRC） |
| --- | --- |
| `kubectl` | `oc`，OpenShift CLI，也支持 `kubectl` 命令 |
| Namespace，命名空间 | Project，项目，概念相同、命令不同 |
| Ingress / LoadBalancer | Route，OpenShift 内置，无需控制器 |
| EBS StorageClass（gp3） | CRC 内置存储提供程序，无需设置 |
| RDS PostgreSQL | 通过 Helm 在集群内运行 PostgreSQL，使用 Bitnami |
| ElastiCache Redis | 通过 Helm 在集群内运行 Redis，使用 Bitnami |
| AWS S3 | 集群内的 MinIO，兼容 S3 |
| Pod Identity / IRSA | 通过 Kubernetes Secret 提供访问密钥 |
| AWS Load Balancer Controller | 不需要，Route 已内置 |
| OIDC / IAM | 不需要 |
| 约每月 135–400 美元 | 免费，在本机运行 |

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

开始前，确认机器具备：

- **CPU**：至少 4 个物理核心，而非仅计算线程，支持虚拟化。
- **RAM**：至少 32 GB 可用内存，CRC 会为其虚拟机预留 9 GB。
- **磁盘**：100 GB 可用空间。
- **操作系统**：Ubuntu 22.04 LTS 或更新版本。

## 准备 Ubuntu <a href="#prepare-ubuntu" id="prepare-ubuntu"></a>

### 打开终端 <a href="#open-a-terminal" id="open-a-terminal"></a>

按 `Ctrl+Alt+T`，或在应用菜单中搜索 **Terminal**（终端）。

本指南的所有命令都在终端输入，并按 **Enter** 运行。

### 更新系统 <a href="#update-your-system" id="update-your-system"></a>

先更新系统，以避免依赖问题：

```shell
sudo apt update && sudo apt upgrade -y
```

{% hint style="info" %}
**sudo**

`sudo` 表示“以管理员身份运行”。系统会提示输入密码，输入的字符不会显示在屏幕上，这是正常行为。
{% endhint %}

### 检查 CPU 虚拟化支持 <a href="#check-cpu-virtualization-support" id="check-cpu-virtualization-support"></a>

CRC 会运行虚拟机，因此 CPU 必须支持硬件虚拟化：

```shell
egrep -c '(vmx|svm)' /proc/cpuinfo
```

- **输出 `0`**：虚拟化已禁用。进入 BIOS/UEFI 设置，启用 VT-x（Intel）或 AMD-V（AMD），重启后再试。
- **输出 `1` 或更大值**：可以继续。

### 安装 KVM 和 libvirt <a href="#install-kvm-and-libvirt" id="install-kvm-and-libvirt"></a>

KVM 是 Linux 内置虚拟机监控器，CRC 使用它运行 OpenShift 集群虚拟机：

```shell
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
```

安装 `virtiofsd`，CRC 需要它与集群虚拟机共享文件系统：

```shell
sudo apt install -y virtiofsd
```

启动 libvirt 服务，并配置开机自动启动：

```shell
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
```

验证服务正在运行：

```shell
sudo systemctl status libvirtd
```

查找绿色的 `Active: active (running)`，按 `q` 退出。

### 将用户加入必需用户组 <a href="#add-user-to-required-groups" id="add-user-to-required-groups"></a>

这样使用 KVM 和 libvirt 时，无需为每条命令都输入 `sudo`：

```shell
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
```

{% hint style="info" %}
**警告**

**必须退出登录后重新登录，或重启，才能生效。**跳过此步骤，CRC 会因“permission denied”（权限被拒绝）而失败。
{% endhint %}

现在重启：

```shell
sudo reboot
```

重新登录后，打开终端验证所属用户组：

```shell
groups
```

列表中应包含 `libvirt` 和 `kvm`。

### 安装 NetworkManager <a href="#install-networkmanager" id="install-networkmanager"></a>

CRC 需要 NetworkManager 管理集群内部域名的 DNS 条目（`*.apps-crc.testing`、`api.crc.testing`）：

```shell
sudo apt install -y network-manager
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```

验证连接状态：

```shell
nmcli general status
```

`STATE` 列应显示 `connected`。

## 安装工具 <a href="#install-tools" id="install-tools"></a>

### 获取 Red Hat 账号和拉取密钥 <a href="#get-a-red-hat-account-and-pull-secret" id="get-a-red-hat-account-and-pull-secret"></a>

CRC 需要免费的 Red Hat 账号来拉取容器镜像。

1. 如果还没有账号，请[创建免费 Red Hat 账号](https://console.redhat.com/)。
2. 在 [console.redhat.com/openshift/create/local](https://console.redhat.com/openshift/create/local) 中点击 **Download OpenShift Local**（下载 OpenShift Local）。
3. 选择 **Linux**，将 `.tar.xz` 文件下载到 `~/Downloads`。
4. 在 Red Hat 控制台的同一页面，点击 **Copy pull secret**（复制拉取密钥），粘贴到文本文件中保存，供后续使用。

### 安装 CRC <a href="#install-crc" id="install-crc"></a>

在 Downloads 文件夹中打开终端。

```shell
cd ~/Downloads
```

解压归档文件。

```shell
tar xf crc-linux-amd64.tar.xz
```

将 `crc` 二进制文件移到系统级位置，使其可在任意终端使用：

```shell
sudo mv crc-*-linux-amd64/crc /usr/local/bin/
```

验证安装：

```shell
crc version
```

终端应输出版本号。

### 安装 Helm <a href="#install-helm" id="install-helm"></a>

Helm 将 n8n 及支持服务安装到集群：

```shell
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

验证：

```shell
helm version
```

### 设置环境变量 <a href="#set-environment-variables" id="set-environment-variables"></a>

```shell
export NAMESPACE=n8n-$(date +%Y%m%d)
echo "Namespace:$NAMESPACE"
```

{% hint style="info" %}
**变量持久性**

这些变量仅在当前终端会话中有效。每次打开新终端继续操作前，都要重新运行此行。
{% endhint %}

## 启动 OpenShift Local <a href="#start-openshift-local" id="start-openshift-local"></a>

### 运行 CRC 设置 <a href="#run-crc-setup" id="run-crc-setup"></a>

此步骤仅需运行一次，会配置 KVM 网络、检查系统要求，并下载约 2.5 GB 的 CRC 包：

```shell
crc setup
```

这需要几分钟。如果提示缺少软件包，请使用 `sudo apt install -y <package-name>` 安装后重新运行。

### 配置 CRC 内存并启动集群 <a href="#configure-crc-memory-and-start-the-cluster" id="configure-crc-memory-and-start-the-cluster"></a>

CRC 默认为虚拟机分配 9 GB RAM。n8n 及支持服务需要更多余量，启动前请将内存设为 14 GB：

```shell
crc config set memory 14336
```

只需设置一次，`crc stop` / `crc start` 循环后仍会保留。

**建议：**先将拉取密钥保存为文件，避免每次都需粘贴：

```shell
# Open the file, paste your pull secret (from earlier), then Ctrl+O to save, Ctrl+X to exit <a href="#open-the-file-paste-your-pull-secret-from-earlier-then-ctrlo-to-save-ctrlx-to-exit" id="open-the-file-paste-your-pull-secret-from-earlier-then-ctrlo-to-save-ctrlx-to-exit"></a>
nano ~/pull-secret.txt

# Restrict permissions so only you can read it <a href="#restrict-permissions-so-only-you-can-read-it" id="restrict-permissions-so-only-you-can-read-it"></a>
chmod 600 ~/pull-secret.txt
```

使用该文件启动 CRC：

```shell
crc start --pull-secret-file ~/pull-secret.txt
```

也可以运行不带此标志的 `crc start`，并在提示时粘贴密钥。

**这需要 10–15 分钟。**完成后会看到类似输出：

```
Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: <generated-password>

Log in as user:
  Username: developer
  Password: developer
```

**现在请保存 `kubeadmin` 密码。**下一步需要使用，之后也可通过 `crc console --credentials` 获取。

### 验证 DNS 解析 <a href="#verify-dns-resolution" id="verify-dns-resolution"></a>

在 Ubuntu 上，CRC 通过 NetworkManager 和 systemd-resolved 自动配置系统解析器，无需手动添加 `/etc/hosts` 条目。

验证 API 可访问：

```shell
sudo ss -tlnp | grep 6443
```

应能看到绑定到 `127.0.0.1:6443` 的进程。如果没有输出，请重新运行 `crc start`。如果 DNS 无法解析 `*.apps-crc.testing`，请参阅故障排查章节。

### 配置 Shell <a href="#configure-your-shell" id="configure-your-shell"></a>

CRC 在虚拟机中包含 `oc` CLI。此命令让它可在终端中使用：

```shell
eval $(crc oc-env)
```

要永久生效，避免每次打开终端都重新运行：

```shell
echo 'eval $(crc oc-env)' >> ~/.bashrc
source ~/.bashrc
```

验证 `oc` 可用：

```shell
oc version
```

### 登录集群 <a href="#log-in-to-the-cluster" id="log-in-to-the-cluster"></a>

```shell
oc login -u kubeadmin -p <your-kubeadmin-password> https://api.crc.testing:6443
```

将 `<your-kubeadmin-password>` 替换为[配置 CRC 内存并启动集群](#configure-crc-memory-and-start-the-cluster)时输出的密码。

验证已登录：

```shell
oc whoami
```

屏幕应输出 `kubeadmin`。

## 单实例部署 <a href="#standalone-deployment" id="standalone-deployment"></a>

单实例模式以单个 Pod 运行 n8n，使用 SQLite，无需外部数据库或 Redis，适合在本地探索 n8n 和测试工作流。

### 创建项目 <a href="#create-the-project" id="create-the-project"></a>

OpenShift 中的**项目**等同于 Kubernetes 命名空间，是资源的隔离空间：

```shell
oc new-project $NAMESPACE
```

### 授予必需的安全权限 <a href="#grant-the-required-security-permission" id="grant-the-required-security-permission"></a>

OpenShift 强制执行名为 **Security Context Constraints（SCC，安全上下文约束）**的严格安全策略。默认情况下，Pod 无法以指定用户 ID 运行。n8n chart 以用户 ID `1000` 运行，因此必须显式允许。

请使用完整的显式形式。简写 `-z` 标志在某些 OpenShift 版本中可能无提示失败：

```shell
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n
```

验证绑定已创建：

```shell
oc get rolebindings -n $NAMESPACE
```

应看到引用 `system:openshift:scc:anyuid` 的绑定。

### 创建必需 Secret <a href="#create-the-required-secret" id="create-the-required-secret"></a>

```shell
oc create secret generic n8n-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$(openssl rand -hex 32)" \
  --from-literal=N8N_HOST="localhost" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http"
```

**立即备份加密密钥：**

```shell
oc get secret n8n-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode
```

复制输出并妥善保存。丢失密钥会使工作流中所有已存储的凭据永久无法读取。

### 创建 values 文件 <a href="#create-your-values-file" id="create-your-values-file"></a>

创建名为 `n8n-standalone-values.yaml` 的文件，可以使用简单文本编辑器 `nano`：

```shell
nano n8n-standalone-values.yaml
```

粘贴以下内容，然后按 `Ctrl+O` 保存、`Ctrl+X` 退出：

```yaml
# n8n-standalone-values.yaml <a href="#n8n-standalone-valuesyaml" id="n8n-standalone-valuesyaml"></a>
# Single pod, SQLite database, no external dependencies. <a href="#single-pod-sqlite-database-no-external-dependencies" id="single-pod-sqlite-database-no-external-dependencies"></a>

queueMode:
  enabled: false

database:
  type: sqlite
  useExternal: false

redis:
  enabled: false

# PVC stores the SQLite database file. <a href="#pvc-stores-the-sqlite-database-file" id="pvc-stores-the-sqlite-database-file"></a>
persistence:
  enabled: true
  size: 5Gi
  # No storageClassName needed — CRC provides a default storage provisioner.

secretRefs:
  existingSecret: "n8n-secrets"

service:
  type: ClusterIP
  port: 5678

# OpenShift: securityContext must be enabled so the pod runs as UID 1000 (node user) <a href="#openshift-securitycontext-must-be-enabled-so-the-pod-runs-as-uid-1000-node-user" id="openshift-securitycontext-must-be-enabled-so-the-pod-runs-as-uid-1000-node-user"></a>
# with fsGroup 1000 (so the PVC is writable). The anyuid SCC granted above <a href="#with-fsgroup-1000-so-the-pvc-is-writable-the-anyuid-scc-granted-above" id="with-fsgroup-1000-so-the-pvc-is-writable-the-anyuid-scc-granted-above"></a>
# allows this. The seccompProfile line is removed from the chart template in <a href="#allows-this-the-seccompprofile-line-is-removed-from-the-chart-template-in" id="allows-this-the-seccompprofile-line-is-removed-from-the-chart-template-in"></a>
# "Deploy n8n" because OpenShift 4.14+ rejects it even with anyuid. <a href="#deploy-n8n-because-openshift-414-rejects-it-even-with-anyuid" id="deploy-n8n-because-openshift-414-rejects-it-even-with-anyuid"></a>
securityContext:
  enabled: true

resources:
  main:
    requests:
      cpu: 100m
      memory: 256Mi
    limits:
      cpu: "1"
      memory: 1Gi

config:
  timezone: UTC
```

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

n8n Helm chart 在 Pod 规范中硬编码了 `seccompProfile: RuntimeDefault`。OpenShift 4.14 及更高版本会将其转换为已弃用的 alpha 注解，在准入阶段被拒绝，即使已授予 `anyuid` SCC 也如此。解决方式是将 chart 拉取到本地，移除这两行，并从修补后的副本安装。

**拉取并修补 chart：**

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Confirm the lines are gone (should return no output) <a href="#confirm-the-lines-are-gone-should-return-no-output" id="confirm-the-lines-are-gone-should-return-no-output"></a>
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml
```

**从修补后的 chart 安装：**

```shell
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml \
  --wait \
  --timeout 10m
```

### 通过端口转发访问 n8n <a href="#access-n8n-using-port-forward" id="access-n8n-using-port-forward"></a>

OpenShift Route 需要主机名，会增加单实例本地访问的复杂性，使用端口转发更简单：

```shell
oc port-forward service/n8n-main --namespace $NAMESPACE 5678:5678
```

保持命令运行，然后在浏览器打开：

```
http://localhost:5678
```

n8n 会提示创建所有者账号。

{% hint style="info" %}
**停止隧道**

按 `Ctrl+C` 停止隧道。以后需要再次访问 n8n 时，重新运行 `port-forward` 命令。
{% endhint %}

### 检查部署状态 <a href="#check-deployment-status" id="check-deployment-status"></a>

```shell
oc get pods -n $NAMESPACE
```

预期输出：

```
NAME                       READY   STATUS    RESTARTS   AGE
n8n-main-7d9f8b-xxxx       1/1     Running   0          3m
```

**单实例部署完成。**

## 多实例队列模式 <a href="#multi-instance-queue-mode" id="multi-instance-queue-mode"></a>

多实例队列模式运行多个 n8n Pod，共享数据库、消息队列和对象存储。需要 [n8n Enterprise 许可证](https://n8n.io/pricing/)。

本指南不使用 AWS 托管服务，而使用集群内的对应组件，模拟本地部署或客户 OpenShift 环境：

| AWS 服务 | 本地对应组件 |
| --- | --- |
| RDS PostgreSQL | PostgreSQL，Bitnami Helm chart |
| ElastiCache Redis | Redis，Bitnami Helm chart |
| S3 | MinIO，兼容 S3，Bitnami Helm chart |

### 安装集群内服务 <a href="#install-in-cluster-services" id="install-in-cluster-services"></a>

#### 创建项目并添加 Bitnami Helm 仓库 <a href="#create-the-project-and-add-bitnami-helm-repo" id="create-the-project-and-add-bitnami-helm-repo"></a>

```shell
oc new-project $NAMESPACE
```

添加 Bitnami chart 仓库，仅需一次：

```shell
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

#### 安装 PostgreSQL <a href="#install-postgresql" id="install-postgresql"></a>

以下命令中，请将 `YourStrongPassword123` 替换为合适的复杂密码。

```shell
helm install postgresql bitnami/postgresql \
  --namespace $NAMESPACE \
  --set auth.username=n8n \
  --set auth.password='YourStrongPassword123' \
  --set auth.database=n8n_enterprise \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

{% hint style="info" %}
**标志**

`global.compatibility.openshift.adaptSecurityContext=auto` 标志告知 Bitnami，让 OpenShift 自动分配正确用户 ID，避免 SCC 错误。
{% endhint %}

保存端点，集群内服务的端点固定：

```
postgresql.YOUR_NAMESPACE.svc.cluster.local
```

将 `YOUR_NAMESPACE` 替换为实际 `$NAMESPACE` 值，例如 `n8n-20260306`。

#### 安装 Redis <a href="#install-redis" id="install-redis"></a>

```shell
helm install redis bitnami/redis \
  --namespace $NAMESPACE \
  --set auth.enabled=false \
  --set architecture=standalone \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

Redis 端点：`redis-master.$NAMESPACE.svc.cluster.local`

#### 安装 MinIO，兼容 S3 的存储 <a href="#install-minio-s3-compatible-storage" id="install-minio-s3-compatible-storage"></a>

以下命令中，请将 `MinioStrongPassword123` 替换为合适的复杂密码。

```shell
helm install minio bitnami/minio \
  --namespace $NAMESPACE \
  --set auth.rootUser=minioadmin \
  --set auth.rootPassword='MinioStrongPassword123' \
  --set global.compatibility.openshift.adaptSecurityContext=auto \
  --wait
```

MinIO 端点：`http://minio:9000`，在同一命名空间中仅使用服务名称即可。

#### 在 MinIO 中创建 n8n 存储桶 <a href="#create-the-n8n-storage-bucket-in-minio" id="create-the-n8n-storage-bucket-in-minio"></a>

n8n 使用 MinIO 前，需要先创建存储桶。请使用 MinIO Web 控制台：

**打开 MinIO 控制台：**

```shell
oc port-forward svc/minio 9001:9001 -n $NAMESPACE
```

保持命令运行，然后在浏览器打开 `http://localhost:9001`。

使用以下信息登录：
- **用户名：**`minioadmin`
- **密码：**`MinioStrongPassword123`

在控制台中：
1. 点击左侧栏 **Buckets**（存储桶）→ **Create Bucket**（创建存储桶）。
2. **Bucket Name**（存储桶名称）：`n8n-data`
3. 点击 **Create Bucket**（创建存储桶）。

回到终端，按 `Ctrl+C` 停止端口转发。

### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

#### 为 n8n 授予 SCC <a href="#grant-scc-for-n8n" id="grant-scc-for-n8n"></a>

```shell
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n-enterprise
```

确认 `oc get rolebindings -n $NAMESPACE` 显示了 `system:openshift:scc:anyuid` 的绑定。

#### 创建必需 Secret <a href="#create-required-secrets" id="create-required-secrets"></a>

```shell
# Core n8n secrets <a href="#core-n8n-secrets" id="core-n8n-secrets"></a>
oc create secret generic n8n-enterprise-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$(openssl rand -hex 32)" \
  --from-literal=N8N_HOST="localhost" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http"
```

**立即备份加密密钥：**

```shell
oc get secret n8n-enterprise-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode
```

将该值妥善保存。

以下命令中，请将 `YourStrongPassword123` 和 `MinioStrongPassword123` 替换为前面步骤设置的密码。

```shell
# Database password (must match what you set when installing PostgreSQL) <a href="#database-password-must-match-what-you-set-when-installing-postgresql" id="database-password-must-match-what-you-set-when-installing-postgresql"></a>
oc create secret generic n8n-enterprise-db-secret \
  --namespace $NAMESPACE \
  --from-literal=password='YourStrongPassword123'

# MinIO credentials <a href="#minio-credentials" id="minio-credentials"></a>
oc create secret generic n8n-minio-secret \
  --namespace $NAMESPACE \
  --from-literal=root-password='MinioStrongPassword123'
```

#### 创建 values 文件 <a href="#create-values-file" id="create-values-file"></a>

创建 `n8n-multimain-ocp-values.yaml`。替换标为 `# <-- REPLACE` 的 **3 个占位值**：

```shell
nano n8n-multimain-ocp-values.yaml
```

```yaml
# n8n-multimain-ocp-values.yaml <a href="#n8n-multimain-ocp-valuesyaml" id="n8n-multimain-ocp-valuesyaml"></a>
# Multi-instance queue mode for OpenShift Local (CRC). <a href="#multi-instance-queue-mode-for-openshift-local-crc" id="multi-instance-queue-mode-for-openshift-local-crc"></a>
# Uses in-cluster PostgreSQL, Redis, and MinIO instead of AWS services. <a href="#uses-in-cluster-postgresql-redis-and-minio-instead-of-aws-services" id="uses-in-cluster-postgresql-redis-and-minio-instead-of-aws-services"></a>
# Requires Enterprise license. <a href="#requires-enterprise-license" id="requires-enterprise-license"></a>

# --- Enterprise license --- <a href="#enterprise-license" id="enterprise-license"></a>
license:
  enabled: true
  activationKey: "your-enterprise-license-key-here"  # <-- REPLACE

# --- Multi-main: 2 replicas (reduced for local resources) --- <a href="#multi-main-2-replicas-reduced-for-local-resources" id="multi-main-2-replicas-reduced-for-local-resources"></a>
multiMain:
  enabled: true
  replicas: 2

# --- Queue mode: 2 worker pods --- <a href="#queue-mode-2-worker-pods" id="queue-mode-2-worker-pods"></a>
queueMode:
  enabled: true
  workerReplicaCount: 2
  workerConcurrency: 5

# --- Webhook processors --- <a href="#webhook-processors" id="webhook-processors"></a>
webhookProcessor:
  enabled: true
  replicaCount: 1
  disableProductionWebhooksOnMainProcess: true

# --- PostgreSQL (in-cluster) --- <a href="#postgresql-in-cluster" id="postgresql-in-cluster"></a>
database:
  type: postgresdb
  useExternal: true
  host: "postgresql.YOUR_NAMESPACE.svc.cluster.local"   # <-- REPLACE YOUR_NAMESPACE
  port: 5432
  database: n8n_enterprise
  schema: "public"
  user: n8n
  passwordSecret:
    name: "n8n-enterprise-db-secret"
    key: "password"

# --- Redis (in-cluster, no TLS) --- <a href="#redis-in-cluster-no-tls" id="redis-in-cluster-no-tls"></a>
redis:
  enabled: true
  useExternal: true
  host: "redis-master.YOUR_NAMESPACE.svc.cluster.local"  # <-- REPLACE YOUR_NAMESPACE
  port: 6379
  tls: false

# --- MinIO (S3-compatible, in-cluster) --- <a href="#minio-s3-compatible-in-cluster" id="minio-s3-compatible-in-cluster"></a>
s3:
  enabled: true
  bucket:
    name: "n8n-data"
    region: "us-east-1"
  host: "http://minio:9000"
  auth:
    autoDetect: false
    accessKeyId: "minioadmin"
    secretAccessKeySecret:
      name: "n8n-minio-secret"
      key: "root-password"
  storage:
    mode: "s3"
    availableModes: "filesystem,s3"
  forcePathStyle: true

# --- Service account --- <a href="#service-account" id="service-account"></a>
serviceAccount:
  create: true
  name: n8n
```

保存并退出 nano（`Ctrl+O`、`Ctrl+X`）。

**部署前**，将两个 `YOUR_NAMESPACE` 占位符替换为实际命名空间值：

```shell
# Check your namespace value <a href="#check-your-namespace-value" id="check-your-namespace-value"></a>
echo $NAMESPACE

# Replace in the file (this edits it automatically) <a href="#replace-in-the-file-this-edits-it-automatically" id="replace-in-the-file-this-edits-it-automatically"></a>
sed -i "s/YOUR_NAMESPACE/$NAMESPACE/g" n8n-multimain-ocp-values.yaml
```

验证替换结果：

```shell
grep "svc.cluster.local" n8n-multimain-ocp-values.yaml
```

两行都应显示实际命名空间名称，而非 `YOUR_NAMESPACE`。

#### 部署 n8n <a href="#deploy-n8n" id="deploy-n8n"></a>

如果此前未修补 chart，现在请拉取并修补：

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml  # should return nothing
```

从修补后的 chart 安装：

```shell
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-multimain-ocp-values.yaml \
  --wait \
  --timeout 15m
```

#### 创建供外部访问的 Route <a href="#create-a-route-for-external-access" id="create-a-route-for-external-access"></a>

OpenShift 的 **Route** 将服务暴露到外部，等同于 Kubernetes Ingress 或 LoadBalancer，无需额外控制器：

```shell
oc expose svc/n8n-main -n $NAMESPACE
```

获取 URL：

```shell
export ROUTE=$(oc get route n8n-main -n $NAMESPACE -o jsonpath='{.spec.host}')
echo "n8n URL: http://$ROUTE"
```

URL 类似：`http://n8n-main-n8n-20260306.apps-crc.testing`

#### 更新主机 Secret <a href="#update-the-host-secret" id="update-the-host-secret"></a>

n8n 需要知道其公开 URL。请使用 Route 主机名更新 Secret，然后重启 Pod：

```shell
ENCRYPTION_KEY=$(oc get secret n8n-enterprise-secrets -n $NAMESPACE \
  -o jsonpath='{.data.N8N_ENCRYPTION_KEY}' | base64 --decode)

oc create secret generic n8n-enterprise-secrets \
  --namespace $NAMESPACE \
  --from-literal=N8N_ENCRYPTION_KEY="$ENCRYPTION_KEY" \
  --from-literal=N8N_HOST="$ROUTE" \
  --from-literal=N8N_PORT="5678" \
  --from-literal=N8N_PROTOCOL="http" \
  --dry-run=client -o yaml | oc apply -f -

oc rollout restart deployment -n $NAMESPACE
```

等待滚动部署完成：

```shell
oc rollout status deployment/n8n-main -n $NAMESPACE
```

#### 验证所有 Pod 正在运行 <a href="#verify-all-pods-are-running" id="verify-all-pods-are-running"></a>

```shell
oc get pods -n $NAMESPACE
```

预期输出，所有 Pod 均为 `Running`：

```
NAME                                    READY   STATUS    RESTARTS   AGE
n8n-main-xxxx-aaaa                      1/1     Running   0          5m
n8n-main-xxxx-bbbb                      1/1     Running   0          5m
n8n-worker-xxxx-aaaa                    1/1     Running   0          5m
n8n-worker-xxxx-bbbb                    1/1     Running   0          5m
n8n-webhook-processor-xxxx-aaaa         1/1     Running   0          5m
postgresql-0                            1/1     Running   0          15m
redis-master-0                          1/1     Running   0          15m
minio-xxxx-xxxx                         1/1     Running   0          15m
```

在浏览器中打开上方输出的 URL。

**多实例部署完成。**


## 更新 n8n <a href="#updating-n8n" id="updating-n8n"></a>

要更改配置或升级 chart 版本，请拉取新版 chart，重新修补，然后升级：

```shell
# Remove the old local chart copy <a href="#remove-the-old-local-chart-copy" id="remove-the-old-local-chart-copy"></a>
rm -rf ~/n8n/

# Pull and patch the new version <a href="#pull-and-patch-the-new-version" id="pull-and-patch-the-new-version"></a>
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version <new-version> --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Standalone <a href="#standalone" id="standalone"></a>
helm upgrade n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml

# Multi-instance <a href="#multi-instance" id="multi-instance"></a>
helm upgrade n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-multimain-ocp-values.yaml
```

## 停止与恢复 CRC <a href="#stopping-and-resuming-crc" id="stopping-and-resuming-crc"></a>

不同会话之间无需删除 CRC，可以停止后再重启：

```shell
# Stop the cluster (saves state) <a href="#stop-the-cluster-saves-state" id="stop-the-cluster-saves-state"></a>
crc stop

# Start it again later <a href="#start-it-again-later" id="start-it-again-later"></a>
crc start
```

重启后重新运行：

```shell
eval $(crc oc-env)
export NAMESPACE=n8n-YYYYMMDD   # use your original date
oc login -u kubeadmin -p <password> https://api.crc.testing:6443
```

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### `crc setup` 失败，提示“libvirt not found”，找不到 libvirt <a href="#crc-setup-fails-with-libvirt-not-found" id="crc-setup-fails-with-libvirt-not-found"></a>

```shell
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients
sudo systemctl start libvirtd
```

然后重新运行 `crc setup`。


### `crc start` 失败，提示“insufficient memory”，内存不足 <a href="#crc-start-fails-with-insufficient-memory" id="crc-start-fails-with-insufficient-memory"></a>

CRC 至少需要 9 GB 可用 RAM。请关闭其他应用后重试。如果已[按说明配置 CRC 内存](#configure-crc-memory-and-start-the-cluster)，CRC 会使用 14 GB。


### n8n Pod 卡在 `Pending`，或因 SCC 错误始终未创建 <a href="#n8n-pod-stuck-in-pending-or-never-created-scc-error" id="n8n-pod-stuck-in-pending-or-never-created-scc-error"></a>

检查事件中的错误：

```shell
oc get events -n $NAMESPACE --sort-by='.lastTimestamp' | tail -20
```

如果看到 `unable to validate against any security context constraint` 或 `seccomp may not be set`，说明 chart 硬编码的 `seccompProfile: RuntimeDefault` 被拒绝。OpenShift 4.14 及更高版本会将其转换为已弃用的 alpha 注解，即使已授予 `anyuid` SCC，准入仍会拒绝。

**1. 使用显式形式授予 anyuid**，简写 `-z` 可能无提示失败：

```shell
# For standalone <a href="#for-standalone" id="for-standalone"></a>
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n

# For multi-instance <a href="#for-multi-instance" id="for-multi-instance"></a>
oc adm policy add-scc-to-user anyuid \
  system:serviceaccount:$NAMESPACE:n8n-enterprise
```

验证：运行 `oc get rolebindings -n $NAMESPACE`，应看到 `system:openshift:scc:anyuid` 的绑定。

**2. 将 chart 拉取到本地，并移除 `seccompProfile` 行：**

```shell
helm pull oci://ghcr.io/n8n-io/n8n-helm-chart/n8n --version 1.0.3 --untar
sed -i '/seccompProfile:/d; /type: RuntimeDefault/d' ~/n8n/templates/deployment-main.yaml

# Confirm they're gone (should return no output) <a href="#confirm-theyre-gone-should-return-no-output" id="confirm-theyre-gone-should-return-no-output"></a>
grep -n "seccomp\|RuntimeDefault" ~/n8n/templates/deployment-main.yaml
```

**3. 卸载后，从修补过的 chart 重新安装：**

```shell
helm uninstall n8n -n $NAMESPACE
helm install n8n ~/n8n/ \
  --namespace $NAMESPACE \
  --values n8n-standalone-values.yaml \
  --wait \
  --timeout 10m
```

### Route URL 返回“Application not available”，应用不可用 <a href="#route-url-returns-application-not-available" id="route-url-returns-application-not-available"></a>

Pod 可能仍在启动。请检查：

```shell
oc get pods -n $NAMESPACE
oc rollout status deployment/n8n-main -n $NAMESPACE
```

同时确认 Route 已存在：

```shell
oc get route -n $NAMESPACE
```

### n8n Pod 卡在 `Pending`，提示 `Insufficient memory` <a href="#n8n-pod-stuck-in-pending-with-insufficient-memory" id="n8n-pod-stuck-in-pending-with-insufficient-memory"></a>

CRC 节点没有足够的可用内存来调度 Pod。

**解决方法：**增加 CRC 虚拟机内存并重启：

```shell
crc stop
crc config set memory 14336
crc start
```

CRC 重启后，Pod 应自动调度。几分钟后仍处于等待状态时，可删除 Pod，强制重新调度：

```shell
oc delete pod -n $NAMESPACE -l app.kubernetes.io/component=main
```

如果机器无法分配 14 GB，也可以在 `n8n-standalone-values.yaml` 中降低 Pod 的内存请求：

```yaml
resources:
  main:
    requests:
      memory: 256Mi
```

然后升级：`helm upgrade n8n ~/n8n/ -n $NAMESPACE -f n8n-standalone-values.yaml`


### DNS 无法解析 `.apps-crc.testing` 或 `api.crc.testing` <a href="#dns-not-resolving-apps-crctesting-or-apicrctesting" id="dns-not-resolving-apps-crctesting-or-apicrctesting"></a>

Ubuntu 上 CRC 会自动配置 DNS。失败时，请重启 NetworkManager：

```shell
sudo systemctl restart NetworkManager
```

如果仍有问题，手动添加条目，CRC 通过 `127.0.0.1` 路由流量：

```shell
sudo tee -a /etc/hosts <<EOF
127.0.0.1 api.crc.testing
127.0.0.1 console-openshift-console.apps-crc.testing
127.0.0.1 oauth-openshift.apps-crc.testing
127.0.0.1 default-route-openshift-image-registry.apps-crc.testing
EOF
```

{% hint style="info" %}
**子域名**

多实例章节暴露 Route 时，会创建新的 `*.apps-crc.testing` 子域名。如果浏览器无法访问，请在 `/etc/hosts` 中添加条目，指向 `127.0.0.1`。
{% endhint %}


### n8n Pod 因 `EACCES: permission denied` 崩溃，发生于写入 `/home/node/.n8n/` 时 <a href="#n8n-pod-crashes-with-eacces-permission-denied-writing-to-homenoden8n" id="n8n-pod-crashes-with-eacces-permission-denied-writing-to-homenoden8n"></a>

这表示 Pod 以 OpenShift 随机分配的 UID 运行，而非 UID 1000，即 n8n 镜像预期的 `node` 用户。values 中设置 `securityContext.enabled: false`，但未设置 `runAsUser: 1000` 和 `fsGroup: 1000` 时会出现此问题：OpenShift 分配随机 UID，无法写入 PVC。

**解决方法：**确保 values 文件中已设置 `securityContext.enabled: true`，且已修补 chart、移除 `seccompProfile`，参阅上方 SCC 错误章节。两项必须同时满足。


### 查看 Pod 日志 <a href="#view-pod-logs" id="view-pod-logs"></a>

```shell
# Main process <a href="#main-process" id="main-process"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=main --tail=50

# Workers <a href="#workers" id="workers"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=worker --tail=50

# Webhook processors <a href="#webhook-processors" id="webhook-processors"></a>
oc logs -n $NAMESPACE -l app.kubernetes.io/component=webhook-processor --tail=50
```

### 查看命名空间中的所有事件 <a href="#all-events-in-the-namespace" id="all-events-in-the-namespace"></a>

```shell
oc get events -n $NAMESPACE --sort-by='.lastTimestamp'
```

## 速查参考 <a href="#quick-reference" id="quick-reference"></a>

### 重新打开终端后重新导出变量 <a href="#re-export-variables-after-reopening-terminal" id="re-export-variables-after-reopening-terminal"></a>

```shell
eval $(crc oc-env)
export NAMESPACE=n8n-YYYYMMDD   # use the date from your original deployment
oc login -u kubeadmin -p <password> https://api.crc.testing:6443
```

### 检查集群状态 <a href="#check-cluster-status" id="check-cluster-status"></a>

```shell
crc status
```

### 打开 OpenShift Web 控制台 <a href="#open-the-openshift-web-console" id="open-the-openshift-web-console"></a>

```shell
crc console
```

使用 `kubeadmin` 和密码登录，以图形界面查看所有运行内容。

### 需要保存的内容 <a href="#things-to-save" id="things-to-save"></a>

| 项目 | 重要原因 |
| --- | --- |
| `kubeadmin` 密码 | 登录集群。 |
| n8n 加密密钥 | 丢失后，所有已存储凭据都将无法读取。 |
| `n8n-standalone-values.yaml` | `helm upgrade` 所必需。 |
| `n8n-multimain-ocp-values.yaml` | `helm upgrade` 所必需。 |
| MinIO root 密码 | 访问 MinIO 控制台。 |
| PostgreSQL 密码 | 访问数据库。 |

## 后续步骤 <a href="#next-steps" id="next-steps"></a>

{% include "../../../../reusable-content/.gitbook/includes/self-hosting/installation/server-setups-next-steps.md" %}

## 相关资源 <a id="related-resources"></a>

* [使用云提供商](./)
* [DigitalOcean](deploy-to-digital-ocean.md)
* [Heroku](deploy-to-heroku.md)
* [Hetzner Cloud](deploy-to-hetzner.md)
* [AWS](deploy-to-aws.md)
* [Azure](deploy-to-azure.md)
* [Google Cloud Run](deploy-to-google-cloud-run.md)
* [Google Kubernetes Engine](deploy-to-google-kubernetes.md)
* [使用 Docker Compose](use-docker-compose.md)
