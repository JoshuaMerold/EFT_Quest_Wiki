from PyQt5.QtGui import QPixmap

class missionDetails:
    def __init__(self, data):
        self.data = data

    def getDetails(self, row):
        details = []
        index = 0
        for name, mission in self.data.items():
            if name == "timestamp":
                continue

            if index == row:
                details = self.data[name]["completeSite"]

            index += 1
        #print(details)

        return details

