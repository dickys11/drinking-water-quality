# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setGeometry(QtCore.QRect(320, 370, 61, 21))
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(80, 150, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 371, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_input = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_input.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_input.setHorizontalSpacing(100)
        self.gridLayout_input.setObjectName("gridLayout_input")
        self.inputLabel_ph = QtWidgets.QLabel(self.gridLayoutWidget)
        self.inputLabel_ph.setObjectName("inputLabel_ph")
        self.gridLayout_input.addWidget(self.inputLabel_ph, 0, 0, 1, 1)
        self.inputLabel_tds = QtWidgets.QLabel(self.gridLayoutWidget)
        self.inputLabel_tds.setObjectName("inputLabel_tds")
        self.gridLayout_input.addWidget(self.inputLabel_tds, 2, 0, 1, 1)
        self.inputLabel_do = QtWidgets.QLabel(self.gridLayoutWidget)
        self.inputLabel_do.setObjectName("inputLabel_do")
        self.gridLayout_input.addWidget(self.inputLabel_do, 1, 0, 1, 1)
        self.doubleSpinBox_ph = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.doubleSpinBox_ph.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_ph.setSizePolicy(sizePolicy)
        self.doubleSpinBox_ph.setWrapping(False)
        self.doubleSpinBox_ph.setButtonSymbols(
            QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_ph.setMaximum(14.0)
        self.doubleSpinBox_ph.setSingleStep(0.1)
        self.doubleSpinBox_ph.setObjectName("doubleSpinBox_ph")
        self.gridLayout_input.addWidget(self.doubleSpinBox_ph, 0, 1, 1, 1)
        self.doubleSpinBox_do = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_do.setMaximum(10.0)
        self.doubleSpinBox_do.setSingleStep(0.1)
        self.doubleSpinBox_do.setObjectName("doubleSpinBox_do")
        self.gridLayout_input.addWidget(self.doubleSpinBox_do, 1, 1, 1, 1)
        self.doubleSpinBox_tds = QtWidgets.QDoubleSpinBox(
            self.gridLayoutWidget)
        self.doubleSpinBox_tds.setMaximum(300.0)
        self.doubleSpinBox_tds.setObjectName("doubleSpinBox_tds")
        self.gridLayout_input.addWidget(self.doubleSpinBox_tds, 2, 1, 1, 1)
        self.label_condition = QtWidgets.QLabel(self.centralwidget)
        self.label_condition.setGeometry(QtCore.QRect(83, 240, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_condition.setFont(font)
        self.label_condition.setText("")
        self.label_condition.setObjectName("label_condition")
        self.label_condition.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Drinking Water Quality"))
        self.label_title.setText(_translate(
            "MainWindow", "Drinking Water Quality Testing With Fuzzy Logic"))
        self.pushButton_calc.setText(_translate("MainWindow", "Calculate"))
        self.label_output.setText(_translate(
            "MainWindow", "Your Drinking Water Quality"))
        self.inputLabel_ph.setText(_translate(
            "MainWindow", "Masukkan Nilai pH (0-14)"))
        self.inputLabel_tds.setText(_translate(
            "MainWindow", "Masukkan Nilai TDS (0-300)"))
        self.inputLabel_do.setText(_translate(
            "MainWindow", "Masukkan Nilai Dissolved Oxygen (0-10)"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
