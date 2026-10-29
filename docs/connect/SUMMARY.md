<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

# 目录 <a id="table-of-contents"></a>

* [连接](README.md)
* [n8n API](n8n-api/README.md)
  * [身份验证](n8n-api/authentication.md)
  * [分页](n8n-api/pagination.md)
  * [幂等性](n8n-api/idempotency.md)
  * [使用 API 调试平台](n8n-api/use-an-api-playground.md)
  * [端点参考](n8n-api/api-reference.md)
  * ```yaml
    props:
      models: true
      downloadLink: true
      grouping: by-tag
    type: builtin:openapi
    dependencies:
      spec:
        ref:
          kind: openapi
          spec: n8n
    ```
* [n8n CLI](n8n-cli.md)
* [连接 n8n MCP 服务器](connect-to-n8n-mcp-server.md)
  * [MCP 客户端连接示例](connect-to-n8n-mcp-server/mcp-client-examples.md)
  * [MCP 服务器工具参考](connect-to-n8n-mcp-server/mcp-server-tools-reference.md)
* [连接 n8n 文档 MCP 服务器](connect-to-n8n-docs-mcp-server.md)
* [创建节点](create-nodes/README.md)
  * [概述](create-nodes/overview.md)
  * [规划节点](create-nodes/plan-your-node/README.md)
    * [选择节点类型](create-nodes/plan-your-node/choose-a-node-type.md)
    * [选择节点构建方式](create-nodes/plan-your-node/choose-a-node-building-style.md)
    * [节点界面设计](create-nodes/plan-your-node/node-ui-design.md)
    * [选择节点文件结构](create-nodes/plan-your-node/choose-node-file-structure.md)
  * [构建节点](create-nodes/build-your-node/README.md)
    * [设置开发环境](create-nodes/build-your-node/set-up-your-development-environment.md)
    * [使用 n8n-node 工具](create-nodes/build-your-node/using-the-n8n-node-tool.md)
    * [教程：构建声明式节点](create-nodes/build-your-node/tutorial-build-a-declarative-style-node.md)
    * [教程：构建编程式节点](create-nodes/build-your-node/tutorial-build-a-programmatic-style-node.md)
    * [参考](create-nodes/build-your-node/reference/README.md)
      * [节点界面元素](create-nodes/build-your-node/reference/node-ui-elements.md)
      * [代码标准](create-nodes/build-your-node/reference/code-standards.md)
      * [错误处理](create-nodes/build-your-node/reference/error-handling.md)
      * [版本控制](create-nodes/build-your-node/reference/versioning.md)
      * [基础文件](create-nodes/build-your-node/reference/base-files/README.md)
        * [结构](create-nodes/build-your-node/reference/base-files/structure.md)
        * [标准参数](create-nodes/build-your-node/reference/base-files/standard-parameters.md)
        * [声明式参数](create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md)
        * [编程式参数](create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md)
        * [编程式 execute 方法](create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md)
      * [codex 文件](create-nodes/build-your-node/reference/codex-files.md)
      * [凭据文件](create-nodes/build-your-node/reference/credentials-files.md)
      * [HTTP 请求辅助方法](create-nodes/build-your-node/reference/http-request-helpers.md)
      * [数据项关联](create-nodes/build-your-node/reference/item-linking.md)
      * [用户体验指南](create-nodes/build-your-node/reference/ux-guidelines.md)
      * [验证指南](create-nodes/build-your-node/reference/verification-guidelines.md)
  * [测试节点](create-nodes/test-your-node/README.md)
    * [在本地运行节点](create-nodes/test-your-node/run-your-node-locally.md)
    * [节点 linter](create-nodes/test-your-node/node-linter.md)
    * [故障排查](create-nodes/test-your-node/troubleshooting.md)
  * [部署节点](create-nodes/deploy-your-node/README.md)
    * [提交社区节点](create-nodes/deploy-your-node/submit-community-nodes.md)
    * [安装私有节点](create-nodes/deploy-your-node/install-private-nodes.md)
