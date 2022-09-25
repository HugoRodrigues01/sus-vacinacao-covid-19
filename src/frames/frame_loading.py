from interfaces import InterfaceFrame
from PyQt6 import QtWidgets, QtCore, QtGui
from configs.global_variables_conf import LOADING_GIF


class FrameLoading(InterfaceFrame):
    def __init__(self):

        self.__loading_gif: str = LOADING_GIF

        # LOADING ALL WIDGETS OF THE LOADING FRAME
        self.load_widgets()

    def load_widgets(self) -> None:

        self.__frame_loading: QtWidgets.QFrame = QtWidgets.QFrame()
        self.__frame_loading.setObjectName("frame_loading")
        self.layout: QtWidgets.QHBoxLayout = QtWidgets.QHBoxLayout()

        self.horizontal_spacer = QtWidgets.QSpacerItem(
            40,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )

        self.label_loading: QtWidgets.QLabel = QtWidgets.QLabel()
        self.label_loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_loading.setMaximumSize(40, 40)
        self.label_loading.setMinimumSize(30, 30)
        self.label_loading.setScaledContents(True)
        self.movie: QtGui.QMovie = QtGui.QMovie(self.__loading_gif)

        self.label_loading.setMovie(self.movie)

        self.__frame_loading.setLayout(self.layout)

        self.layout.addItem(self.horizontal_spacer)
        self.layout.addWidget(self.label_loading)
        self.layout.addItem(self.horizontal_spacer)

    @property
    def frame(self) -> QtWidgets.QFrame:
        return self.__frame_loading

    def start_animation(self) -> None:
        self.movie.start()

    def stop_animation(self) -> None:
        self.stop_animation()
