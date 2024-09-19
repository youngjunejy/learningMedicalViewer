from PySide6.QtWidgets import QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt
from src.QtMPRViewer import *

class QtViewerContainer(QWidget):
  def __init__(self, orientation):
    super().__init__()
    self.orientation = orientation

    self.initBackground()
    layout = QVBoxLayout()
    self.slider = self.createSlider()
    self.view = QtMPRViewer(orientation)
    layout.addWidget(self.slider)
    layout.addWidget(self.view)
    self.setLayout(layout)

  def initBackground(self):
    self.setAutoFillBackground(True)
    palette = self.palette()
    if(self.orientation == 'axial'):
      palette.setColor(QPalette.ColorRole.Window, QColor(251, 76, 53))
    elif(self.orientation == 'coronal'):
      palette.setColor(QPalette.ColorRole.Window, QColor(129, 206, 88))
    elif(self.orientation == 'sagittal'):
      palette.setColor(QPalette.ColorRole.Window, QColor(244, 220, 79))
    self.setPalette(palette)

  def createSlider(self):
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setValue(0)
    slider.setFixedHeight(24)
    slider.valueChanged.connect(self.on_slider_value_changed)

    return slider
  
  def setReader(self, reader):
    self.view.setReader(reader)
    self.slider.setMinimum(self.view.imageViewer.GetSliceMin())
    self.slider.setMaximum(self.view.imageViewer.GetSliceMax())

  def on_slider_value_changed(self, value):
    self.view.setSlice(value)