import sys
import re
import ctypes
import functools
from qtpy import QtWidgets, QtCore
from UI.mainwindow import Ui_MainWindow
from dataModule import *
from PyQt5.QtGui import QIcon, QPixmap

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        myappid = 'eft_quest_wiki.joshua_merold.v_0.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        pixmamp = QPixmap("qw_logo.ico")
        icon = QIcon(pixmamp)
        self.setWindowIcon(icon)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pixmamp = QPixmap("icons/house.jpg")
        icon = QIcon(pixmamp)
        self.ui.pushButton_1.setIcon(icon)

        pixmamp = QPixmap("icons/list.jpg")
        icon = QIcon(pixmamp)
        self.ui.pushButton_2.setIcon(icon)

        pixmamp = QPixmap("icons/fav_blue.jpg")
        icon = QIcon(pixmamp)
        self.ui.pushButton_3.setIcon(icon)

        pixmamp = QPixmap("icons/settings.jpg")
        icon = QIcon(pixmamp)
        self.ui.pushButton_4.setIcon(icon)

        pixmamp = QPixmap("icons/clear.jpg")
        icon = QIcon(pixmamp)
        self.ui.btnClear.setIcon(icon)

        self.ui.table.insertColumn(0)
        self.ui.table.setColumnWidth(0, 50)
        self.ui.table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Fav"))
        self.ui.table.insertColumn(1)
        self.ui.table.setColumnWidth(1, 220)
        self.ui.table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Name"))
        self.ui.table.insertColumn(2)
        self.ui.table.setColumnWidth(2, 100)
        self.ui.table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Vendor"))
        self.ui.table.insertColumn(3)
        self.ui.table.setColumnWidth(3, 130)
        self.ui.table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Map"))
        self.ui.table.insertColumn(4)
        self.ui.table.setColumnWidth(4, 90)
        self.ui.table.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("EXP"))
        self.ui.table.insertColumn(5)
        self.ui.table.setColumnWidth(5, 90)
        self.ui.table.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Roubles"))
        self.ui.table.insertColumn(6)
        self.ui.table.setColumnWidth(6, 117)
        self.ui.table.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("Rep"))
        self.ui.table.insertColumn(7)
        #self.ui.table.setColumnWidth(7, 143)
        self.ui.table.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("HiddenFavValue"))
        #self.ui.table.hideColumn(7)

        self.ui.pages.setCurrentIndex(0)

        self.ui.btnUpdate.clicked.connect(self.update)

        ld = loadData.loadData()
        self.data = ld.load()
        self.showData(self.data)

        self.ui.searchInput.textChanged.connect(self.search)
        self.ui.btnSearch.clicked.connect(self.search)

        self.ui.pushButton_1.clicked.connect(self.goHome)
        self.ui.pushButton_2.clicked.connect(self.goList)
        self.ui.pushButton_3.clicked.connect(self.goFavorites)
        self.ui.pushButton_4.clicked.connect(self.goSettings)

        self.ui.statusbar.addPermanentWidget(self.ui.statusText)
        self.ui.statusText.setText("v0.1 | All data by <a href='https://escapefromtarkov.gamepedia.com/Escape_from_Tarkov_Wiki'>GamePedia</a>")

        self.ui.table.cellDoubleClicked.connect(self.tableClicked)

        slot = functools.partial(self.changeCol, 1)
        self.ui.missionNameCheckbox.clicked.connect(slot)
        slot = functools.partial(self.changeCol, 2)
        self.ui.vendorCheckbox.clicked.connect(slot)
        slot = functools.partial(self.changeCol, 3)
        self.ui.mapCheckbox.clicked.connect(slot)
        slot = functools.partial(self.changeCol, 4)
        self.ui.expCheckbox.clicked.connect(slot)
        slot = functools.partial(self.changeCol, 5)
        self.ui.roublesCheckbox.clicked.connect(slot)
        slot = functools.partial(self.changeCol, 6)
        self.ui.repCheckbox.clicked.connect(slot)

        self.clicked = False
        self.ui.table.horizontalHeader().sortIndicatorChanged.connect(self.sortFav)

        #self.ui.table.clic

    def goHome(self):
        self.ui.pages.setCurrentIndex(0)

    def goList(self):
        self.ui.pages.setCurrentIndex(1)

    def goFavorites(self):
        self.ui.pages.setCurrentIndex(2)
        self.getFav()

    def goSettings(self):
        self.ui.pages.setCurrentIndex(3)

    def update(self):
        rd = requestData.Data()
        print(rd.getCompleteSite())
        temp = rd.transformMissions()
        self.data = temp

        print("Saving...")
        sd = saveData.saveData()
        sd.save(self.data)

        self.showData(self.data)

    def showData(self, data):
        self.ui.table.setRowCount(0)

        count = 0
        for missionName, mission in data.items():
            if missionName == "timestamp" or missionName == "favorite" or missionName == "completeSite":
                continue

            vendor = "-"
            vendors = ["Prapor", "Therapist", "Fence", "Skier", "Peacekeeper", "Mechanic", "Ragman", "Jaeger", "Warden", "Bashkir", "Khokhol"]
            map = "Any"
            maps = ["Factory", "Customs", "Woods", "Shoreline", "Interchange", "The Lab", "Reserve", "Hideout", "Streets of Tarkov", "Suburbs", "Town", "Lighthouse", "Terminal", "Arena", "Private Sector"]
            if "infobox" in mission:
                for info in mission["infobox"]:
                    #print(info)
                    if info in vendors:
                        vendor = info

                    multipleMaps = re.findall(r"(?=("+'|'.join(maps)+r"))", info)
                    if len(multipleMaps) > 0:
                        map = ", ".join(multipleMaps)

                    if info in maps:
                        map = info

            self.data[missionName].update({"Vendor": vendor})
            self.data[missionName].update({"Map": map})

            self.ui.table.insertRow(count)

            missionXP = "-"
            missionRoubles = "-"
            missionRep = "-"

            if "Rewards" in mission:
                missionRewards = mission["Rewards"][0].split("\n")

                for reward in missionRewards:
                    if "EXP" in reward:
                        missionXP = reward.strip("+EXP")

                    elif "Roubles" in reward:
                        missionRoubles = reward.strip("Roubles")

                    elif "Rep" in reward:
                        missionRep = reward.replace("Rep ", "")

            if mission["favorite"] == 0:
                favPic = QPixmap("icons/noFav.jpg")
                favIcon = QIcon(favPic)
                item = QtWidgets.QTableWidgetItem(favIcon, "")
                self.ui.table.setItem(count, 7, QtWidgets.QTableWidgetItem("0"))
            elif mission["favorite"] == 1:
                favPic = QPixmap("icons/fav.jpg")
                favIcon = QIcon(favPic)
                item = QtWidgets.QTableWidgetItem(favIcon, "")
                self.ui.table.setItem(count, 7, QtWidgets.QTableWidgetItem("1"))

            self.ui.table.setItem(count, 0, item)
            self.ui.table.setItem(count, 1, QtWidgets.QTableWidgetItem(missionName))
            self.ui.table.setItem(count, 2, QtWidgets.QTableWidgetItem(vendor))
            self.ui.table.setItem(count, 3, QtWidgets.QTableWidgetItem(map))
            self.ui.table.setItem(count, 4, QtWidgets.QTableWidgetItem(missionXP))
            self.ui.table.setItem(count, 5, QtWidgets.QTableWidgetItem(missionRoubles))
            self.ui.table.setItem(count, 6, QtWidgets.QTableWidgetItem(missionRep))

            count += 1

    def search(self):
        #print(self.data)
        self.ui.pages.setCurrentIndex(1)
        self.input = self.ui.searchInput.text().lower()
        if "ä" in self.input:
            self.input = self.input.replace("ä", "ae")

        foundItems = []
        for name, mission in self.data.items():
            if name == "timestamp" or name == "favorite" or name == "completeSite":
                continue

            if self.input in name.lower():
                foundItems.append(name)
                #print("name")

            for info in mission["infobox"]:
                info = info.lower()

                if self.input in info:
                    foundItems.append(name)
                    #print("infobox" + info)

        for i in range(0, self.ui.table.rowCount()):
            selection = self.ui.table.item(i, 1).text()
            if selection in foundItems:
                self.ui.table.showRow(i)

            else:
                self.ui.table.hideRow(i)

    def tableClicked(self, row, col):
        if col == 0:
            print(row)
            fav = favs.favs(self.data)
            fav.addFav(row)
            self.showData(self.data)

        else:
            self.ui.pages.setCurrentIndex(4)

            md = missionDetails.missionDetails(self.data)
            details = md.getDetails(row)

            self.ui.textBrowser_5.setHtml(details)
            #self.ui.textBrowser_5.setHtml("<img src='icons/settings.jpg' />")

        #print(row, col)

    def getFav(self):
        fav = favs.favs(self.data)
        favorites = fav.loadFavs()

        count = 0
        for name, obj in favorites.items():
            headline = name
            text = "".join(obj)

            if count == 0:
                self.ui.textBrowser_1.setText("<span style='font-weight:600; font-size:10pt'>" + headline + "</span><ul>" + text + "</ul>")
            elif count == 1:
                self.ui.textBrowser_2.setText("<span style='font-weight:600; font-size:10pt'>" + headline + "</span><ul>" + text + "</ul>")
            elif count == 2:
                self.ui.textBrowser_3.setText("<span style='font-weight:600; font-size:10pt'>" + headline + "</span><ul>" + text + "</ul>")
            elif count == 3:
                self.ui.textBrowser_4.setText("<span style='font-weight:600; font-size:10pt'>" + headline + "</span><ul>" + text + "</ul>")
            else:
                break
            count += 1

    def changeCol(self, col):
        print(col)
        if self.ui.table.isColumnHidden(col):
            self.ui.table.showColumn(col)
        else:
            self.ui.table.hideColumn(col)

    def sortFav(self, col):
        if col == 0:
            if self.clicked == False:
                self.ui.table.sortByColumn(7, QtCore.Qt.AscendingOrder)
                self.clicked = True
            else:
                self.ui.table.sortByColumn(7, QtCore.Qt.DescendingOrder)
                self.clicked = False

class main():
    # print(len(sys.argv))
    if len(sys.argv) < 2:
        #print("Hallo")

        app = QtWidgets.QApplication(sys.argv)

        window = mainWindow()
        window.show()

        sys.exit(app.exec_())

    elif len(sys.argv) == 2:
        input = sys.argv[1]
        validation = False
        while not validation:
            if input == "update" or input == "1":
                print("Update startet...")

                rd = requestData.Data()
                data = rd.showData()
                # print(len(data))

                print("Speichervorgang startet...")

                sd = saveData.saveData()
                sd.save(data)

                validation = True

            elif input == "save" or input == "2":

                print("Speichervorgang startet...")

                sd = saveData.saveData()
                sd.save(data)

                validation = True

            elif input == "load" or input == "3":
                print("Lade Daten...")

                ld = loadData.loadData()
                ld.load()

                validation = True

            elif input == "exit" or input == "4":
                validation = True
                quit()

            else:
                print("> FEHLER bei der Eingabe")

    else:
        print("To many attributs: " + str(len(sys.argv)))
