# launcher_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WTOL")
        self.setFixedSize(1000, 750)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # LEFT COLUMN
        left_column = QWidget()
        left_column.setFixedWidth(300)  # Fixed width
        left_layout = QVBoxLayout(left_column)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)  # Uniform spacing between widgets

        # Left top panel (fixed size 300x300)
        left_top_panel = QWidget()
        left_top_panel.setFixedHeight(300)
        left_top_panel.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 10px;
            margin: 5px;
        """)

        # Left bottom panel (takes remaining height)
        left_bottom_panel = QWidget()
        left_bottom_panel.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 10px;
            margin: 5px;
        """)

        # Add top and bottom panels to left layout
        left_layout.addWidget(left_top_panel)
        left_layout.addWidget(left_bottom_panel)  # Expands automatically

        # Set the bottom panel to stretch and fill available space
        left_layout.setStretch(0, 0)  # No stretching for top panel
        left_layout.setStretch(1, 1)  # Stretch for bottom panel

        # RIGHT PANEL
        right_panel = QWidget()
        right_panel.setStyleSheet("""
            background-color: #f0f0f0;
            border-radius: 10px;
            margin: 5px;
        """)

        # Add left column and right panel to the main layout
        main_layout.addWidget(left_column)
        main_layout.addWidget(right_panel, stretch=1)  # Right panel stretches to fill remaining space