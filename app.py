"""
    This project going to connect in SUS`s API.
"""

from PyQt6 import QtCore, QtGui, QtWidgets
from windows_ui import Ui_MainWindow
from windows import LoadingWindow
from models import APISUSControl
import sys
from rich.console import Console
from rich import print

console: Console = Console()

WINDOW_TITLE: str = "SUS vacinação covid-19"
WIDTH: int = 700
HEIGHT: int = 500


class MainWindowControl(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindowControl, self).__init__(*args, **kwargs)

        self.window: Ui_MainWindow = Ui_MainWindow()
        self.window.setupUi(self)

        #-------------------------------------------------
        # Connect to API
        self.api: APISUSControl = APISUSControl()

        self.create_widgets_ui()

        self.load_infos()

        self.window.button_next.pressed.connect(self.next_page)

        self.create_window()

    def create_window(self) -> None:

        print("Loading the windos...")

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WIDTH, HEIGHT)
        self.show()

        self.load = LoadingWindow(self)
        self.load.create_window()

    def create_widgets_ui(self) -> None:

        # Amount of values
        self.amount = QtWidgets.QLabel("Amount of people: ")
        self.amount.setObjectName("label_amount")
        self.amount.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.3);
                font-size: 10px;
                margin-left: 10px;
                background-color: none;
            }
        """)
        
        self.window.statusBar.addWidget(self.amount)

    def add_info(self, headers: list, infos: list, _id: str, row: int, column: int=0) -> None:
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
        #-------------------------------------------------
        label_id: QtWidgets.QLabel = QtWidgets.QLabel("ID: " + str(_id))
        label_id.setObjectName("label-id")
        label_id.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        #-------------------------------------------------

        # CONTAINER INFO
        #-------------------------------------------------
        layout_form_info: QtWidgets.QFormLayout = QtWidgets.QFormLayout()
        #-------------------------------------------------

        # LABELS OF INFO (HEADER - INFO)
        #-------------------------------------------------
        for index, (h, i) in enumerate(list(zip(headers, infos))):

            label_h = QtWidgets.QLabel(str(h.replace("_", " ")))
            label_h.setObjectName("label-h")
            label_h.setMaximumHeight(40)

            text_area_i = QtWidgets.QPlainTextEdit(str(i))
            text_area_i.setReadOnly(True)
            text_area_i.setMaximumHeight(50)
            text_area_i.setObjectName("text-area")

            layout_form_info.setWidget(index, QtWidgets.QFormLayout.ItemRole.LabelRole, label_h)
            layout_form_info.setWidget(index, QtWidgets.QFormLayout.ItemRole.FieldRole, text_area_i)

        #-------------------------------------------------

        # ADD WIDGETS IN GRIDLAYOUT
        #-------------------------------------------------
        grid_layout.addWidget(label_id, 0, 1)
        grid_layout.addLayout(layout_form_info, 1, 1)
        #-------------------------------------------------

        # Add new container in scroll area
        self.window.gridLayout_5.addWidget(frame, row, column)

    def load_infos(self) -> None:
        """
        This function going to load the all datas of SUS of API.

        """

        try:
            self.api.api_start()

             # Get datas of API
            self.data: dict = self.api.get_data()

        except Exception as error:

            console.log(f"-- Error: [red]{error}[/] --")

            ms = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, "Error", str(error), QtWidgets.QMessageBox.StandardButton.Abort | QtWidgets.QMessageBox.StandardButton.Ok, self)

            with open("styles/message_box.qss", "r") as style:
                ms.setStyleSheet(style.read())

            buttons = ms.exec() 

            if buttons == QtWidgets.QMessageBox.StandardButton.Abort:

                print("[bold]Aport[/] button was pressed. Closing the window...")
                exit(1)
        
        else:

            # Verify if the API function get all datas
            console.log("-- The infos of API was loaded! --")

            for index, values in enumerate(self.data["hits"]["hits"]):

                h: list = values["_source"].keys()
                i: list = values["_source"].values()
                _id: str = values["_source"]["paciente_id"]
            
                self.add_info(h, i, _id, index)
            #-------------------------------------------------

            #  change the amount of pleople in status bar
            self.amount.setText(f"Amount of people: {len(self.data['hits']['hits'])}")
            
            print(f"Number page: {self.api.get_number_page}")

    def next_page(self) -> None:
        """
        Going to create the next page of SUS of API.
        """

        self.api.post_data()

        #  Delete all the widgets of scroll area
        while self.window.gridLayout_5.count():
            item = self.window.gridLayout_5.takeAt(0)
            item.widget().deleteLater()

        self.window.label_info_page.setText(f"Infos: Page: {self.api.get_number_page}")

        #  Load the widgets for the next page
        self.load_infos()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowControl()
    sys.exit(app.exec())