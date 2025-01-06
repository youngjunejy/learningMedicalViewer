# VTK

## Interactor

VTK（Visualization Toolkit）中的vtkRenderWindowInteractor是一个用于实现用户与可视化场景交互的关键组件。它负责处理鼠标、键盘和时间相关的事件，并通过VTK的观察者/命令模式将这些事件转换为VTK事件，从而实现与渲染窗口的交互。

具体来说，vtkRenderWindowInteractor的工作流程如下：
1. 事件捕获：当用户在渲染窗口上进行操作（如点击鼠标或按下键盘键）时，vtkRenderWindowInteractor会捕获这些事件。
2. 事件转换：捕获到的事件会被传递给vtkRenderWindowInteractor，然后通过InvokeEvent()方法将其转换为VTK事件。
3. 事件分发：转换后的事件会被分发给注册了该事件的观察者（如vtkInteractorObserver及其子类），这些观察者可以对事件做出响应。
4. 交互风格：vtkRenderWindowInteractor还支持不同的交互风格（如vtkInteractorStyleTrackballCamera），这些风格定义了如何响应用户的交互操作，例如缩放、旋转和移动相机。

在实际应用中，通常需要创建一个vtkRenderWindowInteractor实例，并将其与渲染窗口关联。然后通过调用Initialize()和Start()方法来启动事件循环，从而开始处理用户的交互操作

## Mapper
VTK（Visualization Toolkit）中的Mapper类是一个抽象类，用于将数据集映射到图形系统中进行可视化。Mapper类在VTK的渲染管线中扮演着至关重要的角色，它负责将输入的数据转换为几何图元（如点、线、面等），以便进行渲染和展示。

Mapper类的主要功能包括：

数据映射：将数据集的属性（如颜色、透明度、纹理等）映射到图形原语上，从而实现数据的可视化表达。
空间变换：将数据的坐标（如世界坐标、模型坐标、纹理坐标等）映射到图形系统中，实现数据的空间变换。
结构表示：将数据的拓扑结构（如点、线、面、体等）映射到图形系统中，实现数据的结构表示。
Mapper类有多个子类，根据不同的数据类型和渲染方式，可以分为以下几类：

vtkPolyDataMapper：用于将多边形数据（vtkPolyData）映射到图形原语，是最常用的映射器类，适用于各种几何数据的可视化。
vtkDataSetMapper：用于将任意类型的数据集（vtkDataSet）映射到图形原语。
vtkVolumeMapper：用于体绘制，包括光线投射法和纹理映射法等多种体绘制技术。
Mapper类还提供了多种参数来控制渲染行为，例如：

ScalarVisibility：控制标量数据是否影响Actor的颜色。
ScalarMode：控制Actor的颜色是基于标量点还是单元的值。
ImmediateModeRendering：控制渲染方式，可以选择立即渲染或将其放入渲染列表中。

## Actor
VTK中的vtkActor是用于表示可视化场景中的对象，通常是一个几何体或图形原语，并且具有多种渲染属性。这些属性包括颜色、透明度、光照效果、纹理映射等，通过这些属性可以实现对对象的详细控制和渲染效果的调整
。

vtkActor的主要功能包括：

几何映射：通过mapper将数据集映射到几何形状上，例如使用vtkPolyDataMapper将点云数据映射为三维模型。
属性设置：通过vtkProperty对象设置对象的颜色、透明度、反射光强度等属性。例如，可以使用GetProperty()方法获取或设置属性对象，并通过该对象调整颜色、不透明度等。
位置与变换：vtkActor可以设置位置、缩放和旋转参数，以实现空间变换和定位。
渲染控制：vtkActor与渲染器（vtkRenderer）配合工作，通过相机（vtkCamera）和灯光（vtkLight）来控制对象的显示效果