---
title: 外部密钥
description: 在 n8n 中使用外部密钥保管库。
contentType: howto
nodeTitle: 使用外部密钥存储
originalFilePath: external-secrets.md
originalUrl: https://docs.n8n.io/external-secrets
url: https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 外部密钥 <a href="#external-secrets" id="external-secrets"></a>

{% hint style="info" %}
**功能可用范围**

外部密钥可用于：

- **n8n Cloud：**Enterprise。
- **自托管：**企业版。
{% endhint %}

n8n 支持以下密钥提供商：1Password，通过 [Connect Server](https://developer.1password.com/docs/connect/get-started/)连接；AWS Secrets Manager、Azure Key Vault、GCP Secrets Manager、HashiCorp Vault 和 Infisical。不支持 [HashiCorp Vault Secrets](https://developer.hashicorp.com/hcp/docs/vault-secrets)。

* 自 n8n 2.10.0 起，每个密钥提供商可以连接多个保管库。旧版每个提供商仅支持一个保管库。
* 自 n8n 2.13.0 起，启用相应设置后，项目编辑者可在项目内使用外部密钥，项目管理员还可管理项目保管库。

外部密钥存储中的凭据，仅在凭据字段中解析，其他支持表达式的字段不能解析。

可以使用外部密钥存储管理 n8n 的凭据[^1]。

n8n 将所有凭据加密存储在数据库中，并默认限制访问。外部密钥功能允许将敏感凭据信息存入外部保管库，在需要时由 n8n 加载，提供额外安全层，也能集中管理多个 [n8n 环境](../use-source-control-and-environments/README.md)使用的凭据。

## 全局保管库 <a href="#global-vaults" id="global-vaults"></a>

密钥保管库默认为**全局**：整个实例的用户都可使用引用该保管库密钥的凭据。

在个人项目中，只有实例所有者和管理员可以在凭据中使用全局保管库的密钥。

## 项目保管库 <a href="#project-vaults" id="project-vaults"></a>

实例管理员可以将保管库共享给特定[项目](../manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md)。分配给项目后，只有该项目的凭据可以引用其中密钥。可以选择绑定到单个项目，或保留全局范围。

要更改保管库范围：

1. 在 n8n 中前往 **Settings**（设置）> **External Secrets**（外部密钥）。
1. 找到要配置的保管库，选择 **Edit**（编辑）。
1. 在 **Share**（共享）下选择以下之一：
    - **Global**（全局）：在整个 n8n 实例中共享，允许实例各处的凭据引用这些密钥。
    - **Project**（项目）：限制到特定项目，仅该项目的凭据可访问密钥。
1. **Save**（保存）配置。

## 将 n8n 连接到密钥存储 <a href="#connect-n8n-to-your-secrets-store" id="connect-n8n-to-your-secrets-store"></a>

{% hint style="info" %}
**密钥值**

n8n 仅支持明文形式的密钥值，不支持 JSON 对象。
{% endhint %}

1. 在 n8n 中前往 **Settings**（设置）> **External Secrets**（外部密钥）。
1. 点击 **Add secrets vault**（添加密钥保管库）。
1. 为保管库输入唯一名称。之后在凭据中通过 `{{ $secrets.<vault-name>... }}` 表达式引用此保管库时，名称将作为第一段。
1. 选择受支持的密钥提供商。
1. 输入提供商凭据，详情请参阅下方各提供商章节。
1. **Save**（保存）配置。

只要此存储保持连接，就可以在凭据中引用其密钥。

### 1Password <a href="#1password" id="1password"></a>

{% hint style="info" %}
**需要 1Password Connect Server**

n8n 与 [1Password Connect Server](https://developer.1password.com/docs/connect/get-started/) 集成，这是供机器访问 1Password 的自托管 API，不等同于个人或团队 1Password 账号。使用此提供商必须部署并运行 Connect Server。
{% endhint %}

填写 **Connect Server URL** 和 **Access Token**（访问令牌）。URL 是可访问服务器的地址，例如 `http://localhost:8080`。访问令牌是为 Connect Server 集成创建的令牌。

n8n 读取令牌可访问的全部保管库和条目。每个 1Password 条目成为一个密钥，其字段可作为属性访问。使用 `{{ $secrets.<vault-name>.<item-title>.<field-label> }}` 访问指定字段值。

### AWS Secrets Manager <a href="#aws-secrets-manager" id="aws-secrets-manager"></a>

选择身份验证方式：
* **IAM User**（IAM 用户）：填写 IAM 用户的 **access key ID**（访问密钥 ID）、**secret access key**（秘密访问密钥）和 **region**（区域）。
* **Auto Detect**（自动检测）：n8n 使用 AWS SDK 默认凭据提供程序链，从运行环境自动获取凭据，例如环境变量、共享凭据文件，或 EC2/ECS/EKS 实例角色。适合已提供 AWS 凭据的环境，无需管理长期访问密钥。

无论选择哪种方式，底层 IAM 身份都必须具有 `secretsmanager:ListSecrets`、`secretsmanager:BatchGetSecretValue` 和 `secretsmanager:GetSecretValue` 权限。

{% hint style="warning"%}
**Auto Detect 与自动检测时的密钥作用域**

n8n 不为此保管库接收任何凭据输入，而是解析运行环境中的可用身份。因此，同一 n8n 实例上所有配置为 Auto Detect 的保管库，共享同一个 IAM 身份和同一组权限。无法给不同 Auto Detect 保管库分配不同 IAM 作用域，例如让一个仅访问某项目密钥，另一个仅访问其他项目密钥。

如果需要按保管库、项目或团队限定密钥访问，请改用 IAM User：为每个保管库创建独立 IAM 用户和访问密钥，并附加按 ARN 限定的策略，参阅下方限制性 ARN 策略示例。Auto Detect 最适合单个全局保管库，或共享该保管库的所有项目都应具有相同 AWS 访问权限的配置。
{% endhint %}

要让 n8n 访问 AWS Secrets Manager 中的全部密钥，可以向 IAM 用户附加以下策略：

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AccessAllSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:ListSecrets",
				"secretsmanager:BatchGetSecretValue",
				"secretsmanager:GetResourcePolicy",
				"secretsmanager:GetSecretValue",
				"secretsmanager:DescribeSecret",
				"secretsmanager:ListSecretVersionIds"
			],
			"Resource": "*"
		}
	]
}
```

也可以进一步限制，仅授予 n8n 访问指定 AWS Secrets Manager 密钥的权限。仍需允许 `secretsmanager:ListSecrets` 和 `secretsmanager:BatchGetSecretValue` 访问全部资源。这些权限让 n8n 能检索按 ARN 限定的密钥，但不提供密钥值访问权限。

接下来，将 `secretsmanager:GetSecretValue` 权限的范围设为希望与 n8n 共享的密钥的具体 Amazon Resource Name（ARN）。每个资源 ARN 都应使用正确的区域和账号 ID，可在 AWS 密钥控制台中查找 ARN 详情。

例如，以下 IAM 策略仅允许访问指定 AWS 账号和区域中，名称以 `n8n` 开头的密钥：

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "ListingSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:ListSecrets",
				"secretsmanager:BatchGetSecretValue"
			],
			"Resource": "*"
		},
		{
			"Sid": "RetrievingSecrets",
			"Effect": "Allow",
			"Action": [
				"secretsmanager:GetSecretValue",
				"secretsmanager:DescribeSecret"
			],
			"Resource": [
				"arn:aws:secretsmanager:us-west-2:123456789000:secret:n8n*"
			]
		}
	]
}
```

