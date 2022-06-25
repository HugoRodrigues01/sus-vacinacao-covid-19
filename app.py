"""
    This project going to connect in SUS`s API.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from view import Ui_MainWindow
from controller import LoadingWindow
from utils import Worker
from models import APISUSControl
from rich.console import Console
from rich import print
from time import time
import sys


console: Console = Console()

WINDOW_TITLE: str = "SUS vacinação covid-19"
WIDTH: int = 700
HEIGHT: int = 500


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

        self.load = LoadingWindow(self)
        self.load.create_window()

        # -------------------------------------------------
        # Connect to API
        self.api: APISUSControl = APISUSControl()

        self.create_widgets_ui()

        self.create_window()

        self.window.button_next.pressed.connect(self.next_page)

        # Loading the load window
        self.load.start_animation()

        self.setDisabled(True)

        # Start load_infos function to load infos of API
        self.start_worker(
            function=self.load_infos,
            result=self.format_datas,
            finished=lambda: self.hide_or_show_load_window(),
            error=self.create_message_error,
        )

    def create_window(self) -> None:

        print("Loading the windos...")

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.show()

    def hide_or_show_load_window(self) -> None:
        load_window_is_hide: bool = self.load.isHidden()

        console.log(f"Load window is hide: {load_window_is_hide}")

        if load_window_is_hide:
            self.setDisabled(True)
            self.load.show_window()

        else:
            self.setDisabled(False)
            self.load.hide_window()

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

    def create_message_error(self, error: str) -> None:

        ms = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical,
            "Error",
            str(error),
            QtWidgets.QMessageBox.StandardButton.Abort
            | QtWidgets.QMessageBox.StandardButton.Ok,
            self,
        )

        ms.setParent(self)

        with open("styles/message_box.qss", "r") as style:
            ms.setStyleSheet(style.read())

        buttons = ms.exec()

        if buttons == QtWidgets.QMessageBox.StandardButton.Abort:

            print("[bold]Aport[/] button was pressed. Closing the window...")
            exit(1)

    def load_infos(self) -> dict:
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

        for index, values in enumerate(data["hits"]["hits"]):

            headers: list = values["_source"].keys()
            infos: list = values["_source"].values()
            _id: str = values["_source"]["paciente_id"]

            self.add_info(headers, infos, _id, index)

            # -------------------------------------------------

        #  change the amount of pleople in status bar
        self.amount.setText(f"Amount of people: {len(data['hits']['hits'])}")

    def add_info(
        self, headers: list, infos: list, _id: str, row: int, column: int = 0
    ) -> None:
        """
        Add infos of SUS of API into a widget and then, insert it into the window.
        """

        #  Loading the styles
        style = open("styles/frame.qss", "r")

        frame: QtWidgets.QFrame = QtWidgets.QFrame()
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
        self.window.gridLayout_5.addWidget(frame, row, column)

        self.window.label_info_page.setText(f"Infos: Page {self.api.get_number_page}")

    def start_worker(
        self, function, result, finished=lambda: "", error=lambda: ""
    ) -> None:

        time_start: float = time()

        worker: Worker = Worker(function)
        worker.signals.results.connect(result)
        worker.signals.progress.connect(lambda output: print("Output ", output))
        worker.signals.error.connect(error)
        worker.signals.finished.connect(finished)

        #  Start function(process) in thread
        self.thread.start(worker)

        time_finishe: float = time()

        print(f"Worker finished., {(time_finishe - time_start):.3f}s")

    def next_page(self) -> None:
        """
        Going to create the next page of SUS of API.
        """
        self.hide_or_show_load_window()

        #  Delete all the widgets of scroll area
        while self.window.gridLayout_5.count():
            item = self.window.gridLayout_5.takeAt(0)
            item.widget().deleteLater()

        finished_function = lambda: self.format_datas(self.api.get_data())

        self.start_worker(
            function=self.api.post_data,
            result=lambda: self.hide_or_show_load_window(),
            finished=finished_function,
            error=self.create_message_error,
        )


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowControl()
    sys.exit(app.exec())
