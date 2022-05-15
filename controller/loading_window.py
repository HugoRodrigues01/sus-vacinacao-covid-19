from . import QtCore, QtWidgets, QtGui
from view import Ui_LoadingWindow


class LoadingWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(LoadingWindow, self).__init__(*args, **kwargs)

        self.loading_window: Ui_LoadingWindow = Ui_LoadingWindow()
        self.loading_window.setupUi(self)

    def create_window(self) -> None:
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 150)
        self.show()

    def hide_window(self) -> None:
        self.hide()

    @property
    def value_pregress_bar(self) -> int:
        return self.loading_window.progress_bar_loading.value()
    
    @value_pregress_bar.setter
    def value_pregress_bar(self, value: int) -> None:
        self.loading_window.progress_bar_loading.setValue(value)