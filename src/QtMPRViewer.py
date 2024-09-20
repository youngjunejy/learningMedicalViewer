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
    self.imageViewer.SetRenderWindow(self.GetRenderWindow())
    self.imageViewer.SetInputConnection(reader.GetOutputPort())

    windowLevel = self.imageViewer.GetWindowLevel()
    windowLevel.SetLevel(400)
    windowLevel.SetWindow(1000)

    self.Initialize()
    self.imageViewer.Render()

    print(windowLevel.GetLevel(), windowLevel.GetWindow())

  def setSlice(self, slice):
    self.imageViewer.SetSlice(slice)
    self.imageViewer.Render()
    
  # def getWindowLevel(self, reader:'vtkDICOMImageReader'):
  #   directoryName = reader.GetDirectoryName()
  #   for filename in os.listdir(directoryName):
  #     if filename.endswith('.dcm'):
  #       filepath = os.path.join(directoryName, filename)
  #       ds = pydicom.dcmread(filepath)
  #       if 'WindowWidth' in ds:
  #           window_width = ds.WindowWidth
  #           print(f'File: {filename}, Window Width: {window_width}')
    