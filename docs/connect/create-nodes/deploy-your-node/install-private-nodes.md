---
contentType: howto
nodeTitle: 安装私有节点
originalFilePath: integrations/creating-nodes/deploy/install-private-nodes.md
originalUrl: https://docs.n8n.io/integrations/creating-nodes/deploy/install-private-nodes
url: https://docs.n8n.io/connect/create-nodes/deploy-your-node/install-private-nodes
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 安装私有节点 <a href="#install-private-nodes" id="install-private-nodes"></a>

可以自行构建节点，安装到 n8n 实例中，而不发布到 npm，适合仅供公司内部使用的节点。

## 在 Docker n8n 实例中安装节点 <a href="#install-your-node-in-a-docker-n8n-instance" id="install-your-node-in-a-docker-n8n-instance"></a>

使用 Docker 运行 n8n 时，需要创建一个已在 n8n 中安装节点的 Docker 镜像。

1. 创建 Dockerfile，粘贴[此 Dockerfile](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile)中的代码。

	Dockerfile 应如下所示：

	```Dockerfile
	FROM node:16-alpine

	ARG N8N_VERSION

	RUN if [ -z "$N8N_VERSION" ] ; then echo "The N8N_VERSION argument is missing!" ; exit 1; fi

	# Update everything and install needed dependencies
	RUN apk add --update graphicsmagick tzdata git tini su-exec

	# Set a custom user to not have n8n run as root
	USER root

	# Install n8n and the packages it needs to build it correctly.
	RUN apk --update add --virtual build-dependencies python3 build-base ca-certificates && \
		npm config set python "$(which python3)" && \
		npm_config_user=root npm install -g full-icu n8n@${N8N_VERSION} && \
		apk del build-dependencies \
		&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root;


	# Install fonts
	RUN apk --no-cache add --virtual fonts msttcorefonts-installer fontconfig && \
		update-ms-fonts && \
		fc-cache -f && \
		apk del fonts && \
		find  /usr/share/fonts/truetype/msttcorefonts/ -type l -exec unlink {} \; \
		&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root

	ENV NODE_ICU_DATA /usr/local/lib/node_modules/full-icu

	WORKDIR /data

	COPY docker-entrypoint.sh /docker-entrypoint.sh
	ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]

	EXPOSE 5678/tcp
	```

2. 编译自定义节点代码，使用节点入门项目时运行 `npm run build`。将 **dist** 中的 **node** 和 **credential** 目录复制到容器的 `~/.n8n/custom/` 目录，使 Docker 能够使用它们。

3. 下载 [docker-entrypoint.sh](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/docker-entrypoint.sh) 文件，与 Dockerfile 放在同一目录。

4. 构建 Docker 镜像：

	```Dockerfile
	# Replace <n8n-version-number> with the n8n release version number. 
	# For example, N8N_VERSION=0.177.0
	docker build --build-arg N8N_VERSION=<n8n-version-number> --tag=customizedn8n .
	```

现在可在 Docker 中使用节点。

## 在全局安装的 n8n 实例中安装节点 <a href="#install-your-node-in-a-global-n8n-instance" id="install-your-node-in-a-global-n8n-instance"></a>

如果全局安装了 n8n，请确保在 n8n 内部安装节点，n8n 会找到模块并自动加载。

## 相关资源 <a id="related-resources"></a>

* [部署节点](./)
* [提交社区节点](submit-community-nodes.md)
