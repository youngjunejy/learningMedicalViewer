import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QWidget, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette, QAction

from vtkmodules.vtkIOImage import vtkDICOMImageReader

from src.QtViewerContainer import *

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.init_ui()
    self.create_menu()

    # test
    self.open_file()

  def init_ui(self):
    self.setWindowTitle("Learning Medical Viewer")
    self.resize(1000, 800)

    splitter = QSplitter(Qt.Orientation.Horizontal)

    left_widget = QWidget()
    left_layout = QVBoxLayout()
    left_widget.setLayout(left_layout)
    left_widget.setAutoFillBackground(True)
    palette = left_widget.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(200, 200, 255))
    left_widget.setPalette(palette)

    right_widget = QWidget()
    right_layout = QVBoxLayout()
    h1_layout = QHBoxLayout()
    h2_layout = QHBoxLayout()

    self.axial_viewer = QtViewerContainer('axial')
    self.coronal_viewer = QtViewerContainer('coronal')
    self.sagittal_viewer = QtViewerContainer('sagittal')


    h1_layout.addWidget(self.axial_viewer)
    h1_layout.addWidget(QtViewerContainer('VR'))
    h2_layout.addWidget(self.coronal_viewer)
    h2_layout.addWidget(self.sagittal_viewer)
    
    right_layout.addLayout(h1_layout)
    right_layout.addLayout(h2_layout)

    right_widget.setLayout(right_layout)

    splitter.addWidget(left_widget)
    splitter.addWidget(right_widget)
    splitter.setSizes([240, 560])

    self.setCentralWidget(splitter)

  def create_menu(self):
    menu_bar = self.menuBar()

    file_menu = menu_bar.addMenu("File")

    open_action = QAction("Open", self)
    open_action.triggered.connect(self.open_file)

    file_menu.addAction(open_action)

  def open_file(self):
    reader = vtkDICOMImageReader()
    reader.SetDirectoryName('./sample-data/Circle of Willis')
    reader.Update()

    self.axial_viewer.set_reader(reader)
    self.coronal_viewer.set_reader(reader)
    self.sagittal_viewer.set_reader(reader)

