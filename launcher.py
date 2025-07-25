# launcher.py
from PySide6.QtWidgets import QApplication
import sys
from launcher_window import LauncherWindow  # Import the main window

def main():
    app = QApplication(sys.argv)  # Create the application
    window = LauncherWindow()      # Create the launcher window
    window.show()                  # Show the window
    sys.exit(app.exec())           # Run the event loop

if __name__ == "__main__":
    main()
