from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from src.app import MainWindow

if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()