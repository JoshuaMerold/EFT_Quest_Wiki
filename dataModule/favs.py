import json

class favs:
    def __init__(self, data):
        self.data = data

    def loadFavs(self):
        favorites = {}
        for name, mission in self.data.items():
            if name == "timestamp":
                continue

            if mission["favorite"] == 1:
                favorites[name] = []
                obj = mission["Objectives"]
                #print(name)
                obj = obj[0].split("\n")
                #print(obj)

                for i in range(0, len(obj)):
                    obj[i] = "<li>" + obj[i] + "</li>"

                favorites[name] = obj

        return favorites

    def __transformFavs(self):
        pass

    def addFav(self, row):
        index = 0
        for name, mission in self.data.items():
            if name == "timestamp":
                continue

            if index == row:
                if self.data[name]["favorite"] == 0:
                    self.data[name]["favorite"] = 1

                else:
                    self.data[name]["favorite"] = 0

                break
            index += 1

        try:
            with open('data/savedMissions.json', 'w', encoding="utf-8") as outputFile:
                json.dump(self.data, outputFile, indent=4)

            print("Data saved successfully")

        except Exception as e:
            print("Error while saving")
            print(e)
