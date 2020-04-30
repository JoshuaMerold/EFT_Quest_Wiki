from shutil import copyfile
import json

class saveData:

    def __transformData(self, data):
        #print(data)
        #print("TRANSFORMED")
        return data

    def save(self, data):
        data = self.__transformData(data)
        try:
            copyfile('data/savedMissions.json', 'data/savedMissions_outdated.json')
        
        except Exception as e:
            print("Error while creating backup")
            print(e)
        
        try:
            with open('data/savedMissions.json', 'w', encoding = "utf-8") as outputFile:
                json.dump(data, outputFile, indent = 4)
                
            print("Data saved successfully")

        except Exception as e:
            print("Error while saving")
            print(e)
