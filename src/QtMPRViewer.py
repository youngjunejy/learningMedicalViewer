from PySide6.QtWidgets import QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt

from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkInteractionImage import vtkImageViewer2, vtkResliceImageViewer
from vtkmodules.vtkImagingColor import vtkImageMapToWindowLevelColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader

import vtkmodules.qt.QVTKRenderWindowInteractor as QVTK
QVTKRenderWindowInteractor = QVTK.QVTKRenderWindowInteractor

class QtMPRViewer(QVTKRenderWindowInteractor):
  def __init__(self, orientation):
    super().__init__()

    self.orientation = orientation
    self.imageViewer = vtkImageViewer2()

    if(self.orientation == 'axial'):
      self.imageViewer.SetSliceOrientationToXY()
    elif(self.orientation == 'coronal'):
      self.imageViewer.SetSliceOrientationToXZ()
    elif(self.orientation == 'sagittal'):
      self.imageViewer.SetSliceOrientationToYZ()      

  def setReader(self, reader:'vtkDICOMImageReader'):
    print(reader.GetOutput())

    self.imageViewer.SetRenderWindow(self.GetRenderWindow())
    self.imageViewer.SetInputConnection(reader.GetOutputPort())
    self.Initialize()
    self.imageViewer.Render()

    windowLevel = self.imageViewer.GetWindowLevel()
    print(windowLevel.GetLevel(), windowLevel.GetWindow())


  def setSlice(self, slice):
    self.imageViewer.SetSlice(slice)
    self.imageViewer.Render()