更多 IAM 权限策略示例，请参阅 [AWS 文档](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_iam-policies.html#auth-and-access_examples_batch)。

### Azure Key Vault <a href="#azure-key-vault" id="azure-key-vault"></a>

{% hint style="info" %}
**功能可用范围**

**Azure Cloud** 设置自 n8n 2.35.0 起提供。更早版本仅连接 Azure Public Cloud，现有配置无需更改，继续使用 Azure Public Cloud。
{% endhint %}

填写 **tenant ID**（租户 ID）、**client ID**（客户端 ID）和 **client secret**（客户端密钥）。如何[注册 Microsoft Entra ID 应用并创建服务主体](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)，请参阅 Azure 文档。n8n 仅支持单行密钥值。

选择托管 Key Vault 的 **Azure Cloud** 环境，此选项设置保管库 URL 和 Microsoft Entra 身份验证主机：

| Azure Cloud | 保管库 URL 后缀 | Entra 身份验证主机 |
|-------------|------------------|----------------------|
| **Azure Public Cloud**（默认） | `vault.azure.net` | `https://login.microsoftonline.com` |
| **Azure US Government** | `vault.usgovcloudapi.net` | `https://login.microsoftonline.us` |
| **Azure China** | `vault.azure.cn` | `https://login.partner.microsoftonline.cn` |
| **Custom**（自定义） | 由你提供完整 URL | 由你提供主机 |

对于 **Azure Public Cloud**、**Azure US Government** 和 **Azure China**，填写 **Vault Name**（保管库名称）。n8n 根据名称和所选云环境的后缀构建保管库 URL。

对于 **Custom**，请提供完整 **Vault URL**（保管库 URL），例如 `https://my-vault.vault.usgovcloudapi.net`，而非保管库名称。还可设置可选的 **Authority Host**（身份验证主机），例如 `https://login.microsoftonline.us`，使用其他 Microsoft Entra 身份验证机构。留空时使用默认值（`https://login.microsoftonline.com`）。Azure Stack 或代理环境等场景可使用 Custom。

### GCP Secrets Manager <a href="#gcp-secrets-manager" id="gcp-secrets-manager"></a>

提供服务账号的 **Service Account Key**（服务账号密钥，JSON）。账号至少应具有 `Secret Manager Secret Accessor` 和 `Secret Manager Secret Viewer` 角色。更多信息请参阅 Google 的[服务账号文档](https://cloud.google.com/iam/docs/service-account-overview)。

### HashiCorp Vault <a href="#hashicorp-vault" id="hashicorp-vault"></a>

填写保管库实例的 **Vault URL**，选择 **Authentication Method**（身份验证方式），输入身份验证信息，也可按需提供命名空间。

- 请参阅 HashiCorp 对应身份验证方式的文档：
	- [Token 身份验证方式](https://developer.hashicorp.com/vault/docs/auth/token)。
	- [AppRole 身份验证方式](https://developer.hashicorp.com/vault/docs/auth/approle)。
	- [Userpass 身份验证方式](https://developer.hashicorp.com/vault/docs/auth/userpass)。
- 使用 Vault 命名空间时，可以输入 n8n 应连接的命名空间。更多信息请参阅 [Vault Enterprise 命名空间](https://developer.hashicorp.com/vault/docs/enterprise/namespaces)。

#### 手动配置 KV 挂载 <a href="#manual-kv-mount-configuration" id="manual-kv-mount-configuration"></a>

默认情况下，n8n 通过读取 `sys/mounts` 自动发现 KV 密钥引擎。如果 Vault 令牌无权访问 `sys/mounts`，可以改为手动指定 KV 引擎挂载路径和版本：

- **KV Mount Path**（KV 挂载路径）：KV 密钥引擎的挂载路径，例如 `secret/`。设置后，n8n 跳过 `sys/mounts` 自动发现，直接使用此路径。留空时使用自动发现。
- **KV Version**（KV 版本）：KV 引擎版本，`v1` 或 `v2`，默认为 `v2`。仅在指定 **KV Mount Path** 时生效。

Vault 令牌仍需拥有 KV 路径本身的读取和列表权限。以下是在 `secret/` 挂载 KV v2 时的最小 Vault 策略示例：

```hcl
# Read and list secrets at the "secret/" KV v2 mount <a href="#read-and-list-secrets-at-the-secret-kv-v2-mount" id="read-and-list-secrets-at-the-secret-kv-v2-mount"></a>
path "secret/data/*" {
  capabilities = ["read"]
}
path "secret/metadata/*" {
  capabilities = ["read", "list"]
}
```

对于 KV v1，仅需单个策略路径：

```hcl
# Read and list secrets at the "kv/" KV v1 mount <a href="#read-and-list-secrets-at-the-kv-kv-v1-mount" id="read-and-list-secrets-at-the-kv-kv-v1-mount"></a>
path "kv/*" {
  capabilities = ["read", "list"]
}
```

### Infisical <a href="#infisical" id="infisical"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.26.0 起支持 Infisical 密钥管理。
{% endhint %}


连接 Infisical 需要提供：

- **Site URL**（站点 URL）：Infisical 实例的基础 URL，默认为 `https://app.infisical.com`，仅在自托管 Infisical 时更改。
- **Project ID**（项目 ID）：要读取密钥的 Infisical 项目 ID。
- **Environment**（环境）：环境标识，例如 `dev`、`staging` 或 `prod`。
- **Secret Path**（密钥路径）：项目内读取密钥的路径，默认为 `/`。
- **Authentication Method**（身份验证方式）：选择 **Universal Auth**（通用身份验证，推荐）或 **Access Token**（访问令牌）。

n8n 推荐使用基于 Infisical [Machine Identity](https://infisical.com/docs/documentation/platform/identities/machine-identities)（机器身份）的 Universal Auth，令牌会在过期前自动刷新。

在 Infisical 中，为 Machine Identity 授予能读取目标项目密钥的角色。内置 **Viewer**（查看者）角色可用，也可创建自定义角色，对目标环境和密钥路径授予 `secrets` 的 **Read Value**（读取值）和 **Describe Secret**（描述密钥）权限。参阅 Infisical 的[项目角色文档](https://infisical.com/docs/documentation/platform/access-controls/role-based-access-controls)。

{% tabs %}
{% tab title="Universal Auth（通用身份验证）" %}
提供：

- **Client ID**（客户端 ID）：机器身份的客户端 ID。
- **Client Secret**（客户端密钥）：机器身份的客户端密钥。

在 Infisical 创建机器身份，使用上述角色将其加入项目，再复制客户端 ID 和密钥。参阅 Infisical 的 [Universal Auth 文档](https://infisical.com/docs/documentation/platform/identities/universal-auth)。
{% endtab %}

{% tab title="Access Token（访问令牌）" %}
提供：

- **Access Token**（访问令牌）：在机器身份内签发的令牌。

在 Infisical 创建机器身份，使用上述角色将其加入项目，再点击 `Add Auth Method`，选择 `Token Auth`。参阅 Infisical 的 [Token 身份验证文档](https://infisical.com/docs/documentation/platform/identities/token-auth)。
{% endtab %}
{% endtabs %}

## 在 n8n 凭据中使用密钥 <a href="#use-secrets-in-n8n-credentials" id="use-secrets-in-n8n-credentials"></a>

要在 n8n 凭据中使用密钥存储中的密钥：

1. 创建新凭据，或打开现有凭据。
1. 在希望使用密钥的字段中：
	1. 将鼠标悬停在字段上。
	1. 选择 **Expression**（表达式）。
1. 在希望使用密钥的字段中，输入引用密钥名称的表达式[^2]：
	```js
	{{ $secrets.<vault-name>.<secret-name> }}
	```
	`<vault-name>` 是添加存储时输入的名称。将 `<secret-name>` 替换为保管库中显示的密钥名称。

## 在 n8n 环境中使用外部密钥 <a href="#using-external-secrets-with-n8n-environments" id="using-external-secrets-with-n8n-environments"></a>

n8n 的[源代码管理与环境](../use-source-control-and-environments/README.md)功能允许创建基于 Git 的不同 n8n 环境，但不支持在不同实例中使用不同凭据。可以让各 n8n 实例连接不同保管库或项目环境，通过外部密钥保管库为不同环境提供不同凭据。

例如，有开发和生产两个 n8n 实例。在密钥提供商中创建包含开发、生产两个环境的项目，为各环境生成令牌。使用开发环境令牌连接开发 n8n 实例，使用生产环境令牌连接生产 n8n 实例。

## 在项目中使用外部密钥 <a href="#using-external-secrets-in-projects" id="using-external-secrets-in-projects"></a>

可以将保管库共享给项目，使只有该项目的凭据能引用其密钥。设置步骤请参阅[项目保管库](#project-vaults)。项目级保管库自 n8n 2.11.0 起提供。

### 项目角色的访问权限 <a href="#access-for-project-roles" id="access-for-project-roles"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.13.0 起，可以授予项目编辑者和管理员外部密钥访问权限。在此之前，在 [RBAC 项目](../manage-users-and-access/set-permissions-and-roles-rbac/README.md)中使用外部密钥，要求[实例所有者或实例管理员](../manage-users-and-access/understand-instance-roles.md)是项目成员。
{% endhint %}

自 n8n 2.13.0 起，实例所有者和管理员可以向[项目编辑者](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md#project-editor)和[项目管理员](../manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md#project-admin)授予外部密钥访问权限。

要启用：

1. 前往 **Settings**（设置）> **External Secrets**（外部密钥）。
1. 打开 **Enable external secrets for project roles**（为项目角色启用外部密钥）。

启用后，**Project Editors**（项目编辑者）可以：

-   查看共享给项目的可用外部密钥保管库，位于 **Project**（项目）> **Settings**（设置）。
-   在凭据中使用项目保管库的密钥。

**Project Admins**（项目管理员）还可在相同访问权限基础上：

-   在 **Project**（项目）> **Settings**（设置）中为项目创建新保管库。
-   更新和删除分配给项目的保管库。

{% hint style="info" %}
**全局保管库访问**

在 **Settings**（设置）> **External Secrets**（外部密钥）中创建的全局保管库，会显示在 **Project**（项目）> **Settings**（设置）中，但项目角色仅能只读访问。只有实例管理员可修改或删除全局保管库。
{% endhint %}

### 自定义角色 <a href="#custom-roles" id="custom-roles"></a>

要更细致地控制访问，实例所有者和管理员可以创建[自定义项目角色](../manage-users-and-access/set-permissions-and-roles-rbac/create-custom-project-roles.md)。前往 **Settings**（设置）> **Roles**（角色）> **Project roles**（项目角色）> **Create role**（创建角色），在权限列表中配置：

- **Secrets vaults**（密钥保管库）：控制保管库管理，包括查看、创建、编辑、删除和同步。
- **Secrets**（密钥）：控制角色能否在凭据表达式中使用密钥。

两项权限相互独立。例如，一个角色可能仅需要 **Secrets** 权限，在凭据中使用密钥，而无需管理保管库。完整可用范围列表请参阅[密钥保管库范围](../manage-users-and-access/set-permissions-and-roles-rbac/create-custom-project-roles.md#secret-vault-scopes)。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### 密钥在生产环境中无法解析 <a href="#secrets-dont-resolve-in-production" id="secrets-dont-resolve-in-production"></a>

{% hint style="info" %}
**功能可用范围**

自 n8n 2.13.0 起，[已启用密钥访问](#access-for-project-roles)的项目编辑者或管理员，可以在自己的凭据中使用外部密钥。以下限制仅适用于旧版本或未启用相应开关的情况。
{% endhint %}

在早于 n8n 2.13.0 的版本中，或 **Enable external secrets for project roles** 关闭时，只有实例所有者和管理员能在运行时解析密钥。如果所有者或管理员将其他用户的凭据更新为密钥表达式，预览中可能有效，但生产中可能失败。

此时，仅在实例所有者或管理员拥有的凭据中使用外部密钥。

保护和共享凭据的其他方式，请参阅[管理凭据](README.md)。

[^1]: 在 n8n 中，凭据保存连接特定应用和服务所需的身份验证信息。使用用户名和密码、API 密钥、OAuth 密钥等信息创建凭据后，就可以通过相应应用节点与服务交互。
[^2]: 在 n8n 中，表达式通过执行 JavaScript 代码，动态填充节点参数。无需提供静态值，可以使用 n8n 表达式语法，根据前序节点、其他工作流或 n8n 环境中的数据定义参数值。

## 相关资源 <a id="related-resources"></a>

* [管理凭据](./)
* [安全共享凭据](share-credentials-securely.md)
* [最终用户凭据](end-user-credentials.md)
* [凭据覆盖](credential-overwrites.md)
