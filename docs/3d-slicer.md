# 3D Slicer

- MRML: Medical Reality Markup Language
- vtkMRMLSliceViewDisplayableManager: 管理视图的渲染和交互
- 3D Slicer为什么不适用LPS坐标系？ -> 从历史背景来看，当Slicer在2000年代初期开始开发时，RAS（右侧、前侧、上侧）坐标系已经被GE设备广泛使用，而Siemens等其他公司则使用LPS（左侧、后侧、上侧）坐标系。由于早期的Slicer开发者中有许多来自GE的研究人员，因此选择了RAS作为内部表示的坐标系。

## vtkMRMLSliceNode