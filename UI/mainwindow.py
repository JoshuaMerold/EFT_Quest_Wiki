# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/Quest_Wiki_Logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnUpdate = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnUpdate.setMinimumSize(QtCore.QSize(97, 29))
        self.btnUpdate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUpdate.setStyleSheet("QPushButton#btnUpdate {\n"
"    background-color: rgb(255,255,0255);\n"
"    height: 25px;\n"
"    border: 1px solid rgb(196, 196, 196);\n"
"    border-radius: 5px;\n"
"    color: rgb(196, 196, 196);\n"
"}\n"
"\n"
"QPushButton#btnUpdate:hover {\n"
"    background-color: rgb(252, 186, 3);\n"
"    height: 25px;\n"
"    border: 1px solid rgb(252, 186, 3);\n"
"    border-radius: 5px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton#btnUpdate:pressed {\n"
"    background-color: rgb(252, 186, 3);\n"
"    height: 25px;\n"
"    border: 1px solid rgb(252, 186, 3);\n"
"    border-radius: 5px;\n"
"    color: rgb(255,255,255);     \n"
"}\n"
"")
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnSearch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSearch.setMinimumSize(QtCore.QSize(97, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 179, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 179, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 123, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 179, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.btnSearch.setPalette(palette)
        self.btnSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSearch.setStyleSheet("QPushButton#btnSearch {\n"
"    background-color: rgb(0,123,255);\n"
"    height: 25px;\n"
"    border: 2px solid rgb(0,123,255);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btnSearch:hover {\n"
"    background-color: rgb(0, 179, 255);\n"
"    height: 25px;\n"
"    border: 2px solid rgb(0, 179, 255);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btnSearch:pressed {\n"
"    background-color: rgb(0, 179, 255);\n"
"    height: 25px;\n"
"    border: 2px solid rgb(0, 179, 255);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.searchInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.searchInput.setMaximumSize(QtCore.QSize(16777215, 29))
        self.searchInput.setStyleSheet("height: 25px;\n"
"border: 1px solid rgb(196, 196, 196);\n"
"border-radius: 5px;\n"
"color: rgb(92, 92, 92);\n"
"padding-left: 5px;")
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout.addWidget(self.searchInput)
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnClear.setMinimumSize(QtCore.QSize(29, 29))
        self.btnClear.setMaximumSize(QtCore.QSize(29, 29))
        self.btnClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClear.setStyleSheet("background-color: white;\n"
"border-radius: 5px;\n"
"color: white;")
        self.btnClear.setText("")
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.pages = QtWidgets.QStackedWidget(self.gridLayoutWidget)
        self.pages.setObjectName("pages")
        self.homePage = QtWidgets.QWidget()
        self.homePage.setObjectName("homePage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.homePage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 781, 421))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setStyleSheet("font: 25 8pt \"Quicksand\";")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 3, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.titleLabel.setStyleSheet("font: 16pt \"Raleway\";")
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout_3.addWidget(self.titleLabel, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.pages.addWidget(self.homePage)
        self.listPage = QtWidgets.QWidget()
        self.listPage.setObjectName("listPage")
        self.table = QtWidgets.QTableWidget(self.listPage)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(0, 4, 821, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 179, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 179, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.table.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.table.setFont(font)
        self.table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table.setStyleSheet("border: 1px solid rgb(196, 196, 196);\n"
"border-radius: 5px;")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setProperty("showDropIndicator", False)
        self.table.setDragEnabled(False)
        self.table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table.setShowGrid(False)
        self.table.setGridStyle(QtCore.Qt.NoPen)
        self.table.setCornerButtonEnabled(False)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.verticalHeader().setVisible(False)
        self.pages.addWidget(self.listPage)
        self.favoritesPage = QtWidgets.QWidget()
        self.favoritesPage.setObjectName("favoritesPage")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.favoritesPage)
        self.textBrowser_1.setGeometry(QtCore.QRect(0, 0, 391, 210))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setStyleSheet("")
        self.textBrowser_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.favoritesPage)
        self.textBrowser_2.setGeometry(QtCore.QRect(409, 0, 391, 210))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line = QtWidgets.QFrame(self.favoritesPage)
        self.line.setGeometry(QtCore.QRect(390, 0, 20, 431))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.favoritesPage)
        self.line_2.setGeometry(QtCore.QRect(0, 207, 801, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.favoritesPage)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 220, 391, 210))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.favoritesPage)
        self.textBrowser_4.setGeometry(QtCore.QRect(410, 220, 391, 210))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(9)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pages.addWidget(self.favoritesPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.groupBox = QtWidgets.QGroupBox(self.settingsPage)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 191, 191))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.missionNameCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.missionNameCheckbox.setChecked(True)
        self.missionNameCheckbox.setObjectName("missionNameCheckbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.missionNameCheckbox)
        self.vendorCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.vendorCheckbox.setChecked(True)
        self.vendorCheckbox.setObjectName("vendorCheckbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vendorCheckbox)
        self.mapCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.mapCheckbox.setChecked(True)
        self.mapCheckbox.setObjectName("mapCheckbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mapCheckbox)
        self.expCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.expCheckbox.setChecked(True)
        self.expCheckbox.setObjectName("expCheckbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.expCheckbox)
        self.roublesCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.roublesCheckbox.setChecked(True)
        self.roublesCheckbox.setObjectName("roublesCheckbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.roublesCheckbox)
        self.repCheckbox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.repCheckbox.setChecked(True)
        self.repCheckbox.setObjectName("repCheckbox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.repCheckbox)
        self.pages.addWidget(self.settingsPage)
        self.missionDetailPage = QtWidgets.QWidget()
        self.missionDetailPage.setObjectName("missionDetailPage")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.missionDetailPage)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 10, 781, 411))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(8)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("border: none;")
        self.textBrowser_5.setOpenExternalLinks(True)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pages.addWidget(self.missionDetailPage)
        self.gridLayout_2.addWidget(self.pages, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_1.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton#pushButton_1 {\n"
"background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(255,255,255);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_1:hover {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_1:pressed {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}")
        self.pushButton_1.setText("")
        self.pushButton_1.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout_2.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(255,255,255);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3 {\n"
"background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(255,255,255);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_4.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(255,255,255);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"background-color: rgb(242, 242, 242);\n"
"border: 2px solid rgb(242, 242, 242);\n"
"border-radius: 35px;\n"
"color: white;\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(15, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        self.statusText = QtWidgets.QLabel(self.centralwidget)
        self.statusText.setGeometry(QtCore.QRect(890, 480, 55, 16))
        self.statusText.setTextFormat(QtCore.Qt.RichText)
        self.statusText.setOpenExternalLinks(True)
        self.statusText.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.statusText.setObjectName("statusText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        self.btnClear.clicked.connect(self.searchInput.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EFT-Quest Wiki"))
        self.btnUpdate.setText(_translate("MainWindow", "Update"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Suchbegriff"))
        self.label.setText(_translate("MainWindow", "Welcome to the first version of the \"EFT Quest Wiki\""))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Info</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If u click on &quot;Update&quot; to programm wil update the missions - all favorites will be lost and the programm will freeze but its still working. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">The Updates lasts ~5min.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">I am working on it ...</span></p></body></html>"))
        self.titleLabel.setText(_translate("MainWindow", "Escape From Tarkov - Quest-Wiki"))
        self.table.setSortingEnabled(True)
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "List columns"))
        self.missionNameCheckbox.setText(_translate("MainWindow", "Missionname"))
        self.vendorCheckbox.setText(_translate("MainWindow", "Vendor"))
        self.mapCheckbox.setText(_translate("MainWindow", "Map"))
        self.expCheckbox.setText(_translate("MainWindow", "EXP"))
        self.roublesCheckbox.setText(_translate("MainWindow", "Roubles"))
        self.repCheckbox.setText(_translate("MainWindow", "Rep"))
        self.statusText.setText(_translate("MainWindow", "Text"))
