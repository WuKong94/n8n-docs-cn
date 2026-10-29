---
title: AWS 凭据
description: AWS 凭据文档。使用这些凭据在工作流自动化平台 n8n 中完成 AWS 的身份验证。
contentType:
- integration
- reference
priority: medium
nodeTitle: AWS 凭据
originalFilePath: integrations/builtin/credentials/aws.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/aws
url: https://docs.n8n.io/integrations/builtin/credentials/aws
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# AWS 凭据 <a href="#aws-credentials" id="aws-credentials"></a>

n8n 为 AWS 提供两种凭据类型：

* **AWS (IAM)**：使用访问密钥进行身份验证，包括 Access Key ID（访问密钥 ID）和 Secret Access Key（私有访问密钥）。
* **AWS (Assume Role)**：通过 AWS STS 代入 IAM 角色来进行身份验证。n8n 调用 `AssumeRole` 所用的凭据可手动填写，也可从 n8n 的运行环境中自动读取。

如果在 AWS 基础设施（EKS、ECS 或 EC2）上自托管 n8n，并希望避免在 n8n 中存储静态密钥，请参阅[使用 AWS 系统凭据](#using-aws-system-credentials-federated-authentication)。

## AWS (IAM) 凭据 <a href="#aws-iam-credentials" id="aws-iam-credentials"></a>

这些凭据可用于以下节点的身份验证：

- [AWS Bedrock Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
- [AWS Certificate Manager](../app-nodes/n8n-nodes-base.awscertificatemanager.md)
- [AWS Cognito](../app-nodes/n8n-nodes-base.awscognito.md)
- [AWS Comprehend](../app-nodes/n8n-nodes-base.awscomprehend.md)
- [AWS DynamoDB](../app-nodes/n8n-nodes-base.awsdynamodb.md)
- [AWS Elastic Load Balancing](../app-nodes/n8n-nodes-base.awselb.md)
- [AWS IAM](../app-nodes/n8n-nodes-base.awsiam.md)
- [AWS Lambda](../app-nodes/n8n-nodes-base.awslambda.md)
- [AWS Rekognition](../app-nodes/n8n-nodes-base.awsrekognition.md)
- [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)
- [AWS SES](../app-nodes/n8n-nodes-base.awsses.md)
- [AWS SNS](../app-nodes/n8n-nodes-base.awssns.md)
- [AWS SNS Trigger（触发器）](../trigger-nodes/n8n-nodes-base.awssnstrigger.md)
- [AWS SQS](../app-nodes/n8n-nodes-base.awssqs.md)
- [AWS Textract](../app-nodes/n8n-nodes-base.awstextract.md)
- [AWS Transcribe](../app-nodes/n8n-nodes-base.awstranscribe.md)
- [Embeddings AWS Bedrock（向量嵌入）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)

### 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API 访问密钥

### 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [AWS Identity and Access Management 文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)。

### 使用 API 访问密钥 <a href="#using-api-access-key" id="using-api-access-key"></a>

配置此凭据需要一个 [AWS](https://aws.amazon.com/) 账号，以及：

- AWS **Region**（区域）
- **Access Key ID**（访问密钥 ID）：创建访问密钥时生成。
- **Secret Access Key**（私有访问密钥）：创建访问密钥时生成。

创建访问密钥并设置凭据的步骤如下：

1. 在 n8n 凭据中选择 AWS **Region**（区域）。
1. 登录 [IAM 控制台](https://console.aws.amazon.com/iam)。
2. 在右上角的导航栏选择用户名，再选择 **Security credentials**（安全凭据）。
3. 在 **Access keys**（访问密钥）部分选择 **Create access key**（创建访问密钥）。
4. 在 **Access key best practices & alternatives page**（访问密钥最佳实践与替代方案页面）中选择使用场景。如果未提示创建访问密钥，请选择 **Other**（其他）。
5. 选择 **Next**（下一步）。
6. 为访问密钥设置 **description**（描述）标签值，便于识别，例如 `n8n integration`。
7. 选择 **Create access key**（创建访问密钥）。
8. 显示 **Access Key ID**（访问密钥 ID）和 **Secret Access Key**（私有访问密钥），将它们填入 n8n。
10. 如需使用 **Temporary security credential**（临时安全凭据），开启此选项并添加 **Session token**（会话令牌）。临时安全凭据的更多用法，请参阅 [AWS 临时安全凭据文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)。
11. 如果使用 [Amazon Virtual Private Cloud（VPC）](https://aws.amazon.com/vpc/) 托管 n8n，可以在 VPC 与部分应用之间建立连接。使用 **Custom Endpoints**（自定义端点）填写此连接所需的相关自定义端点。此设置适用于以下应用：
    - Rekognition
    - Lambda
    - SNS
    - SES
    - SQS
    - S3
    - SSM
    - Bedrock

    Bedrock 有两个端点字段：**Bedrock Endpoint**（Bedrock 端点）用于列出可用模型；**Bedrock Runtime Endpoint**（Bedrock 运行时端点）供 [AWS Bedrock Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md) 和 [Embeddings AWS Bedrock](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md) 节点执行推理。如果通过未启用私有 DNS 的 [VPC 接口端点（PrivateLink）](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html) 路由 Bedrock 流量，请同时设置这两个字段。

也可通过 AWS CLI 和 AWS API 生成访问密钥。使用这些方式生成访问密钥的说明，请参阅 [AWS 访问密钥管理文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)。

## AWS (Assume Role) 凭据 <a href="#aws-assume-role-credentials" id="aws-assume-role-credentials"></a>

这些凭据可通过代入 IAM 角色增强安全性，并用于以下节点的身份验证：

* [AWS Bedrock Chat Model（聊天模型）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
* [AWS Certificate Manager](../app-nodes/n8n-nodes-base.awscertificatemanager.md)
* [AWS Cognito](../app-nodes/n8n-nodes-base.awscognito.md)
* [AWS Comprehend](../app-nodes/n8n-nodes-base.awscomprehend.md)
* [AWS DynamoDB](../app-nodes/n8n-nodes-base.awsdynamodb.md)
* [AWS Elastic Load Balancing](../app-nodes/n8n-nodes-base.awselb.md)
* [AWS IAM](../app-nodes/n8n-nodes-base.awsiam.md)
* [AWS Lambda](../app-nodes/n8n-nodes-base.awslambda.md)
* [AWS Rekognition](../app-nodes/n8n-nodes-base.awsrekognition.md)
* [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)
* [AWS SES](../app-nodes/n8n-nodes-base.awsses.md)
* [AWS SNS](../app-nodes/n8n-nodes-base.awssns.md)
* [AWS SNS Trigger（触发器）](../trigger-nodes/n8n-nodes-base.awssnstrigger.md)
* [AWS SQS](../app-nodes/n8n-nodes-base.awssqs.md)
* [AWS Textract](../app-nodes/n8n-nodes-base.awstextract.md)
* [AWS Transcribe](../app-nodes/n8n-nodes-base.awstranscribe.md)
* [Embeddings AWS Bedrock（向量嵌入）](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)

### 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* 角色代入

### 相关资源 <a href="#related-resources" id="related-resources"></a>

有关角色代入的更多信息，请参阅 [AWS IAM 角色文档](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)和 [STS AssumeRole 文档](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)。

### 了解 AWS 角色代入 <a href="#understanding-aws-role-assumption" id="understanding-aws-role-assumption"></a>

AWS 角色代入允许通过临时代入 IAM 角色来安全访问 AWS 资源，无需使用长期访问密钥。这符合 AWS 的安全最佳实践，并支持：

* **跨账户访问：**访问不同 AWS 账户中的资源
* **增强安全性：**使用会自动过期的临时凭据
* **最小权限原则：**仅授予特定任务所需的权限
* **审计记录：**更好地追踪谁访问了哪些资源

n8n 使用官方 AWS SDK 调用 STS `AssumeRole`。在为节点请求签名时，它会请求新的临时凭据，因此无需自行管理凭据过期。这与 AWS (IAM) 凭据中的 **Temporary security credential**（临时安全凭据）选项不同：后者需要填入静态会话令牌，n8n 无法续期；该令牌过期后，必须填写新令牌。

### 设置 AWS Assume Role 凭据 <a href="#setting-up-aws-assume-role-credentials" id="setting-up-aws-assume-role-credentials"></a>

配置此凭据需要：

#### 必填参数 <a href="#required-parameters" id="required-parameters"></a>

* **Region**（区域）：调用 STS 服务以代入角色的 AWS 区域。n8n 会调用此区域的 STS 区域端点，也支持 AWS China（`cn-*`）和 AWS GovCloud（`us-gov-*`）分区（从 n8n 2.29.0 起可用）。
* **Role ARN**（角色 ARN）：要代入的 IAM 角色的 Amazon Resource Name（ARN，Amazon 资源名称），格式为 `arn:aws:iam::123456789012:role/MyRole`。此角色必须具有允许你的凭据代入该角色的信任策略。
* **External ID**（外部 ID）：角色信任策略要求的唯一标识符，用于防止“混淆代理”问题。应自行生成秘密值，并在角色信任策略和此凭据中配置。请将此值视为敏感信息，不要与不受信任的其他 n8n 用户共享。
* **Role Session Name**（角色会话名称）：代入角色会话的名称，用于审计。默认值为 `n8n-session`。此值会出现在 AWS CloudTrail 日志中，便于识别会话。

#### STS 凭据（选择一种方式） <a href="#sts-credentials-choose-one-method" id="sts-credentials-choose-one-method"></a>

提供用于调用 STS AssumeRole 的凭据有两种方式：

##### 方式 1：使用系统凭据（推荐用于服务器部署） <a href="#option-1-use-system-credentials-recommended-for-server-deployments" id="option-1-use-system-credentials-recommended-for-server-deployments"></a>

如果 n8n 服务器的运行环境已具有 AWS 身份，请开启 **Use System Credentials**（使用系统凭据）。n8n 将自动发现调用 `AssumeRole` 所需的凭据，无需在 n8n 中存储静态密钥。n8n 按以下顺序尝试来源，使用第一个返回凭据的来源：

1. 环境变量（`AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY`，以及可选的 `AWS_SESSION_TOKEN`）
2. EKS IAM Roles for Service Accounts（IRSA，服务账户 IAM 角色）
3. EKS Pod Identity（Pod 身份）
4. ECS 或 Fargate 任务角色
5. EC2 实例配置文件

此选项要求 n8n 管理员将环境变量 `N8N_AWS_SYSTEM_CREDENTIALS_ACCESS_ENABLED` 设为 `true`，以启用系统凭据访问。设置详情和安全注意事项，请参阅[使用 AWS 系统凭据](#using-aws-system-credentials-federated-authentication)。

##### 方式 2：手动填写 STS 凭据 <a href="#option-2-manual-sts-credentials" id="option-2-manual-sts-credentials"></a>

如果系统凭据不可用，请手动填写以下内容：

* **STS Access Key ID**（STS 访问密钥 ID）：有权代入目标角色的 IAM 用户或角色的访问密钥 ID。
* **STS Secret Access Key**（STS 私有访问密钥）：与 STS Access Key ID 对应的私有访问密钥。
* **STS Session Token**（STS 会话令牌，可选）：调用 STS 时使用临时凭据所需的会话令牌。

#### 可选参数 <a href="#optional-parameters" id="optional-parameters"></a>

* **Custom Endpoints**（自定义端点）：使用 Amazon VPC 时，可为 AWS 服务指定自定义端点：

    * Rekognition Endpoint（Rekognition 端点）
    * Lambda Endpoint（Lambda 端点）
    * SNS Endpoint（SNS 端点）
    * SES Endpoint（SES 端点）
    * SQS Endpoint（SQS 端点）
    * S3 Endpoint（S3 端点）
    * SSM Endpoint（SSM 端点）
    * Bedrock Endpoint（Bedrock 端点，用于列出可用模型）
    * Bedrock Runtime Endpoint（Bedrock 运行时端点，用于 Bedrock 推理，例如通过 [VPC 接口端点（PrivateLink）](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html)）

### 设置步骤 <a href="#setup-steps" id="setup-steps"></a>

1. 在目标 AWS 账户中创建 IAM 角色。此信任策略适用于**方式 2：手动填写 STS 凭据**。如果使用**方式 1：使用系统凭据**，`Principal` 应为 n8n 自身运行时使用的角色。请参阅[系统凭据的信任策略](#trust-policy-for-system-credentials)。

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::SOURCE-ACCOUNT:root"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "sts:ExternalId": "your-unique-external-id"
           }
         }
       }
     ]
   }
   
   ```
2. 在 n8n 中配置凭据。
   * 选择 AWS **Region**（区域）
   * 输入所创建角色的 **Role ARN**（角色 ARN）
   * 设置唯一的 **External ID**（外部 ID，与信任策略中的值相同）
   * 选择 **STS credentials method**（STS 凭据方式）
   * 输入 **Role Session Name**（角色会话名称），或使用默认值
3. 使用内置测试功能**测试凭据**，验证角色代入是否正常工作。

### 安全最佳实践 <a href="#security-best-practices" id="security-best-practices"></a>

* 为每个凭据使用唯一的 External ID，防止未经授权的访问。
* 轮换用于角色代入的 STS 凭据。
* 对执行代入的凭据和目标角色均应用最小权限原则。
* 在共享实例上保持系统凭据访问关闭。请参阅[使用 AWS 系统凭据](#using-aws-system-credentials-federated-authentication)。

## 使用 AWS 系统凭据（联合身份验证） <a id="using-aws-system-credentials-federated-authentication"></a>

本节适用于自托管 n8n 实例的管理员。

{% hint style="info" %}
系统凭据访问仅适用于自托管 n8n，n8n Cloud 不提供此功能。
{% endhint %}

n8n 在 AWS 基础设施上运行时，基础设施本身即可提供 AWS 身份，无需创建、存储或轮换访问密钥。这是在 EKS、ECS 和 EC2 上对工作负载进行身份验证的标准方式，安全团队也经常要求采用这种方式（“零静态密钥”）。

n8n 使用官方 AWS SDK 凭据提供程序读取这些**系统凭据**。开启 **Use System Credentials**（使用系统凭据）时，将其用作 **AWS (Assume Role)** 凭据执行角色代入的初始凭据。此方式适用于所有接受 AWS (Assume Role) 凭据的节点，包括 AWS Bedrock AI 节点。

{% hint style="info" %}
系统凭据始终是角色代入的起点，n8n 不会直接使用此身份调用 AWS。仍然必须填写 **Role ARN**（角色 ARN），且该角色必须信任 n8n 运行时所用的身份。

如果 n8n 当前使用的角色已经具备工作流所需的权限，请填写该角色自身的 ARN，并允许其代入自身。请参阅[系统凭据的信任策略](#trust-policy-for-system-credentials)。
{% endhint %}

### 启用访问 <a id="enabling-access"></a>

系统凭据访问**默认关闭**。要启用此功能，请在每个 n8n 实例（主实例和工作节点）上设置以下环境变量：

```bash
N8N_AWS_SYSTEM_CREDENTIALS_ACCESS_ENABLED=true
```

{% hint style="warning" %}
启用后，任何能够创建 AWS (Assume Role) 凭据的 n8n 用户，都可以使用服务器自身的 AWS 身份作为角色代入的起点。仅在单租户自托管实例上启用，并确保信任所有能够创建凭据的用户。

要限制工作流通过服务器身份执行的操作，请尽量减少服务器自身的 IAM 权限。理想情况下，仅对工作流应使用的特定角色授予 `sts:AssumeRole` 权限，并为每个角色设置 External ID 保护。
{% endhint %}

### 支持的凭据来源 <a id="supported-credential-sources"></a>

n8n 按以下顺序尝试来源，使用第一个返回凭据的来源：

| 顺序 | 来源 | n8n 如何检测 | 典型平台 |
|---|---|---|---|
| 1 | 环境变量 | `AWS_ACCESS_KEY_ID` 和 `AWS_SECRET_ACCESS_KEY`（以及可选的 `AWS_SESSION_TOKEN`） | 任意平台 |
| 2 | EKS IAM Roles for Service Accounts（IRSA，服务账户 IAM 角色） | `AWS_ROLE_ARN` 和 `AWS_WEB_IDENTITY_TOKEN_FILE` | Amazon EKS |
| 3 | EKS Pod Identity（Pod 身份） | `AWS_CONTAINER_CREDENTIALS_FULL_URI` | Amazon EKS |
| 4 | ECS 或 Fargate 任务角色 | `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` | Amazon ECS / Fargate |
| 5 | EC2 实例配置文件 | EC2 实例元数据服务（IMDSv2） | Amazon EC2 |

请注意以下事项：

* 配置相应平台功能后，AWS 会自动注入来源 2 至 4 所需的检测变量，无需自行设置。
* 如果在容器中设置了 `AWS_ACCESS_KEY_ID` 和 `AWS_SECRET_ACCESS_KEY`，它们将优先于 IRSA、Pod Identity 和实例角色。如需使用联合身份凭据来源，请移除这两个变量。
* n8n 会在需要时解析系统凭据，因此能够自动获取已轮换或短期有效的源凭据，例如 Kubernetes 轮换的 IRSA 令牌。
* 有意不支持从 `~/.aws`（`AWS_PROFILE`）读取 AWS CLI 配置档案。

#### 使用 IRSA 的 Amazon EKS <a id="amazon-eks-with-irsa"></a>

[IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) 将 IAM 角色关联到运行 n8n 的 Kubernetes 服务账户。用角色 ARN（`eks.amazonaws.com/role-arn`）为服务账户添加注解。随后 EKS 会将 `AWS_ROLE_ARN` 和 `AWS_WEB_IDENTITY_TOKEN_FILE` 注入 Pod，n8n 通过 STS 区域端点交换令牌。

#### 使用 Pod Identity 的 Amazon EKS <a id="amazon-eks-with-pod-identity"></a>

[EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) 是比 IRSA 更新的替代方案。安装 Pod Identity Agent 插件，并在 n8n 服务账户与 IAM 角色之间创建 Pod 身份关联，无需设置 OIDC 提供商。

#### Amazon ECS 和 Fargate <a id="amazon-ecs-and-fargate"></a>

为 n8n 任务定义分配一个[任务角色](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)。

#### Amazon EC2 <a id="amazon-ec2"></a>

为运行 n8n 的实例附加[实例配置文件](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)。n8n 使用 IMDSv2，因此可在已禁用 IMDSv1 的实例上工作。

### 系统凭据的信任策略 <a id="trust-policy-for-system-credentials"></a>

填入 **Role ARN**（角色 ARN）的角色必须信任 n8n 运行时所用的身份：IRSA 角色、Pod Identity 角色、ECS 任务角色或 EC2 实例角色。请将该角色的 ARN 用作 `Principal`，不要使用账户根主体。

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/n8n-service-account-role"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "your-unique-external-id"
        }
      }
    }
  ]
}
```

要找到用作 `Principal` 的 ARN，请在 n8n 容器或实例内部运行 `aws sts get-caller-identity`。

如果 n8n 运行时所用的角色已经具备工作流所需的权限，请将该角色设为 **Role ARN**（角色 ARN），并按照上文所示，将其自身 ARN 添加到信任策略。即使角色代入自身，AWS 也要求这样设置。

n8n 运行时所用的角色还需要对目标角色拥有 `sts:AssumeRole` 权限。请仅对工作流应使用的特定角色授予此权限，不要授予 `*`。

### AWS China 和 GovCloud <a id="aws-china-and-govcloud"></a>

{% hint style="info" %}
**从 n8n 2.29.0 起可用**。早期版本的 n8n 会调用 STS 全局端点，导致 IRSA 在 AWS China 和 GovCloud 分区中失败。
{% endhint %}

系统凭据和角色代入适用于所有 AWS 分区。n8n 根据凭据的区域调用 STS 区域端点：`sts.{region}.amazonaws.com.cn` 用于 AWS China（`cn-*`），`sts.us-gov-{east,west}-1.amazonaws.com` 用于 AWS GovCloud（`us-gov-*`）。

### 代理行为 <a id="proxy-behavior"></a>

如果实例使用 HTTP(S) 代理（`HTTPS_PROXY`、`HTTP_PROXY`、`NO_PROXY`），n8n 会通过代理发送 STS 调用，包括 Web 身份令牌交换和 `AssumeRole`。对链路本地元数据服务（EC2 IMDS、ECS 和 Pod Identity 端点）的请求始终直接发送，不经过代理。这些地址仅能从主机自身访问。

### 相关环境变量 <a id="related-environment-variables"></a>

| 变量 | 默认值 | 用途 |
|---|---|---|
| `N8N_AWS_SYSTEM_CREDENTIALS_ACCESS_ENABLED` | `false` | 允许 AWS (Assume Role) 凭据的 **Use System Credentials**（使用系统凭据）选项读取服务器的 AWS 身份。 |
| `N8N_AWS_SYSTEM_CREDENTIALS_SDK_SOURCES` | `all` | 过渡性变量，从 n8n 2.29.0 起可用。控制哪些系统凭据来源通过 AWS SDK 解析，而非 n8n 的旧版解析器。接受 `all`、`none`，或由 `environment`、`roleForServiceAccount`、`podIdentity`、`containerMetadata`、`instanceMetadata` 组成的逗号分隔子集。仅在升级后 AWS 身份验证出现故障时更改。n8n 将在未来版本移除此标志。 |
| `N8N_AWS_LEGACY_SIGNER` | `false` | 过渡性变量，从 n8n 2.30.0 起可用。设为 `true` 时，使用旧版 `aws4` 签名器为 AWS 请求签名，代替 AWS 的 Signature V4 实现。仅在升级后 AWS 请求失败时用于回退。n8n 将在未来版本移除此标志。 |

### 故障排查 <a id="troubleshooting"></a>

* **"Access to AWS system credentials disabled, contact your administrator."**（AWS 系统凭据访问已禁用，请联系管理员）：**Use System Credentials**（使用系统凭据）已开启，但服务器上的 `N8N_AWS_SYSTEM_CREDENTIALS_ACCESS_ENABLED` 未设为 `true`。
* **使用了错误的身份**：环境变量优先于 IRSA，IRSA 优先于 Pod Identity、ECS 和 EC2。最常见原因是容器中遗留了 `AWS_ACCESS_KEY_ID`。请参阅[支持的凭据来源](#supported-credential-sources)。
* **在 EKS 上测试凭据失败**：检查服务账户注解（IRSA）或 Pod 身份关联，并确认 Pod 已收到注入的环境变量（`kubectl exec <pod-name> -- env | grep AWS`）。
* **`AccessDenied` 错误（调用 `sts:AssumeRole` 时）**：n8n 已找到系统凭据，但目标角色拒绝接受。请检查角色信任策略是否指定了 n8n 运行时所用的身份，以及 **External ID**（外部 ID）是否与策略条件一致。请参阅[系统凭据的信任策略](#trust-policy-for-system-credentials)。
