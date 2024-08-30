import sys
import SimpleITK as sitk
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

class MPRViewer(QMainWindow):
    def __init__(self, image):
        super().__init__()
        self.setWindowTitle("MPR Viewer")

        self.image_array = sitk.GetArrayFromImage(image)
        self.current_slice = 0

        self.label = QLabel()
        self.update_image()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setRange(0, self.image_array.shape[0] - 1)
        self.slider.valueChanged.connect(self.change_slice)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_image(self):
        slice_image = self.image_array[self.current_slice, :, :]
        qimage = self.convert_to_qimage(slice_image)
        self.label.setPixmap(QPixmap.fromImage(qimage))

    def convert_to_qimage(self, array):
        height, width = array.shape
        array = ((array - array.min()) / (array.max() - array.min()) * 255).astype(np.uint8)
        return QImage(array.data, width, height, width * array.itemsize, QImage.Format_Grayscale8)

    def change_slice(self, value):
        self.current_slice = value
        self.update_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image = sitk.ReadImage("data/CT-chest.nrrd")
    viewer = MPRViewer(image)
    viewer.show()
    sys.exit(app.exec())