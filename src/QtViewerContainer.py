from PySide6.QtWidgets import QMainWindow, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt
from src.QtMPRViewer import *

class QtViewerContainer(QWidget):
  def __init__(self, orientation):
    super().__init__()
    self.orientation = orientation

    self.init_background()

    layout = QVBoxLayout()
    self.slider = self.create_slider()
    self.view = QtMPRViewer(orientation)
    layout.addWidget(self.slider)
    layout.addWidget(self.view)

    self.setLayout(layout)


  def init_background(self):
    self.setAutoFillBackground(True)
    palette = self.palette()
    if(self.orientation == 'axial'):
      palette.setColor(QPalette.ColorRole.Window, QColor(251, 76, 53))
    elif(self.orientation == 'coronal'):
      palette.setColor(QPalette.ColorRole.Window, QColor(129, 206, 88))
    elif(self.orientation == 'sagittal'):
      palette.setColor(QPalette.ColorRole.Window, QColor(244, 220, 79))
    self.setPalette(palette)

  def create_slider(self):
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setValue(50)
    slider.setFixedHeight(24)

    return slider
  
  def set_reader(self, reader):
    self.view.set_reader(reader)