from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderer
)
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import (vtkImageViewer2, vtkResliceImageViewer)
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (vtkSliderRepresentation2D, vtkSliderWidget)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage

def main():
  reader = vtkDICOMImageReader()
  reader.SetDirectoryName('./sample-data/Circle of Willis')
  reader.Update()

  viewer1 = vtkResliceImageViewer()
  viewer1.SetSlice(50)
  viewer1.SetInputData(reader.GetOutput())
  viewer1.SetSliceOrientationToXY()
  viewer1.GetRenderer().ResetCamera()
  viewer1.Render()

  # viewer2 = vtkResliceImageViewer()
  # viewer2.SetInputData(reader.GetOutput())
  # viewer2.SetSliceOrientationToXZ()

  # viewer3 = vtkResliceImageViewer()
  # viewer3.SetInputData(reader.GetOutput())
  # viewer3.SetSliceOrientationToYZ()


  # viewer1.GetRenderer().SetViewport(0, 0.5, 0.5, 1)
  # viewer2.GetRenderer().SetViewport(0.5, 0.5, 1, 1)
  # viewer3.GetRenderer().SetViewport(0, 0, 0.5, 0.5) 

  interactor = vtkRenderWindowInteractor()
  interactor.SetRenderWindow(viewer1.GetRenderWindow())

  interactor.Start()

if __name__ == '__main__':
    main()