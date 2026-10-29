---
title: Edit Image（编辑图片）
contentType:
- integration
- reference
priority: medium
nodeTitle: Edit Image（编辑图片）
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.editimage.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage
description: 了解 n8n 工作流自动化平台中的 Edit Image 节点，包括用法说明和示例链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---
<!-- 简体中文翻译；来源 n8n-io/n8n-docs；原文版本见 upstream.json。 -->


# Edit Image（编辑图片） <a id="edit-image"></a>

使用 Edit Image 节点处理和编辑图片。

{% hint style="info" %}
**依赖项**

1. 如果不是通过 Docker 运行 n8n，需要安装 [GraphicsMagick](http://www.graphicsmagick.org/README.html)。
2. 需要使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md)（读写磁盘文件）或 [HTTP Request](n8n-nodes-base.httprequest/README.md)（HTTP 请求）等节点，将图片文件作为数据属性传入 Edit Image 节点。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Blur**（模糊）：降低图片的清晰度。
* **Border**（边框）：为图片添加边框。
* **Composite**（合成）：将一张图片叠加到另一张图片上。
* **Create**（创建）：创建新图片。
* **Crop**（裁剪）：裁剪图片。
* **Draw**（绘制）：在图片上绘图。
* **Get Information**（获取信息）：获取图片信息。
* **Multi Step**（多步骤）：对图片执行多个操作。
* **Resize**（调整大小）：更改图片尺寸。
* **Rotate**（旋转）：旋转图片。
* **Shear**（错切）：沿 X 轴或 Y 轴对图片进行错切。
* **Text**（文本）：在图片上添加文本。
* **Transparent**（透明）：将图片中的某种颜色设为透明。

## 节点参数 <a href="#node-parameters" id="node-parameters"></a>

此节点的参数取决于所选操作。

### Blur（模糊）参数 <a href="#blur-parameters" id="blur-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Blur**（模糊）：输入 0 到 1000 之间的数值，设置模糊强度。值越大，图片越模糊。
* **Sigma**：输入 0 到 1000 之间的数值，设置模糊的 sigma 值。值越大，图片越模糊。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Border（边框）参数 <a href="#border-parameters" id="border-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Border Width**（边框宽度）：输入边框宽度。
* **Border Height**（边框高度）：输入边框高度。
* **Border Color**（边框颜色）：输入十六进制颜色值，或选择色块打开颜色选择器。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Composite（合成）参数 <a href="#composite-parameters" id="composite-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称，这张图片用作底图。
* **Composite Image Property**（叠加图片属性）：输入存放叠加图片的二进制属性名称，该图片将叠加到 **Property Name**（属性名称）指定的图片上。
* **Operator**（运算符）：选择决定合成方式的合成运算符，可选：
  * **Add**
  * **Atop**
  * **Bumpmap**
  * **Copy**
  * **Copy Black**
  * **Copy Blue**
  * **Copy Cyan**
  * **Copy Green**
  * **Copy Magenta**
  * **Copy Opacity**
  * **Copy Red**
  * **Copy Yellow**
  * **Difference**
  * **Divide**
  * **In**
  * **Minus**
  * **Multiply**
  * **Out**
  * **Over**
  * **Plus**
  * **Subtract**
  * **Xor**
* **Position X**（X 坐标）：输入叠加图片在 x 轴上的位置（水平方向）。
* **Position Y**（Y 坐标）：输入叠加图片在 y 轴上的位置（垂直方向）。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Create（创建）参数 <a href="#create-parameters" id="create-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Background Color**（背景色）：设置图片背景色。可以输入十六进制颜色值，或选择色块打开颜色选择器。
* **Image Width**（图片宽度）：输入图片宽度。
* **Image Height**（图片高度）：输入图片高度。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Crop（裁剪）参数 <a href="#crop-parameters" id="crop-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Width**（宽度）：输入裁剪后的目标宽度。
* **Height**（高度）：输入裁剪后的目标高度。
* **Position X**（X 坐标）：输入裁剪起点在 x 轴上的位置（水平方向）。
* **Position Y**（Y 坐标）：输入裁剪起点在 y 轴上的位置（垂直方向）。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Draw（绘制）参数 <a href="#draw-parameters" id="draw-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Primitive**（图形）：选择要绘制的基本图形，可选：
  * **Circle**（圆）
  * **Line**（线）
  * **Rectangle**（矩形）
