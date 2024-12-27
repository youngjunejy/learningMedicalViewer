from PySide6.QtWidgets import QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt

import pydicom
import os

from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkInteractionImage import vtkImageViewer2, vtkResliceImageViewer
from vtkmodules.vtkImagingColor import vtkImageMapToWindowLevelColors
from vtkmodules.vtkIOImage import vtkDICOMImageReader
from vtkmodules.vtkCommonDataModel import vtkImageData

import vtkmodules.qt.QVTKRenderWindowInteractor as QVTK
QVTKRenderWindowInteractor = QVTK.QVTKRenderWindowInteractor

class QtMPRViewer(QVTKRenderWindowInteractor):
  def __init__(self, orientation):
    super().__init__()

    self.orientation = orientation

    self.imageViewer = vtkResliceImageViewer()
    self.imageViewer.SetRenderWindow(self.GetRenderWindow())
    
    if(self.orientation == 'axial'):
      self.imageViewer.SetSliceOrientationToXY()
    elif(self.orientation == 'coronal'):
      self.imageViewer.SetSliceOrientationToXZ()
    elif(self.orientation == 'sagittal'):
      self.imageViewer.SetSliceOrientationToYZ()

  def closeEvent(self, event):
    self.imageViewer.GetRenderWindow().Finalize()
    super().closeEvent(event)

  def setImage(self, imageData:'vtkImageData'):
    if imageData is None:
      print("Invalid image data")
      return

    self.imageViewer.SetInputData(imageData)
    self.imageViewer.SetColorWindow(1000)
    self.imageViewer.SetColorLevel(400)

    self.Initialize()
    self.imageViewer.Render()

  def setSlice(self, sliceIndex):
    self.imageViewer.SetSlice(sliceIndex)
    self.imageViewer.Render()
    