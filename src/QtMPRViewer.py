from PySide6.QtWidgets import QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt

from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper, vtkRenderer
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkInteractionImage import vtkImageViewer2, vtkResliceImageViewer

import vtkmodules.qt.QVTKRenderWindowInteractor as QVTK
QVTKRenderWindowInteractor = QVTK.QVTKRenderWindowInteractor

class QtMPRViewer(QVTKRenderWindowInteractor):
  def __init__(self, orientation):
    super().__init__()

    self.orientation = orientation
    
  def set_reader(self, reader):
    # renderer = vtkRenderer()
    # self.GetRenderWindow().AddRenderer(renderer)

    # cone = vtkConeSource()
    # cone.SetResolution(8)

    # mapper = vtkPolyDataMapper()
    # mapper.SetInputConnection(cone.GetOutputPort())

    # actor = vtkActor()
    # actor.SetMapper(mapper)

    # renderer.AddActor(actor)
    # renderer.SetBackground(0.5, 0.5, 0.5)

    # self.Initialize()
    # self.Start()


    image_viewer = vtkImageViewer2()
    image_viewer.SetRenderWindow(self.GetRenderWindow())

    image_viewer.SetInputConnection(reader.GetOutputPort())

    self.Initialize()
    image_viewer.Render()
    # self.Start()


  # def set_slice(self, slice):
  #   self.viewer.SetSlice(slice)

  # def render(self):
  #   # renderer.Render()