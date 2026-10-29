---
title: 评估
description: 使用 n8n 评估功能构建可靠的 AI 工作流。通过比较已知测试用例的输出，增强对 LLM 驱动工作流的信心。
contentType: overview
nodeTitle: 理解为什么要测试
originalFilePath: advanced-ai/evaluations/overview.md
originalUrl: https://docs.n8n.io/advanced-ai/evaluations/overview
url: https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test
layout:
  description:
    visible: false
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# 概览 <a href="#overview" id="overview"></a>


## 什么是评估？ <a href="#what-are-evaluations" id="what-are-evaluations"></a>

评估是检查 AI 工作流可靠性的关键手段，可能决定工作流是一个不稳定的概念验证，还是可稳健运行的生产流程。构建阶段和部署到生产环境后，都需要评估。

评估的基础是让工作流处理测试数据集。数据集包含多个测试用例，每个用例都包含工作流的示例输入，通常也包含预期输出。

评估可以帮助你：

* **使用多种输入测试工作流**，了解其在边界情况中的表现。
* **放心修改**，避免无意间影响其他部分。
* **比较不同模型或提示词的表现**。

以下视频介绍了什么是评估、为什么有用，以及其工作方式：

{% embed url="https://www.youtube.com/embed/5LlF196PKaE" %}


## 为什么需要评估？ <a href="#why-is-evaluation-needed" id="why-is-evaluation-needed"></a>

AI 模型与代码有本质区别。代码具有确定性，可以分析其行为；LLM 则像黑盒，很难用同样的方式推断。因此，需要输入数据、观察输出，从而*衡量* LLM 的表现。

只有使用能准确反映生产环境各类边界情况的多组输入运行模型后，才能对模型的可靠性建立信心。

## 两种评估方式 <a href="#two-types-of-evaluation" id="two-types-of-evaluation"></a>

### 轻量评估（部署前） <a href="#light-evaluation-pre-deployment" id="light-evaluation-pre-deployment"></a>

构建干净、全面的数据集很难。在早期构建阶段，通常只需生成少量示例，就足以迭代工作流，使其达到可发布或概念验证的状态。可以直接查看和比较结果，了解工作流质量，无需设置正式指标。

### 基于指标的评估（部署后） <a href="#metric-based-evaluation-post-deployment" id="metric-based-evaluation-post-deployment"></a>

部署工作流后，可以更容易地从生产执行中构建更大、更有代表性的数据集。发现问题时，将触发问题的输入加入数据集。修复后，应让工作流重新处理整个数据集，进行[回归测试](https://en.wikipedia.org/wiki/Regression_testing)，检查修复是否无意间影响了其他部分。

测试用例过多时，难以逐一检查。评估通过指标衡量输出质量，指标是表示某项特征的数值，也便于跟踪不同运行之间的质量变化。

### 评估方式对比 <a href="#comparison-of-evaluation-types" id="comparison-of-evaluation-types"></a>

| | 轻量评估（部署前） | 基于指标的评估（部署后） |
|-----------------------------------------------------|-----------------------------------------|------------------------------------------------|
| **每次迭代的<br>性能提升** | 较大 | 较小 |
| **数据集规模** | 较小 | 较大 |
| **数据集来源** | 手工生成<br>AI 生成<br>其他 | 生产执行<br>AI 生成<br>其他 |
| **实际输出** | 必需 | 必需 |
| **预期输出** | 可选 | 通常必需 |
| **评估指标** | 可选 | 必需 |

## 了解更多 <a href="#learn-more" id="learn-more"></a>

* [轻量评估](run-quick-evaluations.md)：适合在开发过程中，使用人工挑选的测试用例评估 AI 工作流。
* [基于指标的评估](use-metrics-to-measure-quality.md)：通过对大型数据集评分和计算指标，在生产环境中保持性能和正确性。
* [技巧与常见问题](fix-common-issues.md)：了解如何设置特定评估场景，以及如何解决常见问题。

## 相关资源 <a id="related-resources"></a>

* [测试和改进 AI 工作流](./)
* [运行快速评估](run-quick-evaluations.md)
* [使用指标衡量质量](use-metrics-to-measure-quality.md)
* [解决常见问题](fix-common-issues.md)
