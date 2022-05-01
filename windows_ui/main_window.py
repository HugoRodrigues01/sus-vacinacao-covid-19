# Form implementation generated from reading ui file 'windows_ui/ui_files/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 505)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("windows_ui/ui_files/../../img/hospital.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("* {\n"
"background-color: rgb(49, 49, 74);\n"
"color: black;\n"
"border: none;\n"
"}\n"
"\n"
"QLabel#label_sus {\n"
"color: rgb(98, 98, 148);\n"
"}\n"
"\n"
"/* QSCROLL BAR VETICAL */\n"
"QScrollBar:vertical{\n"
"background-color: rgb(65, 65, 98);\n"
"margin: 15px 0 15px 0;\n"
"border: none;\n"
"width: 14px;\n"
"border-radius:0;\n"
"}\n"
"\n"
"/* HANDEL */\n"
"QScrollBar::handle {\n"
"background-color: rgb(85, 85, 129);\n"
"min-height: 30px;\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"background-color: rgb(106, 106, 161);\n"
"}\n"
"\n"
"/* SUB-LINE QSCROLLBAR VERTICAL */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 15px;\n"
"border: none;\n"
"background-color: rgb(65, 65, 98);\n"
"border-top-left-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:hover {\n"
"background-color: rgb(31, 31, 47);\n"
"}\n"
"\n"
"QScrollBar::sub-line:pressed {\n"
"background-color: rgb(72, 72, 109);\n"
"}\n"
"\n"
"/* SUB-LINE QSCROLLBAR HORIZONTAL */\n"
"QScrollBar::sub-line:horizontal {\n"
"height: 15px;\n"
"border: none;\n"
"background-color: rgb(65, 65, 98);\n"
"border-radius: 7px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* ADD-LINE QSCROLLBAR VERTICAL  */\n"
"QScrollBar::add-line:vertical {\n"
"height: 15px;\n"
"border: none;\n"
"background-color: rgb(65, 65, 98);\n"
"border-bottom-left-radius: 7px;\n"
"border-bottom-right-radius: 7px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:hover {\n"
"background-color: rgb(31, 31, 47);\n"
"}\n"
"\n"
"QScrollBar::add-line:pressed {\n"
"background-color: rgb(72, 72, 109);\n"
"}\n"
"\n"
"/* ADD-LINE QSCROLLBAR HORIZONTAL  */\n"
"QScrollBar::add-line:horizontal {\n"
"height: 15px;\n"
"border: none;\n"
"background-color: rgb(65, 65, 98);\n"
"border-radius: 7px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QStatusBar {\n"
"background-color: rgb(37, 37, 57)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_sus = QtWidgets.QHBoxLayout()
        self.horizontalLayout_sus.setObjectName("horizontalLayout_sus")
        self.label_img_sus = QtWidgets.QLabel(self.centralwidget)
        self.label_img_sus.setMinimumSize(QtCore.QSize(0, 0))
        self.label_img_sus.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_img_sus.setText("")
        self.label_img_sus.setPixmap(QtGui.QPixmap("windows_ui/ui_files/../../img/hospital.png"))
        self.label_img_sus.setObjectName("label_img_sus")
        self.horizontalLayout_sus.addWidget(self.label_img_sus)
        self.label_sus = QtWidgets.QLabel(self.centralwidget)
        self.label_sus.setStyleSheet("font-family: monospace;\n"
"font-weight: bold;\n"
"font-size:  18pt;")
        self.label_sus.setObjectName("label_sus")
        self.horizontalLayout_sus.addWidget(self.label_sus)
        self.verticalLayout.addLayout(self.horizontalLayout_sus)
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_menu.setStyleSheet("QPushButton {\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"padding: 5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgba(255, 255, 255, 0.5);\n"
"font-family: monospace;\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_info_page = QtWidgets.QLabel(self.frame_menu)
        self.label_info_page.setObjectName("label_info_page")
        self.horizontalLayout.addWidget(self.label_info_page)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_go_back = QtWidgets.QPushButton(self.frame_menu)
        self.button_go_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.button_go_back.setObjectName("button_go_back")
        self.horizontalLayout.addWidget(self.button_go_back)
        self.button_next = QtWidgets.QPushButton(self.frame_menu)
        self.button_next.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.button_next.setObjectName("button_next")
        self.horizontalLayout.addWidget(self.button_next)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_infos = QtWidgets.QFrame(self.centralwidget)
        self.frame_infos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_infos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_infos.setObjectName("frame_infos")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_infos)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_infos)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 324))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_infos)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionhelp = QtGui.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actionadd = QtGui.QAction(MainWindow)
        self.actionadd.setObjectName("actionadd")
        self.actionOk = QtGui.QAction(MainWindow)
        self.actionOk.setObjectName("actionOk")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sus.setText(_translate("MainWindow", "SUS-COVID-19"))
        self.label_info_page.setText(_translate("MainWindow", "Infos: Page 1"))
        self.button_go_back.setText(_translate("MainWindow", "<"))
        self.button_next.setText(_translate("MainWindow", ">"))
        self.actionhelp.setText(_translate("MainWindow", "help"))
        self.actionadd.setText(_translate("MainWindow", "add"))
        self.actionOk.setText(_translate("MainWindow", "Ok"))
