from . import QtCore, QtWidgets, QtGui
from view import Ui_LoadingWindow
import time

LOAD_GIF: str = "img/loadgif.gif"


class LoadingWindow(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(LoadingWindow, self).__init__(*args, **kwargs)

        self.loading_window: Ui_LoadingWindow = Ui_LoadingWindow()
        self.loading_window.setupUi(self)

        # Resizing gif
        self.loading_window.label_gif.setScaledContents(True)

        self.movie: QtGui.QMovie = QtGui.QMovie(LOAD_GIF)

        self.loading_window.label_gif.setMovie(self.movie)

    def create_window(self) -> None:
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint
            | QtCore.Qt.WindowType.WindowStaysOnTopHint
            | QtCore.Qt.WindowType.WindowSystemMenuHint
        )
        self.setFixedSize(50, 50)
        self.show()

    def start_animation(self) -> None:
        self.movie.start()

    def stop_animation(self) -> None:
        self.movie.stop()

    def hide_window(self) -> None:
        self.hide()

    def show_window(self) -> None:
        self.show()
