# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from callbacks import callback


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 641, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.input_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.input_layout.setContentsMargins(0, 0, 0, 0)
        self.input_layout.setObjectName("input_layout")
        self.hours_field = QtWidgets.QPlainTextEdit(
            self.horizontalLayoutWidget)
        self.hours_field.setObjectName("hours_field")
        self.input_layout.addWidget(self.hours_field)
        self.minuits_field = QtWidgets.QPlainTextEdit(
            self.horizontalLayoutWidget)
        self.minuits_field.setObjectName("minuits_field")
        self.input_layout.addWidget(self.minuits_field)
        self.seconds_field = QtWidgets.QPlainTextEdit(
            self.horizontalLayoutWidget)
        self.seconds_field.setObjectName("seconds_field")
        self.input_layout.addWidget(self.seconds_field)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(80, 60, 530, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.button_layout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setObjectName("button_layout")
        self.clear_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clear_btn.setObjectName("clear_btn")
        self.button_layout.addWidget(self.clear_btn)
        self.extend_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.extend_btn.setObjectName("extend_btn")
        self.button_layout.addWidget(self.extend_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.cancel_btn.setObjectName("cancel_btn")
        self.button_layout.addWidget(self.cancel_btn)
        self.submit_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.submit_btn.setObjectName("submit_btn")
        self.button_layout.addWidget(self.submit_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ShutDownify"))
        self.hours_field.setPlainText(_translate("MainWindow", "0"))
        self.minuits_field.setPlainText(_translate("MainWindow", "0"))
        self.seconds_field.setPlainText(_translate("MainWindow", "0"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.extend_btn.setText(_translate("MainWindow", "Extend"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.submit_btn.setText(_translate("MainWindow", "Submit"))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        self.call = callback()
        super(MainWindow, self).__init__(parent=parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('shutdown.ico'))
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # add listeners to buttons and fields
        self.ui.clear_btn.clicked.connect(self.clear_fields)
        self.ui.submit_btn.installEventFilter(self)
        self.ui.extend_btn.installEventFilter(self)
        self.ui.cancel_btn.installEventFilter(self)
        self.ui.hours_field.installEventFilter(self)
        self.ui.minuits_field.installEventFilter(self)
        self.ui.seconds_field.installEventFilter(self)

    def clear_fields(self):
        self.ui.hours_field.setPlainText("0")
        self.ui.minuits_field.setPlainText("0")
        self.ui.seconds_field.setPlainText("0")

    # EVENT FILTER
    # NOT RECOMMENDED in general to use the setplaintext function in a event filter directly  as it will cause unknown errors , clear references must be made in future versions
    def eventFilter(self, source, event):

        # Alternative to the click.connect()
        # handles mousevents

        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.hrs_val = int(self.ui.hours_field.toPlainText())
            self.min_val = int(self.ui.minuits_field.toPlainText())
            self.sec_val = int(self.ui.seconds_field.toPlainText())
            if (self.sec_val >= 3 or self.min_val > 0 or self.hrs_val > 0) and source is self.ui.submit_btn or source is self.ui.extend_btn:
                self.call.submit(self.hrs_val, self.min_val, self.sec_val)
            if source is self.ui.cancel_btn:
                self.call.cancel()

        # Clears the field value  if the user enters the fields
        if event.type() == QtCore.QEvent.Enter:
            if type(source) is QtWidgets.QPlainTextEdit:
                if source.toPlainText() == '0':
                    source.setPlainText("")
                    return True
        # Sets the field value to 0 if the user leaves the fields
        if event.type() == QtCore.QEvent.CursorChange:
            print(source.objectName())
        if event.type() == QtCore.QEvent.Leave:

            if(type(source) is QtWidgets.QPlainTextEdit):
                # if the user enters a letter in the hours field or if its empty
                if(any(c.isalpha() for c in self.ui.hours_field.toPlainText()) or self.ui.hours_field.toPlainText() == ''):
                    self.ui.hours_field.setPlainText("0")
                if(any(c.isalpha() for c in self.ui.minuits_field.toPlainText()) or self.ui.minuits_field.toPlainText() == ''):
                    self.ui.minuits_field.setPlainText("0")
                if(any(c.isalpha() for c in self.ui.seconds_field.toPlainText()) or self.ui.seconds_field.toPlainText() == ''):
                    self.ui.seconds_field.setPlainText("0")

        return QtWidgets.QWidget.eventFilter(self, source, event)


# for colors
# QLineEdit
# {
#     background-color: black
# }

# QLineEdit[text = ""]
# {
#     background-color: red
# }

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
