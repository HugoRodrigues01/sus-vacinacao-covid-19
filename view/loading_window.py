# Form implementation generated from reading ui file 'view/ui_files/loading_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoadingWindow(object):
    def setupUi(self, LoadingWindow):
        LoadingWindow.setObjectName("LoadingWindow")
        LoadingWindow.resize(94, 73)
        LoadingWindow.setMinimumSize(QtCore.QSize(0, 26))
        LoadingWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        LoadingWindow.setAutoFillBackground(False)
        LoadingWindow.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(LoadingWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_loading = QtWidgets.QFrame(LoadingWindow)
        self.frame_loading.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_loading.setStyleSheet("* {\n"
"border: 0;\n"
"color: white;\n"
"}\n"
"\n"
"QFrame  {\n"
"    background-color: rgba(37, 37, 56, 0);\n"
"   border-radius:  50%;\n"
"}\n"
"\n"
"QProgressBar {\n"
"max-height: 5px;\n"
"border: 0;\n"
"color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color:rgb(98, 98, 148) ;\n"
"}")
        self.frame_loading.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_loading.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_loading.setObjectName("frame_loading")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_loading)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_gif = QtWidgets.QLabel(self.frame_loading)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gif.sizePolicy().hasHeightForWidth())
        self.label_gif.setSizePolicy(sizePolicy)
        self.label_gif.setMinimumSize(QtCore.QSize(0, 0))
        self.label_gif.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_gif.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_gif.setStyleSheet("background: none;\n"
"border-radius: 50%;")
        self.label_gif.setMidLineWidth(0)
        self.label_gif.setText("")
        self.label_gif.setObjectName("label_gif")
        self.verticalLayout_2.addWidget(self.label_gif)
        self.verticalLayout.addWidget(self.frame_loading)

        self.retranslateUi(LoadingWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadingWindow)

    def retranslateUi(self, LoadingWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadingWindow.setWindowTitle(_translate("LoadingWindow", "Dialog"))
