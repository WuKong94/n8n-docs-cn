---
title: 自定义模板库
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->

在环境变量中，将 `N8N_TEMPLATES_HOST` 设为 API 的基础 URL。

### 端点 <a href="#endpoints" id="endpoints"></a>

你的 API 必须提供与 n8n 相同的端点和数据结构。

端点如下：

| 方法 | 路径 | 用途 |
| ------ | ---- | ------- |
| GET | `/templates/workflows/<id>` | 获取模板元数据，用于预览和浏览 |
| GET | `/workflows/templates/<id>` | 获取要导入画布的工作流数据 |
| GET | `/templates/search` | 搜索工作流模板 |
| GET | `/templates/collections/<id>` | 获取指定模板集合 |
| GET | `/templates/collections` | 列出所有模板集合 |
| GET | `/templates/categories` | 列出所有模板类别 |
| GET | `/health` | 健康检查端点 |

{% hint style="warning" %}
**重要：需要两种不同的响应格式**

两个工作流端点要求**不同的响应格式**：

- **`/templates/workflows/{id}`**：返回模板本身，其中的 `workflow` 键包含工作流
- **`/workflows/templates/{id}`**：返回模板包含的工作流

详情请参阅下方的数据结构说明。
{% endhint %}

### 查询参数 <a href="#query-parameters" id="query-parameters"></a>

`/templates/search` 端点接受以下查询参数：

| 参数 | 类型 | 说明 |
|------------|----------------------------------------------|--------------------------------------------------|
| `page` | 整数 | 要返回的结果页码 |
| `rows` | 整数 | 每页最多返回的结果数 |
| `category` | 以逗号分隔的字符串列表（类别） | 要搜索的类别 |
| `search` | 字符串 | 搜索词 |

`/templates/collections` 端点接受以下查询参数：

| 参数 | 类型 | 说明 |
|------------|----------------------------------------------|---------------------------------|
| `category` | 以逗号分隔的字符串列表（类别） | 要搜索的类别 |
| `search` | 字符串 | 搜索词 |

### 数据结构 <a href="#schemas" id="schemas"></a>

两个工作流端点的关键区别如下：

```json
// GET /templates/workflows/{id} returns (wrapped):
{
  "workflow": {
    "id": 123,
    "name": "...",
    "totalViews": 1000,
    // ... see full workflow item schema below
    "workflow": {    // actual workflow definition
      "nodes": [...],
      "connections": {}
    }
  }
}

// GET /workflows/templates/{id} returns (flat):
{
  "id": 123,
  "name": "...",
  "workflow": {      // actual workflow definition
    "nodes": [...],
    "connections": {}
  }
}
```

响应对象的详细数据结构：

<details>

<summary>显示 <code>workflow</code> 条目数据结构</summary>

用于 `/templates/workflows/{id}` 端点（包裹在 `workflow` 键中）。

此结构描述在搜索和浏览界面中展示模板所用的元数据。其中包含一个嵌套的 `workflow` 属性，保存实际可导入的工作流定义。

```json title="工作流条目数据结构"
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "totalViews": {
      "type": "number"
    },
    "price": {},
    "purchaseUrl": {},
    "recentViews": {
      "type": "number"
    },
    "createdAt": {
      "type": "string"
    },
    "user": {
      "type": "object",
      "properties": {
        "username": {
          "type": "string"
        },
        "verified": {
          "type": "boolean"
        }
      },
      "required": [
        "username",
        "verified"
      ]
    },
    "nodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "icon": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "codex": {
            "type": "object",
            "properties": {
              "data": {
                "type": "object",
                "properties": {
                  "details": {
                    "type": "string"
                  },
                  "resources": {
                    "type": "object",
                    "properties": {
                      "generic": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "string"
                            },
                            "icon": {
                              "type": "string"
                            },
                            "label": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "url",
                            "label"
                          ]
                        }
                      },
                      "primaryDocumentation": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "url": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "url"
                          ]
                        }
                      }
                    },
                    "required": [
                      "primaryDocumentation"
                    ]
                  },
                  "categories": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "nodeVersion": {
                    "type": "string"
                  },
                  "codexVersion": {
                    "type": "string"
                  }
                },
                "required": [
                  "categories"
                ]
              }
            }
          },
          "group": {
            "type": "string"
          },
          "defaults": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "color": {
                "type": "string"
              }
            },
            "required": [
              "name"
            ]
          },
          "iconData": {
            "type": "object",
            "properties": {
              "icon": {
                "type": "string"
              },
              "type": {
                "type": "string"
              },
              "fileBuffer": {
                "type": "string"
              }
            },
            "required": [
              "type"
            ]
          },
          "displayName": {
            "type": "string"
          },
          "typeVersion": {
            "type": "number"
          },
          "nodeCategories": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "number"
                },
                "name": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name"
              ]
            }
          }
        },
        "required": [
          "id",
          "icon",
          "name",
          "codex",
          "group",
          "defaults",
          "iconData",
          "displayName",
          "typeVersion"
        ]
      }
    },
    "description": {
      "type": "string"
    },
    "image": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "url": {
            "type": "string"
          }
        }
      }
    },
    "categories": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          }
        }
      }
    },
    "workflowInfo": {
      "type": "object",
      "properties": {
        "nodeCount": {
          "type": "number"
        },
        "nodeTypes": {
          "type": "object"
        }
      }
    },
    "workflow": {
      "type": "object",
      "properties": {
        "nodes": {
          "type": "array"
        },
        "connections": {
          "type": "object"
        },
        "settings": {
          "type": "object"
        },
        "pinData": {
          "type": "object"
        }
      },
      "required": [
        "nodes",
        "connections"
      ]
    }
  },
  "required": [
    "id",
    "name",
    "totalViews",
    "createdAt",
    "user",
    "nodes",
    "workflow"
  ]
}
```

</details>

<details>

<summary>显示 <code>category</code> 条目数据结构</summary>

```json title="类别条目数据结构"
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

</details>

<details>

<summary>显示 <code>collection</code> 条目数据结构</summary>

```json title="集合条目数据结构"
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "rank": {
      "type": "number"
    },
    "name": {
      "type": "string"
    },
    "totalViews": {},
    "createdAt": {
      "type": "string"
    },
    "workflows": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          }
        },
        "required": [
          "id"
        ]
      }
    },
    "nodes": {
      "type": "array",
      "items": {}
    }
  },
  "required": [
    "id",
    "rank",
    "name",
    "totalViews",
    "createdAt",
    "workflows",
    "nodes"
  ]
}
```

</details>

也可以交互式探索 n8n 的 API 端点：

[https://api.n8n.io/templates/categories](https://api.n8n.io/templates/categories)
[https://api.n8n.io/templates/collections](https://api.n8n.io/templates/collections)
[https://api.n8n.io/templates/search](https://api.n8n.io/templates/search)
[https://api.n8n.io/health](https://api.n8n.io/health)


可以[联系我们](mailto:help@n8n.io)获取更多支持。
