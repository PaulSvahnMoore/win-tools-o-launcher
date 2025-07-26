from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

class LauncherWindow(QMainWindow):
    def __init__(self):                         # Constructor for the main window
        super().__init__()                      # Initialize the main window
        self.setWindowTitle("WTOL")             # Set the window title
        self.setFixedSize(1000, 750)            # Set fixed size for the window

        # Central widget
        central_widget = QWidget()              # Create a central widget
        self.setCentralWidget(central_widget)   # Set the central widget

        layout = QHBoxLayout(central_widget)    # Create a horizontal layout for the central widget

        # Left panel (fixed width, rounded)
        left_panel = QWidget()                  # Create the left panel
        left_panel.setFixedWidth(300)           # Set fixed width for the left panel
        left_panel.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 10px;
            margin: 5px;
        """)

        # Right panel (takes remaining space)
        right_panel = QWidget()                 # Create the right panel
        right_panel.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 10px;
            margin: 5px;
        """)

        layout.addWidget(left_panel)
        layout.addWidget(right_panel)
