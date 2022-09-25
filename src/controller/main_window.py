"""
    This project going to connect in SUS`s API.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from views import Ui_MainWindow
from utils import start_worker, format_datas
from models import APISUSControl
from rich.console import Console
from rich import print
from frames import FrameReload, FrameLoading
import sys
from typing import Union
from configs.global_variables_conf import STYLE_FRAMES
from configs.global_conf import HEIGHT, WINDOW_TITLE, WIDTH

console: Console = Console()


class MainWindowControl(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindowControl, self).__init__(*args, **kwargs)

        # Thres for others process
        self.thread: QtCore.QThreadPool = QtCore.QThreadPool()
        self.thread.setParent(self)

        # -------------------------------------------------
        # Loadding windows

        self.window: Ui_MainWindow = Ui_MainWindow()
        self.window.setupUi(self)
        # -------------------------------------------------

        # --------------------------------------------------
        # Loading frames
        self.frame_loading: FrameLoading = FrameLoading()
        self.frame_reload: FrameReload = FrameReload()
        # --------------------------------------------------

        # Connect to API
        self.api: APISUSControl = APISUSControl()

        # CONNECT THE EVENTS
        # --------------------------------------------------
        self.window.button_next.pressed.connect(self.next_page)
        self.frame_reload.button_connect(
            self.frame_reload.button_reload, self.button_reload
        )
        # --------------------------------------------------

        # --------------------------------------------------
        # Default start

        self.window.frame_infos.hide()
        self.frame_loading.start_animation()

        self.window.layout_central_widget.addWidget(self.frame_loading.frame, 1)

        self.window.button_go_back.setDisabled(True)
        self.window.button_next.setDisabled(True)

        # Start
        # function -> function for worker
        # thread -> thread for function worker
        # result -> after results of function
        # finished -> when the function finished
        # error -> if error
        start_worker(
            function=self.load_infos,
            thread=self.thread,
            result=self.format_datas,
            finished=self.hide_or_show_load_window,
            error=self.open_frame_reload,
        )
        # --------------------------------------------------

    def create_window(self) -> None:

        print("Loading the windos...")

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.show()

    def hide_or_show_load_window(self) -> None:
        frame_infos_is_hide: bool = self.window.frame_infos.isHidden()

        print(f"Frame infos is hide: {frame_infos_is_hide}")

        if frame_infos_is_hide:

            self.window.button_go_back.setDisabled(False)
            self.window.button_next.setDisabled(False)

            self.frame_loading.frame.hide()
            self.window.frame_infos.show()

        else:
            self.window.button_go_back.setDisabled(True)
            self.window.button_next.setDisabled(True)

            self.frame_loading.frame.show()
            self.window.frame_infos.hide()

    def create_widgets_ui(self) -> None:

        # Amount of values
        self.amount = QtWidgets.QLabel("Amount of people: ")
        self.amount.setObjectName("label_amount")
        self.amount.setStyleSheet(
            """
            QLabel {
                color: rgba(255, 255, 255, 0.3);
                font-size: 10px;
                margin-left: 10px;
                background-color: none;
            }
        """
        )

        self.window.statusBar.addWidget(self.amount)

    def open_frame_reload(self) -> None:
        self.window.frame_infos.hide()
        self.window.scroll_area.hide()

        self.window.frame_menu.setDisabled(True)

        if self.frame_reload.frame.isHidden():
            self.frame_reload.frame.show()

        self.window.layout_central_widget.addWidget(self.frame_reload.frame, 1)

    def load_infos(self) -> Union[dict, ValueError]:
        """
        This function going to load the all datas of SUS´API.

        """

        try:
            self.api.api_start()

            # Get datas of API
            data: dict = self.api.get_data()

        except Exception as error:

            console.log(f"-- Error: [red]{error}[/] --")

        else:

            return data

        raise ValueError

    def format_datas(self, data) -> None:
        """
        After the datas was loaded, this function will format all datas.
        """

        # Verify if the API function get all datas
        console.log("-- The infos of API was loaded! --")

        # formating the datas
        result: list = format_datas(data)

        for value in result:

            # inserting the datas into of window
            self.add_info(value["headers"], value["infos"], value["id"], value["index"])

        #  change the amount of pleople in status bar
        self.amount.setText(f"Amount of people: {len(data['hits']['hits'])}")

    def add_info(
        self, headers: list, infos: list, _id: int, row: int, column: int = 0
    ) -> None:

        """
        Add infos of SUS of API into a widget and then, insert it into the window.
        """
        #  Loading the styles
        style = open(STYLE_FRAMES + "/frame_infos.qss", "r")

        frame: QtWidgets.QFrame = QtWidgets.QFrame()
        frame.setObjectName("frame_widgets_api")
        # Insert the style into the frame
        frame.setStyleSheet(style.read())
        frame.setMaximumWidth(600)

        grid_layout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(frame)

        # LABLE ID
        # -------------------------------------------------
        label_id: QtWidgets.QLabel = QtWidgets.QLabel("ID: " + str(_id))
        label_id.setObjectName("label-id")
        label_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # -------------------------------------------------

        # CONTAINER INFO
        # -------------------------------------------------
        layout_form_info: QtWidgets.QFormLayout = QtWidgets.QFormLayout()
        # -------------------------------------------------

        # LABELS OF INFO (HEADER - INFO)
        # -------------------------------------------------
        for index, (h, i) in enumerate(list(zip(headers, infos))):

            label_h = QtWidgets.QLabel(str(h.replace("_", " ")))
            label_h.setObjectName("label-h")
            label_h.setMaximumHeight(40)

            text_area_i = QtWidgets.QPlainTextEdit(str(i))
            text_area_i.setReadOnly(True)
            text_area_i.setMaximumHeight(50)
            text_area_i.setObjectName("text-area")

            layout_form_info.setWidget(
                index, QtWidgets.QFormLayout.ItemRole.LabelRole, label_h
            )
            layout_form_info.setWidget(
                index, QtWidgets.QFormLayout.ItemRole.FieldRole, text_area_i
            )

        # -------------------------------------------------

        # ADD WIDGETS IN GRIDLAYOUT
        # -------------------------------------------------
        grid_layout.addWidget(label_id, 0, 1)
        grid_layout.addLayout(layout_form_info, 1, 1)
        # -------------------------------------------------

        # Add new container in scroll area
        self.window.layout_g_scroll_area_infos.addWidget(frame, row, column)

        self.window.label_info_page.setText(f"Infos: Page {self.api.get_number_page}")

    def next_page(self) -> None:
        """
        Going to create the next page of SUS of API.
        """

        self.hide_or_show_load_window()

        not_delete: list = ["frame_loading", "frame_reload"]

        #  Delete all the widgets of scroll area
        while self.window.layout_g_scroll_area_infos.count():
            item = self.window.layout_g_scroll_area_infos.takeAt(0)

            if not item.widget().objectName() in not_delete:
                item.widget().deleteLater()

        # self.window.frame_reload.deleteLater()

        finished_function = lambda: self.format_datas(self.api.get_data())

        start_worker(
            function=self.api.post_data,
            thread=self.thread,
            result=lambda: self.hide_or_show_load_window(),
            finished=finished_function,
            error=self.open_frame_reload,
        )

    def button_reload(self):
        """
        This function will try reload the datas of API
        """

        self.hide_or_show_load_window()
        self.frame_reload.frame.hide()
        start_worker(
            function=self.load_infos,
            thread=self.thread,
            result=self.format_datas,
            finished=self.hide_or_show_load_window,
            error=self.open_frame_reload,
        )

    def closeEvent(self, a0) -> None:
        self.hide()

        print("Closing window, good bye!!")
        sys.exit(0)