* **Color**（颜色）：设置图形颜色。可以输入十六进制颜色值，或选择色块打开颜色选择器。
* **Start Position X**（起点 X 坐标）：输入开始绘制的位置，沿 x 轴（水平方向）。
* **Start Position Y**（起点 Y 坐标）：输入开始绘制的位置，沿 y 轴（垂直方向）。
* **End Position X**（终点 X 坐标）：输入结束绘制的位置，沿 x 轴（水平方向）。
* **End Position Y**（终点 Y 坐标）：输入结束绘制的位置，沿 y 轴（垂直方向）。
* **Corner Radius**（圆角半径）：输入圆角半径数值。设置后，绘制的图形将具有圆角。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Get Information（获取信息）参数 <a href="#get-information-parameters" id="get-information-parameters"></a>

此操作只需填写存放图片数据的二进制属性的 **Property Name**（属性名称）。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Multi Step（多步骤）参数 <a href="#multi-step-parameters" id="multi-step-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Operations**（操作）：添加多步骤操作中要执行的操作，可使用其他任意操作。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Resize（调整大小）参数 <a href="#resize-parameters" id="resize-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Width**（宽度）：输入图片的新宽度。
* **Height**（高度）：输入图片的新高度。
* **Option**（选项）：选择调整图片大小的方式，可选：
  * **Ignore Aspect Ratio**（忽略宽高比）：忽略原始宽高比，精确调整到输入的高度和宽度。
  * **Maximum Area**（最大区域）：输入的高度和宽度是图片允许的最大尺寸。保持图片宽高比，且不超过输入的高度和／或宽度。
  * **Minimum Area**（最小区域）：输入的高度和宽度是图片要求的最小尺寸。保持图片宽高比，且不小于输入的高度和／或宽度。
  * **Only if Larger**（仅当原图较大时）：仅在图片大于输入宽度和高度时调整大小，并保持宽高比。
  * **Only if Smaller**（仅当原图较小时）：仅在图片小于输入宽度和高度时调整大小，并保持宽高比。
  * **Percent**（百分比）：将宽度和高度视为原图尺寸的百分比来调整大小。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Rotate（旋转）参数 <a href="#rotate-parameters" id="rotate-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Rotate**（旋转）：输入旋转角度，范围为 -360 到 360 度。
* **Background Color**（背景色）：输入十六进制颜色值，或选择色块打开颜色选择器。当图片以非 90 度整数倍的角度旋转时，此颜色用于填充产生的空白区域。若 **Rotate**（旋转）为 90 度的整数倍，则不使用此背景色。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Shear（错切）参数 <a href="#shear-parameters" id="shear-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Degrees X**（X 轴角度）：输入沿 x 轴错切的角度。
* **Degrees Y**（Y 轴角度）：输入沿 y 轴错切的角度。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Text（文本）参数 <a href="#text-parameters" id="text-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Text**（文本）：输入要写在图片上的文本。
* **Font Size**（字号）：选择文本字号。
* **Font Color**（字体颜色）：输入十六进制颜色值，或选择色块打开颜色选择器。
* **Position X**（X 坐标）：输入文本起点在 x 轴上的位置（水平方向）。
* **Position Y**（Y 坐标）：输入文本起点在 y 轴上的位置（垂直方向）。
* **Max Line Length**（最大行长度）：输入每行在换行之前允许的最大字符数。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

### Transparent（透明）参数 <a href="#transparent-parameters" id="transparent-parameters"></a>

* **Property Name**（属性名称）：输入存放图片数据的二进制属性名称。
* **Color**（颜色）：设置要变为透明的颜色。可以输入十六进制颜色值，或选择色块打开颜色选择器。

可选配置请参阅[节点选项](n8n-nodes-base.editimage.md#node-options)。

## 节点选项 <a href="#node-options" id="node-options"></a>

* **File Name**（文件名称）：输入输出文件的名称。
* **Format**（格式）：输入输出文件的图片格式，可选：
  * **bmp**
  * **gif**
  * **jpeg**
  * **png**
  * **tiff**
  * **WebP**

**Text**（文本）操作还包含 **Font Name or ID**（字体名称或 ID）选项。可从下拉列表选择字体，或通过[表达式](../../../build/work-with-data/expressions-versus-data-nodes.md)指定 ID。

## 模板与示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Edit Image 集成模板](https://n8n.io/integrations/edit-image)，或[搜索所有模板](https://n8n.io/workflows/)
