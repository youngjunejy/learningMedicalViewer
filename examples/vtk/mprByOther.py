from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderer
)
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkInteractionImage import (vtkImageViewer2, vtkResliceImageViewer)
from vtkmodules.vtkRenderingCore import vtkRenderWindowInteractor
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkInteractionWidgets import (vtkSliderRepresentation2D, vtkSliderWidget)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleImage

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

# class MouseWheelInteractorStyle(vtkInteractorStyleImage):
#     def __init__(self, viewer):
#       self.viewer = viewer

#     def OnMouseWheelForward(self):
#       current_slice = self.viewer.GetSlice()
#       if current_slice < self.viewer.GetNumberOfSlices() - 1:
#           self.viewer.SetSlice(current_slice + 1)
#           self.viewer.Render()

#     def OnMouseWheelBackward(self):
#       current_slice = self.viewer.GetSlice()
#       if current_slice > 0:
#           self.viewer.SetSlice(current_slice - 1)
#           self.viewer.Render()

def createMPRViewer(orientation, reader, renWin):
  colors = vtkNamedColors()

  imageViewer = vtkResliceImageViewer()
  imageViewer.SetInputData(reader.GetOutput())
  
  imageViewer.SetRenderWindow(renWin)
  imageViewer.SetupInteractor(renWin.GetInteractor())
  
  renderer = vtkRenderer()
  if orientation == 'axial':
    renderer.SetViewport(0, 0.5, 0.5, 1)
    renderer.SetBackground(colors.GetColor3d('Red'))
    imageViewer.SetSliceOrientationToXY()
      
  elif orientation == 'coronal':
    renderer.SetViewport(0, 0, 0.5, 0.5)
    renderer.SetBackground(colors.GetColor3d('Green'))
    imageViewer.SetSliceOrientationToYZ()
      
  elif orientation == 'sagittal':
    renderer.SetViewport(0.5, 0, 1, 0.5)
    renderer.SetBackground(colors.GetColor3d('Yellow'))
    imageViewer.SetSliceOrientationToXZ()

  imageViewer.Render()
  imageViewer.SetRenderer(renderer)
  renWin.AddRenderer(renderer)
  return imageViewer

def main(argv):
  reader = vtkDICOMImageReader()
  reader.SetDirectoryName('./sample-data/Circle of Willis')
  reader.Update()

  renWin = vtkRenderWindow()
  renWin.SetWindowName('LearningMedicalViewer')
  renWin.SetSize(800, 800)

  

  iren = vtkRenderWindowInteractor()
  iren.SetRenderWindow(renWin)
  
  for orientation in ['axial', 'coronal', 'sagittal']:
    imageViewer = createMPRViewer(orientation, reader, renWin)
    # style = MouseWheelInteractorStyle(imageViewer)
    # iren.SetInteractorStyle(style)
    # imageViewer.SetupInteractor(iren)

  iren.Initialize()
  iren.Start()

if __name__ == '__main__':
    import sys

    main(sys.argv)