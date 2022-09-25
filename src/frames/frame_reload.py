from PyQt6 import QtWidgets, QtCore, QtGui
from interfaces import InterfaceFrame
from typing import TextIO
from configs.global_variables_conf import STYLE_FRAMES


class FrameReload(InterfaceFrame):
    def __init__(self) -> None:

        self.load_widgets()

    def load_widgets(self) -> None:

        self.horizontal_spacer = QtWidgets.QSpacerItem(
            40,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )

        self.horizontal_spacer_fixed = QtWidgets.QSpacerItem(
            40,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )

        self.layout = QtWidgets.QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.__frame_reload = QtWidgets.QFrame()
        self.__frame_reload.setObjectName("frame_reload")
        self.__frame_reload.setLayout(self.layout)

        self.label = QtWidgets.QLabel("Sorry, you are off-line")
        self.label.setObjectName("label_sorry")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.button_reload = QtWidgets.QPushButton("Reload")
        self.button_reload.setObjectName("button_reload")
        self.button_reload.setMaximumSize(300, 40)
        self.button_reload.setMinimumSize(300, 40)
        self.button_reload.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        # ADD ALL WIDGETS INTO THE LAYOUT
        self.layout.addItem(self.horizontal_spacer, 0, 0)
        self.layout.addWidget(self.label, 1, 0, 1, 1)
        self.layout.addItem(self.horizontal_spacer_fixed, 2, 0, 1, 1)
        self.layout.addWidget(self.button_reload, 3, 0, 1, 1)
        self.layout.addItem(self.horizontal_spacer, 4, 0)

        # Loading the styles
        self.load_style()

    @property
    def frame(self) -> QtWidgets.QFrame:

        return self.__frame_reload

    def load_style(self, style="frame_reload.qss") -> None:

        with open(STYLE_FRAMES + "/" + style, "r") as file_style:
            self.__frame_reload.setStyleSheet(file_style.read())

    def button_connect(self, button: QtWidgets.QPushButton, conection) -> None:
        button.pressed.connect(conection)
