# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\popup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUp(object):
    def setupUi(self, PopUp):
        PopUp.setObjectName("PopUp")
        PopUp.resize(400, 48)
        PopUp.setStyleSheet("background-color: white;")
        self.gridLayoutWidget = QtWidgets.QWidget(PopUp)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(PopUp)
        QtCore.QMetaObject.connectSlotsByName(PopUp)

    def retranslateUi(self, PopUp):
        _translate = QtCore.QCoreApplication.translate
        PopUp.setWindowTitle(_translate("PopUp", "Dialog"))
        self.label.setText(_translate("PopUp", "Updating data, please wait ..."))
