from PyQt6 import QtCore, QtWidgets, QtGui
from windows_ui import Ui_LoadingWindow


class LoadingWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(LoadingWindow, self).__init__(*args, **kwargs)

        self.loading_window: Ui_LoadingWindow = Ui_LoadingWindow()
        self.loading_window.setupUi(self)

    def create_window(self) -> None:

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 200)
        self.show()