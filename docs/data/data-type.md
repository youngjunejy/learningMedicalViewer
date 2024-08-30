# 常用数据类型

## 体数据（Volume Data）

### NIFTI

### NRRD(N-dimensional Recursively Navigable Data)
- 一种用于表示和处理 N 维栅格数据的工具，它提供了一种有效且通用的方式来处理科学和医学图像。
- 包含一个单个的数据头文件和既能分开又能合并的图像文件，能够准确地表示 N 维度的栅格信息。

### MHD & ZRAW
"MHD ZRAW" 是一种常见的医学图像数据格式，通常用于存储和处理医学图像数据。具体来说，MHD文件是元数据文件，包含有关数据集的信息，例如数据的大小、数据类型和数据的维度。ZRAW文件则是原始数据文件，包含数据集的实际像素值。

## 模型数据（Model Data）
- STL
- OBJ

## 场景数据

存储应用状态

## QA

Q：体数据和模型数据的区别？
A：体数据是一种三维数据，它描述了空间中连续体特征。它包含体细节，即不仅有表面信息，还有内部结构信息。模型数据则是一种抽象的数据结构，用于描述现实世界中的对象或系统，模型数据可以是矢量数据或栅格数据。

Q: NRRD vs NIFTI
A: https://discourse.slicer.org/t/nrrd-vs-nifti-which-one-to-choose/7799/2