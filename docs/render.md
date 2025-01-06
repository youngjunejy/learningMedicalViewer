# Render

## Terminology
- window width: 图像中显示的灰度范围
- window level: 灰度范围的中心值

## MPR(Multi Planar Reconstruction)

参考资料：
- MPR-Viewer：https://github.com/MohdFarag/MPR-Viewer.git
  - python实现
- MPRSimpleViewer：https://github.com/rcorredorj/MPRSimpleViewer
  - c++实现
  - 代码结构简单
- https://discourse.vtk.org/t/wrong-mpr-image-orientation-when-using-vtkresliceimageviewer/4158

## VR(Volume Rendering)
体积渲染技术直接从三维数据场中生成图像，不依赖于中间几何图元。光线投影算法是体积渲染中常用的算法，它通过模拟光线穿过三维数据场的过程，计算每个采样点的颜色和不透明度，从而生成高质量的三维图像。

## Surface Rendering
表面渲染技术通过提取医学图像中的表面信息，并使用多边形片来拟合等值面，从而生成三维模型。Marching Cubes算法是表面渲染中常用的经典算法之一，它能够高效地处理离散的三维数据场，生成高质量的三维表面模型。

## SSD(Surface Shadow Display)

## VE(Virtual Endoscopy)