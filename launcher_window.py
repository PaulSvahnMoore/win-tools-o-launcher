# launcher_window.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WTOL")
        self.setFixedSize(900, 600)  # Set window size
