# Load default configs
import src.configs.global_conf

from controller import MainWindowControl
from PyQt6 import QtCore, QtWidgets
import sys


def manager(window) -> None:
    """
    Manager of project, SUS´s API.
    """

    # Create the widgets of window
    window.create_widgets_ui()

    # Generate window
    window.create_window()


if __name__ == "__main__":
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: QtWidgets.QMainWindow = MainWindowControl()
    manager(window)
    sys.exit(app.exec())
